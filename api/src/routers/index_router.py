from fastapi import APIRouter

from .chat_router import chat_router


index_router = APIRouter()

index_router.include_router(chat_router, prefix="/chat")
