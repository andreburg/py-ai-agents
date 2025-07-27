from fastapi import APIRouter

from ..application.agents.npc_agent import npc_agent
from ..domain.models.completion import Completion


chat_router = APIRouter()


@chat_router.post("/completions")
async def route_chat_completion(completion: Completion):
    agent_response = await npc_agent.run(completion.message)
    print(agent_response)
    return agent_response
