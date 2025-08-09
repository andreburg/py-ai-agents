import asyncio
import sys
from data.db import get_pool
from handlers.object_handler import ObjectHandler


async def run():
    [bucket, key] = sys.argv[1:]
    pool = await get_pool()
    async with pool.acquire() as conn:
        object_handler = ObjectHandler(conn)
        await object_handler.handle_object_upload(bucket, key)


if __name__ == "__main__":
    asyncio.run(run())
