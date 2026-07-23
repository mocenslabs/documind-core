"""Import smoke tests for the application foundation."""

from app.core.config.settings import Settings, settings
from app.core.logging.logger import configure_logging
from app.main import main
from app.presentation.cli import app


def test_application_modules_import() -> None:
    """Verify the bootstrap modules can be imported."""
    assert Settings is not None
    assert settings is not None
    assert callable(configure_logging)
    assert callable(main)
    assert app.info.name == "documind"
