from __future__ import annotations

from src.rag.rag_pipeline import answer_question


def draft_literature_review_notes() -> dict:
    return answer_question(
        "Draft structured literature review notes from the uploaded papers with themes, methods, limitations, and research gaps.",
        top_k=12,
    )
