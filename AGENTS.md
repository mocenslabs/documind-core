# DocuMind Core Development Instructions

## Project

DocuMind is an AI-powered repository analysis engine.

The current milestone is building the Core engine.

The first public capability will be README generation.

Everything must be designed to support future analyzers.

---

## Architecture

Follow Clean Architecture.

Never create circular dependencies.

Keep modules loosely coupled.

Favor composition over inheritance.

---

## Python

Python 3.12+

Use type hints everywhere.

Avoid Any unless strictly necessary.

Use dataclasses or Pydantic when appropriate.

---

## Style

Use Ruff.

Use Black.

Use MyPy.

Code must pass all three.

---

## Documentation

Everything in English.

Docstrings in English.

Comments only when necessary.

---

## Project Rules

Do not generate placeholder code.

Do not leave TODOs.

Do not implement features outside the requested scope.

Always update documentation when implementing a module.

---

## Git

Use Conventional Commits.

Never modify unrelated files.

Keep commits focused.

---

## Quality

Readable code is preferred over clever code.

Small modules.

Single responsibility.

SOLID.

---

## Testing

New functionality should include tests whenever applicable.

---

## AI Providers

The system must remain provider-agnostic.

Never hardcode Gemini-specific logic into the Core.

---

## Goal

Build a production-quality AI analysis engine.

Not a demo.

Not a tutorial.

Production quality.
