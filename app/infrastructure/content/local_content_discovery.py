"""Local content discovery engine."""

from __future__ import annotations

from app.domain.content.entities import ContentMatch
from app.domain.content.interfaces import ContentDiscoveryEngine
from app.domain.parser.entities import ParsedDocument


class LocalContentDiscovery(ContentDiscoveryEngine):
    """Extract structured information from parsed documents."""

    _KEYWORDS: dict[str, tuple[str, ...]] = {
        "python": ("python",),
        "django": ("django",),
        "fastapi": ("fastapi",),
        "flask": ("flask",),
        "vue": ("vue",),
        "react": ("react",),
        "docker": ("docker",),
        "postgresql": ("postgres", "postgresql"),
        "redis": ("redis",),
        "celery": ("celery",),
        "openai": ("openai",),
        "anthropic": ("anthropic",),
        "ollama": ("ollama",),
        "langchain": ("langchain",),
        "chromadb": ("chromadb",),
        "qdrant": ("qdrant",),
        "milvus": ("milvus",),
    }

    def discover(
        self,
        documents: tuple[ParsedDocument, ...],
    ) -> list[ContentMatch]:
        """Extract deterministic knowledge from parsed documents."""

        matches: list[ContentMatch] = []

        for document in documents:
            content = document.plain_text.lower()

            for category, keywords in self._KEYWORDS.items():
                if any(keyword in content for keyword in keywords):
                    matches.append(
                        ContentMatch(
                            category="technology",
                            value=category,
                            source=document,
                        )
                    )

        return matches
