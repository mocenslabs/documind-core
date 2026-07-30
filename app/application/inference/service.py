"""Inference application service."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.inference.interfaces import InferenceEngine
from app.domain.knowledge.graph import KnowledgeGraph

from .models import InferenceResponse


@dataclass(frozen=True, slots=True)
class InferenceService:
    """Coordinate repository inference."""

    engine: InferenceEngine

    def infer(
        self,
        graph: KnowledgeGraph,
    ) -> InferenceResponse:
        """Generate observations."""

        observations = self.engine.infer(
            graph,
        )

        return InferenceResponse(
            observations=tuple(observations),
        )
