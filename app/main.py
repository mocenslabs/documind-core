"""Application entry point for the DocuMind command-line interface."""

from app.core.logging.logger import configure_logging
from app.presentation.cli import app


def main() -> None:
    """Configure application services and start the command-line interface."""
    configure_logging()
    app()


if __name__ == "__main__":
    main()
