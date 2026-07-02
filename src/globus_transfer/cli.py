"""Command-line interface for globus-transfer."""

from typing import Annotated

import typer
from rich.console import Console

from globus_transfer.config import AppPaths, get_app_paths
from globus_transfer.logging import configure_logging

app = typer.Typer(
    name="gtransfer",
    help="Manage Globus transfers from the command line.",
    no_args_is_help=True,
)
console = Console()


def _placeholder(command: str) -> None:
    console.print(f"[yellow]{command}[/yellow] is not implemented yet.")
    raise typer.Exit(code=0)


@app.callback()
def main(
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Enable verbose diagnostic logging."),
    ] = False,
) -> None:
    """Configure shared command-line behavior."""
    configure_logging(verbose=verbose)


@app.command()
def login() -> None:
    """Authenticate with Globus."""
    _placeholder("login")


@app.command()
def logout() -> None:
    """Remove locally stored Globus authentication state."""
    _placeholder("logout")


@app.command()
def endpoint() -> None:
    """Inspect or manage Globus endpoints."""
    _placeholder("endpoint")


@app.command()
def copy() -> None:
    """Submit a one-time Globus transfer."""
    _placeholder("copy")


@app.command()
def sync() -> None:
    """Submit a synchronization transfer."""
    _placeholder("sync")


@app.command()
def status() -> None:
    """Show the status of a Globus transfer."""
    _placeholder("status")


@app.command()
def history() -> None:
    """List recent Globus transfer activity."""
    _placeholder("history")


@app.command()
def resume() -> None:
    """Resume a saved or interrupted transfer workflow."""
    _placeholder("resume")


@app.command()
def doctor(
    show_paths: Annotated[
        bool,
        typer.Option("--show-paths", help="Display configuration and cache paths."),
    ] = False,
) -> None:
    """Run local environment checks."""
    paths = get_app_paths()
    console.print("[green]gtransfer is installed and ready.[/green]")
    console.print("Globus integration will be added in a future milestone.")
    if show_paths:
        _print_paths(paths)


def _print_paths(paths: AppPaths) -> None:
    console.print(f"Config directory: {paths.config_dir}")
    console.print(f"Cache directory: {paths.cache_dir}")
    console.print(f"Data directory: {paths.data_dir}")
