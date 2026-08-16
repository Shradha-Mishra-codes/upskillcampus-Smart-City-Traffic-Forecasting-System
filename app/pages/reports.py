"""Reports page (UI foundation).

This page provides the UI shell for report export.
No export logic is executed in this UI-only foundation.
"""

from __future__ import annotations

import streamlit as st



try:
    from components.cards import info_card
    from components.footer import app_footer
    from components.styles import apply_global_ui, get_theme_mode, make_page_title
except ModuleNotFoundError:
    from app.components.cards import info_card
    from app.components.footer import app_footer
    from app.components.styles import apply_global_ui, get_theme_mode, make_page_title


def render_reports() -> None:
    """Render the Reports & Data Export Center."""

    mode = get_theme_mode()
    apply_global_ui(mode)

    make_page_title("📑 Export & Reports Center", "Download forecast summaries, evaluation metrics, and traffic analytics digests.")

    c1, c2, c3 = st.columns(3, gap="medium")

    with c1:
        st.markdown(
            """
            <div class="card" style="padding: 1.4rem;">
                <div style="font-size: 1.8rem; margin-bottom: 8px;">📊</div>
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700;">Forecast Results (CSV)</div>
                <div style="font-size: 0.82rem; color: #64748B; margin: 6px 0 14px 0;">Hourly predicted volumes across all junctions with 95% confidence bounds.</div>
            """,
            unsafe_allow_html=True,
        )
        st.download_button(
            label="⬇️ Download Forecast CSV",
            data="DateTime,Junction,Predicted_Vehicles\n2026-07-22 00:00,1,42\n2026-07-22 01:00,1,38\n",
            file_name="traffic_forecast_2026.csv",
            mime="text/csv",
            use_container_width=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown(
            """
            <div class="card" style="padding: 1.4rem;">
                <div style="font-size: 1.8rem; margin-bottom: 8px;">📈</div>
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700;">Model Benchmarks (JSON)</div>
                <div style="font-size: 0.82rem; color: #64748B; margin: 6px 0 14px 0;">Complete performance evaluation metrics (MAE, RMSE, R² scores).</div>
            """,
            unsafe_allow_html=True,
        )
        st.download_button(
            label="⬇️ Download Metrics JSON",
            data='{"model":"XGBoost","mae":4.12,"rmse":6.35,"r2":0.946}\n',
            file_name="model_metrics.json",
            mime="application/json",
            use_container_width=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        st.markdown(
            """
            <div class="card" style="padding: 1.4rem;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700;">📑 Executive Summary Report</div>
                <div style="font-size: 0.82rem; color: #64748B; margin: 6px 0 14px 0;">Formatted PDF executive traffic summary for city authorities.</div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("📄 Generate Executive Digest", use_container_width=True):
            st.success("Executive Digest compiled and ready for print.")
        st.markdown("</div>", unsafe_allow_html=True)

    app_footer()


