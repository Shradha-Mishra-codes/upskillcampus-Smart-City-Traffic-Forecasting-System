"""Training page (UI foundation).

This page provides the UI shell for model training and evaluation.
No ML logic is executed in this UI-only foundation.
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


def render_training() -> None:
    """Render the Model Training & Evaluation workspace."""

    mode = get_theme_mode()
    apply_global_ui(mode)

    make_page_title("🤖 AI Model Training & Benchmarking", "Train, tune, and evaluate machine learning models for traffic prediction.")

    kpi_cards_grid(
        kpis=[
            {"title": "Best Model", "value": "XGBoost Regressor", "icon": "🏆", "delta": "Top Accuracy", "accent_color": "#2563EB"},
            {"title": "Validation MAE", "value": "4.12 Vehicles", "icon": "🎯", "delta": "Optimal Error", "accent_color": "#10B981"},
            {"title": "R² Variance Score", "value": "0.946", "icon": "📈", "delta": "94.6% Fit", "accent_color": "#06B6D4"},
            {"title": "Training Duration", "value": "1.42 Seconds", "icon": "⚡", "delta": "Fast Execution", "accent_color": "#8B5CF6"},
        ],
        columns=4,
    )

    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

    col_models, col_metrics = st.columns([6, 6], gap="medium")

    with col_models:
        st.markdown(
            """
            <div class="card" style="padding: 1.4rem;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700; margin-bottom: 12px;">
                    🎛️ Algorithm Selection & Hyperparameters
                </div>
            """,
            unsafe_allow_html=True,
        )

        model_type = st.selectbox(
            "Select Machine Learning Architecture",
            ["XGBoost Regressor (Recommended)", "Random Forest Regressor", "Linear Ridge Regression", "LSTM Recurrent Network"],
        )

        n_estimators = st.slider("Number of Estimators / Trees", 50, 500, 150, 50)
        max_depth = st.slider("Max Tree Depth", 3, 15, 6, 1)

        if st.button("🚀 Execute Model Training Pipeline", use_container_width=True):
            st.success(f"Model {model_type} successfully trained with n_estimators={n_estimators}, max_depth={max_depth}!")

        st.markdown("</div>", unsafe_allow_html=True)

    with col_metrics:
        st.markdown(
            """
            <div class="card" style="padding: 1.4rem;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700; margin-bottom: 12px;">
                    📊 Model Benchmark Comparison
                </div>
                <table style="width: 100%; border-collapse: collapse; font-size: 0.85rem;">
                    <thead>
                        <tr style="border-bottom: 1px solid rgba(148,163,184,0.2); text-align: left; color: #64748B;">
                            <th style="padding: 6px;">Model</th>
                            <th style="padding: 6px;">MAE</th>
                            <th style="padding: 6px;">RMSE</th>
                            <th style="padding: 6px;">R²</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid rgba(148,163,184,0.1); background: rgba(37, 99, 235, 0.06);">
                            <td style="padding: 8px 6px; font-weight: 700; color: #2563EB;">🥇 XGBoost</td>
                            <td style="padding: 8px 6px;">4.12</td>
                            <td style="padding: 8px 6px;">6.35</td>
                            <td style="padding: 8px 6px; font-weight: 700;">0.946</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(148,163,184,0.1);">
                            <td style="padding: 8px 6px; font-weight: 700;">🥈 Random Forest</td>
                            <td style="padding: 8px 6px;">4.85</td>
                            <td style="padding: 8px 6px;">7.12</td>
                            <td style="padding: 8px 6px;">0.924</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(148,163,184,0.1);">
                            <td style="padding: 8px 6px; font-weight: 700;">🥉 LSTM Neural Net</td>
                            <td style="padding: 8px 6px;">5.10</td>
                            <td style="padding: 8px 6px;">7.45</td>
                            <td style="padding: 8px 6px;">0.912</td>
                        </tr>
                        <tr>
                            <td style="padding: 8px 6px; font-weight: 700;">Linear Ridge</td>
                            <td style="padding: 8px 6px;">7.92</td>
                            <td style="padding: 8px 6px;">11.30</td>
                            <td style="padding: 8px 6px;">0.785</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Loss Curve
    st.markdown("<div style='margin-top: 16px;'></div>", unsafe_allow_html=True)
    epochs = [f"Iter #{i}" for i in range(1, 11)]
    loss_val = [18.2, 14.5, 11.2, 8.7, 6.9, 5.4, 4.8, 4.3, 4.15, 4.12]
    fig_loss = line_chart_figure(
        x=epochs,
        y=loss_val,
        title="Training Loss Convergence Curve (MAE Loss)",
        x_label="Training Iterations",
        y_label="Validation Loss",
        color="#8B5CF6",
    )
    plotly_figure(fig_loss)

    app_footer()


