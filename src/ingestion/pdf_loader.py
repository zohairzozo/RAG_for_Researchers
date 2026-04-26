from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import fitz  # PyMuPDF


@dataclass
class PageText:
    page_number: int
    text: str


def load_pdf_pages(pdf_path: str | Path) -> list[PageText]:
    """Extract text from each PDF page.

    Uses sort=True to improve natural reading order for many research PDFs.
    """
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    pages: list[PageText] = []

    with fitz.open(pdf_path) as doc:
        for page_index, page in enumerate(doc, start=1):
            text = page.get_text("text", sort=True)
            pages.append(PageText(page_number=page_index, text=text or ""))

    return pages
