"""Professional footer component for the Streamlit SaaS UI."""

from __future__ import annotations

from datetime import datetime

import streamlit as st

from config.settings import AppSettings


def app_footer() -> None:
    """Render the app footer."""

    st.markdown("---")

    last_updated = datetime.utcnow().strftime("%Y-%m-%d")

    st.markdown(
        f"""
        <div style="display:flex; justify-content:space-between; align-items:center; gap:16px; flex-wrap:wrap;">
            <div style="color:#64748B; font-weight:800;">
                {AppSettings.APP_ICON} {AppSettings.APP_NAME} <span style="font-weight:700;">· v1.0</span>
            </div>
            <div style="color:#64748B; font-weight:700;">Last updated: {last_updated} UTC</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

