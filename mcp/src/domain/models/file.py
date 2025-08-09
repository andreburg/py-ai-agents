from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class FileBase(BaseModel):
    file_name: str
    bucket: str
    object_key: str


class FileCreate(FileBase): ...


class File(FileBase):
    id: UUID
    created_at: datetime
