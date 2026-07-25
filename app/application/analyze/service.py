"""Repository analysis application service."""

from __future__ import annotations

from app.application.analyze.models import AnalysisResult
from app.application.discovery.service import DiscoveryService
from app.application.knowledge.service import KnowledgeService
from app.domain.repository.interfaces import RepositoryLoader
from app.domain.repository.value_objects import RepositorySnapshotRequest


class AnalyzeRepositoryService:
    """Coordinate the complete repository analysis pipeline."""

    def __init__(
        self,
        repository_loader: RepositoryLoader,
        discovery_service: DiscoveryService,
        knowledge_service: KnowledgeService,
    ) -> None:
        self._repository_loader = repository_loader
        self._discovery_service = discovery_service
        self._knowledge_service = knowledge_service

    def analyze(
        self,
        request: RepositorySnapshotRequest,
    ) -> AnalysisResult:
        """Analyze a repository."""

        repository = self._repository_loader.load(request)

        facts = self._discovery_service.discover(repository)

        knowledge = self._knowledge_service.build(facts)

        return AnalysisResult(
            repository=repository,
            facts=facts,
            knowledge=knowledge,
        )
