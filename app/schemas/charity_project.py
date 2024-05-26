from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt, validator


class CharityProjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1)
    full_amount: PositiveInt

    @validator('name')
    def name_cant_be_null(cls, value):
        if value is None:
            raise ValueError('Название проекта не может быть пустым.')
        return value


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime] = None


class CharityProjectUpdate(CharityProjectCreate):
    name: Optional[str] = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(min_length=1)
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid
