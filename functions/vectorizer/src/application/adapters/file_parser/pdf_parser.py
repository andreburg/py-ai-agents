import io
import pdfplumber
from .base import FileParser


class PdfParser(FileParser):
    def extract_text(self, file_bytes: bytes) -> str:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
