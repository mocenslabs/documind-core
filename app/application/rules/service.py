"""Application service for rule evaluation."""

from collections.abc import Sequence
from dataclasses import dataclass

from app.domain.discovery.facts import RawFact
from app.domain.knowledge.entities import Knowledge
from app.domain.rules.interfaces import Rule


@dataclass(frozen=True, slots=True)
class RuleEngineService:
    """Evaluate independent rules against raw repository facts."""

    rules: tuple[Rule, ...]

    def evaluate(self, facts: Sequence[RawFact]) -> list[Knowledge]:
        """Return knowledge produced by each configured rule in rule order."""
        return [knowledge for rule in self.rules for knowledge in rule.apply(facts)]
