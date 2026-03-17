import os
from dotenv import load_dotenv
from langfuse import get_client

load_dotenv()

langfuse = get_client()

def fetch_prompts(system_prompt_name: str, user_prompt_name: str, context: str, question: str) -> tuple[str, str]:
    system_prompt = langfuse.get_prompt(system_prompt_name)
    user_prompt = langfuse.get_prompt(user_prompt_name)

    compiled_system_prompt = system_prompt.compile()
    compiled_user_prompt = user_prompt.compile(
        context=context,
        question=question,
    )

    return compiled_system_prompt, compiled_user_prompt