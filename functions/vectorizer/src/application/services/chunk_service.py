from uuid import UUID
from asyncpg import Connection
from langchain_text_splitters import RecursiveCharacterTextSplitter

from application.services.embedding_service import EmbeddingService
from domain.models.chunk import Chunk, ChunkCreate


class ChunkService:
    _conn: Connection
    _embedding_service: EmbeddingService

    def __init__(self, conn: Connection):
        self._conn = conn
        self._embedding_service = EmbeddingService()

    def chunk_text(self, text: str, chunk_size=1000, chunk_overlap=200) -> list[str]:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )
        return text_splitter.split_text(text)

    async def chunk_file(self, file_id: UUID, file_content: str) -> list[ChunkCreate]:
        content_chunks = self.chunk_text(file_content)
        chunks = []
        for i, chunk_content in enumerate(content_chunks):
            embedding = await self._embedding_service.get_embedding(chunk_content)
            chunks.append(
                ChunkCreate(
                    file_id=file_id,
                    chunk_index=i,
                    content=chunk_content,
                    embedding=embedding,
                )
            )
        return chunks

    async def create_chunk(self, chunk: ChunkCreate):
        result = await self._conn.fetchrow(
            """
                INSERT INTO tiny.chunk (file_id, chunk_index, content, embedding)
                VALUES ($1, $2, $3, $4)
                RETURNING id, file_id, chunk_index, content, embedding, created_at
            """,
            chunk.file_id,
            chunk.chunk_index,
            chunk.content,
            chunk.embedding,
        )

        if not result:
            raise Exception("Failed to insert chunk")

        return Chunk(**dict(result))

    async def create_chunks(self, chunks: list[ChunkCreate]):
        for chunk in chunks:
            await self.create_chunk(chunk)
