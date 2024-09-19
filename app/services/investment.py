from collections import deque
from datetime import datetime

from app.models import BaseProjectDonation


def close_project_donation(
    obj: BaseProjectDonation,
) -> BaseProjectDonation:
    """Закрываем завершенный проект/пожертвование."""

    if obj.invested_amount == obj.full_amount:
        obj.fully_invested = True
        obj.close_date = datetime.now()
    return obj


def investment(
    obj: BaseProjectDonation,
    not_invested_projects_donations: list[BaseProjectDonation],
) -> list[BaseProjectDonation]:
    """Инвестируем пожертвования в проекты."""

    investment_queue = deque(not_invested_projects_donations)

    changed_objs = []
    while obj.full_amount - obj.invested_amount > 0 and investment_queue:
        invest_item: BaseProjectDonation = investment_queue[0]

        deficit: int = min(
            obj.full_amount - obj.invested_amount,
            invest_item.full_amount - invest_item.invested_amount,
        )

        obj.invested_amount += deficit
        invest_item.invested_amount += deficit

        invest_item = close_project_donation(invest_item)
        if invest_item.fully_invested:
            investment_queue.popleft()

        changed_objs.append(invest_item)

    obj = close_project_donation(obj)
    changed_objs.append(obj)

    return changed_objs
