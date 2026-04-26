from __future__ import annotations

from src.rag.rag_pipeline import answer_question


def extract_methods() -> dict:
    return answer_question(
        "Extract the methods, models, equations, datasets, boundary conditions, and evaluation metrics mentioned in the uploaded papers.",
        top_k=12,
    )
