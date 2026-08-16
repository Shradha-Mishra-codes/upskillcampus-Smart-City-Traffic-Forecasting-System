"""Preprocessing page (UI foundation).

This page provides the UI shell for preprocessing and data preparation.
"""

from __future__ import annotations

import streamlit as st



try:
    from components.cards import kpi_cards_grid
    from components.footer import app_footer
    from components.styles import apply_global_ui, get_theme_mode, make_page_title
except ModuleNotFoundError:
    from app.components.cards import kpi_cards_grid
    from app.components.footer import app_footer
    from app.components.styles import apply_global_ui, get_theme_mode, make_page_title


def render_preprocessing() -> None:
    """Render the Preprocessing and Feature Pipeline page."""

    mode = get_theme_mode()
    apply_global_ui(mode)

    make_page_title("🧹 Preprocessing & Feature Engineering", "Configure feature pipelines, temporal encodings, and missing data imputation.")

    kpi_cards_grid(
        kpis=[
            {"title": "Missing Values", "value": "0 Imputed", "icon": "🧽", "delta": "Clean Input", "accent_color": "#2563EB"},
            {"title": "Outliers Filtered", "value": "142 Records", "icon": "✂️", "delta": "IQR Threshold 3.0", "accent_color": "#06B6D4"},
            {"title": "Engineered Features", "value": "12 Derived", "icon": "🧩", "delta": "Lag + Cyclical", "accent_color": "#8B5CF6"},
            {"title": "Train / Test Split", "value": "80 / 20", "icon": "✂️", "delta": "Time Series Sequential", "accent_color": "#10B981"},
        ],
        columns=4,
    )

    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

    col_pipeline, col_preview = st.columns([6, 6], gap="medium")

    with col_pipeline:
        st.markdown(
            """
            <div class="card" style="padding: 1.4rem;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700; margin-bottom: 12px;">
                    ⚙️ Active Pipeline Transformations
                </div>
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    <div style="padding: 12px; border-radius: 12px; background: rgba(37, 99, 235, 0.08); border-left: 4px solid #2563EB;">
                        <div style="font-weight: 700; font-size: 0.9rem;">1. Temporal Feature Extraction</div>
                        <div style="font-size: 0.8rem; color: #64748B; margin-top: 2px;">Extracts <code>Hour</code>, <code>DayOfWeek</code>, <code>Month</code>, <code>Quarter</code>, <code>IsWeekend</code> from DateTime.</div>
                    </div>
                    <div style="padding: 12px; border-radius: 12px; background: rgba(6, 182, 212, 0.08); border-left: 4px solid #06B6D4;">
                        <div style="font-weight: 700; font-size: 0.9rem;">2. Cyclical Sine/Cosine Transform</div>
                        <div style="font-size: 0.8rem; color: #64748B; margin-top: 2px;">Converts 24-hour cycle to <code>sin_hour</code> and <code>cos_hour</code> for smooth periodic ML boundaries.</div>
                    </div>
                    <div style="padding: 12px; border-radius: 12px; background: rgba(139, 92, 246, 0.08); border-left: 4px solid #8B5CF6;">
                        <div style="font-weight: 700; font-size: 0.9rem;">3. Lag Features & Rolling Window</div>
                        <div style="font-size: 0.8rem; color: #64748B; margin-top: 2px;">Calculates <code>lag_1h</code>, <code>lag_24h</code>, and <code>rolling_mean_3h</code> for autogressive signals.</div>
                    </div>
                    <div style="padding: 12px; border-radius: 12px; background: rgba(16, 185, 129, 0.08); border-left: 4px solid #10B981;">
                        <div style="font-weight: 700; font-size: 0.9rem;">4. MinMax Feature Scaling</div>
                        <div style="font-size: 0.8rem; color: #64748B; margin-top: 2px;">Normalizes numerical feature ranges [0, 1] for neural network convergence.</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_preview:
        st.markdown(
            """
            <div class="card" style="padding: 1.4rem;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700; margin-bottom: 12px;">
                    👁️ Feature Matrix Preview
                </div>
                <table style="width: 100%; border-collapse: collapse; font-size: 0.82rem;">
                    <thead>
                        <tr style="border-bottom: 1px solid rgba(148,163,184,0.2); text-align: left; color: #64748B;">
                            <th style="padding: 6px;">DateTime</th>
                            <th style="padding: 6px;">Junction</th>
                            <th style="padding: 6px;">sin_hour</th>
                            <th style="padding: 6px;">lag_1h</th>
                            <th style="padding: 6px;">Vehicles</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid rgba(148,163,184,0.1);">
                            <td style="padding: 6px;">2015-11-01 00:00</td>
                            <td style="padding: 6px;">1</td>
                            <td style="padding: 6px;">0.000</td>
                            <td style="padding: 6px;">15</td>
                            <td style="padding: 6px; font-weight: 700;">15</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(148,163,184,0.1);">
                            <td style="padding: 6px;">2015-11-01 01:00</td>
                            <td style="padding: 6px;">1</td>
                            <td style="padding: 6px;">0.258</td>
                            <td style="padding: 6px;">15</td>
                            <td style="padding: 6px; font-weight: 700;">13</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(148,163,184,0.1);">
                            <td style="padding: 6px;">2015-11-01 02:00</td>
                            <td style="padding: 6px;">1</td>
                            <td style="padding: 5px;">0.500</td>
                            <td style="padding: 6px;">13</td>
                            <td style="padding: 6px; font-weight: 700;">10</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(148,163,184,0.1);">
                            <td style="padding: 6px;">2015-11-01 03:00</td>
                            <td style="padding: 6px;">1</td>
                            <td style="padding: 6px;">0.707</td>
                            <td style="padding: 6px;">10</td>
                            <td style="padding: 6px; font-weight: 700;">7</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            """,
            unsafe_allow_html=True,
        )

    app_footer()


