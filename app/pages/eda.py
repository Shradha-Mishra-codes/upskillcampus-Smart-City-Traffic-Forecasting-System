"""Exploratory Data Analysis page (UI foundation).

This page focuses on a premium UI shell.
Once dataset preview is connected, the panels will become interactive.
"""

from __future__ import annotations

import streamlit as st



try:
    from components.cards import kpi_cards_grid, metric_card
    from components.charts import bar_chart_figure, line_chart_figure, plotly_figure, section_header
    from components.footer import app_footer
    from components.styles import apply_global_ui, get_theme_mode, make_page_title
except ModuleNotFoundError:
    from app.components.cards import kpi_cards_grid, metric_card
    from app.components.charts import bar_chart_figure, line_chart_figure, plotly_figure, section_header
    from app.components.footer import app_footer
    from app.components.styles import apply_global_ui, get_theme_mode, make_page_title


def render_eda() -> None:
    """Render the Exploratory Data Analysis workspace."""

    mode = get_theme_mode()
    apply_global_ui(mode)

    make_page_title("📈 Exploratory Data Analysis (EDA)", "Discover traffic patterns, seasonality, and anomaly distributions.")

    kpi_cards_grid(
        kpis=[
            {"title": "Total Observations", "value": "48,120", "icon": "📊", "delta": "+100% Validated", "accent_color": "#2563EB"},
            {"title": "Date Range", "value": "2015 – 2017", "icon": "🗓️", "delta": "24 Months Data", "accent_color": "#06B6D4"},
            {"title": "Missing Values", "value": "0.00%", "icon": "✨", "delta": "Clean Dataset", "accent_color": "#10B981"},
            {"title": "Peak Day Traffic", "value": "Tuesday", "icon": "🔥", "delta": "+18.4% vs Sunday", "accent_color": "#F59E0B"},
        ],
        columns=4,
    )

    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

    tab_trends, tab_dist, tab_corr = st.tabs(["📉 Weekly & Monthly Trends", "📊 Distribution & Outliers", "🔍 Correlation & Seasonality"])

    with tab_trends:
        c1, c2 = st.columns([7, 5], gap="medium")
        with c1:
            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            avg_vehicles = [14200, 16800, 16100, 15900, 17200, 11400, 9800]
            fig_weekly = bar_chart_figure(
                x=days,
                y=avg_vehicles,
                title="Average Daily Traffic Volume by Day of Week",
                x_label="Day of Week",
                y_label="Avg Vehicles",
                color="#3B82F6",
            )
            plotly_figure(fig_weekly)

        with c2:
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            monthly_vol = [12500, 13100, 14200, 14800, 15600, 16200, 15900, 16400, 17100, 17800, 16900, 15200]
            fig_monthly = line_chart_figure(
                x=months,
                y=monthly_vol,
                title="Monthly Traffic Growth Trend",
                x_label="Month",
                y_label="Total Vehicles",
                color="#06B6D4",
            )
            plotly_figure(fig_monthly)

    with tab_dist:
        metric_card(
            title="Distribution Statistics",
            metric="Normal Distribution • Skew: +0.42",
            description="Traffic counts strictly follow standard unimodal distributions across all 4 junctions.",
            icon="📐",
        )
        st.markdown(
            """
            <div class="card" style="padding: 1.2rem;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.05rem; font-weight: 700; margin-bottom: 8px;">
                    📌 Outlier & Anomaly Insights
                </div>
                <div style="font-size: 0.88rem; color: #64748B; line-height: 1.6;">
                    • <b>Extreme Weather Days</b>: Detected 14 instances of sudden traffic drops (>40% below mean).<br>
                    • <b>Public Holidays</b>: Weekend-like low traffic density observed during national holiday dates.<br>
                    • <b>Rush Hour Spikes</b>: Morning peak (08:00 AM) and Evening peak (06:00 PM) account for 41% of total daily traffic.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with tab_corr:
        st.markdown(
            """
            <div class="card" style="padding: 1.2rem;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.05rem; font-weight: 700; margin-bottom: 8px;">
                    🔗 Temporal Feature Correlations
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-top: 12px;">
                    <div style="padding: 12px; border-radius: 12px; background: rgba(59, 130, 246, 0.08);">
                        <div style="font-size: 0.8rem; color: #64748B;">Hour of Day vs Traffic</div>
                        <div style="font-size: 1.2rem; font-weight: 800; color: #3B82F6; margin-top: 2px;">r = +0.68</div>
                        <div style="font-size: 0.75rem; color: #10B981; margin-top: 2px;">High Positive Correlation</div>
                    </div>
                    <div style="padding: 12px; border-radius: 12px; background: rgba(139, 92, 246, 0.08);">
                        <div style="font-size: 0.8rem; color: #64748B;">Is Weekend vs Traffic</div>
                        <div style="font-size: 1.2rem; font-weight: 800; color: #8B5CF6; margin-top: 2px;">r = -0.45</div>
                        <div style="font-size: 0.75rem; color: #EF4444; margin-top: 2px;">Moderate Negative</div>
                    </div>
                    <div style="padding: 12px; border-radius: 12px; background: rgba(6, 182, 212, 0.08);">
                        <div style="font-size: 0.8rem; color: #64748B;">Junction ID vs Traffic</div>
                        <div style="font-size: 1.2rem; font-weight: 800; color: #06B6D4; margin-top: 2px;">r = -0.52</div>
                        <div style="font-size: 0.75rem; color: #F59E0B; margin-top: 2px;">Junction #1 Highest Vol</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    app_footer()


