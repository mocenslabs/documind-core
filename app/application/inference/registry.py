"""Inference registry."""

from __future__ import annotations

from dataclasses import dataclass

from app.application.inference.builtin_composite_rules import (
    builtin_composite_rules,
)
from app.application.inference.builtin_rules import (
    builtin_inference_rules,
)
from app.domain.inference.composite_rules import (
    CompositeInferenceRule,
)
from app.domain.inference.rules import (
    InferenceRule,
)


@dataclass(frozen=True, slots=True)
class InferenceRegistry:
    """Registry of inference rules."""

    simple_rules: tuple[InferenceRule, ...]

    composite_rules: tuple[CompositeInferenceRule, ...]


def builtin_registry() -> InferenceRegistry:
    """Create the default inference registry."""

    return InferenceRegistry(
        simple_rules=builtin_inference_rules(),
        composite_rules=builtin_composite_rules(),
    )
