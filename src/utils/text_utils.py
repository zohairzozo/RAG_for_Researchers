from __future__ import annotations

import re


def normalize_whitespace(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def short_text(text: str, max_chars: int = 500) -> str:
    text = normalize_whitespace(text)
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "..."
