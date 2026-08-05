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
            node="Python",
            observation=Observation(
                code="language.python",
                title="Python detected",
                description="Repository uses Python.",
                severity=Severity.INFO,
                priority=Priority.LOW,
                actions=(
                    SuggestedAction(
                        title="Review Python version",
                        description="Verify the supported Python version.",
                    ),
                ),
                category=ObservationCategory.ARCHITECTURE,
                confidence=Confidence.CERTAIN,
            ),
        ),
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
        InferenceRule(
            node="Redis",
            observation=Observation(
                code="database.redis",
                title="Redis detected",
                description="Repository uses Redis.",
                severity=Severity.INFO,
                priority=Priority.MEDIUM,
                actions=(
                    SuggestedAction(
                        title="Review persistence",
                        description="Verify whether Redis persistence is required.",
                    ),
                ),
                category=ObservationCategory.DATABASE,
                confidence=Confidence.CERTAIN,
            ),
        ),
        InferenceRule(
            node="GitHub Actions",
            observation=Observation(
                code="ci.github_actions",
                title="GitHub Actions detected",
                description="Repository uses GitHub Actions.",
                severity=Severity.INFO,
                priority=Priority.LOW,
                actions=(
                    SuggestedAction(
                        title="Review CI workflow",
                        description="Verify automated checks run on every change.",
                    ),
                ),
                category=ObservationCategory.DEVOPS,
                confidence=Confidence.CERTAIN,
            ),
        ),
        InferenceRule(
            node="Vite",
            observation=Observation(
                code="build.vite",
                title="Vite detected",
                description="Repository uses Vite.",
                severity=Severity.INFO,
                priority=Priority.LOW,
                actions=(
                    SuggestedAction(
                        title="Review build configuration",
                        description="Verify production build configuration.",
                    ),
                ),
                category=ObservationCategory.ARCHITECTURE,
                confidence=Confidence.CERTAIN,
            ),
        ),
    )
