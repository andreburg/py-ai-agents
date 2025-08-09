from abc import ABC, abstractmethod


class FileParser(ABC):
    @abstractmethod
    def extract_text(self, file_bytes: bytes) -> str:
        pass
