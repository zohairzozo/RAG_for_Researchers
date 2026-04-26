from src.ingestion.chunker import chunk_pages
from src.ingestion.pdf_loader import PageText


def test_chunk_pages_creates_chunks():
    pages = [PageText(page_number=1, text="Introduction\n" + "word " * 700)]
    chunks = chunk_pages(
        pages=pages,
        paper_id="p1",
        title="Test Paper",
        chunk_size_words=100,
        chunk_overlap_words=20,
    )
    assert len(chunks) > 1
    assert chunks[0].paper_id == "p1"
