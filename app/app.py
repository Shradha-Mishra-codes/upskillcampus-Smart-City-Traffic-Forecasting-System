"""Streamlit entrypoint with centralized, scalable navigation.

Phase 2 implements:
- Responsive sidebar (icon-based)
- Top navbar (title, theme toggle, status badge)
- Global theme + Plotly theme integration (safe if Plotly missing)
- Shared, modular page rendering (UI-only foundation for each phase)

No ML logic is implemented in Phase 2.
"""

from __future__ import annotations

from pathlib import Path
import sys

# Ensure the repository root is on sys.path so `import app.*` resolves to the
# local `app/` package.
_REPO_ROOT = Path(__file__).resolve().parents[1]
_APP_DIR = Path(__file__).resolve().parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))
if str(_APP_DIR) not in sys.path:
    sys.path.insert(0, str(_APP_DIR))

import streamlit as st

try:
    from app.components.footer import app_footer
    from app.components.navbar import navbar
    from app.components.sidebar import NAV_ITEMS, render_sidebar
    from app.components.styles import apply_global_ui, get_theme_mode
    from app.pages.about import render_about
    from app.pages.analytics import render_analytics
    from app.pages.dashboard import render_dashboard
    from app.pages.eda import render_eda
    from app.pages.forecasting import render_forecasting
    from app.pages.preprocessing import render_preprocessing
    from app.pages.reports import render_reports
    from app.pages.settings import render_settings
    from app.pages.training import render_training
    from app.pages.upload import render_upload
except ImportError:
    from components.footer import app_footer
    from components.navbar import navbar
    from components.sidebar import NAV_ITEMS, render_sidebar
    from components.styles import apply_global_ui, get_theme_mode
    from pages.about import render_about
    from pages.analytics import render_analytics
    from pages.dashboard import render_dashboard
    from pages.eda import render_eda
    from pages.forecasting import render_forecasting
    from pages.preprocessing import render_preprocessing
    from pages.reports import render_reports
    from pages.settings import render_settings
    from pages.training import render_training
    from pages.upload import render_upload

PAGE_RENDERERS: dict[str, callable[[], None]] = {
    "dashboard": render_dashboard,
    "upload": render_upload,
    "eda": render_eda,
    "preprocessing": render_preprocessing,
    "training": render_training,
    "forecasting": render_forecasting,
    "analytics": render_analytics,
    "reports": render_reports,
    "settings": render_settings,
    "about": render_about,
}


def _dataset_status() -> str:
    return "Dataset: Not connected (UI foundation)"


def _get_valid_keys() -> set[str]:
    return {item.key for item in NAV_ITEMS}


def main() -> None:
    """Application entrypoint."""

    from config.settings import AppSettings

    st.set_page_config(
        page_title=AppSettings.APP_NAME,
        page_icon=AppSettings.APP_ICON,
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    mode = get_theme_mode()
    apply_global_ui(mode)

    navbar(dataset_status=_dataset_status())

    active_key = render_sidebar(active_key="dashboard")

    valid_keys = _get_valid_keys()
    if active_key not in valid_keys:
        active_key = "dashboard"

    render_fn = PAGE_RENDERERS.get(active_key)
    if render_fn is None:
        render_dashboard()
    else:
        st.markdown("<div style='margin-top: 6px;'></div>", unsafe_allow_html=True)
        render_fn()

    app_footer()


if __name__ == "__main__":
    main()

