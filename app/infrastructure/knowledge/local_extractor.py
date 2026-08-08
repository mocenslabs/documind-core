"""Local repository knowledge extractor."""

from __future__ import annotations

import re

from app.domain.knowledge.entities import KnowledgeCandidate
from app.domain.knowledge.evidence import KnowledgeEvidence
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
        ("container", r"\bdocker[\s_-]?compose\b", "Docker Compose"),
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

    def extract(
        self,
        documents: tuple[ParsedDocument, ...],
    ) -> list[KnowledgeCandidate]:
        """Extract candidate knowledge."""

        candidates: list[KnowledgeCandidate] = []

        for document in documents:
            text = document.plain_text.lower()

            for category, pattern, value in self._PATTERNS:
                if not re.search(pattern, text):
                    continue

                evidence = self._build_evidence(
                    document,
                    value,
                )

                candidates.append(
                    KnowledgeCandidate(
                        category=category,
                        value=value,
                        confidence=self._confidence_for_evidence(
                            evidence,
                        ),
                        source=document.path,
                        evidence=evidence,
                    )
                )

        return candidates

    def _build_evidence(
        self,
        document: ParsedDocument,
        value: str,
    ) -> KnowledgeEvidence:
        """Build evidence describing how a candidate was detected."""

        if document.path.name in {
            "pyproject.toml",
            "requirements.txt",
            "package.json",
        }:
            return KnowledgeEvidence(
                source=document.path,
                kind="dependency",
                value=value,
            )

        return KnowledgeEvidence(
            source=document.path,
            kind="content",
            value=value,
        )

    def _confidence_for_evidence(
        self,
        evidence: KnowledgeEvidence,
    ) -> float:
        """Determine confidence from evidence strength."""

        if evidence.kind in {
            "dependency",
            "configuration",
        }:
            return 1.0

        return 0.9
