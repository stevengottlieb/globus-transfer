"""Module entry point for ``python -m globus_transfer``."""

from globus_transfer.cli import app


def main() -> None:
    """Run the command-line application."""
    app()


if __name__ == "__main__":
    main()
