from __future__ import annotations


def format_sources_for_display(sources: list[dict]) -> list[dict]:
    formatted: list[dict] = []
    for i, source in enumerate(sources, start=1):
        formatted.append(
            {
                "source_id": f"S{i}",
                "title": source.get("title", "Unknown title"),
                "page": source.get("page", "N/A"),
                "section": source.get("section", "Unknown"),
                "score": source.get("score"),
                "text": source.get("text", ""),
                "paper_id": source.get("paper_id"),
                "chunk_index": source.get("chunk_index"),
            }
        )
    return formatted
