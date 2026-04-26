from __future__ import annotations

from src.database.sqlite_db import get_connection, init_db


def upsert_paper(
    paper_id: str,
    title: str,
    file_name: str,
    file_path: str,
    num_pages: int,
    num_chunks: int,
) -> None:
    init_db()
    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO papers (
                paper_id, title, file_name, file_path, num_pages, num_chunks
            )
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(paper_id) DO UPDATE SET
                title=excluded.title,
                file_name=excluded.file_name,
                file_path=excluded.file_path,
                num_pages=excluded.num_pages,
                num_chunks=excluded.num_chunks
            """,
            (paper_id, title, file_name, file_path, num_pages, num_chunks),
        )


def list_papers() -> list[dict]:
    init_db()
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT paper_id, title, file_name, file_path, num_pages, num_chunks, created_at
            FROM papers
            ORDER BY created_at DESC
            """
        ).fetchall()

    return [dict(row) for row in rows]
