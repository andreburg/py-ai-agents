from application.adapters.file_parser.factory import get_parser
from domain.models.object import Object


class ObjectService:
    def __init__(self): ...

    async def get_object(self, bucket: str, key: str) -> Object:
        buffer: bytes

        with open(key, "rb") as f:
            buffer = f.read()

        parser = get_parser(key)
        content = parser.extract_text(buffer)

        name = key.split("/")[-1]

        return Object(bucket=bucket, object_key=key, content=content, file_name=name)
