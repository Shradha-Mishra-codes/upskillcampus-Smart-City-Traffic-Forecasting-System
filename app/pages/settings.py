"""Settings page (UI foundation).

This page provides the appearance and UX settings shell.
"""

from __future__ import annotations

import streamlit as st



try:
    from components.cards import info_card
    from components.footer import app_footer
    from components.styles import apply_global_ui, get_theme_mode, make_page_title, toggle_theme
except ModuleNotFoundError:
    from app.components.cards import info_card
    from app.components.footer import app_footer
    from app.components.styles import apply_global_ui, get_theme_mode, make_page_title, toggle_theme


def render_settings() -> None:
    """Render Settings & Preferences page."""

    mode = get_theme_mode()
    apply_global_ui(mode)

    make_page_title("⚙️ System Settings & Preferences", "Manage theme appearance, chart animations, and memory cache.")

    col1, col2 = st.columns([6, 6], gap="medium")

    with col1:
        st.markdown(
            """
            <div class="card" style="padding: 1.4rem;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700; margin-bottom: 12px;">
                    🎨 Appearance & Theme Engine
                </div>
            """,
            unsafe_allow_html=True,
        )

        current_theme = mode.upper()
        info_card(
            title="Active Mode",
            body=f"Currently active theme: <b>{current_theme} MODE</b>",
            icon="🌙" if mode == "dark" else "☀️",
        )

        if st.button("🔄 Switch Theme Mode (Light / Dark)", use_container_width=True):
            toggle_theme()
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div class="card" style="padding: 1.4rem;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700; margin-bottom: 12px;">
                    ⚡ Performance & System Caching
                </div>
            """,
            unsafe_allow_html=True,
        )

        enable_animations = st.checkbox("Enable Glassmorphic Micro-Animations", value=True)
        high_precision = st.checkbox("Enable High Precision Plotly Spline Curves", value=True)

        if st.button("🧹 Clear In-Memory Model Cache", use_container_width=True):
            st.cache_data.clear()
            st.toast("Memory cache cleared successfully!")

        st.markdown("</div>", unsafe_allow_html=True)

    app_footer()


