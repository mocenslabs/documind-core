from app.application.recommendation.service import RecommendationService
from app.domain.inference.actions import SuggestedAction
from app.domain.inference.category import ObservationCategory
from app.domain.inference.confidence import Confidence
from app.domain.inference.entities import Observation
from app.domain.inference.priority import Priority
from app.domain.inference.severity import Severity
from app.domain.recommendation.entities import Recommendation
from app.domain.recommendation.interfaces import RecommendationEngine


class FakeRecommendationEngine(RecommendationEngine):
    def __init__(self) -> None:
        self.observations: tuple[Observation, ...] | None = None

    def recommend(
        self,
        observations: tuple[Observation, ...],
    ) -> tuple[Recommendation, ...]:
        self.observations = observations

        if not observations:
            return ()

        observation = observations[0]

        return (
            Recommendation(
                id=observation.code,
                title="Review settings",
                description="Verify production settings.",
                observation=observation,
            ),
        )


def build_observation() -> Observation:
    return Observation(
        code="framework.django",
        title="Django detected",
        description="Repository uses Django.",
        severity=Severity.INFO,
        priority=Priority.MEDIUM,
        category=ObservationCategory.ARCHITECTURE,
        confidence=Confidence.CERTAIN,
        actions=(
            SuggestedAction(
                title="Review settings",
                description="Verify production settings.",
            ),
        ),
    )


def test_recommendation_service_delegates_to_engine() -> None:
    engine = FakeRecommendationEngine()
    service = RecommendationService(engine=engine)
    observation = build_observation()

    response = service.recommend((observation,))

    assert engine.observations == (observation,)
    assert len(response.recommendations) == 1
    assert response.recommendations[0].id == "framework.django"
    assert response.recommendations[0].observation is observation


def test_recommendation_service_returns_empty_response() -> None:
    engine = FakeRecommendationEngine()
    service = RecommendationService(engine=engine)

    response = service.recommend(())

    assert response.recommendations == ()
