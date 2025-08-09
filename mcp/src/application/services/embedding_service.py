from langchain_ollama import OllamaEmbeddings


class EmbeddingService:
    def __init__(self):
        self._model = OllamaEmbeddings(model="nomic-embed-text")

    async def get_embedding(self, text: str) -> str:
        embedding = await self._model.aembed_query(text)
        return self.stringify_embedding(embedding)

    def stringify_embedding(self, embedding: list[float]) -> str:
        return "[" + ",".join(map(str, embedding)) + "]"
