"""Local filesystem scanner."""

from __future__ import annotations

from pathlib import Path, PurePosixPath

from app.domain.repository.entities import RepositorySnapshot
from app.domain.scanner.entities import ScanDocument, ScanResult
from app.domain.scanner.interfaces import Scanner

_SUPPORTED_FILENAMES = frozenset(
    {
        "README.md",
        "README",
        "pyproject.toml",
        "requirements.txt",
        "requirements-dev.txt",
        "package.json",
        "package-lock.json",
        "pnpm-lock.yaml",
        "yarn.lock",
        "Dockerfile",
        "docker-compose.yml",
        "docker-compose.yaml",
        "compose.yml",
        "compose.yaml",
        "vite.config.js",
        "vite.config.ts",
        "vite.config.mjs",
        "vite.config.cjs",
        "manage.py",
    }
)

_SUPPORTED_SUFFIXES = frozenset(
    {
        ".yaml",
        ".yml",
    }
)


class LocalScanner(Scanner):
    """Read supported repository documents from disk."""

    def scan(
        self,
        snapshot: RepositorySnapshot,
    ) -> ScanResult:
        """Read known repository files."""

        documents: list[ScanDocument] = []

        for relative_path in snapshot.files:
            if not self._is_supported(relative_path):
                continue

            absolute_path = snapshot.root_path / Path(relative_path)

            if not absolute_path.is_file():
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

    @staticmethod
    def _is_supported(
        relative_path: PurePosixPath,
    ) -> bool:
        """Return whether a repository file should be scanned."""

        if relative_path.name in _SUPPORTED_FILENAMES:
            return True

        return relative_path.suffix.lower() in _SUPPORTED_SUFFIXES
