from __future__ import annotations

from dataclasses import dataclass

from src.config.settings import settings
from src.ingestion.pdf_loader import PageText
from src.ingestion.text_cleaner import clean_pdf_text
from src.utils.id_utils import stable_hash


@dataclass
class TextChunk:
    chunk_id: str
    paper_id: str
    title: str
    page: int
    section: str
    text: str
    chunk_index: int


def _word_windows(words: list[str], chunk_size: int, overlap: int) -> list[list[str]]:
    if not words:
        return []

    windows: list[list[str]] = []
    start = 0
    step = max(1, chunk_size - overlap)

    while start < len(words):
        end = start + chunk_size
        window = words[start:end]
        if window:
            windows.append(window)
        if end >= len(words):
            break
        start += step

    return windows


def detect_section_name(text: str) -> str:
    """Basic section detection.

    Later we can make this better with structured parsing.
    """
    section_keywords = [
        "abstract",
        "introduction",
        "related work",
        "method",
        "methodology",
        "experiments",
        "results",
        "discussion",
        "conclusion",
        "references",
    ]

    first_lines = [line.strip() for line in text.splitlines()[:8] if line.strip()]
    for line in first_lines:
        clean = line.lower().strip(" .:-0123456789")
        for keyword in section_keywords:
            if clean == keyword or clean.startswith(keyword):
                return keyword.title()

    return "Unknown"


def chunk_pages(
    pages: list[PageText],
    paper_id: str,
    title: str,
    chunk_size_words: int | None = None,
    chunk_overlap_words: int | None = None,
) -> list[TextChunk]:
    chunk_size = chunk_size_words or settings.CHUNK_SIZE_WORDS
    overlap = chunk_overlap_words or settings.CHUNK_OVERLAP_WORDS

    chunks: list[TextChunk] = []
    chunk_index = 0

    for page in pages:
        clean_text = clean_pdf_text(page.text)
        if not clean_text:
            continue

        section = detect_section_name(clean_text)
        words = clean_text.split()
        for window in _word_windows(words, chunk_size=chunk_size, overlap=overlap):
            chunk_text = " ".join(window)
            raw_id = f"{paper_id}:{page.page_number}:{chunk_index}:{chunk_text[:80]}"
            chunk_id = stable_hash(raw_id, length=24)

            chunks.append(
                TextChunk(
                    chunk_id=chunk_id,
                    paper_id=paper_id,
                    title=title,
                    page=page.page_number,
                    section=section,
                    text=chunk_text,
                    chunk_index=chunk_index,
                )
            )
            chunk_index += 1

    return chunks
