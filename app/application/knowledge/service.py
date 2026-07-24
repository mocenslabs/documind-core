"""Application service for repository knowledge."""

from collections.abc import Sequence
from dataclasses import dataclass

from app.application.rules.service import RuleEngineService
from app.domain.discovery.facts import RawFact
from app.domain.knowledge.entities import Knowledge
from app.domain.knowledge.interfaces import KnowledgeEngine


@dataclass(frozen=True, slots=True)
class KnowledgeService(KnowledgeEngine):
    """Produce repository knowledge through the configured rule engine."""

    rule_engine: RuleEngineService

    def build(self, facts: Sequence[RawFact]) -> list[Knowledge]:
        """Build normalized knowledge from the supplied raw facts."""
        return self.rule_engine.evaluate(facts)
