from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

from .providers import openai_provider

model = OpenAIModel("gpt-4.1-nano", provider=openai_provider)
npc_agent = Agent(model)
