import streamlit as st  # type: ignore

from src.config.settings import settings
from src.database.sqlite_db import init_db
from src.ui.home import render_home_page
from src.ui.upload_page import render_upload_page
from src.ui.chat_page import render_chat_page
from src.ui.paper_library_page import render_library_page
from src.ui.search_page import render_search_page
from dotenv import load_dotenv  # type: ignore

load_dotenv()


def main() -> None:
    st.set_page_config(
        page_title=settings.APP_NAME,
        page_icon="📚",
        layout="wide",
    )

    init_db()

    st.sidebar.title("📚 Research RAG")
    page = st.sidebar.radio(
        "Navigation",
        [
            "Home",
            "Upload Papers",
            "Ask Questions",
            "Paper Library",
            "Search Papers",
        ],
    )

    st.sidebar.divider()
    st.sidebar.caption("MVP: local PDFs + embeddings + ChromaDB + citations")

    if page == "Home":
        render_home_page()
    elif page == "Upload Papers":
        render_upload_page()
    elif page == "Ask Questions":
        render_chat_page()
    elif page == "Paper Library":
        render_library_page()
    elif page == "Search Papers":
        render_search_page()


if __name__ == "__main__":
    main()
