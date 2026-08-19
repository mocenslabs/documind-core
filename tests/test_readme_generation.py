from __future__ import annotations

from app.application.generation.service import ReadmeGenerationService
from app.domain.generation.entities import ReadmeGenerationContext
from app.infrastructure.generation.fake_provider import (
    FakeReadmeGenerationProvider,
)


def test_fake_provider_generates_deterministic_readme() -> None:
    context = ReadmeGenerationContext(
        repository_name="DocuMind",
        technologies=("Python", "JavaScript"),
        frameworks=("Django", "Vue"),
        containers=("Docker",),
        ci_platforms=("GitHub Actions",),
        observations=(),
        recommendations=(),
    )

    result = FakeReadmeGenerationProvider().generate(context)

    assert result.content == (
        "# DocuMind\n"
        "\n"
        "## Technologies\n"
        "- Python\n"
        "- JavaScript\n"
        "\n"
        "## Frameworks\n"
        "- Django\n"
        "- Vue\n"
        "\n"
        "## Containers\n"
        "- Docker\n"
        "\n"
        "## CI Platforms\n"
        "- GitHub Actions\n"
        "\n"
        "## Observations\n"
        "- None detected.\n"
        "\n"
        "## Recommendations\n"
        "- None detected.\n"
    )


def test_readme_generation_service_delegates_to_provider() -> None:
    context = ReadmeGenerationContext(
        repository_name="DocuMind",
        technologies=(),
        frameworks=(),
        containers=(),
        ci_platforms=(),
        observations=(),
        recommendations=(),
    )

    service = ReadmeGenerationService(
        provider=FakeReadmeGenerationProvider(),
    )

    result = service.generate(context)

    assert result.content.startswith("# DocuMind\n")


def test_fake_provider_includes_observations_and_recommendations() -> None:
    context = ReadmeGenerationContext(
        repository_name="DocuMind",
        technologies=(),
        frameworks=(),
        containers=(),
        ci_platforms=(),
        observations=("Django detected",),
        recommendations=("Review Django settings",),
    )

    result = FakeReadmeGenerationProvider().generate(context)

    assert result.content == (
        "# DocuMind\n"
        "\n"
        "## Technologies\n"
        "- None detected.\n"
        "\n"
        "## Frameworks\n"
        "- None detected.\n"
        "\n"
        "## Containers\n"
        "- None detected.\n"
        "\n"
        "## CI Platforms\n"
        "- None detected.\n"
        "\n"
        "## Observations\n"
        "- Django detected\n"
        "\n"
        "## Recommendations\n"
        "- Review Django settings\n"
    )


def test_fake_provider_handles_empty_context_deterministically() -> None:
    context = ReadmeGenerationContext(
        repository_name="EmptyRepo",
        technologies=(),
        frameworks=(),
        containers=(),
        ci_platforms=(),
        observations=(),
        recommendations=(),
    )

    result = FakeReadmeGenerationProvider().generate(context)

    assert result.content == (
        "# EmptyRepo\n"
        "\n"
        "## Technologies\n"
        "- None detected.\n"
        "\n"
        "## Frameworks\n"
        "- None detected.\n"
        "\n"
        "## Containers\n"
        "- None detected.\n"
        "\n"
        "## CI Platforms\n"
        "- None detected.\n"
        "\n"
        "## Observations\n"
        "- None detected.\n"
        "\n"
        "## Recommendations\n"
        "- None detected.\n"
    )
