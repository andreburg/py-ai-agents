from application.services.chunk_service import ChunkService
from application.services.embedding_service import EmbeddingService


async def get_related_information(query: str) -> str:
    """Retrieve business domain information based on a query.

    Args:
        query: The search query.
    """

    embedding_service = EmbeddingService()
    chunk_service = ChunkService()

    embedding = await embedding_service.get_embedding(query)
    rows = await chunk_service.get_closest_chunks(embedding)

    return "\n\n".join(f"# {row.file_name}\n{row.content}\n" for row in rows)
