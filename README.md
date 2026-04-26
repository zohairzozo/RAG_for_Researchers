# Research RAG MVP

A Python + Streamlit MVP for a research-paper RAG assistant.

## What this MVP does

- Upload PDF research papers.
- Extract page-wise text with PyMuPDF.
- Clean and chunk paper text.
- Embed chunks with SentenceTransformers.
- Store chunks in ChromaDB.
- Ask questions over your personal paper knowledge base.
- Return answers with source chunks/citations.
- Search arXiv and Semantic Scholar metadata.

## What this MVP does not do yet

- It does not scrape Google Scholar.
- It does not do OCR for scanned PDFs.
- It does not parse equations/tables perfectly.
- It does not implement multi-user authentication.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

Optional, for generated answers:

```bash
cp .env.example .env
# add your OPENAI_API_KEY inside .env
```

## Run

```bash
streamlit run app.py
```

## MVP workflow

1. Open the Streamlit app.
2. Go to **Upload Papers**.
3. Upload one or more PDFs.
4. Click **Ingest uploaded PDFs**.
5. Go to **Ask Questions**.
6. Ask questions about the uploaded papers.

## Suggested first test questions

- What is the main contribution of these papers?
- What methods are used?
- What datasets or experiments are reported?
- What limitations are mentioned?
- What are possible research gaps?
