from pydantic import BaseModel


class Completion(BaseModel):
    message: str