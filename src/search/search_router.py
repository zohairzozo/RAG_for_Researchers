from __future__ import annotations

from src.search.arxiv_client import search_arxiv
from src.search.semantic_scholar_client import search_semantic_scholar


def search_papers(query: str, source: str = "all", limit: int = 5) -> list[dict]:
    source = source.lower().strip()

    if source == "arxiv":
        return search_arxiv(query, limit=limit)

    if source == "semantic_scholar":
        return search_semantic_scholar(query, limit=limit)

    if source == "all":
        per_source = max(1, limit // 2)
        results: list[dict] = []
        errors: list[str] = []

        for fn in [search_arxiv, search_semantic_scholar]:
            try:
                results.extend(fn(query, limit=per_source))
            except Exception as exc:
                errors.append(str(exc))

        return results[:limit]

    raise ValueError(f"Unknown source: {source}")
