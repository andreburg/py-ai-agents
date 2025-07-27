from datetime import datetime
from numpy import number
from pydantic import BaseModel, Field


class Chunk(BaseModel):
    id: str
    file_id: int
    chunk_index: number
    content: str
    embedding: list[float] = Field(..., min_items=1536, max_items=1536)
    created_at: datetime