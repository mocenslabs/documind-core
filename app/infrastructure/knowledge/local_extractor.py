"""Local repository knowledge extractor."""

from __future__ import annotations

import re
from pathlib import PurePosixPath

from app.domain.knowledge.entities import KnowledgeCandidate
from app.domain.knowledge.interfaces import KnowledgeExtractor
from app.domain.parser.entities import ParsedDocument


class LocalKnowledgeExtractor(KnowledgeExtractor):
    """Extract repository knowledge from parsed documents."""

    _PATTERNS: tuple[tuple[str, str, str], ...] = (
        # Frameworks
        ("framework", r"\bdjango\b", "Django"),
        (
            "framework",
            r"\bdjango[\s_-]?rest[\s_-]?framework\b|\brest_framework\b",
            "Django REST Framework",
        ),
        ("framework", r"\bfastapi\b", "FastAPI"),
        ("framework", r"\bflask\b", "Flask"),
        ("framework", r"\bvue(?:\.js)?\b", "Vue"),
        ("framework", r"\breact(?:\.js)?\b", "React"),
        ("framework", r"\bangular(?:\.js)?\b", "Angular"),
        # Databases
        ("database", r"\bpostgres(?:ql)?\b", "PostgreSQL"),
        ("database", r"\bmysql\b", "MySQL"),
        ("database", r"\bsqlite\b", "SQLite"),
        ("database", r"\bredis\b", "Redis"),
        # Containers
        ("container", r"\bdocker\b", "Docker"),
        (
            "container",
            r"\bdocker[\s_-]?compose\b",
            "Docker Compose",
        ),
        # CI
        (
            "ci",
            r"\bgithub[\s_-]+actions\b",
            "GitHub Actions",
        ),
        # Tools
        ("tool", r"\bruff\b", "Ruff"),
        ("tool", r"\bblack\b", "Black"),
        ("tool", r"\bpytest\b", "Pytest"),
        ("tool", r"\bmypy\b", "Mypy"),
        ("tool", r"\bcelery\b", "Celery"),
        # Runtime / frontend tooling
        ("runtime", r"\bnode(?:\.js)?\b", "Node.js"),
        ("tool", r"\bvite\b", "Vite"),
    )

    _HIGH_CONFIDENCE_FILENAMES = frozenset(
        {
            "pyproject.toml",
            "requirements.txt",
            "requirements-dev.txt",
            "package.json",
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

    def extract(
        self,
        documents: tuple[ParsedDocument, ...],
    ) -> list[KnowledgeCandidate]:
        """Extract candidate knowledge."""

        candidates: list[KnowledgeCandidate] = []

        for document in documents:
            text = document.plain_text.lower()
            confidence = self._confidence_for(document.path)

            for category, pattern, value in self._PATTERNS:
                if not re.search(pattern, text):
                    continue

                candidates.append(
                    KnowledgeCandidate(
                        category=category,
                        value=value,
                        confidence=confidence,
                        source=document.path,
                    )
                )

        return candidates

    @classmethod
    def _confidence_for(
        cls,
        path: PurePosixPath,
    ) -> float:
        """Return extraction confidence based on source quality."""

        if path.name in cls._HIGH_CONFIDENCE_FILENAMES:
            return 1.0

        if path.name == "README.md":
            return 0.9

        return 0.7
