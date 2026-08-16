"""Data Upload page (UI foundation).

This page provides a professional upload UX.
"""

from __future__ import annotations

import streamlit as st



try:
    from components.cards import empty_state, info_card
    from components.footer import app_footer
    from components.styles import apply_global_ui, get_theme_mode, make_page_title
except ModuleNotFoundError:
    from app.components.cards import empty_state, info_card
    from app.components.footer import app_footer
    from app.components.styles import apply_global_ui, get_theme_mode, make_page_title


def render_upload() -> None:
    """Render the Data Upload page."""

    mode = get_theme_mode()
    apply_global_ui(mode)

    make_page_title("📂 Data Upload & Validation", "Ingest traffic datasets (CSV format) for pattern learning and forecasting.")

    col1, col2 = st.columns([7, 5], gap="medium")

    with col1:
        st.markdown(
            """
            <div class="card" style="padding: 1.5rem; margin-bottom: 20px;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.2rem; font-weight: 700; margin-bottom: 8px;">
                    📤 Upload Traffic CSV Dataset
                </div>
                <div style="font-size: 0.85rem; color: #64748B; margin-bottom: 16px;">
                    Select or drag a structured traffic CSV file containing junction timestamps and vehicle counts.
                </div>
            """,
            unsafe_allow_html=True,
        )

        uploaded = st.file_uploader(
            label="Upload Traffic Dataset",
            type=("csv",),
            accept_multiple_files=False,
            help="Supported headers: DateTime, Junction, Vehicles, ID",
        )

        st.markdown("</div>", unsafe_allow_html=True)

        if uploaded is None:
            empty_state(
                icon="📥",
                title="Awaiting Dataset File",
                description="Upload a CSV file above to run automated schema checks and preview records.",
            )
        else:
            info_card(
                title="File Uploaded Successfully",
                body=f"Received: <b>{uploaded.name}</b> ({uploaded.size / 1024:.1f} KB). Ready for preprocessing.",
                icon="✅",
            )

    with col2:
        st.markdown(
            """
            <div class="card" style="padding: 1.5rem;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700; margin-bottom: 12px;">
                    📋 Expected Dataset Schema
                </div>
                <div style="display: flex; flex-direction: column; gap: 10px; font-size: 0.88rem;">
                    <div style="padding: 10px; border-radius: 10px; background: rgba(59, 130, 246, 0.08); display: flex; justify-content: space-between; align-items: center;">
                        <span><code>DateTime</code> (YYYY-MM-DD HH:MM)</span>
                        <span style="color: #3B82F6; font-weight: 700; font-size: 0.75rem;">Required</span>
                    </div>
                    <div style="padding: 10px; border-radius: 10px; background: rgba(59, 130, 246, 0.08); display: flex; justify-content: space-between; align-items: center;">
                        <span><code>Junction</code> (Integer ID 1-4)</span>
                        <span style="color: #3B82F6; font-weight: 700; font-size: 0.75rem;">Required</span>
                    </div>
                    <div style="padding: 10px; border-radius: 10px; background: rgba(59, 130, 246, 0.08); display: flex; justify-content: space-between; align-items: center;">
                        <span><code>Vehicles</code> (Count Numeric)</span>
                        <span style="color: #3B82F6; font-weight: 700; font-size: 0.75rem;">Target</span>
                    </div>
                    <div style="padding: 10px; border-radius: 10px; background: rgba(59, 130, 246, 0.08); display: flex; justify-content: space-between; align-items: center;">
                        <span><code>ID</code> (Unique Row Key)</span>
                        <span style="color: #64748B; font-weight: 700; font-size: 0.75rem;">Optional</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    app_footer()


