from __future__ import annotations

from pathlib import Path

from src.ingestion.pdf_loader import PageText
from src.utils.id_utils import file_hash
from src.utils.text_utils import normalize_whitespace


def guess_title_from_first_page(pages: list[PageText], fallback: str) -> str:
    """Very simple title heuristic for MVP.

    Later we can replace this with GROBID or Crossref DOI metadata.
    """
    if not pages:
        return fallback

    lines = [normalize_whitespace(line) for line in pages[0].text.splitlines()]
    lines = [line for line in lines if len(line) >= 8]

    # Research paper title is often among the first meaningful lines.
    for line in lines[:15]:
        lower = line.lower()
        if not any(skip in lower for skip in ["abstract", "keywords", "arxiv", "doi"]):
            return line[:250]

    return fallback


def extract_basic_metadata(pdf_path: str | Path, pages: list[PageText]) -> dict:
    pdf_path = Path(pdf_path)
    paper_id = file_hash(pdf_path)
    fallback_title = pdf_path.stem.replace("_", " ")

    return {
        "paper_id": paper_id,
        "title": guess_title_from_first_page(pages, fallback=fallback_title),
        "file_name": pdf_path.name,
        "file_path": str(pdf_path),
        "num_pages": len(pages),
    }
