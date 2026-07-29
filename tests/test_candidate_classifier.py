from pathlib import PurePosixPath

from app.application.knowledge.classification import (
    CandidateClassifier,
)
from app.domain.knowledge.entities import KnowledgeCandidate


def test_group_candidates() -> None:
    classifier = CandidateClassifier()

    grouped = classifier.classify(
        (
            KnowledgeCandidate(
                category="framework",
                value="Django",
                confidence=1.0,
                source=PurePosixPath("README.md"),
            ),
            KnowledgeCandidate(
                category="framework",
                value="FastAPI",
                confidence=1.0,
                source=PurePosixPath("README.md"),
            ),
            KnowledgeCandidate(
                category="database",
                value="PostgreSQL",
                confidence=1.0,
                source=PurePosixPath("README.md"),
            ),
        )
    )

    assert len(grouped["framework"]) == 2
    assert len(grouped["database"]) == 1
