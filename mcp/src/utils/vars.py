import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


def get_environment_variable(name: str, fallback: Optional[str] = None):
    environment_variable = os.environ.get(name) or fallback
    assert environment_variable
    return environment_variable


MCP_TRANSPORT = "streamable-http"

MCP_NAME = get_environment_variable("MCP_NAME")

MCP_PORT = int(get_environment_variable("MCP_PORT"))
MCP_HOST = get_environment_variable("MCP_HOST")

DATABASE_URL = get_environment_variable("DATABASE_URL")
