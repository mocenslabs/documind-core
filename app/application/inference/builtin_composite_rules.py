"""Built-in composite inference rules."""

from __future__ import annotations

from app.domain.inference.actions import SuggestedAction
from app.domain.inference.category import ObservationCategory
from app.domain.inference.composite_rules import CompositeInferenceRule
from app.domain.inference.confidence import Confidence
from app.domain.inference.entities import Observation
from app.domain.inference.priority import Priority
from app.domain.inference.severity import Severity


def builtin_composite_rules() -> tuple[
    CompositeInferenceRule,
    ...,
]:
    """Return composite rules."""

    return (
        CompositeInferenceRule(
            nodes=(
                "Django",
                "PostgreSQL",
            ),
            observation=Observation(
                code="stack.django.postgresql",
                title="Django + PostgreSQL stack",
                description="Repository appears to use Django with PostgreSQL.",
                severity=Severity.INFO,
                priority=Priority.HIGH,
                actions=(
                    SuggestedAction(
                        title="Review ORM configuration",
                        description="Verify database configuration and migrations.",
                    ),
                ),
                category=ObservationCategory.ARCHITECTURE,
                confidence=Confidence.HIGH,
            ),
        ),
        CompositeInferenceRule(
            nodes=(
                "Docker",
                "PostgreSQL",
            ),
            observation=Observation(
                code="stack.containerized.database",
                title="Containerized database",
                description="Database appears to be containerized.",
                severity=Severity.INFO,
                priority=Priority.MEDIUM,
                actions=(
                    SuggestedAction(
                        title="Persist database data",
                        description="Verify Docker volumes for PostgreSQL.",
                    ),
                ),
                category=ObservationCategory.DEVOPS,
                confidence=Confidence.HIGH,
            ),
        ),
        CompositeInferenceRule(
            nodes=(
                "Django",
                "Docker",
            ),
            observation=Observation(
                code="stack.django.docker",
                title="Containerized Django application",
                description="Repository appears to run Django in Docker.",
                severity=Severity.INFO,
                priority=Priority.MEDIUM,
                actions=(
                    SuggestedAction(
                        title="Review application container",
                        description="Verify the Django container follows "
                        "production practices.",
                    ),
                ),
                category=ObservationCategory.DEVOPS,
                confidence=Confidence.HIGH,
            ),
        ),
        CompositeInferenceRule(
            nodes=(
                "Django",
                "PostgreSQL",
                "Docker",
            ),
            observation=Observation(
                code="stack.django.postgresql.docker",
                title="Containerized Django + PostgreSQL stack",
                description=(
                    "Repository appears to use Django and PostgreSQL "
                    "within a Docker-based environment."
                ),
                severity=Severity.INFO,
                priority=Priority.HIGH,
                actions=(
                    SuggestedAction(
                        title="Review production stack",
                        description=(
                            "Verify application, database, networking, "
                            "volumes, and deployment configuration."
                        ),
                    ),
                ),
                category=ObservationCategory.DEVOPS,
                confidence=Confidence.HIGH,
            ),
        ),
    )
