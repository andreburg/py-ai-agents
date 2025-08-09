import io
import docx
from .base import FileParser


class DocxParser(FileParser):
    def extract_text(self, file_bytes: bytes) -> str:
        document = docx.Document(io.BytesIO(file_bytes))
        return "\n".join(p.text for p in document.paragraphs)
