"""About page (UI foundation).

This page describes the application and its dashboard experience.
"""

from __future__ import annotations

import streamlit as st

from config.settings import AppSettings


try:
    from components.cards import info_card
    from components.footer import app_footer
    from components.styles import apply_global_ui, get_theme_mode, make_page_title
except ModuleNotFoundError:
    from app.components.cards import info_card
    from app.components.footer import app_footer
    from app.components.styles import apply_global_ui, get_theme_mode, make_page_title
from config.settings import AppSettings


def render_about() -> None:
    """Render About System & Architecture page."""

    mode = get_theme_mode()
    apply_global_ui(mode)

    make_page_title("ℹ️ About Smart City Traffic Platform", "System architecture, machine learning models, and technology stack.")

    col1, col2 = st.columns([7, 5], gap="medium")

    with col1:
        st.markdown(
            f"""
            <div class="card" style="padding: 1.5rem;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.3rem; font-weight: 800; color: #2563EB; margin-bottom: 8px;">
                    {AppSettings.APP_ICON} {AppSettings.APP_NAME}
                </div>
                <div style="font-size: 0.9rem; color: #64748B; line-height: 1.6; margin-bottom: 16px;">
                    An enterprise AI solution for real-time traffic monitoring, congestion pattern discovery, and predictive urban mobility forecasting across smart city junctions.
                </div>
                <div style="font-weight: 700; font-size: 0.95rem; margin-bottom: 8px;">Key Capabilities:</div>
                <ul style="font-size: 0.88rem; color: #64748B; line-height: 1.6; padding-left: 20px;">
                    <li><b>Temporal Feature Engineering</b>: Cyclical sine/cosine encodings, lag metrics, and holiday awareness.</li>
                    <li><b>High Accuracy Regressors</b>: XGBoost, Random Forest, and Deep LSTM ensemble forecasting.</li>
                    <li><b>Executive SaaS Interface</b>: Real-time interactive dashboards with glassmorphism UI & dual-theme support.</li>
                    <li><b>Spatial Bottleneck Alerts</b>: Automated congestion hotspot identification by hour and location.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="card" style="padding: 1.5rem;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700; margin-bottom: 12px;">
                    💻 Tech Stack & Architecture
                </div>
                <div style="display: flex; flex-direction: column; gap: 10px; font-size: 0.88rem;">
                    <div style="padding: 10px; border-radius: 10px; background: rgba(59, 130, 246, 0.08); display: flex; justify-content: space-between;">
                        <span style="font-weight: 600;">Frontend UI Framework</span>
                        <span style="color: #3B82F6; font-weight: 700;">Streamlit + Vanilla Glass CSS</span>
                    </div>
                    <div style="padding: 10px; border-radius: 10px; background: rgba(6, 182, 212, 0.08); display: flex; justify-content: space-between;">
                        <span style="font-weight: 600;">Interactive Visuals</span>
                        <span style="color: #06B6D4; font-weight: 700;">Plotly Graph Objects</span>
                    </div>
                    <div style="padding: 10px; border-radius: 10px; background: rgba(139, 92, 246, 0.08); display: flex; justify-content: space-between;">
                        <span style="font-weight: 600;">Data Processing</span>
                        <span style="color: #8B5CF6; font-weight: 700;">Pandas & NumPy</span>
                    </div>
                    <div style="padding: 10px; border-radius: 10px; background: rgba(16, 185, 129, 0.08); display: flex; justify-content: space-between;">
                        <span style="font-weight: 600;">Machine Learning</span>
                        <span style="color: #10B981; font-weight: 700;">XGBoost & Scikit-Learn</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    app_footer()


