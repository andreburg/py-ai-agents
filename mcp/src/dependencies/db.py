import asyncpg
from typing import Optional


class Database:
    _pool: Optional[asyncpg.pool.Pool] = None

    @classmethod
    async def connect(cls, dsn: str):
        if cls._pool is None:
            cls._pool = await asyncpg.create_pool(dsn)
        return cls._pool

    @classmethod
    def get_pool(cls) -> asyncpg.pool.Pool:
        if cls._pool is None:
            raise RuntimeError("Database pool is not initialized. Call connect() first.")
        return cls._pool

    @classmethod
    async def close(cls):
        if cls._pool is not None:
            await cls._pool.close()
            cls._pool = None
