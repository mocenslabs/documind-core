from app.domain.knowledge.graph import KnowledgeGraph
from app.infrastructure.inference.local_engine import (
    LocalInferenceEngine,
)


def test_local_engine() -> None:
    graph = KnowledgeGraph()

    graph.add_node("Django")
    graph.add_node("Docker")

    engine = LocalInferenceEngine()

    observations = engine.infer(graph)

    codes = {observation.code for observation in observations}

    assert "framework.django" in codes
    assert "container.docker" in codes

    assert "stack.django.docker" in codes

    assert len(observations) == 3


def test_local_engine_evaluates_composite_rules() -> None:
    graph = KnowledgeGraph()

    graph.add_node("Django")
    graph.add_node("PostgreSQL")
    graph.add_node("Docker")

    engine = LocalInferenceEngine()

    observations = engine.infer(graph)

    codes = {observation.code for observation in observations}

    assert "framework.django" in codes
    assert "database.postgresql" in codes
    assert "container.docker" in codes

    assert "stack.django.postgresql" in codes
    assert "stack.containerized.database" in codes
    assert "stack.django.docker" in codes
    assert "stack.django.postgresql.docker" in codes

    assert len(observations) == 7


def test_local_engine_does_not_fire_missing_rules() -> None:
    graph = KnowledgeGraph()

    graph.add_node("Django")

    engine = LocalInferenceEngine()

    observations = engine.infer(graph)

    codes = {observation.code for observation in observations}

    assert codes == {
        "framework.django",
    }


def test_local_engine_returns_empty_for_empty_graph() -> None:
    graph = KnowledgeGraph()

    engine = LocalInferenceEngine()

    observations = engine.infer(graph)

    assert observations == []
