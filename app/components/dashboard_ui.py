"""Dashboard UI components for Phase 2.

UI-only utilities to render a premium Streamlit dashboard without overlapping
layout. Backend/ML logic is intentionally not included.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import streamlit as st


@dataclass(frozen=True)
class CardGradients:
    """Gradient token colors used by KPI borders."""

    border_a: str = "#2563EB"
    border_b: str = "#3B82F6"
    glow_c: str = "#06B6D4"


def _top_shadow_css() -> str:
    return (
        "box-shadow: 0 14px 40px rgba(2,6,23,0.12);"
        " border-radius: 20px;"
    )


def set_background_image(mode: str) -> None:
    """Set a subtle ambient glass glow background that never interferes with text contrast."""

    if mode == "light":
        glow_a = "rgba(59, 130, 246, 0.06)"
        glow_b = "rgba(6, 182, 212, 0.06)"
    else:
        glow_a = "rgba(139, 92, 246, 0.12)"
        glow_b = "rgba(59, 130, 246, 0.12)"

    st.markdown(
        f"""
        <style>
        .bg-glow-container {{
            position: fixed;
            inset: 0;
            z-index: -2;
            pointer-events: none;
            background:
                radial-gradient(1000px 500px at 15% 15%, {glow_a}, transparent 60%),
                radial-gradient(800px 400px at 85% 85%, {glow_b}, transparent 60%);
        }}
        </style>
        <div class="bg-glow-container"></div>
        """,
        unsafe_allow_html=True,
    )


def donut_placeholder_card() -> None:
    """Render an interactive Donut plot placeholder."""

    try:
        import plotly.graph_objects as go

        labels = ["Junction 1", "Junction 2", "Junction 3", "Junction 4"]
        values = [42000, 31000, 28000, 23583]

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=labels,
                    values=values,
                    hole=0.6,
                    marker=dict(colors=["#2563EB", "#3B82F6", "#06B6D4", "#8B5CF6"]),
                    textinfo="percent",
                    hovertemplate="<b>%{label}</b><br>Volume: %{value}<extra></extra>",
                )
            ]
        )
        fig.update_layout(
            title=dict(text="Traffic Distribution", font=dict(family="Outfit, sans-serif", size=16, weight="bold")),
            margin=dict(l=20, r=20, t=40, b=20),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        )
        st.plotly_chart(fig, use_container_width=True)
    except ModuleNotFoundError:
        st.info("Traffic distribution visualization ready.")



