"""Forecasting page (UI foundation).

This page provides the UI shell for forecast visualization.
No prediction logic is executed in this UI-only foundation.
"""

from __future__ import annotations

import streamlit as st



try:
    from components.cards import kpi_cards_grid
    from components.charts import line_chart_figure, plotly_figure
    from components.footer import app_footer
    from components.styles import apply_global_ui, get_theme_mode, make_page_title
except ModuleNotFoundError:
    from app.components.cards import kpi_cards_grid
    from app.components.charts import line_chart_figure, plotly_figure
    from app.components.footer import app_footer
    from app.components.styles import apply_global_ui, get_theme_mode, make_page_title


def render_forecasting() -> None:
    """Render the Interactive Traffic Forecasting page."""

    mode = get_theme_mode()
    apply_global_ui(mode)

    make_page_title("🔮 AI Traffic Forecasting Engine", "Generate multi-step horizon predictions for smart urban traffic management.")

    kpi_cards_grid(
        kpis=[
            {"title": "Forecast Horizon", "value": "24 Hours Ahead", "icon": "🕒", "delta": "Configurable", "accent_color": "#2563EB"},
            {"title": "Target Junction", "value": "Junction #1 (North)", "icon": "📍", "delta": "High Volume", "accent_color": "#06B6D4"},
            {"title": "Model In Use", "value": "XGBoost + Lag-24", "icon": "🤖", "delta": "94.6% Accuracy", "accent_color": "#8B5CF6"},
            {"title": "Confidence Interval", "value": "95% Bounds", "icon": "🛡️", "delta": "Low Variance", "accent_color": "#10B981"},
        ],
        columns=4,
    )

    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

    c_ctrl, c_plot = st.columns([4, 8], gap="medium")

    with c_ctrl:
        st.markdown(
            """
            <div class="card" style="padding: 1.4rem;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700; margin-bottom: 12px;">
                    ⚙️ Forecast Controls
                </div>
            """,
            unsafe_allow_html=True,
        )

        selected_junction = st.selectbox("Select Target Junction", ["Junction #1 (North)", "Junction #2 (East)", "Junction #3 (Central)", "Junction #4 (South)"])
        horizon_hours = st.slider("Prediction Horizon (Hours)", 6, 72, 24, 6)
        include_confidence = st.checkbox("Show 95% Confidence Interval Bounds", value=True)

        if st.button("✨ Generate Forecast", use_container_width=True):
            st.toast(f"Forecast updated for {selected_junction} ({horizon_hours} Hours)!")

        st.markdown("</div>", unsafe_allow_html=True)

    with c_plot:
        forecast_x = [f"+{h}h" for h in range(1, horizon_hours + 1)]
        # Generate smooth forecast curve
        import math
        base_val = 40
        forecast_y = [round(base_val + 25 * math.sin(i / 3) + (i * 0.4)) for i in range(1, horizon_hours + 1)]

        fig_forecast = line_chart_figure(
            x=forecast_x,
            y=forecast_y,
            title=f"Predicted Traffic Flow - Next {horizon_hours} Hours ({selected_junction})",
            x_label="Forecast Horizon",
            y_label="Predicted Vehicle Count",
            color="#2563EB",
        )
        plotly_figure(fig_forecast)

    app_footer()


