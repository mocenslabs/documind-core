"""Repository analysis application service."""

from __future__ import annotations

from app.application.discovery.service import DiscoveryService
from app.application.inference.service import InferenceService
from app.application.knowledge.service import KnowledgeService
from app.application.parser.service import ParserService
from app.application.recommendation.service import RecommendationService
from app.application.scanner.service import ScannerService
from app.domain.knowledge.entities import Knowledge
from app.domain.knowledge.graph import KnowledgeGraph
from app.domain.repository.interfaces import RepositoryLoader
from app.domain.repository.value_objects import RepositorySnapshotRequest

from .models import AnalysisResult


class AnalyzeRepositoryService:
    """Coordinate the repository analysis pipeline."""

    def __init__(
        self,
        repository_loader: RepositoryLoader,
        scanner_service: ScannerService,
        parser_service: ParserService,
        discovery_service: DiscoveryService,
        knowledge_service: KnowledgeService,
        inference_service: InferenceService,
        recommendation_service: RecommendationService,
    ) -> None:
        self._repository_loader = repository_loader
        self._scanner_service = scanner_service
        self._parser_service = parser_service
        self._discovery_service = discovery_service
        self._knowledge_service = knowledge_service
        self._inference_service = inference_service
        self._recommendation_service = recommendation_service

    def analyze(
        self,
        request: RepositorySnapshotRequest,
    ) -> AnalysisResult:
        """Execute the repository analysis pipeline."""

        repository = self._repository_loader.load(request)

        scan_result = self._scanner_service.scan(repository)

        parse_result = self._parser_service.parse(
            scan_result.documents,
        )

        facts = self._discovery_service.discover(repository)

        knowledge = self._knowledge_service.build(facts)

        knowledge_graph = self._build_knowledge_graph(
            knowledge,
        )

        inference_result = self._inference_service.infer(
            knowledge_graph,
        )

        recommendation_result = self._recommendation_service.recommend(
            inference_result.observations,
        )

        return AnalysisResult(
            repository=repository,
            scanned_documents=scan_result.documents,
            parsed_documents=parse_result.documents,
            facts=facts,
            knowledge=knowledge,
            observations=inference_result.observations,
            recommendations=recommendation_result.recommendations,
        )

    @staticmethod
    def _build_knowledge_graph(
        knowledge: list[Knowledge],
    ) -> KnowledgeGraph:
        """Build a knowledge graph from normalized knowledge."""

        graph = KnowledgeGraph()

        for item in knowledge:
            graph.add_node(
                item.name,
            )

        return graph
