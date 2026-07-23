"""Command-line interface configuration."""

import typer

app = typer.Typer(
    name="documind",
    help="AI-powered repository analysis.",
    no_args_is_help=True,
)
