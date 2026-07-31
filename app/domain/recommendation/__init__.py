"""Recommendation domain."""

from .entities import Recommendation
from .interfaces import RecommendationEngine

__all__ = [
    "Recommendation",
    "RecommendationEngine",
]
