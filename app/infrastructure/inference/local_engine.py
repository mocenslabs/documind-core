"""Local inference engine."""

from __future__ import annotations

from app.application.inference.composite_rule_engine import (
    CompositeInferenceRuleEngine,
)
from app.application.inference.registry import (
    builtin_registry,
)
from app.application.inference.rule_engine import (
    InferenceRuleEngine,
)
from app.domain.inference.entities import Observation
from app.domain.inference.interfaces import InferenceEngine
from app.domain.knowledge.graph import KnowledgeGraph


class LocalInferenceEngine(InferenceEngine):
    """Rule-based inference engine."""

    def __init__(self) -> None:
        registry = builtin_registry()

        self._rules = InferenceRuleEngine(
            registry.simple_rules,
        )

        self._composite = CompositeInferenceRuleEngine(
            registry.composite_rules,
        )

    def infer(
        self,
        graph: KnowledgeGraph,
    ) -> list[Observation]:
        """Generate observations."""

        observations = self._rules.evaluate(
            graph,
        )

        observations.extend(
            self._composite.evaluate(
                graph,
            )
        )

        return observations
