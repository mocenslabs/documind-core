"""Build README generation context from analysis results."""

from __future__ import annotations

from dataclasses import dataclass

from app.application.analyze.models import AnalysisResult
from app.domain.generation.entities import ReadmeGenerationContext
from app.domain.knowledge.entities import (
    CIPlatform,
    Container,
    Framework,
    Technology,
)


@dataclass(frozen=True, slots=True)
class ReadmeGenerationContextBuilder:
    """Build structured README context from repository analysis."""

    def build(
        self,
        analysis: AnalysisResult,
    ) -> ReadmeGenerationContext:
        """Build README generation context from an analysis result."""

        technologies: list[str] = []
        frameworks: list[str] = []
        containers: list[str] = []
        ci_platforms: list[str] = []

        for item in analysis.knowledge:
            if isinstance(item, Technology):
                technologies.append(item.name)
            elif isinstance(item, Framework):
                frameworks.append(item.name)
            elif isinstance(item, Container):
                containers.append(item.name)
            elif isinstance(item, CIPlatform):
                ci_platforms.append(item.name)

        return ReadmeGenerationContext(
            repository_name=analysis.repository.repository.locator,
            technologies=tuple(sorted(set(technologies))),
            frameworks=tuple(sorted(set(frameworks))),
            containers=tuple(sorted(set(containers))),
            ci_platforms=tuple(sorted(set(ci_platforms))),
            observations=tuple(
                observation.title for observation in analysis.observations
            ),
            recommendations=tuple(
                recommendation.title for recommendation in analysis.recommendations
            ),
        )
