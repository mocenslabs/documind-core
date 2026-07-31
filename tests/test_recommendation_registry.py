from app.application.recommendation.registry import (
    RecommendationRegistry,
)
from app.domain.inference.actions import SuggestedAction
from app.domain.inference.category import ObservationCategory
from app.domain.inference.confidence import Confidence
from app.domain.inference.entities import Observation
from app.domain.inference.priority import Priority
from app.domain.inference.severity import Severity
from app.domain.recommendation.entities import Recommendation


def build_recommendation() -> Recommendation:
    observation = Observation(
        code="framework.python",
        title="Python detected",
        description="Repository uses Python.",
        severity=Severity.INFO,
        priority=Priority.MEDIUM,
        category=ObservationCategory.ARCHITECTURE,
        confidence=Confidence.CERTAIN,
        actions=(
            SuggestedAction(
                title="Review runtime",
                description="Verify supported version.",
            ),
        ),
    )

    return Recommendation(
        id="framework.python",
        title="Python detected",
        description="Repository uses Python.",
        observation=observation,
    )


def test_registry_add() -> None:
    registry = RecommendationRegistry()

    recommendation = build_recommendation()

    registry.add(recommendation)

    assert registry.all() == (recommendation,)


def test_registry_extend() -> None:
    registry = RecommendationRegistry()

    recommendation = build_recommendation()

    registry.extend((recommendation,))

    assert len(registry.all()) == 1


def test_registry_clear() -> None:
    registry = RecommendationRegistry()

    registry.add(build_recommendation())

    registry.clear()

    assert registry.all() == ()
