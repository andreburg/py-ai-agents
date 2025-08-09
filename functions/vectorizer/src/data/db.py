import asyncpg

from utils.vars import DATABASE_URL


async def get_pool():
    return await asyncpg.create_pool(DATABASE_URL)
