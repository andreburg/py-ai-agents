from asyncio.log import logger

import asyncpg
from domain.models.chunk import ChunkEnriched
from utils.vars import DATABASE_URL


class ChunkService:
    def __init__(self): ...
    async def get_closest_chunks(self, query_embedding: str, k: int = 5) -> list[ChunkEnriched]:
        pool = await asyncpg.create_pool(DATABASE_URL)
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                """
                SELECT chunk.id as id, content, chunk_index, embedding <-> $1::vector AS similarity, file_name, file_id, chunk.created_at as created_at
                FROM tiny.chunk chunk
                INNER JOIN tiny.file file ON file.id=chunk.file_id
                ORDER BY embedding <-> $1::vector
                LIMIT $2
                """,
                query_embedding,
                k,
            )

            return [ChunkEnriched(**dict(row)) for row in rows if row]
