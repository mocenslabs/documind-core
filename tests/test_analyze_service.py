from pathlib import Path, PurePosixPath

from app.application.analyze.service import AnalyzeRepositoryService
from app.application.inference.models import InferenceResponse
from app.application.knowledge.graph_builder import KnowledgeGraphBuilder
from app.application.knowledge.registry_service import KnowledgeRegistryService
from app.application.knowledge.relationship_builder import (
    KnowledgeRelationshipBuilder,
)
from app.application.knowledge.service import KnowledgeExtractionService
from app.application.parser.service import ParserService
from app.application.recommendation.models import RecommendationResponse
from app.application.scanner.service import ScannerService
from app.domain.discovery.facts import FoundFile
from app.domain.inference.entities import Observation
from app.domain.knowledge.entities import (
    KnowledgeCandidate,
    Technology,
)
from app.domain.knowledge.graph import KnowledgeGraph
from app.domain.knowledge.interfaces import KnowledgeExtractor
from app.domain.parser.entities import ParsedDocument
from app.domain.parser.interfaces import Parser
from app.domain.repository.entities import RepositorySnapshot
from app.domain.repository.interfaces import RepositoryLoader
from app.domain.repository.value_objects import (
    RepositoryReference,
    RepositorySnapshotRequest,
)
from app.domain.scanner.entities import (
    ScanDocument,
    ScanResult,
)
from app.domain.scanner.interfaces import Scanner


class FakeRepositoryLoader(RepositoryLoader):
    def load(
        self,
        request: RepositorySnapshotRequest,
    ) -> RepositorySnapshot:
        return RepositorySnapshot(
            repository=request.repository,
            root_path=Path("."),
            files=(PurePosixPath("README.md"),),
            directories=(),
        )


class FakeScanner(Scanner):
    def scan(
        self,
        repository: RepositorySnapshot,
    ) -> ScanResult:
        return ScanResult(
            documents=(
                ScanDocument(
                    path=PurePosixPath("README.md"),
                    content="# Documind\n\nDjango",
                ),
            )
        )


class FakeParser(Parser):
    def parse(
        self,
        document: ScanDocument,
    ) -> ParsedDocument:
        return ParsedDocument(
            path=document.path,
            language="markdown",
            title="README",
            plain_text=document.content,
            sections=(),
            metadata={},
        )


class FakeDiscoveryService:
    def discover(
        self,
        documents: tuple[ParsedDocument, ...],
    ) -> list[FoundFile]:
        return [
            FoundFile(
                PurePosixPath("README.md"),
            )
        ]


class FakeKnowledgeService:
    def build(
        self,
        facts: list[FoundFile],
    ) -> list[Technology]:
        return [
            Technology(
                name="Python",
                source=PurePosixPath("pyproject.toml"),
            ),
        ]


class FakeInferenceService:
    def __init__(self) -> None:
        self.graph: KnowledgeGraph | None = None

    def infer(
        self,
        graph: KnowledgeGraph,
    ) -> InferenceResponse:
        self.graph = graph

        return InferenceResponse(
            observations=(),
        )


class FakeRecommendationService:
    def __init__(self) -> None:
        self.observations: tuple[Observation, ...] | None = None

    def recommend(
        self,
        observations: tuple[Observation, ...],
    ) -> RecommendationResponse:
        self.observations = observations

        return RecommendationResponse(
            recommendations=(),
        )


class FakeKnowledgeExtractor(KnowledgeExtractor):
    def extract(
        self,
        documents: tuple[ParsedDocument, ...],
    ) -> list[KnowledgeCandidate]:
        return [
            KnowledgeCandidate(
                category="framework",
                value="Django",
                confidence=1.0,
                source=PurePosixPath("README.md"),
            )
        ]


def test_analyze_pipeline() -> None:
    inference_service = FakeInferenceService()
    recommendation_service = FakeRecommendationService()

    service = AnalyzeRepositoryService(
        repository_loader=FakeRepositoryLoader(),
        scanner_service=ScannerService(
            scanner=FakeScanner(),
        ),
        parser_service=ParserService(
            parser=FakeParser(),
        ),
        discovery_service=FakeDiscoveryService(),  # type: ignore[arg-type]
        knowledge_service=FakeKnowledgeService(),  # type: ignore[arg-type]
        knowledge_extraction_service=KnowledgeExtractionService(
            extractor=FakeKnowledgeExtractor(),
        ),
        knowledge_registry_service=KnowledgeRegistryService(),
        knowledge_relationship_builder=KnowledgeRelationshipBuilder(),
        knowledge_graph_builder=KnowledgeGraphBuilder(),
        inference_service=inference_service,  # type: ignore[arg-type]
        recommendation_service=recommendation_service,  # type: ignore[arg-type]
    )

    result = service.analyze(
        RepositorySnapshotRequest(
            repository=RepositoryReference(locator="."),
        )
    )

    assert len(result.scanned_documents) == 1
    assert len(result.parsed_documents) == 1
    assert len(result.facts) == 1
    assert len(result.knowledge) == 1
    assert len(result.observations) == 0
    assert len(result.recommendations) == 0

    assert inference_service.graph is not None
    assert inference_service.graph.has_node("Python")

    assert recommendation_service.observations == ()
