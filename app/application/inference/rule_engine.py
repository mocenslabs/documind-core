"""Inference rule engine."""

from __future__ import annotations

from app.domain.inference.entities import Observation
from app.domain.inference.rules import InferenceRule
from app.domain.knowledge.graph import KnowledgeGraph


class InferenceRuleEngine:
    """Evaluate inference rules."""

    def __init__(
        self,
        rules: tuple[
            InferenceRule,
            ...,
        ],
    ) -> None:
        self._rules = rules

    def evaluate(
        self,
        graph: KnowledgeGraph,
    ) -> list[Observation]:
        """Evaluate all rules."""

        observations: list[Observation] = []

        for rule in self._rules:
            if graph.has_node(rule.node):
                observations.append(rule.observation)

        return observations
