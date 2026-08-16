"""Responsive left sidebar with icon-based navigation.

Central navigation is managed by app/app.py.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

import streamlit as st


@dataclass(frozen=True)
class NavItem:
    key: str
    label: str
    icon: str
    category: str = "OVERVIEW"


NAV_ITEMS: List[NavItem] = [
    # Overview
    NavItem(key="dashboard", label="Dashboard", icon="📊", category="OVERVIEW"),
    # Data Pipeline
    NavItem(key="upload", label="Data Upload", icon="📂", category="DATA PIPELINE"),
    NavItem(key="eda", label="Exploratory Analysis", icon="📈", category="DATA PIPELINE"),
    NavItem(key="preprocessing", label="Preprocessing", icon="🧹", category="DATA PIPELINE"),
    # AI Models & Forecasting
    NavItem(key="training", label="Model Training", icon="🤖", category="AI & FORECASTING"),
    NavItem(key="forecasting", label="Traffic Forecasting", icon="🔮", category="AI & FORECASTING"),
    NavItem(key="analytics", label="Advanced Analytics", icon="📉", category="AI & FORECASTING"),
    # System & Reports
    NavItem(key="reports", label="Reports & Export", icon="📑", category="SYSTEM"),
    NavItem(key="settings", label="Settings", icon="⚙️", category="SYSTEM"),
    NavItem(key="about", label="About System", icon="ℹ️", category="SYSTEM"),
]


def render_sidebar(active_key: str) -> str:
    """Render a premium glassmorphic sidebar and return navigation selection."""

    if "nav_selection" not in st.session_state:
        st.session_state.nav_selection = active_key

    # Brand Header Logo
    st.sidebar.markdown(
        """
        <div style="padding: 10px 4px 18px 4px; display: flex; align-items: center; gap: 12px;">
            <div style="font-size: 28px; background: linear-gradient(135deg, #2563EB, #06B6D4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900;">
                🚦
            </div>
            <div>
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 800; letter-spacing: -0.02em; line-height: 1.2;">
                    SmartCity AI
                </div>
                <div style="font-size: 0.72rem; color: #64748B; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase;">
                    Traffic Platform
                </div>
            </div>
        </div>
        <style>
            .nav-cat-header {
                font-size: 0.68rem;
                font-weight: 800;
                color: #64748B;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                margin: 16px 0 6px 8px;
            }
            .stSidebar button {
                text-align: left !important;
                justify-content: flex-start !important;
                padding-left: 14px !important;
                height: 42px !important;
                border-radius: 12px !important;
            }
            .active-nav button {
                background: linear-gradient(135deg, rgba(37, 99, 235, 0.2), rgba(6, 182, 212, 0.15)) !important;
                border-color: rgba(37, 99, 235, 0.5) !important;
                color: #3B82F6 !important;
                box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15) !important;
                font-weight: 700 !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    categories = ["OVERVIEW", "DATA PIPELINE", "AI & FORECASTING", "SYSTEM"]

    for cat in categories:
        st.sidebar.markdown(f"<div class='nav-cat-header'>{cat}</div>", unsafe_allow_html=True)
        cat_items = [item for item in NAV_ITEMS if item.category == cat]

        for item in cat_items:
            is_active = st.session_state.nav_selection == item.key
            label = f"{item.icon} {item.label}"
            
            # Wrap button in active container if selected
            if is_active:
                st.sidebar.markdown("<div class='active-nav'>", unsafe_allow_html=True)
            
            if st.sidebar.button(
                label,
                key=f"nav_{item.key}",
                use_container_width=True,
            ):
                st.session_state.nav_selection = item.key
                st.rerun()

            if is_active:
                st.sidebar.markdown("</div>", unsafe_allow_html=True)

    st.sidebar.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
    st.sidebar.markdown(
        """
        <div style="padding: 12px; border-radius: 14px; background: rgba(34, 197, 94, 0.08); border: 1px solid rgba(34, 197, 94, 0.2); text-align: center;">
            <div style="font-size: 0.75rem; font-weight: 700; color: #10B981;">🟢 System Operational</div>
            <div style="font-size: 0.7rem; color: #64748B; margin-top: 2px;">Smart City SaaS v1.0</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    return str(st.session_state.nav_selection)


