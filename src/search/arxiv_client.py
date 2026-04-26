from __future__ import annotations

import urllib.parse

import feedparser
import requests


ARXIV_API_URL = "https://export.arxiv.org/api/query"


def search_arxiv(query: str, limit: int = 5) -> list[dict]:
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": limit,
        "sortBy": "relevance",
        "sortOrder": "descending",
    }

    url = f"{ARXIV_API_URL}?{urllib.parse.urlencode(params)}"
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    feed = feedparser.parse(response.text)
    results: list[dict] = []

    for entry in feed.entries:
        pdf_url = None
        for link in entry.get("links", []):
            if link.get("type") == "application/pdf":
                pdf_url = link.get("href")

        authors = [author.name for author in entry.get("authors", [])]
        year = entry.get("published", "")[:4] or None

        results.append(
            {
                "source": "arxiv",
                "title": entry.get("title", "").replace("\n", " ").strip(),
                "authors": authors,
                "year": year,
                "abstract": entry.get("summary", "").replace("\n", " ").strip(),
                "doi": None,
                "url": entry.get("link"),
                "pdf_url": pdf_url,
            }
        )

    return results
