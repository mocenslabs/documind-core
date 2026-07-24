"""Repository analysis application service."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from app.application.analyze.models import AnalysisResult


class AnalyzeRepositoryService:
    """
    Coordinates the complete repository analysis pipeline.

    This service orchestrates the existing application services without
    containing business rules.
    """

    def __init__(
        self,
        repository_loader: Any,
        discovery_service: Any,
        rules_service: Any,
        knowledge_service: Any,
    ) -> None:
        self._repository_loader = repository_loader
        self._discovery_service = discovery_service
        self._rules_service = rules_service
        self._knowledge_service = knowledge_service

    def analyze(self, repository_path: Path) -> AnalysisResult:
        """Execute the complete repository analysis pipeline."""

        repository = self._repository_loader.load(repository_path)

        facts = self._discovery_service.discover(repository)

        rules = self._rules_service.evaluate(facts)

        knowledge = self._knowledge_service.build(
            repository=repository,
            facts=facts,
            rules=rules,
        )

        return AnalysisResult(
            repository=repository,
            facts=facts,
            rules=rules,
            knowledge=knowledge,
        )
