"""Top navigation bar for the app.

Contains:
- Project title
- Theme toggle
- Status indicator
- Current dataset status placeholder

Routing is centralized in app/main.py.

"""

from __future__ import annotations

import streamlit as st

from components.styles import get_theme_mode, toggle_theme
from config.settings import AppSettings



def _status_badge(text: str) -> str:
    return (
        "<div style=\""
        "padding:6px 12px; border-radius:999px; background: rgba(34,197,94,0.15); "
        "color:#22C55E; font-weight:900; font-size:12px;\">"
        f"{text}</div>"
    )


def navbar(dataset_status: str = "No dataset loaded") -> None:
    """Render a modern SaaS top navbar."""

    theme_mode = get_theme_mode()
    theme_icon = "☀️" if theme_mode == "dark" else "🌙"
    theme_label = "Light Mode" if theme_mode == "dark" else "Dark Mode"

    st.markdown(
        """
        <style>
        .topbar-wrapper {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(148, 163, 184, 0.2);
            border-radius: 16px;
            padding: 12px 20px;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        }
        .topbar-left {
            display: flex;
            align-items: center;
            gap: 14px;
        }
        .topbar-title {
            font-family: 'Outfit', sans-serif;
            font-size: 1.15rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .topbar-right {
            display: flex;
            align-items: center;
            gap: 14px;
        }
        .badge-status {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 5px 12px;
            border-radius: 999px;
            background: rgba(34, 197, 94, 0.12);
            border: 1px solid rgba(34, 197, 94, 0.3);
            color: #10B981;
            font-size: 0.78rem;
            font-weight: 700;
        }
        .badge-dataset {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 5px 12px;
            border-radius: 999px;
            background: rgba(59, 130, 246, 0.12);
            border: 1px solid rgba(59, 130, 246, 0.3);
            color: #3B82F6;
            font-size: 0.78rem;
            font-weight: 700;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    top_col1, top_col2, top_col3 = st.columns([4, 4, 3], gap="medium")

    with top_col1:
        st.markdown(
            f"""
            <div class='topbar-title'>
                <span style='font-size:1.4rem;'>{AppSettings.APP_ICON}</span>
                <span>{AppSettings.APP_NAME}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with top_col2:
        # Search & Dataset status badge
        st.markdown(
            f"""
            <div style="display:flex; align-items:center; gap:10px; height:100%;">
                <div class="badge-status">🟢 Engine Online</div>
                <div class="badge-dataset">📦 {dataset_status}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with top_col3:
        btn_col, search_col = st.columns([2, 1])
        with btn_col:
            if st.button(f"{theme_icon} {theme_label}", key="topbar_theme_toggle", use_container_width=True):
                toggle_theme()
                st.rerun()
        with search_col:
            st.markdown(
                """
                <div style="text-align:right; font-size:1.2rem; cursor:pointer;" title="Notifications & Help">
                    🔔
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown("<div style='margin-bottom:12px;'></div>", unsafe_allow_html=True)


