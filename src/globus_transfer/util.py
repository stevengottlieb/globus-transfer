"""Shared utility helpers."""

from collections.abc import Iterable


def comma_join(values: Iterable[str]) -> str:
    """Return a comma-separated string for display."""
    return ", ".join(values)
