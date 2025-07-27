from pydantic_ai.providers.openai import OpenAIProvider

from src.utils.env import OPENAI_API_KEY

openai_provider = OpenAIProvider(api_key=OPENAI_API_KEY)
