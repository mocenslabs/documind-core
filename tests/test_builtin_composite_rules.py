from app.application.inference.builtin_composite_rules import (
    builtin_composite_rules,
)


def test_builtin_composite_rules() -> None:
    rules = builtin_composite_rules()

    assert len(rules) >= 2
