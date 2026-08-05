"""Local repository knowledge extractor."""

from __future__ import annotations

from app.domain.knowledge.entities import KnowledgeCandidate
from app.domain.knowledge.interfaces import KnowledgeExtractor
from app.domain.parser.entities import ParsedDocument


class LocalKnowledgeExtractor(KnowledgeExtractor):
    """Extract basic knowledge from parsed repository documents."""

    _PATTERNS: tuple[tuple[str, str, str], ...] = (
        # Frameworks
        ("framework", "django", "Django"),
        ("framework", "djangorestframework", "Django REST Framework"),
        ("framework", "rest_framework", "Django REST Framework"),
        ("framework", "fastapi", "FastAPI"),
        ("framework", "flask", "Flask"),
        ("framework", "vue", "Vue"),
        ("framework", "react", "React"),
        ("framework", "angular", "Angular"),
        # Databases
        ("database", "postgres", "PostgreSQL"),
        ("database", "postgresql", "PostgreSQL"),
        ("database", "mysql", "MySQL"),
        ("database", "sqlite", "SQLite"),
        ("database", "redis", "Redis"),
        # Containers
        ("container", "docker", "Docker"),
        ("container", "docker compose", "Docker Compose"),
        # CI
        ("ci", "github actions", "GitHub Actions"),
        # Tools
        ("tool", "ruff", "Ruff"),
        ("tool", "black", "Black"),
        ("tool", "pytest", "Pytest"),
        ("tool", "mypy", "Mypy"),
        ("tool", "celery", "Celery"),
    )

    def extract(
        self,
        documents: tuple[ParsedDocument, ...],
    ) -> list[KnowledgeCandidate]:
        """Extract candidate knowledge."""

        candidates: list[KnowledgeCandidate] = []

        for document in documents:
            text = document.plain_text.lower()

            for category, pattern, value in self._PATTERNS:
                if pattern not in text:
                    continue

                candidates.append(
                    KnowledgeCandidate(
                        category=category,
                        value=value,
                        confidence=1.0,
                        source=document.path,
                    )
                )

        return candidates
