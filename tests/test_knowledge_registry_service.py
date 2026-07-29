from pathlib import PurePosixPath

from app.application.knowledge.registry_service import (
    KnowledgeRegistryService,
)
from app.domain.knowledge.entities import KnowledgeCandidate


def test_build_registry() -> None:
    service = KnowledgeRegistryService()

    registry = service.build(
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

    assert len(registry.get("framework")) == 1
    assert len(registry.get("database")) == 1
