from app.application.inference.builtin_rules import (
    builtin_inference_rules,
)


def test_builtin_rules() -> None:
    rules = builtin_inference_rules()

    assert len(rules) >= 3
