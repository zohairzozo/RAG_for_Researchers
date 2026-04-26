from __future__ import annotations

import streamlit as st

from src.config.settings import settings
from src.ingestion.ingestion_pipeline import ingest_pdf
from src.utils.file_utils import save_uploaded_file


def render_upload_page() -> None:
    st.title("⬆️ Upload Papers")
    st.write("Upload PDF papers to add them to your personal RAG knowledge base.")

    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True,
    )

    if not uploaded_files:
        st.info("Upload at least one PDF to begin.")
        return

    st.write(f"Selected files: {len(uploaded_files)}")
    for file in uploaded_files:
        st.caption(file.name)

    if st.button("Ingest uploaded PDFs", type="primary"):
        progress = st.progress(0)
        status = st.empty()

        for i, uploaded_file in enumerate(uploaded_files, start=1):
            status.write(f"Processing {uploaded_file.name}...")
            saved_path = save_uploaded_file(uploaded_file, settings.UPLOAD_DIR)

            try:
                result = ingest_pdf(saved_path)
                st.success(
                    f"Indexed: {result['title']} | "
                    f"Pages: {result['num_pages']} | "
                    f"Chunks: {result['num_chunks']}"
                )
            except Exception as exc:
                st.error(f"Failed to ingest {uploaded_file.name}: {exc}")

            progress.progress(i / len(uploaded_files))

        status.write("Done.")
