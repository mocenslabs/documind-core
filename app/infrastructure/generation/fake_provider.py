"""Deterministic README generation provider for tests."""

from __future__ import annotations

from app.domain.generation.entities import (
    GeneratedReadme,
    ReadmeGenerationContext,
)
from app.domain.generation.interfaces import ReadmeGenerationProvider


class FakeReadmeGenerationProvider(ReadmeGenerationProvider):
    """Generate deterministic README content without an external AI provider."""

    def generate(
        self,
        context: ReadmeGenerationContext,
    ) -> GeneratedReadme:
        """Generate deterministic README content."""

        lines = [
            f"# {context.repository_name}",
            "",
            "## Technologies",
        ]

        if context.technologies:
            lines.extend(f"- {technology}" for technology in context.technologies)
        else:
            lines.append("- None detected.")

        lines.extend(
            [
                "",
                "## Frameworks",
            ]
        )

        if context.frameworks:
            lines.extend(f"- {framework}" for framework in context.frameworks)
        else:
            lines.append("- None detected.")

        lines.extend(
            [
                "",
                "## Containers",
            ]
        )

        if context.containers:
            lines.extend(f"- {container}" for container in context.containers)
        else:
            lines.append("- None detected.")

        lines.extend(
            [
                "",
                "## CI Platforms",
            ]
        )

        if context.ci_platforms:
            lines.extend(f"- {platform}" for platform in context.ci_platforms)
        else:
            lines.append("- None detected.")

        lines.extend(
            [
                "",
                "## Observations",
            ]
        )

        if context.observations:
            lines.extend(f"- {observation}" for observation in context.observations)
        else:
            lines.append("- None detected.")

        lines.extend(
            [
                "",
                "## Recommendations",
            ]
        )

        if context.recommendations:
            lines.extend(
                f"- {recommendation}" for recommendation in context.recommendations
            )
        else:
            lines.append("- None detected.")

        return GeneratedReadme(
            content="\n".join(lines) + "\n",
        )
