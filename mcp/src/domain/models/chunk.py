from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class ChunkBase(BaseModel):
    file_id: UUID
    chunk_index: int
    content: str
    embedding: str


class Chunk(ChunkBase):
    id: UUID
    file_id: UUID
    chunk_index: int
    content: str
    embedding: str
    created_at: datetime


class ChunkEnriched(BaseModel):
    id: UUID
    file_id: UUID
    chunk_index: int
    content: str
    created_at: datetime
    file_name: str
