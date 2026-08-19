"""README generation domain entities."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ReadmeGenerationContext:
    """Structured context used to generate a repository README."""

    repository_name: str
    technologies: tuple[str, ...]
    frameworks: tuple[str, ...]
    containers: tuple[str, ...]
    ci_platforms: tuple[str, ...]
    observations: tuple[str, ...]
    recommendations: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class GeneratedReadme:
    """Generated README content."""

    content: str
