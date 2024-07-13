from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charity_project_crud, donation_crud
from app.models import BaseProjectDonation, CharityProject, Donation
from app.services.investment import investment


async def to_investment(
        obj: BaseProjectDonation,
        session: AsyncSession
) -> BaseProjectDonation:
    """Подготовить данные для инвестирования."""

    if obj.invested_amount is None:
        setattr(obj, 'invested_amount', 0)

    not_invested_projects_donations = None
    if isinstance(obj, CharityProject):
        not_invested_projects_donations = await donation_crud.get_multi(
            session, not_full_invested=True)
    elif isinstance(obj, Donation):
        not_invested_projects_donations = await charity_project_crud.get_multi(
            session, not_full_invested=True)

    session.add_all(investment(obj, not_invested_projects_donations))
    await session.commit()
    await session.refresh(obj)

    return obj
