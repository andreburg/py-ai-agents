from domain.models.file import FileBase


class Object(FileBase):
    content: str
