"""Streamlit entrypoint — Smart City Traffic Analytics Platform.

Responsibilities:
- set_page_config (must be first Streamlit call)
- Auto-load dataset from data/raw/train.csv into session_state
- Apply global glassmorphism UI theme
- Render top navbar + custom sidebar navigation
- Route to the correct page renderer
"""

from __future__ import annotations

from pathlib import Path
import sys

import streamlit as st

# ── Ensure repo root & app dir are importable ─────────────────────────────────
_REPO_ROOT = Path(__file__).resolve().parents[1]
_APP_DIR   = Path(__file__).resolve().parent
for _p in [str(_REPO_ROOT), str(_APP_DIR)]:
    if _p not in sys.path:
        sys.path.insert(0, _p)

# ── Internal imports (try both package and direct paths) ──────────────────────
try:
    from components.data_loader   import dataset_info, load_dataset
    from components.footer        import app_footer
    from components.navbar        import navbar
    from components.sidebar       import NAV_ITEMS, render_sidebar
    from components.styles        import apply_global_ui, get_theme_mode
    from pages.dashboard          import render_dashboard
    from pages.upload             import render_upload
    from pages.eda                import render_eda
    from pages.preprocessing      import render_preprocessing
    from pages.training           import render_training
    from pages.forecasting        import render_forecasting
    from pages.analytics          import render_analytics
    from pages.reports            import render_reports
    from pages.settings           import render_settings
    from pages.about              import render_about
except ImportError:
    from app.components.data_loader   import dataset_info, load_dataset
    from app.components.footer        import app_footer
    from app.components.navbar        import navbar
    from app.components.sidebar       import NAV_ITEMS, render_sidebar
    from app.components.styles        import apply_global_ui, get_theme_mode
    from app.pages.dashboard          import render_dashboard
    from app.pages.upload             import render_upload
    from app.pages.eda                import render_eda
    from app.pages.preprocessing      import render_preprocessing
    from app.pages.training           import render_training
    from app.pages.forecasting        import render_forecasting
    from app.pages.analytics          import render_analytics
    from app.pages.reports            import render_reports
    from app.pages.settings           import render_settings
    from app.pages.about              import render_about


PAGE_RENDERERS: dict = {
    "dashboard":     render_dashboard,
    "upload":        render_upload,
    "eda":           render_eda,
    "preprocessing": render_preprocessing,
    "training":      render_training,
    "forecasting":   render_forecasting,
    "analytics":     render_analytics,
    "reports":       render_reports,
    "settings":      render_settings,
    "about":         render_about,
}


def main() -> None:
    from config.settings import AppSettings

    st.set_page_config(
        page_title=AppSettings.APP_NAME,
        page_icon=AppSettings.APP_ICON,
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # ── Auto-load dataset on first run ────────────────────────────────────────
    load_dataset()

    # ── Theme & global CSS ───────────────────────────────────────────────────
    mode = get_theme_mode()
    apply_global_ui(mode)

    # ── Top Navbar ───────────────────────────────────────────────────────────
    info = dataset_info()
    ds_label = (
        f"📂 {info['rows']:,} rows · {info['junctions']} junctions · {info['date_range']}"
        if info["status"] == "Connected"
        else "⚠️ Dataset not connected"
    )
    navbar(dataset_status=ds_label)

    # ── Sidebar Navigation ───────────────────────────────────────────────────
    active_key = render_sidebar(active_key="dashboard")

    valid_keys = {item.key for item in NAV_ITEMS}
    if active_key not in valid_keys:
        active_key = "dashboard"

    # ── Page Render ──────────────────────────────────────────────────────────
    render_fn = PAGE_RENDERERS.get(active_key, render_dashboard)
    st.markdown("<div style='margin-top:6px;'></div>", unsafe_allow_html=True)
    render_fn()

    app_footer()


if __name__ == "__main__":
    main()
