from pathlib import PurePosixPath

from app.application.knowledge.deduplication import (
    CandidateDeduplicator,
)
from app.domain.knowledge.entities import KnowledgeCandidate


def test_remove_duplicates() -> None:
    deduplicator = CandidateDeduplicator()

    result = deduplicator.deduplicate(
        (
            KnowledgeCandidate(
                category="framework",
                value="Django",
                confidence=1.0,
                source=PurePosixPath("README.md"),
            ),
            KnowledgeCandidate(
                category="framework",
                value="Django",
                confidence=1.0,
                source=PurePosixPath("pyproject.toml"),
            ),
            KnowledgeCandidate(
                category="database",
                value="PostgreSQL",
                confidence=1.0,
                source=PurePosixPath("README.md"),
            ),
        )
    )

    assert len(result) == 2
