"""Shared styling and theme utilities for the Streamlit SaaS UI.

This module provides:
- Global CSS injection
- Light/Dark theme support
- Plotly template switching via plotly.io templates
- Shared UI helpers
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Any, Dict, Literal, Optional

import streamlit as st


ThemeMode = Literal["light", "dark"]


@dataclass(frozen=True)
class ThemeTokens:
    primary: str = "#2563EB"
    secondary: str = "#3B82F6"
    accent: str = "#06B6D4"
    success: str = "#10B981"
    warning: str = "#F59E0B"
    danger: str = "#EF4444"
    purple: str = "#8B5CF6"
    neutral_dark: str = "#0A0E1A"
    neutral_gray: str = "#64748B"
    light_bg: str = "#F1F5F9"
    card_bg: str = "#FFFFFF"
    border: str = "#E2E8F0"


def _ensure_theme_session_state() -> None:
    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "dark"


def get_theme_mode() -> ThemeMode:
    _ensure_theme_session_state()
    mode = str(st.session_state.theme_mode).lower()
    return "light" if mode == "light" else "dark"


def toggle_theme() -> None:
    current = get_theme_mode()
    st.session_state.theme_mode = "light" if current == "dark" else "dark"


def apply_theme(mode: ThemeMode) -> None:
    tokens = ThemeTokens()

    if mode == "light":
        bg_main = "#F8FAFC"
        bg_gradient = "radial-gradient(circle at 10% 20%, rgba(59, 130, 246, 0.08) 0%, transparent 40%), radial-gradient(circle at 90% 80%, rgba(6, 182, 212, 0.08) 0%, transparent 45%)"
        surface = "rgba(255, 255, 255, 0.82)"
        surface_hover = "rgba(255, 255, 255, 0.95)"
        text = "#0F172A"
        text_heading = "#0F172A"
        muted = "#64748B"
        border = "rgba(226, 232, 240, 0.9)"
        border_hover = "rgba(37, 99, 235, 0.4)"
        shadow = "0 10px 25px -5px rgba(148, 163, 184, 0.15), 0 8px 10px -6px rgba(148, 163, 184, 0.1)"
        shadow_hover = "0 20px 30px -10px rgba(37, 99, 235, 0.18)"
        sidebar_bg = "rgba(255, 255, 255, 0.75)"
        input_bg = "rgba(255, 255, 255, 0.9)"
    else:
        bg_main = "#0B0F19"
        bg_gradient = "radial-gradient(circle at 15% 15%, rgba(139, 92, 246, 0.15) 0%, transparent 45%), radial-gradient(circle at 85% 75%, rgba(59, 130, 246, 0.15) 0%, transparent 50%)"
        surface = "rgba(15, 23, 42, 0.68)"
        surface_hover = "rgba(30, 41, 59, 0.85)"
        text = "#F8FAFC"
        text_heading = "#FFFFFF"
        muted = "#94A3B8"
        border = "rgba(148, 163, 184, 0.18)"
        border_hover = "rgba(59, 130, 246, 0.5)"
        shadow = "0 10px 30px -5px rgba(0, 0, 0, 0.4), 0 0 15px rgba(59, 130, 246, 0.05)"
        shadow_hover = "0 20px 35px -5px rgba(0, 0, 0, 0.5), 0 0 25px rgba(139, 92, 246, 0.25)"
        sidebar_bg = "rgba(11, 15, 25, 0.85)"
        input_bg = "rgba(15, 23, 42, 0.8)"

    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Outfit:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"], .stApp {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        color: {text};
    }}

    .stApp {{
        background-color: {bg_main};
        background-image: {bg_gradient};
        background-attachment: fixed;
    }}

    /* Global Animations & Transitions */
    * {{
        transition: background-color 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(8px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    .main .block-container {{
        animation: fadeIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 1350px;
    }}

    /* Hide default Streamlit decoration header bar */
    header[data-testid="stHeader"] {{
        background: transparent !important;
        height: 0px !important;
    }}

    /* Glassmorphic Card Engine */
    .card, div[data-testid="stForm"] {{
        background: {surface} !important;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid {border} !important;
        border-radius: 18px !important;
        box-shadow: {shadow} !important;
        padding: 1.25rem;
        margin-bottom: 1.25rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }}

    .card:hover {{
        background: {surface_hover} !important;
        border-color: {border_hover} !important;
        box-shadow: {shadow_hover} !important;
        transform: translateY(-3px);
    }}

    /* Container element overrides for glassmorphism */
    div[data-testid="stVerticalBlockBorderWrapper"] > div {{
        border-radius: 18px !important;
        background: {surface} !important;
        backdrop-filter: blur(14px);
        border: 1px solid {border} !important;
        box-shadow: {shadow} !important;
        transition: all 0.3s ease !important;
    }}

    div[data-testid="stVerticalBlockBorderWrapper"] > div:hover {{
        border-color: {border_hover} !important;
        box-shadow: {shadow_hover} !important;
    }}

    /* Headers & Typography */
    h1, h2, h3, .section-header {{
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        color: {text_heading} !important;
        letter-spacing: -0.025em !important;
    }}

    .section-header {{
        font-size: 1.5rem;
        margin-bottom: 0.25rem;
    }}

    .muted {{
        color: {muted} !important;
    }}

    /* Buttons Styling */
    button[kind="secondary"], button[kind="primary"], div.stButton > button {{
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.25s ease !important;
        border: 1px solid {border} !important;
        background: {surface} !important;
        color: {text} !important;
        backdrop-filter: blur(8px);
    }}

    div.stButton > button:hover {{
        border-color: {tokens.primary} !important;
        background: linear-gradient(135deg, {tokens.primary}, {tokens.secondary}) !important;
        color: #FFFFFF !important;
        box-shadow: 0 8px 20px rgba(37, 99, 235, 0.35) !important;
        transform: translateY(-2px);
    }}

    div.stButton > button:active {{
        transform: translateY(0);
    }}

    /* Input fields styling */
    input, select, textarea, div[data-baseweb="input"] {{
        border-radius: 10px !important;
        background-color: {input_bg} !important;
        color: {text} !important;
        border-color: {border} !important;
    }}

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {{
        background: {sidebar_bg} !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-right: 1px solid {border} !important;
    }}

    section[data-testid="stSidebar"] .block-container {{
        padding-top: 1.5rem;
    }}

    /* Plotly transparent background */
    .js-plotly-plot .plotly .main-svg, .js-plotly-plot .plotly .bg {{
        background: transparent !important;
    }}

    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
        width: 8px;
        height: 8px;
    }}
    ::-webkit-scrollbar-track {{
        background: transparent;
    }}
    ::-webkit-scrollbar-thumb {{
        background: {border};
        border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
        background: {muted};
    }}
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)


def set_plotly_theme(mode: ThemeMode) -> None:
    """Configure Plotly theme. Safe if plotly is missing."""
    try:
        import plotly.io as pio
    except ModuleNotFoundError:
        return

    pio.templates.default = "plotly_white" if mode == "light" else "plotly_dark"


def apply_global_ui(mode: ThemeMode) -> None:
    apply_theme(mode)
    set_plotly_theme(mode)


def st_kpi_value_style(value: str) -> None:
    st.markdown(
        f"<div style='font-size: 32px; font-weight: 800; letter-spacing: -0.02em;'>{value}</div>",
        unsafe_allow_html=True,
    )


def make_page_title(title: str, subtitle: Optional[str] = None) -> None:
    st.markdown(
        f"""
        <div style="margin-bottom: 20px;">
            <div style="font-family:'Outfit', sans-serif; font-size: 2rem; font-weight: 800; letter-spacing: -0.03em;">{title}</div>
            {f'<div class="muted" style="font-size: 1rem; font-weight: 500; margin-top: 4px;">{subtitle}</div>' if subtitle else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )


def chart_container_start(height_px: int = 360) -> None:
    st.markdown(
        f"<div class='card' style='height:{height_px}px;'>",
        unsafe_allow_html=True,
    )


def chart_container_end() -> None:
    st.markdown("</div>", unsafe_allow_html=True)


def info_banner(icon: str, title: str, description: str) -> None:
    st.info(f"{icon} {title}\n\n{description}")


def empty_state(icon: str, title: str, description: str) -> None:
    st.warning(f"{icon} {title}\n\n{description}")


def set_link_color() -> None:
    mode = get_theme_mode()
    color = "#2563EB" if mode == "light" else "#60A5FA"
    st.markdown(f"<style>a {{ color: {color}; }}</style>", unsafe_allow_html=True)


def as_dict() -> Dict[str, Any]:
    return ThemeTokens().__dict__


