# DocuMind Core

DocuMind Core is the provider-agnostic engine for AI-powered repository
analysis. Its first public capability will be README generation.

## Requirements

- Python 3.12 or later

## Setup

Copy `.env.example` to `.env` to configure the local environment.

## Development

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project and development tools in editable mode:

```bash
python -m pip install -e ".[dev]"
```

Install the Git hooks:

```bash
pre-commit install
```

Run the quality checks:

```bash
ruff check .
ruff format --check .
black --check .
mypy
pytest
```

## Commands

Run the configured CLI:

```bash
python -m app.main --help
```
