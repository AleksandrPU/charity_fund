from collections import deque
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charity_project_crud, donation_crud
from app.models import CharityProject, Donation


class CharityProjectService:

    def __init__(self, session: AsyncSession):
        self.session = session
        self.project_queue = deque()
        self.donation_queue = deque()

    async def add_to_queue(self, obj):
        self.project_queue.extend(
            await charity_project_crud.get_multi(
                self.session,
                not_full_invested=True
            )
        )
        self.donation_queue.extend(
            await donation_crud.get_multi(
                self.session,
                not_full_invested=True
            )
        )

        if isinstance(obj, CharityProject):
            self.project_queue.append(obj)
        elif isinstance(obj, Donation):
            self.donation_queue.append(obj)

        self.session.add(obj)

        await self.invest_donation()

    async def close_project_donation(self, obj):
        if obj.invested_amount == obj.full_amount:
            obj.fully_invested = True
            obj.close_date = datetime.now()
        return obj

    async def invest_donation(self):
        while self.donation_queue and self.project_queue:
            donation = self.donation_queue[0]

            if getattr(donation, 'invested_amount') is None:
                setattr(donation, 'invested_amount', 0)

            while (
                    self.project_queue and
                    (donation.full_amount - donation.invested_amount > 0)
            ):
                project = self.project_queue[0]

                if getattr(project, 'invested_amount') is None:
                    setattr(project, 'invested_amount', 0)

                deficit: int = min(
                    project.full_amount - project.invested_amount,
                    donation.full_amount - donation.invested_amount
                )

                project.invested_amount += deficit
                donation.invested_amount += deficit

                if await self.close_project_donation(project):
                    self.project_queue.popleft()

                self.session.add(project)

            if await self.close_project_donation(donation):
                self.donation_queue.popleft()

            self.session.add(donation)
