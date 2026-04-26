from __future__ import annotations

from typing import Any

import chromadb

from src.config.settings import settings
from src.ingestion.chunker import TextChunk


def get_chroma_client() -> chromadb.PersistentClient:
    return chromadb.PersistentClient(path=str(settings.VECTOR_STORE_DIR))


def get_collection():
    client = get_chroma_client()
    return client.get_or_create_collection(
        name=settings.COLLECTION_NAME,
        metadata={"description": "Research paper chunks"},
    )


def chunk_to_metadata(chunk: TextChunk) -> dict[str, Any]:
    return {
        "paper_id": chunk.paper_id,
        "title": chunk.title,
        "page": chunk.page,
        "section": chunk.section,
        "chunk_index": chunk.chunk_index,
    }


def upsert_chunks(chunks: list[TextChunk], embeddings: list[list[float]]) -> None:
    if not chunks:
        return

    if len(chunks) != len(embeddings):
        raise ValueError("Number of chunks and embeddings must match.")

    collection = get_collection()

    collection.upsert(
        ids=[chunk.chunk_id for chunk in chunks],
        documents=[chunk.text for chunk in chunks],
        embeddings=embeddings,
        metadatas=[chunk_to_metadata(chunk) for chunk in chunks],
    )


def query_collection(query_embedding: list[float], top_k: int) -> list[dict]:
    collection = get_collection()

    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    documents = result.get("documents", [[]])[0]
    metadatas = result.get("metadatas", [[]])[0]
    distances = result.get("distances", [[]])[0]
    ids = result.get("ids", [[]])[0]

    records: list[dict] = []
    for doc_id, text, metadata, distance in zip(ids, documents, metadatas, distances):
        # Chroma distance is smaller when closer. Convert to a simple similarity-like score.
        score = round(1.0 / (1.0 + float(distance)), 4)
        records.append(
            {
                "id": doc_id,
                "text": text,
                "score": score,
                **(metadata or {}),
            }
        )

    return records
