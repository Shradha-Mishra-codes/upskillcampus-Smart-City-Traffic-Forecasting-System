"""Shared layout utilities for Phase 2 UI.

These helpers keep pages consistent and reduce duplication.
"""

from __future__ import annotations

from typing import Optional

import streamlit as st

try:
    from components.styles import make_page_title
except ModuleNotFoundError:
    from app.components.styles import make_page_title


def page_top(title: str, subtitle: Optional[str] = None) -> None:
    """Render a standard page title section."""

    make_page_title(title=title, subtitle=subtitle)


def responsive_grid(columns: int = 3):
    """Create responsive columns with a consistent gap."""

    return st.columns(columns, gap="large")

