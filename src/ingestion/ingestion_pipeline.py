from __future__ import annotations

from pathlib import Path

from src.database.paper_repository import upsert_paper
from src.embeddings.embedding_model import embed_texts
from src.ingestion.chunker import chunk_pages
from src.ingestion.metadata_extractor import extract_basic_metadata
from src.ingestion.pdf_loader import load_pdf_pages
from src.vectorstore.chroma_store import upsert_chunks


def ingest_pdf(pdf_path: str | Path) -> dict:
    """Full MVP ingestion pipeline.

    PDF -> pages -> metadata -> chunks -> embeddings -> ChromaDB + SQLite.
    """
    pages = load_pdf_pages(pdf_path)
    metadata = extract_basic_metadata(pdf_path, pages)

    chunks = chunk_pages(
        pages=pages,
        paper_id=metadata["paper_id"],
        title=metadata["title"],
    )

    embeddings = embed_texts([chunk.text for chunk in chunks])
    upsert_chunks(chunks, embeddings)

    upsert_paper(
        paper_id=metadata["paper_id"],
        title=metadata["title"],
        file_name=metadata["file_name"],
        file_path=metadata["file_path"],
        num_pages=metadata["num_pages"],
        num_chunks=len(chunks),
    )

    return {
        **metadata,
        "num_chunks": len(chunks),
    }
