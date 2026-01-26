"""Tests for moldecode."""

from __future__ import annotations

import moldecode


def test_version() -> None:
    """Test that version is defined."""
    assert hasattr(moldecode, "__version__")
    assert isinstance(moldecode.__version__, str)


def test_all_exports() -> None:
    """Test that __all__ is defined."""
    assert hasattr(moldecode, "__all__")
    assert isinstance(moldecode.__all__, list)
