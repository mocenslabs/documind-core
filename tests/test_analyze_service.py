from __future__ import annotations

from pathlib import PurePosixPath

from app.application.analyze.service import AnalyzeRepositoryService
from app.domain.discovery.facts import FoundFile, RawFact
from app.domain.knowledge.entities import Knowledge, Technology
from app.domain.repository.entities import RepositorySnapshot
from app.domain.repository.value_objects import (
    RepositoryReference,
    RepositorySnapshotRequest,
)


class FakeRepositoryLoader:
    def load(self, request: RepositorySnapshotRequest) -> RepositorySnapshot:
        return RepositorySnapshot(
            repository=request.repository,
            root_path=request.repository.locator,  # type: ignore[arg-type]
            files=(PurePosixPath("pyproject.toml"),),
            directories=(),
        )


class FakeDiscoveryService:
    def discover(self, snapshot: RepositorySnapshot) -> list[RawFact]:
        return [
            FoundFile(PurePosixPath("pyproject.toml")),
        ]


class FakeKnowledgeService:
    def build(self, facts: list[RawFact]) -> list[Knowledge]:
        return [
            Technology(
                name="Python",
                source=PurePosixPath("pyproject.toml"),
            )
        ]


def test_analyze_pipeline() -> None:
    request = RepositorySnapshotRequest(repository=RepositoryReference(locator="."))

    service = AnalyzeRepositoryService(
        repository_loader=FakeRepositoryLoader(),  # type: ignore[arg-type]
        discovery_service=FakeDiscoveryService(),  # type: ignore[arg-type]
        knowledge_service=FakeKnowledgeService(),  # type: ignore[arg-type]
    )

    result = service.analyze(request)

    assert len(result.facts) == 1
    assert len(result.knowledge) == 1
