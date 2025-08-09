import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


def get_var(name: str, fallback: Optional[str] = None):
    environment_variable = os.environ.get(name) or fallback
    assert environment_variable
    return environment_variable


OPENAI_API_KEY = get_var("OPENAI_API_KEY")
DATABASE_URL = get_var("DATABASE_URL")
