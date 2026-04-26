from __future__ import annotations

import re

from src.utils.text_utils import normalize_whitespace


def clean_pdf_text(text: str) -> str:
    """Clean common PDF extraction noise.

    This is intentionally conservative for the MVP.
    """
    if not text:
        return ""

    # Join words broken by hyphenation at line endings: "meth-\nod" -> "method"
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)

    # Normalize line breaks.
    text = text.replace("\r", "\n")

    # Remove repeated spaces.
    text = normalize_whitespace(text)

    return text
