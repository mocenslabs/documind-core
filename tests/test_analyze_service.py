from collections.abc import Sequence
from pathlib import Path, PurePosixPath

from app.application.analyze.service import AnalyzeRepositoryService
from app.application.discovery.service import DiscoveryService
from app.application.knowledge.service import KnowledgeService
from app.application.rules.service import RuleEngineService
from app.application.scanner.service import ScannerService
from app.domain.discovery.facts import FoundFile, RawFact
from app.domain.knowledge.entities import Knowledge, Technology
from app.domain.repository.entities import RepositorySnapshot
from app.domain.repository.interfaces import RepositoryLoader
from app.domain.repository.value_objects import (
    RepositoryReference,
    RepositorySnapshotRequest,
)
from app.domain.rules.interfaces import Rule
from app.domain.scanner.entities import ScanDocument, ScanResult
from app.domain.scanner.interfaces import Scanner


class FakeRepositoryLoader(RepositoryLoader):
    def load(self, request: RepositorySnapshotRequest) -> RepositorySnapshot:
        return RepositorySnapshot(
            repository=request.repository,
            root_path=Path(request.repository.locator),
            files=(PurePosixPath("README.md"),),
            directories=(),
        )


class FakeScanner(Scanner):
    def scan(self, snapshot: RepositorySnapshot) -> ScanResult:
        return ScanResult(
            documents=(
                ScanDocument(
                    path=PurePosixPath("README.md"),
                    content="# Documind",
                ),
            )
        )


class FakeDiscoveryService(DiscoveryService):
    def discover(
        self,
        repository: RepositorySnapshot,
    ) -> list[RawFact]:
        return [
            FoundFile(PurePosixPath("README.md")),
        ]


class FakeRule(Rule):
    def apply(
        self,
        facts: Sequence[RawFact],
    ) -> list[Knowledge]:
        return [
            Technology(
                name="Python",
                source=PurePosixPath("pyproject.toml"),
            )
        ]


def test_analyze_pipeline() -> None:
    request = RepositorySnapshotRequest(
        repository=RepositoryReference(locator="."),
    )

    knowledge_service = KnowledgeService(
        rule_engine=RuleEngineService(
            rules=(FakeRule(),),
        ),
    )

    service = AnalyzeRepositoryService(
        repository_loader=FakeRepositoryLoader(),
        scanner_service=ScannerService(scanner=FakeScanner()),
        discovery_service=FakeDiscoveryService(),
        knowledge_service=knowledge_service,
    )

    result = service.analyze(request)

    assert len(result.scanned_documents) == 1
    assert result.scanned_documents[0].content == "# Documind"

    assert len(result.facts) == 1
    assert len(result.knowledge) == 1
