from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Central app settings.

    Keep MVP settings here so every module uses the same paths and model names.
    """

    APP_NAME: str = "Research RAG MVP"

    BASE_DIR: Path = Path(__file__).resolve().parents[2]
    DATA_DIR: Path = BASE_DIR / "data"
    UPLOAD_DIR: Path = DATA_DIR / "uploads"
    RAW_PAPERS_DIR: Path = DATA_DIR / "raw_papers"
    PROCESSED_DIR: Path = DATA_DIR / "processed"
    VECTOR_STORE_DIR: Path = DATA_DIR / "vector_store"
    SQLITE_PATH: Path = DATA_DIR / "research_rag.sqlite3"

    COLLECTION_NAME: str = "research_papers"

    EMBEDDING_MODEL_NAME: str = os.getenv(
        "EMBEDDING_MODEL_NAME",
        "sentence-transformers/all-MiniLM-L6-v2",
    )

    CHUNK_SIZE_WORDS: int = int(os.getenv("CHUNK_SIZE_WORDS", "280"))
    CHUNK_OVERLAP_WORDS: int = int(os.getenv("CHUNK_OVERLAP_WORDS", "60"))
    TOP_K: int = int(os.getenv("TOP_K", "6"))

    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY") or None
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    SEMANTIC_SCHOLAR_API_KEY: str | None = os.getenv("SEMANTIC_SCHOLAR_API_KEY") or None

    def create_dirs(self) -> None:
        for path in [
            self.DATA_DIR,
            self.UPLOAD_DIR,
            self.RAW_PAPERS_DIR,
            self.PROCESSED_DIR,
            self.VECTOR_STORE_DIR,
        ]:
            path.mkdir(parents=True, exist_ok=True)


settings = Settings()
settings.create_dirs()
