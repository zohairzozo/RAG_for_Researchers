from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PaperRecord:
    paper_id: str
    title: str
    file_name: str
    file_path: str
    num_pages: int
    num_chunks: int
