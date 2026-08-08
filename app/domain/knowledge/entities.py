"""Immutable repository knowledge entities."""

from dataclasses import dataclass, field
from pathlib import PurePosixPath

from app.domain.knowledge.evidence import KnowledgeEvidence


@dataclass(frozen=True, slots=True)
class Knowledge:
    """Represent normalized knowledge derived from a source path."""

    name: str
    source: PurePosixPath


@dataclass(frozen=True, slots=True)
class Technology(Knowledge):
    """Represent a detected programming technology."""


@dataclass(frozen=True, slots=True)
class Framework(Knowledge):
    """Represent a detected application framework or tool."""


@dataclass(frozen=True, slots=True)
class Container(Knowledge):
    """Represent a detected container technology."""


@dataclass(frozen=True, slots=True)
class CIPlatform(Knowledge):
    """Represent a detected continuous-integration platform."""


@dataclass(frozen=True, slots=True)
class KnowledgeCandidate:
    """Raw knowledge extracted from repository content."""

    category: str
    value: str
    confidence: float
    source: PurePosixPath
    evidence: KnowledgeEvidence | None = None


@dataclass(slots=True)
class KnowledgeRegistry:
    """Structured repository knowledge."""

    categories: dict[
        str,
        list[KnowledgeCandidate],
    ] = field(default_factory=dict)

    def add(
        self,
        candidate: KnowledgeCandidate,
    ) -> None:
        """Register a knowledge candidate."""

        self.categories.setdefault(
            candidate.category,
            [],
        ).append(candidate)

    def get(
        self,
        category: str,
    ) -> tuple[KnowledgeCandidate, ...]:
        """Return all candidates of one category."""

        return tuple(
            self.categories.get(
                category,
                [],
            )
        )

    def all(
        self,
    ) -> dict[
        str,
        tuple[KnowledgeCandidate, ...],
    ]:
        """Return every stored category."""

        return {key: tuple(value) for key, value in self.categories.items()}
