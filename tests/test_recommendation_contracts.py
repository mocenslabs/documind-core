from typing import get_type_hints

from app.application.recommendation.service import RecommendationService
from app.domain.recommendation.interfaces import RecommendationEngine


def test_recommendation_service_contract() -> None:
    hints = get_type_hints(RecommendationService)

    assert hints["engine"] is RecommendationEngine
