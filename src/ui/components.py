from __future__ import annotations

import streamlit as st


def source_card(source: dict, index: int) -> None:
    """Render one retrieved source chunk."""
    title = source.get("title") or "Unknown title"
    page = source.get("page")
    section = source.get("section") or "Unknown section"
    score = source.get("score")

    label = f"Source {index}: {title}"
    with st.expander(label, expanded=index == 1):
        st.caption(f"Page: {page} | Section: {section} | Similarity score: {score}")
        st.write(source.get("text", ""))


def paper_result_card(result: dict, index: int) -> None:
    """Render one metadata search result."""
    with st.container(border=True):
        st.markdown(f"### {index}. {result.get('title', 'Untitled')}")
        st.caption(
            f"Year: {result.get('year', 'N/A')} | "
            f"Source: {result.get('source', 'N/A')} | "
            f"DOI: {result.get('doi', 'N/A')}"
        )
        authors = result.get("authors") or []
        if authors:
            st.write("**Authors:** " + ", ".join(authors[:8]))
        abstract = result.get("abstract") or "No abstract available."
        st.write(abstract[:1200] + ("..." if len(abstract) > 1200 else ""))
        if result.get("url"):
            st.link_button("Open source page", result["url"])
        if result.get("pdf_url"):
            st.link_button("Open PDF", result["pdf_url"])
