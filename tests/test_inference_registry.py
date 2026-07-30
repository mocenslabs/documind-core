from app.application.inference.registry import (
    builtin_registry,
)


def test_registry() -> None:
    registry = builtin_registry()

    assert len(registry.simple_rules) >= 3
    assert len(registry.composite_rules) >= 2
