from datetime import datetime
from typing import Optional, Union

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    PositiveInt,
)
from pydantic.functional_validators import field_validator

from app.core.constants import (
    DESCRIPTION_MIN_LENGTH,
    NAME_MAX_LENGTH,
    NAME_MIN_LENGTH,
)


def name_cant_be_null(value: str) -> Union[str, None]:
    if value is None:
        raise ValueError("Название проекта не может быть пустым.")
    return value


class CharityProjectCreate(BaseModel):
    name: str = Field(
        min_length=NAME_MIN_LENGTH,
        max_length=NAME_MAX_LENGTH,
    )
    description: str = Field(min_length=DESCRIPTION_MIN_LENGTH)
    full_amount: PositiveInt

    _name_cant_be_null = field_validator(
        "name",
        mode="before",
    )(name_cant_be_null)


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime] = None


class CharityProjectUpdate(BaseModel):
    name: str | None = Field(
        None,
        min_length=NAME_MIN_LENGTH,
        max_length=NAME_MAX_LENGTH,
    )
    description: str | None = Field(
        None,
        min_length=DESCRIPTION_MIN_LENGTH,
    )
    full_amount: PositiveInt | None = None

    _name_cant_be_null = field_validator(
        "name",
        mode="before",
    )(name_cant_be_null)

    model_config = ConfigDict(extra="forbid")
