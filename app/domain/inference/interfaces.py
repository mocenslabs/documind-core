"""Inference contracts."""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.domain.knowledge.graph import KnowledgeGraph

from .entities import Observation


class InferenceEngine(ABC):
    """Generate observations from a knowledge graph."""

    @abstractmethod
    def infer(
        self,
        graph: KnowledgeGraph,
    ) -> list[Observation]:
        """Infer repository observations."""
