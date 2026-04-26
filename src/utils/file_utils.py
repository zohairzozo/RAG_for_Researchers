from __future__ import annotations

import re
from pathlib import Path

import streamlit as st


def safe_filename(filename: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9_.-]+", "_", filename.strip())
    return name or "uploaded_file.pdf"


def save_uploaded_file(uploaded_file: st.runtime.uploaded_file_manager.UploadedFile, target_dir: Path) -> Path:
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / safe_filename(uploaded_file.name)

    with path.open("wb") as f:
        f.write(uploaded_file.getbuffer())

    return path
