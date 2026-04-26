from __future__ import annotations

from src.rag.rag_pipeline import answer_question


def compare_papers() -> dict:
    return answer_question(
        "Compare the uploaded papers in terms of problem, method, data, results, and limitations.",
        top_k=12,
    )
