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


def test_recommendations_are_based_on_observation_actions() -> None:
    from app.application.recommendation.rule_engine import (
        RecommendationRuleEngine,
    )
    from app.domain.inference.actions import SuggestedAction
    from app.domain.inference.category import ObservationCategory
    from app.domain.inference.confidence import Confidence
    from app.domain.inference.entities import Observation
    from app.domain.inference.priority import Priority
    from app.domain.inference.severity import Severity

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

    engine = RecommendationRuleEngine()

    recommendations = engine.recommend(
        (observation,),
    )

    assert len(recommendations) == 1
    assert recommendations[0].title == "Review settings"
    assert recommendations[0].description == "Verify production settings."
    assert recommendations[0].id == "framework.django"


def test_observation_without_actions_produces_no_recommendation() -> None:
    from app.application.recommendation.rule_engine import (
        RecommendationRuleEngine,
    )
    from app.domain.inference.category import ObservationCategory
    from app.domain.inference.confidence import Confidence
    from app.domain.inference.entities import Observation
    from app.domain.inference.priority import Priority
    from app.domain.inference.severity import Severity

    observation = Observation(
        code="framework.django",
        title="Django detected",
        description="Repository uses Django.",
        severity=Severity.INFO,
        priority=Priority.MEDIUM,
        actions=(),
        category=ObservationCategory.ARCHITECTURE,
        confidence=Confidence.CERTAIN,
    )

    engine = RecommendationRuleEngine()

    recommendations = engine.recommend(
        (observation,),
    )

    assert recommendations == ()
