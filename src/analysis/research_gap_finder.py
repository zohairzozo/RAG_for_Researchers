from __future__ import annotations

from src.rag.rag_pipeline import answer_question


def find_research_gaps() -> dict:
    return answer_question(
        "Identify possible research gaps, open problems, and future work directions from the uploaded papers.",
        top_k=12,
    )
