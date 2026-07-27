"""Repository analysis application service."""

from __future__ import annotations

from app.application.discovery.service import DiscoveryService
from app.application.knowledge.service import KnowledgeService
from app.application.scanner.service import ScannerService
from app.domain.repository.interfaces import RepositoryLoader
from app.domain.repository.value_objects import RepositorySnapshotRequest

from .models import AnalysisResult


class AnalyzeRepositoryService:
    """Coordinate the repository analysis pipeline."""

    def __init__(
        self,
        repository_loader: RepositoryLoader,
        scanner_service: ScannerService,
        discovery_service: DiscoveryService,
        knowledge_service: KnowledgeService,
    ) -> None:
        self._repository_loader = repository_loader
        self._scanner_service = scanner_service
        self._discovery_service = discovery_service
        self._knowledge_service = knowledge_service

    def analyze(
        self,
        request: RepositorySnapshotRequest,
    ) -> AnalysisResult:
        """Execute the complete analysis pipeline."""

        repository = self._repository_loader.load(request)

        scan_result = self._scanner_service.scan(repository)

        facts = self._discovery_service.discover(repository)

        knowledge = self._knowledge_service.build(facts)

        return AnalysisResult(
            repository=repository,
            scanned_documents=scan_result.documents,
            facts=facts,
            knowledge=knowledge,
        )
