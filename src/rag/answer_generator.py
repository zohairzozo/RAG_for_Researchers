from __future__ import annotations

from openai import OpenAI

from src.config.settings import settings
from src.rag.prompt_templates import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE


def _fallback_answer(question: str, context: str) -> str:
    """Fallback when no LLM API key is available.

    This keeps the app useful locally: it retrieves sources and tells the user
    exactly which chunks look relevant.
    """
    if not context.strip():
        return (
            "I could not find relevant chunks in the current knowledge base. "
            "Please upload and ingest papers first."
        )

    return (
        "I found relevant source chunks for your question, but no OPENAI_API_KEY is configured, "
        "so I cannot generate a polished natural-language answer yet.\n\n"
        "Use the retrieved sources below to inspect the evidence. "
        "To enable generated answers, add OPENAI_API_KEY to your .env file.\n\n"
        f"Question: {question}"
    )


def generate_answer(question: str, context: str) -> str:
    if not settings.OPENAI_API_KEY:
        return _fallback_answer(question, context)

    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    prompt = USER_PROMPT_TEMPLATE.format(question=question, context=context)

    response = client.responses.create(
        model=settings.OPENAI_MODEL,
        instructions=SYSTEM_PROMPT,
        input=prompt,
    )

    return response.output_text
