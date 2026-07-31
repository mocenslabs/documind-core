from app.application.recommendation.rule_engine import (
    RecommendationRuleEngine,
)
from app.domain.inference.actions import SuggestedAction
from app.domain.inference.category import ObservationCategory
from app.domain.inference.confidence import Confidence
from app.domain.inference.entities import Observation
from app.domain.inference.priority import Priority
from app.domain.inference.severity import Severity


def test_rule_engine_build() -> None:
    engine = RecommendationRuleEngine()

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

    recommendations = engine.build(
        (observation,),
    )

    assert len(recommendations) == 1
    assert recommendations[0].id == "framework.python"
