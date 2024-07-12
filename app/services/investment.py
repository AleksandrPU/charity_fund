from collections import deque
from datetime import datetime

from app.models import BaseProjectDonation, CharityProject, Donation


def close_project_donation(
        obj: BaseProjectDonation
) -> BaseProjectDonation:
    """Закрываем завершенный проект/пожертвование."""

    if obj.invested_amount == obj.full_amount:
        obj.fully_invested = True
        obj.close_date = datetime.now()
    return obj


def calculate_investment(
        project_queue: deque[CharityProject],
        donation_queue: deque[Donation]
) -> list[BaseProjectDonation]:
    """Вычисления при инвестировании."""

    changed_objs = []
    while donation_queue and project_queue:
        donation = donation_queue[0]

        while (
                project_queue and
                (donation.full_amount - donation.invested_amount > 0)
        ):
            project = project_queue[0]

            deficit: int = min(
                project.full_amount - project.invested_amount,
                donation.full_amount - donation.invested_amount
            )

            project.invested_amount += deficit
            donation.invested_amount += deficit

            project = close_project_donation(project)
            if project.fully_invested:
                project_queue.popleft()

            changed_objs.append(project)

        donation = close_project_donation(donation)
        if donation.fully_invested:
            donation_queue.popleft()

        changed_objs.append(donation)

    return changed_objs


def investment(
        not_invested_projects: list[CharityProject],
        not_invested_donations: list[Donation]
) -> list[BaseProjectDonation]:
    """Инвестируем пожертвования в проекты."""

    project_queue = deque(not_invested_projects)
    donation_queue = deque(not_invested_donations)

    changed_objs = calculate_investment(project_queue, donation_queue)

    return changed_objs
