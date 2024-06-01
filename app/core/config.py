from typing import Optional

from pydantic import BaseSettings, EmailStr
from sqlalchemy.engine import URL


class Settings(BaseSettings):
    app_title: str = 'QRKot'
    app_description: str = 'Фонд собирает пожертвования на различные проекты.'
<<<<<<< Updated upstream
    # database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    # database_url: str = 'postgresql+asyncpg://fastapi:mysecretpassword@db:5432/fastapi'
    # dialect+driver://username:password@host:port/database
    database_dialect_driver: str = 'sqlite+aiosqlite'
    database_username: str = None
    database_password: str = None
    database_host: str = None
    database_port: int = None
    database_db: str = './fastapi.db'
    database_url: URL = URL.create(
        database_dialect_driver,
        username=database_username,
        password=database_password,
        host=database_host,
        database=database_db,
    )
=======
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    # postgres_user: str = 'fastapi'
    # postgres_password: str = 'mysecretpassword'
    # postgres_db: str = 'fastapi'
    # database_url: str = 'postgresql+asyncpg://fastapi:mysecretpassword@db:5432/fastapi'
>>>>>>> Stashed changes
    secret: str = 'secret'
    token_lifetime: int = 3600
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
