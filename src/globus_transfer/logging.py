"""Logging configuration for the command-line application."""

import logging


def configure_logging(*, verbose: bool = False) -> None:
    """Configure process-wide logging."""
    level = logging.DEBUG if verbose else logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(levelname)s:%(name)s:%(message)s",
    )
