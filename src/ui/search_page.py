from __future__ import annotations

import streamlit as st

from src.search.search_router import search_papers
from src.ui.components import paper_result_card


def render_search_page() -> None:
    st.title("🔎 Search Papers")
    st.write(
        "Search paper metadata from arXiv and Semantic Scholar. "
        "For MVP ingestion, download the PDF manually and upload it in Upload Papers."
    )

    query = st.text_input("Search query", placeholder="physics informed neural networks crack detection")
    source = st.selectbox("Source", ["arxiv", "semantic_scholar", "all"])
    limit = st.slider("Number of results", min_value=3, max_value=20, value=5)

    if st.button("Search", type="primary", disabled=not query.strip()):
        with st.spinner("Searching scholarly metadata..."):
            results = search_papers(query=query, source=source, limit=limit)

        if not results:
            st.warning("No results found.")
            return

        for i, result in enumerate(results, start=1):
            paper_result_card(result, i)
