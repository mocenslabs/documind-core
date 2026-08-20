"""Application service for repository README generation."""

from __future__ import annotations

from dataclasses import dataclass

from app.application.analyze.models import AnalysisResult
from app.domain.generation.entities import GeneratedReadme

from .context_builder import ReadmeGenerationContextBuilder
from .service import ReadmeGenerationService


@dataclass(frozen=True, slots=True)
class RepositoryReadmeGenerationService:
    """Generate a README from a completed repository analysis."""

    context_builder: ReadmeGenerationContextBuilder
    generation_service: ReadmeGenerationService

    def generate(
        self,
        analysis: AnalysisResult,
    ) -> GeneratedReadme:
        """Generate a README from repository analysis."""

        context = self.context_builder.build(analysis)

        return self.generation_service.generate(context)
