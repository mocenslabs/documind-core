"""Composite inference rule engine."""

from __future__ import annotations

from app.domain.inference.composite_rules import (
    CompositeInferenceRule,
)
from app.domain.inference.entities import Observation
from app.domain.knowledge.graph import KnowledgeGraph


class CompositeInferenceRuleEngine:
    """Evaluate composite inference rules."""

    def __init__(
        self,
        rules: tuple[
            CompositeInferenceRule,
            ...,
        ],
    ) -> None:
        self._rules = rules

    def evaluate(
        self,
        graph: KnowledgeGraph,
    ) -> list[Observation]:
        """Evaluate composite rules."""

        observations: list[Observation] = []

        for rule in self._rules:
            if all(graph.has_node(node) for node in rule.nodes):
                observations.append(
                    rule.observation,
                )

        return observations
