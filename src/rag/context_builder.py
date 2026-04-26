from __future__ import annotations


def build_context(sources: list[dict], max_chars: int = 12000) -> str:
    parts: list[str] = []
    total = 0

    for i, source in enumerate(sources, start=1):
        title = source.get("title", "Unknown title")
        page = source.get("page", "N/A")
        section = source.get("section", "Unknown")
        text = source.get("text", "")

        block = (
            f"[S{i}] Title: {title}\n"
            f"Page: {page}\n"
            f"Section: {section}\n"
            f"Text: {text}\n"
        )

        if total + len(block) > max_chars:
            break

        parts.append(block)
        total += len(block)

    return "\n---\n".join(parts)
