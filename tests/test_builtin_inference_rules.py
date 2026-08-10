from app.application.inference.builtin_rules import (
    builtin_inference_rules,
)


def test_builtin_rules_have_expected_nodes() -> None:
    rules = builtin_inference_rules()

    nodes = {rule.node for rule in rules}

    assert nodes == {
        "Python",
        "Django",
        "Docker",
        "PostgreSQL",
        "Redis",
        "GitHub Actions",
        "Vite",
    }


def test_builtin_rules_have_unique_observation_codes() -> None:
    rules = builtin_inference_rules()

    codes = [rule.observation.code for rule in rules]

    assert len(codes) == len(set(codes))


def test_builtin_rules_have_observations() -> None:
    rules = builtin_inference_rules()

    assert all(rule.observation.code for rule in rules)
    assert all(rule.observation.title for rule in rules)
    assert all(rule.observation.description for rule in rules)
