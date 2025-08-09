import mimetypes
from .txt_parser import TxtParser
from .pdf_parser import PdfParser
from .docx_parser import DocxParser
from .base import FileParser

EXTENSION_MAP: dict[str, type[FileParser]] = {
    ".txt": TxtParser,
    ".pdf": PdfParser,
    ".docx": DocxParser,
}


def get_parser(filename: str) -> FileParser:
    for ext, parser_cls in EXTENSION_MAP.items():
        if filename.lower().endswith(ext):
            return parser_cls()

    mime_type, _ = mimetypes.guess_type(filename)
    raise ValueError(f"Unsupported file type: {filename} ({mime_type})")
