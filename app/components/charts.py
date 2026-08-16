"""Plotly chart wrapper helpers.

All pages should use these helpers to avoid duplicating Plotly figure setup.
The functions are UI-level wrappers (Streamlit rendering) and/or figure
builders that return Plotly figures.

Phase 2: UI foundation only; charts support empty data with friendly
placeholders.
"""

from __future__ import annotations

from typing import Any, Optional, Sequence

import streamlit as st


def section_header(title: str, subtitle: Optional[str] = None) -> None:
    """Render a consistent section header."""

    st.markdown(
        f"<div class='section-header'>{title}</div>",
        unsafe_allow_html=True,
    )
    if subtitle:
        st.markdown(
            f"<div class='muted' style='margin-top:-6px; font-weight:700;'>{subtitle}</div>",
            unsafe_allow_html=True,
        )


def chart_container(title: str, subtitle: Optional[str] = None, height_px: int = 420) -> Any:
    """Open a standard card-like container and render the title."""

    st.markdown(
        f"""
        <div class='card' style='padding:16px; height:auto; margin-bottom:16px;'>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<div style='font-weight:900; font-size:16px; margin-bottom:8px;'>{title}</div>",
        unsafe_allow_html=True,
    )

    if subtitle:
        st.markdown(
            f"<div class='muted' style='font-weight:700; margin-top:-8px; margin-bottom:10px;'>{subtitle}</div>",
            unsafe_allow_html=True,
        )

    return st.container()


def chart_container_close() -> None:
    """Close a previously opened chart container."""

    st.markdown("</div>", unsafe_allow_html=True)


def plotly_figure(figure: Any, *, use_container_width: bool = True) -> None:
    """Render a Plotly figure using Streamlit.

    Plotly is an optional runtime dependency for Phase 2.
    """

    try:
        import plotly.graph_objects as go  # noqa: F401
    except ModuleNotFoundError:
        st.info("Plotly is not installed in this environment. Charts are unavailable.")
        return

    st.plotly_chart(figure, use_container_width=use_container_width)


def empty_plot_figure(title: str = "No data") -> Any:
    """Create a simple Plotly figure placeholder."""

    try:
        import plotly.graph_objects as go
    except ModuleNotFoundError:
        return None

    fig = go.Figure()
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=20, r=20, t=40, b=20),
        title=dict(text=title, x=0.5),
        xaxis_visible=False,
        yaxis_visible=False,
    )
    return fig


def line_chart_figure(
    x: Sequence[Any],
    y: Sequence[float],
    *,
    title: str,
    x_label: str = "",
    y_label: str = "",
    color: Optional[str] = "#3B82F6",
) -> Any:
    """Build an interactive Plotly line chart with sleek glass visual styling."""

    try:
        import plotly.graph_objects as go
    except ModuleNotFoundError:
        return None

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=list(x),
            y=list(y),
            mode="lines+markers",
            name=title,
            line=dict(color=color or "#3B82F6", width=3, shape="spline"),
            marker=dict(size=7, color=color or "#3B82F6", line=dict(width=2, color="#FFFFFF")),
            fill="tozeroy",
            fillcolor="rgba(59, 130, 246, 0.08)",
            hovertemplate="<b>%{x}</b><br>%{y} " + (y_label or "Value") + "<extra></extra>",
        )
    )

    fig.update_layout(
        title=dict(text=title, font=dict(family="Outfit, sans-serif", size=16)),
        margin=dict(l=30, r=20, t=50, b=30),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(title=x_label, showgrid=False, zeroline=False),
        yaxis=dict(title=y_label, showgrid=True, gridcolor="rgba(148, 163, 184, 0.12)", zeroline=False),
        hovermode="x unified",
    )
    return fig


def bar_chart_figure(
    x: Sequence[Any],
    y: Sequence[float],
    *,
    title: str,
    x_label: str = "",
    y_label: str = "",
    color: Optional[str] = "#06B6D4",
) -> Any:
    """Build an interactive Plotly bar chart."""

    try:
        import plotly.graph_objects as go
    except ModuleNotFoundError:
        return None

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=list(x),
            y=list(y),
            marker=dict(
                color=color or "#06B6D4",
                line=dict(color="rgba(255,255,255,0.2)", width=1),
            ),
            hovertemplate="<b>%{x}</b><br>%{y}<extra></extra>",
        )
    )
    fig.update_layout(
        title=dict(text=title, font=dict(family="Outfit, sans-serif", size=16)),
        margin=dict(l=30, r=20, t=50, b=30),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(title=x_label, showgrid=False),
        yaxis=dict(title=y_label, showgrid=True, gridcolor="rgba(148, 163, 184, 0.12)"),
    )
    return fig


def heatmap_figure(
    z: Sequence[Sequence[float]],
    *,
    title: str,
    x_labels: Sequence[Any],
    y_labels: Sequence[Any],
) -> Any:
    """Build an interactive Plotly heatmap chart."""

    try:
        import plotly.graph_objects as go
    except ModuleNotFoundError:
        return None

    fig = go.Figure(
        data=go.Heatmap(
            z=z,
            x=list(x_labels),
            y=list(y_labels),
            hovertemplate="%{y} | %{x}<br>Traffic: <b>%{z}</b><extra></extra>",
            colorscale=[[0, "#0F172A"], [0.5, "#2563EB"], [1, "#06B6D4"]],
            showscale=True,
        )
    )
    fig.update_layout(
        title=dict(text=title, font=dict(family="Outfit, sans-serif", size=16)),
        margin=dict(l=30, r=20, t=50, b=30),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
    )
    return fig



def render_empty_chart(title: str, subtitle: Optional[str] = None) -> None:
    """Render a consistent empty chart experience."""

    if subtitle:
        st.markdown(
            f"<div class='muted' style='font-weight:700; margin-bottom:10px;'>{subtitle}</div>",
            unsafe_allow_html=True,
        )

    fig = empty_plot_figure(title=title)
    if fig is None:
        return
    plotly_figure(fig)

