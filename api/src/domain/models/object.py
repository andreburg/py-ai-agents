from datetime import datetime
from typing import Any
from typing_extensions import Buffer
from pydantic import BaseModel


class Object(BaseModel):
    object_key: str
    file_name: str
    mime_type: str
    metadata: Any
    created_at: datetime
    content: Buffer
