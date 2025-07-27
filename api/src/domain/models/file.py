from datetime import datetime
from typing import Any
from pydantic import BaseModel


class File(BaseModel):
    id: str
    file_name: str
    mime_type: str
    object_key: str
    metadata: Any
    created_at: datetime
