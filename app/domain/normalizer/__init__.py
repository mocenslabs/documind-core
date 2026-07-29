"""Knowledge normalization domain."""

from .entities import NormalizedKnowledge
from .interfaces import KnowledgeNormalizer

__all__ = [
    "KnowledgeNormalizer",
    "NormalizedKnowledge",
]
