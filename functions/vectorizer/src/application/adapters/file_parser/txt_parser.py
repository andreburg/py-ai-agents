from .base import FileParser


class TxtParser(FileParser):
    def extract_text(self, file_bytes: bytes) -> str:
        return file_bytes.decode("utf-8")
