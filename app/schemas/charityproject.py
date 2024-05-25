from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt


class CharityProjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1)
    full_amount: PositiveInt


class CharityProjectDB(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime] = None
