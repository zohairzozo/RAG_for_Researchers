from __future__ import annotations

from src.rag.answer_generator import generate_answer
from src.rag.citation_formatter import format_sources_for_display
from src.rag.context_builder import build_context
from src.vectorstore.retriever import retrieve_relevant_chunks


def answer_question(question: str, top_k: int = 6) -> dict:
    sources = retrieve_relevant_chunks(question, top_k=top_k)
    context = build_context(sources)
    answer = generate_answer(question, context)

    return {
        "question": question,
        "answer": answer,
        "sources": format_sources_for_display(sources),
    }
