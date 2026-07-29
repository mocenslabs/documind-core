from pathlib import PurePosixPath

from app.application.knowledge.classification import (
    CandidateClassifier,
)
from app.application.knowledge.service import (
    KnowledgeClassificationService,
)
from app.domain.knowledge.entities import KnowledgeCandidate


def test_classification_service() -> None:
    service = KnowledgeClassificationService(
        classifier=CandidateClassifier(),
    )

    result = service.classify(
        (
            KnowledgeCandidate(
                category="framework",
                value="Django",
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

    assert "framework" in result.categories
    assert "database" in result.categories
