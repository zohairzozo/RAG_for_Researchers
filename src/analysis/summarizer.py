from __future__ import annotations

from src.rag.rag_pipeline import answer_question


def summarize_current_library() -> dict:
    return answer_question(
        "Summarize the main contributions, methods, results, and limitations of the uploaded papers.",
        top_k=10,
    )
