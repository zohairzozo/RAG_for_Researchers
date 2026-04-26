from __future__ import annotations

import pandas as pd
import streamlit as st

from src.database.paper_repository import list_papers


def render_library_page() -> None:
    st.title("🗂️ Paper Library")
    papers = list_papers()

    if not papers:
        st.info("No papers indexed yet. Upload PDFs first.")
        return

    df = pd.DataFrame(papers)
    st.dataframe(df, use_container_width=True, hide_index=True)
