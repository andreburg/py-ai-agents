import asyncio
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

from application.tools.rag_tool import get_related_information
from dependencies.db import Database
from utils.vars import DATABASE_URL, MCP_NAME, MCP_HOST, MCP_PORT, MCP_TRANSPORT

load_dotenv()

mcp = FastMCP(name=MCP_NAME, port=MCP_PORT, host=MCP_HOST)

mcp.add_tool(get_related_information)


async def setup():
    await Database.connect(DATABASE_URL)


if __name__ == "__main__":
    asyncio.run(setup())
    mcp.run(transport=MCP_TRANSPORT)
