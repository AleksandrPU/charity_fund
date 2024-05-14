from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt


class DonationCreate(BaseModel):
    comment: Optional[str]
    full_amount: PositiveInt


class DonationDBUser(BaseModel):
    id: int
    comment: Optional[str]
    full_amount: PositiveInt
    create_date: datetime


class DonationDBSuperuser(BaseModel):
    id: int
    user_id: int
    comment: Optional[str]
    full_amount: PositiveInt
    invested_amount: int = 0
    fully_invested: bool = False
    create_date: datetime
    close_date: datetime
