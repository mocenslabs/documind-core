"""Local filesystem scanner."""

from __future__ import annotations

from pathlib import Path

from app.domain.repository.entities import RepositorySnapshot
from app.domain.scanner.entities import ScanDocument, ScanResult
from app.domain.scanner.interfaces import Scanner

_SUPPORTED_FILES = frozenset(
    {
        "README.md",
        "pyproject.toml",
        "requirements.txt",
        "package.json",
        "Dockerfile",
        "docker-compose.yml",
    }
)


class LocalScanner(Scanner):
    """Read supported repository documents from disk."""

    def scan(self, snapshot: RepositorySnapshot) -> ScanResult:
        """Read known repository files."""

        documents: list[ScanDocument] = []

        for relative_path in snapshot.files:
            if relative_path.name not in _SUPPORTED_FILES:
                continue

            absolute_path = snapshot.root_path / Path(relative_path)

            if not absolute_path.exists():
                continue

            content = absolute_path.read_text(
                encoding="utf-8",
                errors="ignore",
            )

            documents.append(
                ScanDocument(
                    path=relative_path,
                    content=content,
                )
            )

        return ScanResult(
            documents=tuple(documents),
        )
