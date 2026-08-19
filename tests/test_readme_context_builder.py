from __future__ import annotations

from pathlib import Path, PurePosixPath

from app.application.analyze.models import AnalysisResult
from app.application.generation.context_builder import (
    ReadmeGenerationContextBuilder,
)
from app.domain.inference.category import ObservationCategory
from app.domain.inference.confidence import Confidence
from app.domain.inference.entities import Observation
from app.domain.inference.priority import Priority
from app.domain.inference.severity import Severity
from app.domain.knowledge.entities import (
    CIPlatform,
    Container,
    Framework,
    Technology,
)
from app.domain.recommendation.entities import Recommendation
from app.domain.repository.entities import RepositorySnapshot
from app.domain.repository.value_objects import RepositoryReference


def _analysis(
    *,
    knowledge: tuple[
        Technology | Framework | Container | CIPlatform,
        ...,
    ] = (),
    observations: tuple[Observation, ...] = (),
    recommendations: tuple[Recommendation, ...] = (),
) -> AnalysisResult:
    """Create a minimal analysis result for context-builder tests."""

    repository = RepositorySnapshot(
        repository=RepositoryReference(locator="documind"),
        root_path=Path("."),
        files=(),
        directories=(),
    )

    return AnalysisResult(
        repository=repository,
        scanned_documents=(),
        parsed_documents=(),
        facts=(),
        knowledge=knowledge,
        observations=observations,
        recommendations=recommendations,
    )


def test_build_context_extracts_knowledge_by_type() -> None:
    analysis = _analysis(
        knowledge=(
            Technology(
                name="Python",
                source=PurePosixPath("pyproject.toml"),
            ),
            Framework(
                name="Django",
                source=PurePosixPath("pyproject.toml"),
            ),
            Container(
                name="Docker",
                source=PurePosixPath("Dockerfile"),
            ),
            CIPlatform(
                name="GitHub Actions",
                source=PurePosixPath(".github/workflows/ci.yml"),
            ),
        ),
    )

    context = ReadmeGenerationContextBuilder().build(analysis)

    assert context.repository_name == "documind"
    assert context.technologies == ("Python",)
    assert context.frameworks == ("Django",)
    assert context.containers == ("Docker",)
    assert context.ci_platforms == ("GitHub Actions",)


def test_build_context_extracts_observations_and_recommendations() -> None:
    observation = Observation(
        code="framework.django",
        title="Django detected",
        description="Repository uses Django.",
        severity=Severity.INFO,
        priority=Priority.MEDIUM,
        category=ObservationCategory.ARCHITECTURE,
        confidence=Confidence.CERTAIN,
    )

    recommendation = Recommendation(
        id="framework.django",
        title="Review Django settings",
        description="Verify production settings.",
        observation=observation,
    )

    context = ReadmeGenerationContextBuilder().build(
        _analysis(
            observations=(observation,),
            recommendations=(recommendation,),
        )
    )

    assert context.observations == ("Django detected",)
    assert context.recommendations == ("Review Django settings",)


def test_build_context_removes_duplicates_and_orders_values() -> None:
    analysis = _analysis(
        knowledge=(
            Technology(
                name="Vue",
                source=PurePosixPath("package.json"),
            ),
            Technology(
                name="Python",
                source=PurePosixPath("pyproject.toml"),
            ),
            Technology(
                name="Vue",
                source=PurePosixPath("package-lock.json"),
            ),
            Technology(
                name="Python",
                source=PurePosixPath("requirements.txt"),
            ),
        ),
    )

    context = ReadmeGenerationContextBuilder().build(analysis)

    assert context.technologies == ("Python", "Vue")


def test_build_context_returns_empty_collections_for_empty_analysis() -> None:
    context = ReadmeGenerationContextBuilder().build(_analysis())

    assert context.technologies == ()
    assert context.frameworks == ()
    assert context.containers == ()
    assert context.ci_platforms == ()
    assert context.observations == ()
    assert context.recommendations == ()
