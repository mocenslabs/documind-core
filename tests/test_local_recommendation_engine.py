from app.domain.inference.actions import SuggestedAction
from app.domain.inference.category import ObservationCategory
from app.domain.inference.confidence import Confidence
from app.domain.inference.entities import Observation
from app.domain.inference.priority import Priority
from app.domain.inference.severity import Severity
from app.infrastructure.recommendation.local_engine import (
    LocalRecommendationEngine,
)


def test_local_recommendation_engine() -> None:
    engine = LocalRecommendationEngine()

    observation = Observation(
        code="framework.django",
        title="Django detected",
        description="Repository uses Django.",
        severity=Severity.INFO,
        priority=Priority.MEDIUM,
        actions=(
            SuggestedAction(
                title="Review settings",
                description="Verify production settings.",
            ),
        ),
        category=ObservationCategory.ARCHITECTURE,
        confidence=Confidence.CERTAIN,
    )

    result = engine.recommend((observation,))

    assert len(result) == 1
    assert result[0].id == "framework.django"
    assert result[0].observation is observation
