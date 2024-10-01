from typing import Optional

from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = "QRKot"
    app_description: str = "Фонд собирает пожертвования на различные проекты."

    db_drivername: str = "sqlite+aiosqlite"
    postgres_host: Optional[str] = None
    postgres_port: Optional[int] = None
    postgres_user: Optional[str] = None
    postgres_password: Optional[str] = None
    postgres_base: str = "./fastapi.db"

    secret: str = "secret"

    token_lifetime: int = 3600

    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    debug_echo: Optional[bool] = False

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
