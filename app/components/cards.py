"""UI card components for the Streamlit SaaS dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Optional

import streamlit as st


@dataclass(frozen=True)
class CardPalette:
    """Default palette (aligned with docs/design.md)."""

    primary: str = "#2563EB"
    accent: str = "#06B6D4"


def _accent_left_bar(color: str) -> str:
    return (
        f"background:{color}; width: 10px; border-radius: 18px; margin-right: 12px;"
    )


def kpi_card(
    title: str,
    value: Any,
    icon: str = "",
    delta: Optional[str] = None,
    accent_color: str = "#2563EB",
    height: int = 140,
) -> None:
    """Render a premium glassmorphic KPI card."""

    is_positive = "+" in str(delta) if delta else True
    delta_bg = "rgba(16, 185, 129, 0.12)" if is_positive else "rgba(239, 68, 68, 0.12)"
    delta_color = "#10B981" if is_positive else "#EF4444"

    st.markdown(
        f"""
        <div class="card" style="position: relative; overflow: hidden; padding: 1.2rem;">
            <div style="position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, {accent_color}, rgba(6, 182, 212, 0.8));"></div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                <div style="font-size: 0.85rem; font-weight: 700; color: #64748B; letter-spacing: 0.02em;">{title}</div>
                <div style="font-size: 1.3rem; line-height: 1;">{icon}</div>
            </div>
            <div style="font-family: 'Outfit', sans-serif; font-size: 1.8rem; font-weight: 800; letter-spacing: -0.03em; margin: 4px 0;">{value}</div>
            {f'''<div style="display: inline-flex; align-items: center; gap: 4px; padding: 3px 8px; border-radius: 6px; background: {delta_bg}; color: {delta_color}; font-size: 0.75rem; font-weight: 700; margin-top: 4px;">{delta}</div>''' if delta else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )


def metric_card(
    title: str,
    metric: Any,
    description: str = "",
    icon: str = "",
    accent_color: str = CardPalette().accent,
) -> None:
    """Render a compact glassmorphic metric card."""

    st.markdown(
        f"""
        <div class="card" style="padding: 1.1rem;">
            <div style="display: flex; align-items: flex-start; gap: 12px;">
                <div style="width: 4px; height: 38px; border-radius: 4px; background: {accent_color};"></div>
                <div style="flex: 1;">
                    <div style="font-size: 0.8rem; font-weight: 700; color: #64748B;">{icon} {title}</div>
                    <div style="font-family: 'Outfit', sans-serif; font-size: 1.25rem; font-weight: 800; margin-top: 4px;">{metric}</div>
                    {f'<div style="font-size: 0.78rem; color: #94A3B8; margin-top: 4px;">{description}</div>' if description else ''}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def info_card(title: str, body: str, icon: str = "ℹ️") -> None:
    """Render a glassmorphic info card."""

    st.markdown(
        f"""
        <div class="card" style="padding: 1.2rem;">
            <div style="display: flex; align-items: center; gap: 8px; font-weight: 800; font-size: 0.95rem; margin-bottom: 6px;">
                <span>{icon}</span> <span>{title}</span>
            </div>
            <div style="font-size: 0.88rem; color: #64748B; line-height: 1.5;">{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def empty_state(icon: str, title: str, description: str) -> None:
    """Render a stylish glass empty-state card."""

    st.markdown(
        f"""
        <div style="padding: 2rem; border-radius: 18px; border: 2px dashed rgba(148, 163, 184, 0.25); background: rgba(255, 255, 255, 0.02); text-align: center; margin-bottom: 1.25rem;">
            <div style="font-size: 2.2rem; margin-bottom: 8px;">{icon}</div>
            <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700; margin-bottom: 4px;">{title}</div>
            <div style="font-size: 0.85rem; color: #64748B; max-width: 400px; margin: 0 auto;">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def kpi_cards_grid(kpis: Iterable[dict[str, Any]], columns: int = 4) -> None:
    """Render KPI cards in a responsive grid using Streamlit columns."""

    cols = st.columns(columns, gap="medium")
    for idx, kpi in enumerate(kpis):
        with cols[idx % columns]:
            kpi_card(
                title=str(kpi.get("title", "")),
                value=kpi.get("value", "—"),
                icon=str(kpi.get("icon", "")),
                delta=kpi.get("delta"),
                accent_color=str(kpi.get("accent_color", CardPalette().primary)),
            )


