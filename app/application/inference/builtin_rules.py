"""Built-in inference rules."""

from __future__ import annotations

from app.domain.inference.actions import SuggestedAction
from app.domain.inference.category import ObservationCategory
from app.domain.inference.confidence import Confidence
from app.domain.inference.entities import Observation
from app.domain.inference.priority import Priority
from app.domain.inference.rules import InferenceRule
from app.domain.inference.severity import Severity


def builtin_inference_rules() -> tuple[
    InferenceRule,
    ...,
]:
    """Return built-in rules."""

    return (
        InferenceRule(
            node="Django",
            observation=Observation(
                code="framework.django",
                title="Django detected",
                description="Repository uses Django.",
                severity=Severity.INFO,
                priority=Priority.MEDIUM,
                actions=(
                    SuggestedAction(
                        title="Review settings",
                        description="Verify production settings.",
                    ),
                ),
                category=ObservationCategory.ARCHITECTURE,
                confidence=Confidence.CERTAIN,
            ),
        ),
        InferenceRule(
            node="Docker",
            observation=Observation(
                code="container.docker",
                title="Docker detected",
                description="Repository includes Docker.",
                severity=Severity.INFO,
                priority=Priority.LOW,
                actions=(
                    SuggestedAction(
                        title="Validate image",
                        description="Check Docker image best practices.",
                    ),
                ),
                category=ObservationCategory.DEVOPS,
                confidence=Confidence.CERTAIN,
            ),
        ),
        InferenceRule(
            node="PostgreSQL",
            observation=Observation(
                code="database.postgresql",
                title="PostgreSQL detected",
                description="Repository uses PostgreSQL.",
                severity=Severity.INFO,
                priority=Priority.MEDIUM,
                actions=(
                    SuggestedAction(
                        title="Review backups",
                        description="Ensure backup strategy exists.",
                    ),
                ),
                category=ObservationCategory.DATABASE,
                confidence=Confidence.CERTAIN,
            ),
        ),
    )
