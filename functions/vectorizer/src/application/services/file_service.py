from asyncpg import Connection

from domain.models.file import File, FileCreate


class FileService:
    _conn: Connection

    def __init__(self, conn: Connection):
        self._conn = conn

    async def create_file(self, file: FileCreate):
        result = await self._conn.fetchrow(
            """
            INSERT INTO tiny.file (id, file_name, bucket, object_key)
            VALUES (gen_random_uuid(), $1, $2, $3)
            RETURNING id, file_name, bucket, object_key, created_at
        """,
            file.file_name,
            file.bucket,
            file.object_key,
        )

        if not result:
            raise Exception("EEeh")

        return File(**dict(result))
