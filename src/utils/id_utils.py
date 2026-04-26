from __future__ import annotations

import hashlib
from pathlib import Path


def stable_hash(text: str, length: int = 16) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:length]


def file_hash(path: str | Path, length: int = 16) -> str:
    path = Path(path)
    sha = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            sha.update(block)
    return sha.hexdigest()[:length]
