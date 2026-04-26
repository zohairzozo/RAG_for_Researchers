from __future__ import annotations

from src.embeddings.embedding_model import embed_query
from src.embeddings.reranker import simple_rerank
from src.vectorstore.chroma_store import query_collection


def retrieve_relevant_chunks(question: str, top_k: int = 6) -> list[dict]:
    query_embedding = embed_query(question)
    results = query_collection(query_embedding=query_embedding, top_k=top_k)
    return simple_rerank(results)
