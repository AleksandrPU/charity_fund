from sqlalchemy import Column, Integer, MetaData
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)
Base.metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

url = URL(
    settings.db_drivername,
    settings.postgres_user,
    settings.postgres_password,
    settings.postgres_host,
    settings.postgres_port,
    settings.postgres_db,
    {},
)

engine = create_async_engine(
    url,
    echo=settings.debug_echo,
    isolation_level=(
        "REPEATABLE READ" if "postgresql" in settings.db_drivername else "SERIALIZABLE"
    ),
)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
