from __future__ import annotations

import streamlit as st

from src.config.settings import settings
from src.rag.rag_pipeline import answer_question
from src.ui.components import source_card


def render_chat_page() -> None:
    st.title("💬 Ask Questions")
    st.write("Ask questions over your uploaded research-paper knowledge base.")

    with st.sidebar:
        st.subheader("Retrieval settings")
        top_k = st.slider("Top-k source chunks", min_value=2, max_value=12, value=settings.TOP_K)

    question = st.text_area(
        "Your question",
        placeholder="Example: What are the main limitations mentioned in these papers?",
        height=120,
    )

    if st.button("Ask", type="primary", disabled=not question.strip()):
        with st.spinner("Retrieving relevant paper chunks and generating answer..."):
            result = answer_question(question=question, top_k=top_k)

        st.subheader("Answer")
        st.write(result["answer"])

        st.subheader("Sources")
        sources = result.get("sources", [])
        if not sources:
            st.warning("No relevant sources found. Upload and ingest PDFs first.")
        for i, source in enumerate(sources, start=1):
            source_card(source, i)
