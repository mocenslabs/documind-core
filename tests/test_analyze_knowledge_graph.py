from pathlib import PurePosixPath

from app.application.analyze.service import AnalyzeRepositoryService
from app.domain.knowledge.entities import (
    Framework,
    Technology,
)


def test_build_knowledge_graph_creates_relationships() -> None:
    graph = AnalyzeRepositoryService._build_knowledge_graph(
        [
            Technology(
                name="Python",
                source=PurePosixPath("pyproject.toml"),
            ),
            Framework(
                name="Django",
                source=PurePosixPath("manage.py"),
            ),
        ]
    )

    assert graph.has_node("Python")
    assert graph.has_node("Django")

    assert len(graph.relationships) == 2

    assert graph.neighbors("Python") == ("Django",)
    assert graph.neighbors("Django") == ("Python",)
