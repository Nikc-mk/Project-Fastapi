from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.config import (
    PG_HOST,
    PG_PORT,
    POSTGRES_DB,
    POSTGRES_PASSWORD,
    POSTGRES_USER,
)

DATABASE_URL = (
    f"postgresql+asyncpg:"
    f"//{POSTGRES_USER}:{POSTGRES_PASSWORD}@{PG_HOST}:{PG_PORT}/{POSTGRES_DB}"
)

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
