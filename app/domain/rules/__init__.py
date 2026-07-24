"""Rule domain contracts."""

from app.domain.rules.entities import RuleResult
from app.domain.rules.interfaces import Rule

__all__ = ["Rule", "RuleResult"]
