from __future__ import annotations

import requests

from src.config.settings import settings


SEMANTIC_SCHOLAR_SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search"


def search_semantic_scholar(query: str, limit: int = 5) -> list[dict]:
    headers = {}
    if settings.SEMANTIC_SCHOLAR_API_KEY:
        headers["x-api-key"] = settings.SEMANTIC_SCHOLAR_API_KEY

    params = {
        "query": query,
        "limit": limit,
        "fields": "title,authors,year,abstract,url,externalIds,openAccessPdf,citationCount",
    }

    response = requests.get(
        SEMANTIC_SCHOLAR_SEARCH_URL,
        params=params,
        headers=headers,
        timeout=30,
    )
    response.raise_for_status()

    data = response.json()
    results: list[dict] = []

    for item in data.get("data", []):
        external_ids = item.get("externalIds") or {}
        open_pdf = item.get("openAccessPdf") or {}
        authors = [a.get("name", "") for a in item.get("authors", []) if a.get("name")]

        results.append(
            {
                "source": "semantic_scholar",
                "title": item.get("title"),
                "authors": authors,
                "year": item.get("year"),
                "abstract": item.get("abstract"),
                "doi": external_ids.get("DOI"),
                "url": item.get("url"),
                "pdf_url": open_pdf.get("url"),
                "citation_count": item.get("citationCount"),
            }
        )

    return results
