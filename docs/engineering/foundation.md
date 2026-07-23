# Engineering Foundation

## Tooling Choices

DocuMind Core uses Ruff for fast linting and import ordering, Black for a
consistent Python code style, MyPy for strict static type checking, and Pytest
for automated tests. Structuring these tools in `pyproject.toml` keeps their
configuration close to the package metadata.

Pre-commit runs the most immediate checks before a commit is created. Its
hooks fix whitespace and end-of-file issues, validate YAML and TOML files, run
Ruff and its formatter, and run Black. This gives contributors fast feedback
without replacing the full quality checks in continuous integration.

## Development Workflow

Create a Python 3.12 or later virtual environment, activate it, and install
the project with the `dev` extra:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pre-commit install
```

Work against the editable installation. The installed hooks run automatically
when creating commits. Run the commands below locally before opening a review
when a complete validation is useful.

## Code Quality Pipeline

The quality pipeline checks source consistency, types, and behavior in this
order:

1. Ruff checks lint rules and import ordering.
2. Ruff format and Black verify formatting.
3. MyPy checks the configured application and test modules in strict mode.
4. Pytest runs the test suite.

```bash
ruff check .
ruff format --check .
black --check .
mypy
pytest
```
