from asyncpg import Connection
from application.services.chunk_service import ChunkService
from application.services.file_service import FileService
from application.services.object_service import ObjectService
from domain.models.file import FileCreate


class ObjectHandler:
    def __init__(self, conn: Connection):
        self._object_service = ObjectService()
        self._file_service = FileService(conn)
        self._chunk_service = ChunkService(conn)

    async def handle_object_upload(self, bucket: str, key: str):
        object = await self._object_service.get_object(bucket, key)
        base_file = FileCreate(**object.__dict__)

        file = await self._file_service.create_file(base_file)

        chunks = await self._chunk_service.chunk_file(file.id, object.content)
        await self._chunk_service.create_chunks(chunks)
