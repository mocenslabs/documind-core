"""Application service for README generation."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.generation.entities import (
    GeneratedReadme,
    ReadmeGenerationContext,
)
from app.domain.generation.interfaces import ReadmeGenerationProvider


@dataclass(frozen=True, slots=True)
class ReadmeGenerationService:
    """Coordinate README generation."""

    provider: ReadmeGenerationProvider

    def generate(
        self,
        context: ReadmeGenerationContext,
    ) -> GeneratedReadme:
        """Generate a README using the configured provider."""

        return self.provider.generate(context)
