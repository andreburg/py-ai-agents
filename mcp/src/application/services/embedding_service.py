from openai import AsyncOpenAI


class EmbeddingService:
    def __init__(self):
        self._model = AsyncOpenAI()

    async def get_embedding(self, text: str) -> str:
        response = await self._model.embeddings.create(input=text, model="text-embedding-3-small")
        embedding = response.data[0].embedding
        return self.stringify_embedding(embedding)

    def stringify_embedding(self, embedding: list[float]) -> str:
        return "[" + ",".join(map(str, embedding)) + "]"
