import streamlit as st


def render_home_page() -> None:
    st.title("📚 Research RAG MVP")
    st.write(
        """
        This MVP helps researchers upload papers, build a personal knowledge base,
        and ask citation-grounded questions over the uploaded PDFs.
        """
    )

    st.subheader("What works now")
    st.markdown(
        """
        - Upload PDF research papers
        - Extract and clean text
        - Chunk pages into searchable passages
        - Generate local embeddings
        - Store chunks in ChromaDB
        - Ask questions with source citations
        - Search arXiv and Semantic Scholar metadata
        """
    )

    st.subheader("Recommended workflow")
    st.markdown(
        """
        1. Go to **Upload Papers**.
        2. Upload one or more PDFs.
        3. Click **Ingest uploaded PDFs**.
        4. Go to **Ask Questions**.
        5. Ask questions about your papers.
        """
    )

    st.info(
        "Development done by Zohair Ahmed"
    )
