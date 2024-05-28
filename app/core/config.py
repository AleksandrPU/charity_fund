from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'QRKot'
    app_description: str = 'Фонд собирает пожертвования на различные проекты.'
    # database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    postgres_user: str = 'fastapi'
    postgres_password: str = 'mysecretpassword'
    postgres_db: str = 'fastapi'
    database_url: str = 'postgresql+asyncpg://fastapi:mysecretpassword@db:5432/fastapi'
    secret: str = 'secret'
    # token_lifetime: int = 3600
    token_lifetime: int = 360000
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
