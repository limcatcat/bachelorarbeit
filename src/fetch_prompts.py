import os
from dotenv import load_dotenv
from langfuse import get_client

load_dotenv()

langfuse = get_client()

def fetch_prompts(
    system_prompt_name: str,
    user_prompt_name: str,
    context: str,
    question: str,
    system_prompt_content: str | None = None,
    system_prompt_compile_kwargs: dict[str, str] | None = None,
) -> tuple[str, str]:
    if system_prompt_content is not None:
        compiled_system_prompt = system_prompt_content
    else:
        system_prompt = langfuse.get_prompt(system_prompt_name)
        if system_prompt_compile_kwargs:
            compiled_system_prompt = system_prompt.compile(**system_prompt_compile_kwargs)
        else:
            compiled_system_prompt = system_prompt.compile()

    user_prompt = langfuse.get_prompt(user_prompt_name)
    compiled_user_prompt = user_prompt.compile(
        context=context,
        question=question,
    )

    return compiled_system_prompt, compiled_user_prompt