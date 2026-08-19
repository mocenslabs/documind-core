"""Contracts for README generation."""

from __future__ import annotations

from abc import ABC, abstractmethod

from .entities import GeneratedReadme, ReadmeGenerationContext


class ReadmeGenerationProvider(ABC):
    """Generate README content from structured repository context."""

    @abstractmethod
    def generate(
        self,
        context: ReadmeGenerationContext,
    ) -> GeneratedReadme:
        """Generate README content from repository context."""
