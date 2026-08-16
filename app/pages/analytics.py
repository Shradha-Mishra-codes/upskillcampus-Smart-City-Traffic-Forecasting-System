"""Analytics page (UI foundation).

This page provides the UI shell for executive analytics.
No model results are computed in this UI-only foundation.
"""

from __future__ import annotations

import streamlit as st



try:
    from components.cards import kpi_cards_grid
    from components.charts import heatmap_figure, plotly_figure
    from components.footer import app_footer
    from components.styles import apply_global_ui, get_theme_mode, make_page_title
except ModuleNotFoundError:
    from app.components.cards import kpi_cards_grid
    from app.components.charts import heatmap_figure, plotly_figure
    from app.components.footer import app_footer
    from app.components.styles import apply_global_ui, get_theme_mode, make_page_title


def render_analytics() -> None:
    """Render the Executive Analytics & Bottleneck Diagnosis page."""

    mode = get_theme_mode()
    apply_global_ui(mode)

    make_page_title("📉 Advanced Traffic Analytics", "Deep spatial-temporal analytics, bottleneck diagnosis, and congestion trends.")

    kpi_cards_grid(
        kpis=[
            {"title": "Peak Congestion", "value": "18:30 PM", "icon": "⏰", "delta": "+24% Concentration", "accent_color": "#F59E0B"},
            {"title": "Primary Bottleneck", "value": "Junction #1 North", "icon": "🚨", "delta": "Critical Red Alert", "accent_color": "#EF4444"},
            {"title": "Flow Efficiency", "value": "78.4%", "icon": "⚡", "delta": "Moderate Velocity", "accent_color": "#06B6D4"},
            {"title": "Sensor Coverage", "value": "100% Active", "icon": "📡", "delta": "17 Signal Nodes", "accent_color": "#10B981"},
        ],
        columns=4,
    )

    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([7, 5], gap="medium")

    with col1:
        st.markdown("<div class='card' style='padding:1.2rem;'>", unsafe_allow_html=True)
        heatmap_data = [
            [25, 42, 85, 92, 45, 18],
            [15, 30, 78, 88, 52, 22],
            [12, 22, 65, 75, 40, 15],
            [8, 15, 42, 58, 28, 10],
        ]
        fig_heat = heatmap_figure(
            z=heatmap_data,
            title="Hourly Congestion Intensity Heatmap (By Junction)",
            x_labels=["04:00", "08:00", "12:00", "16:00", "20:00", "00:00"],
            y_labels=["Junction 1", "Junction 2", "Junction 3", "Junction 4"],
        )
        plotly_figure(fig_heat)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div class="card" style="padding: 1.4rem;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700; margin-bottom: 12px;">
                    🚨 Bottleneck Risk Assessment
                </div>
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    <div style="padding: 12px; border-radius: 12px; background: rgba(239, 68, 68, 0.08); border-left: 4px solid #EF4444;">
                        <div style="font-weight: 700; font-size: 0.9rem; color: #EF4444;">🔴 High Risk: Junction #1 (North Highway)</div>
                        <div style="font-size: 0.8rem; color: #64748B; margin-top: 2px;">Extremely dense bottleneck during evening commute (17:30–19:30). Traffic signal re-timing recommended.</div>
                    </div>
                    <div style="padding: 12px; border-radius: 12px; background: rgba(245, 158, 11, 0.08); border-left: 4px solid #F59E0B;">
                        <div style="font-weight: 700; font-size: 0.9rem; color: #F59E0B;">🟡 Moderate Risk: Junction #2 (East Corridor)</div>
                        <div style="font-size: 0.8rem; color: #64748B; margin-top: 2px;">Morning rush hour slowdown (08:00–09:30). Average speed drops to 18 km/h.</div>
                    </div>
                    <div style="padding: 12px; border-radius: 12px; background: rgba(16, 185, 129, 0.08); border-left: 4px solid #10B981;">
                        <div style="font-weight: 700; font-size: 0.9rem; color: #10B981;">🟢 Low Risk: Junction #4 (South Bypass)</div>
                        <div style="font-size: 0.8rem; color: #64748B; margin-top: 2px;">Smooth vehicular flow maintained across all 24 hours. Zero congestion incidents reported.</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    app_footer()


