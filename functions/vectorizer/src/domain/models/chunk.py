from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class ChunkBase(BaseModel):
    file_id: UUID
    chunk_index: int
    content: str
    embedding: str


class ChunkCreate(ChunkBase): ...


class Chunk(ChunkBase):
    id: UUID
    created_at: datetime
