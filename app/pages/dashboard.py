"""Executive Dashboard — powered by real train.csv dataset.

Displays live KPIs, hourly traffic trends, junction distribution,
and congestion heatmap computed from the loaded DataFrame.
"""

from __future__ import annotations

import streamlit as st

try:
    from components.cards        import empty_state, kpi_card
    from components.charts       import heatmap_figure, line_chart_figure, bar_chart_figure, plotly_figure, section_header
    from components.dashboard_ui import donut_placeholder_card, set_background_image
    from components.data_loader  import get_df, dataset_is_loaded
    from components.styles       import apply_global_ui, get_theme_mode
except ModuleNotFoundError:
    from app.components.cards        import empty_state, kpi_card
    from app.components.charts       import heatmap_figure, line_chart_figure, bar_chart_figure, plotly_figure, section_header
    from app.components.dashboard_ui import donut_placeholder_card, set_background_image
    from app.components.data_loader  import get_df, dataset_is_loaded
    from app.components.styles       import apply_global_ui, get_theme_mode


def render_dashboard() -> None:
    """Render the Executive Traffic Dashboard with real data."""

    mode = get_theme_mode()
    apply_global_ui(mode)
    set_background_image(mode)

    df = get_df()

    # ── Hero Banner ───────────────────────────────────────────────────────────
    date_range = (
        f"{df['DateTime'].min().strftime('%d %b %Y')} → {df['DateTime'].max().strftime('%d %b %Y')}"
        if df is not None else "No data loaded"
    )
    st.markdown(
        f"""
        <div class="card" style="padding:1.8rem; margin-bottom:24px;
             background:linear-gradient(135deg,rgba(37,99,235,0.12),rgba(139,92,246,0.12));
             border-color:rgba(37,99,235,0.3);">
            <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:16px;">
                <div>
                    <div style="font-size:0.82rem; font-weight:800; color:#3B82F6;
                                letter-spacing:0.06em; text-transform:uppercase;">
                        Executive Dashboard
                    </div>
                    <div style="font-family:'Outfit',sans-serif; font-size:1.8rem;
                                font-weight:800; margin-top:4px;">
                        Smart City Traffic Analytics 🚦
                    </div>
                    <div style="font-size:0.9rem; color:#64748B; margin-top:4px;">
                        Dataset: <strong>{date_range}</strong> &nbsp;|&nbsp;
                        Real-time congestion intelligence &amp; pattern insights.
                    </div>
                </div>
                <div style="padding:8px 16px; border-radius:999px;
                            background:rgba(59,130,246,0.15);
                            border:1px solid rgba(59,130,246,0.3);
                            font-weight:700; font-size:0.85rem; color:#3B82F6;">
                    🗓️ Historical Analysis Mode
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── KPI Cards ─────────────────────────────────────────────────────────────
    if df is not None:
        total_vehicles  = int(df["Vehicles"].sum())
        avg_vehicles    = round(df["Vehicles"].mean(), 1)
        peak_hour_idx   = df.groupby("Hour")["Vehicles"].mean().idxmax()
        num_junctions   = df["Junction"].nunique()
        busiest_jn      = df.groupby("Junction")["Vehicles"].sum().idxmax()

        kpis = [
            {"title": "Total Vehicles",   "value": f"{total_vehicles:,}",       "icon": "🚗",  "delta": "All junctions combined",           "accent_color": "#2563EB"},
            {"title": "Avg Vehicles/Hr",  "value": f"{avg_vehicles}",            "icon": "⏱️",  "delta": "Per hour across all junctions",    "accent_color": "#06B6D4"},
            {"title": "Peak Hour",        "value": f"{peak_hour_idx:02d}:00",    "icon": "🕒",  "delta": "Highest avg traffic hour",          "accent_color": "#F59E0B"},
            {"title": "Active Junctions", "value": f"{num_junctions}",           "icon": "🏙️",  "delta": "Monitored intersections",           "accent_color": "#8B5CF6"},
            {"title": "Busiest Junction", "value": f"Junction {busiest_jn}",     "icon": "🚦",  "delta": "Highest cumulative volume",         "accent_color": "#10B981"},
        ]
    else:
        kpis = [
            {"title": "Total Vehicles",   "value": "—", "icon": "🚗",  "delta": "No data",  "accent_color": "#2563EB"},
            {"title": "Avg Vehicles/Hr",  "value": "—", "icon": "⏱️",  "delta": "No data",  "accent_color": "#06B6D4"},
            {"title": "Peak Hour",        "value": "—", "icon": "🕒",  "delta": "No data",  "accent_color": "#F59E0B"},
            {"title": "Active Junctions", "value": "—", "icon": "🏙️",  "delta": "No data",  "accent_color": "#8B5CF6"},
            {"title": "Busiest Junction", "value": "—", "icon": "🚦",  "delta": "No data",  "accent_color": "#10B981"},
        ]

    cols = st.columns(5, gap="small")
    for idx, kpi in enumerate(kpis):
        with cols[idx]:
            kpi_card(
                title=kpi["title"],
                value=kpi["value"],
                icon=kpi["icon"],
                delta=kpi["delta"],
                accent_color=kpi["accent_color"],
            )

    st.markdown("<div style='margin-bottom:18px;'></div>", unsafe_allow_html=True)

    # ── Main Visual Row: Hourly Trend + Donut Distribution ────────────────────
    col_chart, col_donut = st.columns([7, 5], gap="medium")

    with col_chart:
        if df is not None:
            hourly = df.groupby("Hour")["Vehicles"].mean().reset_index()
            fig_trend = line_chart_figure(
                x=[f"{int(h):02d}:00" for h in hourly["Hour"]],
                y=hourly["Vehicles"].tolist(),
                title="Average Hourly Traffic Volume (All Junctions)",
                x_label="Hour of Day",
                y_label="Avg Vehicles",
                color="#2563EB",
            )
            plotly_figure(fig_trend)
        else:
            empty_state("No dataset loaded", "Upload or connect train.csv to see traffic trends.")

    with col_donut:
        if df is not None:
            import plotly.graph_objects as go
            jn_vols = df.groupby("JunctionName")["Vehicles"].sum()
            fig_donut = go.Figure(go.Pie(
                labels=jn_vols.index.tolist(),
                values=jn_vols.values.tolist(),
                hole=0.55,
                marker=dict(colors=["#2563EB", "#06B6D4", "#8B5CF6", "#10B981"]),
                textinfo="label+percent",
                hovertemplate="<b>%{label}</b><br>%{value:,} vehicles<extra></extra>",
            ))
            fig_donut.update_layout(
                title="Junction Volume Distribution",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                margin=dict(l=10, r=10, t=50, b=10),
                showlegend=False,
            )
            plotly_figure(fig_donut)
        else:
            donut_placeholder_card()

    st.markdown("<div style='margin-bottom:18px;'></div>", unsafe_allow_html=True)

    # ── Secondary Row: Junction Table + Heatmap + Day-of-Week Bar ─────────────
    c_tbl, c_heat, c_bar = st.columns(3, gap="medium")

    with c_tbl:
        if df is not None:
            jn_summary = (
                df.groupby(["Junction", "JunctionName"])["Vehicles"]
                .agg(["sum", "mean"])
                .reset_index()
                .sort_values("sum", ascending=False)
            )
            rows_html = ""
            for _, row in jn_summary.iterrows():
                avg = row["mean"]
                if avg >= 40:
                    status = "<span style='color:#EF4444;font-weight:700;'>🔴 Heavy</span>"
                elif avg >= 20:
                    status = "<span style='color:#F59E0B;font-weight:700;'>🟡 Moderate</span>"
                else:
                    status = "<span style='color:#10B981;font-weight:700;'>🟢 Smooth</span>"
                rows_html += f"""
                    <tr style='border-bottom:1px solid rgba(148,163,184,0.1);'>
                        <td style='padding:8px 6px;font-weight:700;'>{row['JunctionName']}</td>
                        <td style='padding:8px 6px;'>{int(row['sum']):,}</td>
                        <td style='padding:8px 6px;'>{status}</td>
                    </tr>"""
        else:
            rows_html = "<tr><td colspan='3' style='text-align:center;padding:20px;color:#64748B;'>No data</td></tr>"

        st.markdown(
            f"""
            <div class="card" style="padding:1.2rem; height:100%;">
                <div style="font-family:'Outfit',sans-serif;font-size:1.1rem;font-weight:700;
                            margin-bottom:12px;display:flex;align-items:center;justify-content:space-between;">
                    <span>📍 Junction Traffic Summary</span>
                    <span style="font-size:0.75rem;color:#10B981;font-weight:700;">Live Data</span>
                </div>
                <table style="width:100%;border-collapse:collapse;font-size:0.85rem;">
                    <thead>
                        <tr style="border-bottom:1px solid rgba(148,163,184,0.2);text-align:left;color:#64748B;">
                            <th style="padding:6px;">Junction</th>
                            <th style="padding:6px;">Total Vehicles</th>
                            <th style="padding:6px;">Status</th>
                        </tr>
                    </thead>
                    <tbody>{rows_html}</tbody>
                </table>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c_heat:
        if df is not None:
            pivot = df.pivot_table(
                values="Vehicles", index="DayOfWeek", columns="Junction", aggfunc="mean"
            ).fillna(0)
            day_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            y_labels = [day_labels[i] for i in pivot.index if i < len(day_labels)]
            x_labels = [f"Jn {c}" for c in pivot.columns]
            fig_heat = heatmap_figure(
                z=pivot.values.tolist(),
                title="Avg Traffic by Day & Junction",
                x_labels=x_labels,
                y_labels=y_labels,
            )
            plotly_figure(fig_heat)
        else:
            empty_state("Heatmap unavailable", "Load dataset to see congestion density.")

    with c_bar:
        if df is not None:
            dow = df.groupby("WeekDay")["Vehicles"].mean()
            order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            dow = dow.reindex([d for d in order if d in dow.index])
            fig_bar = bar_chart_figure(
                x=dow.index.tolist(),
                y=dow.values.tolist(),
                title="Avg Traffic by Day of Week",
                x_label="Day",
                y_label="Avg Vehicles",
                color="#8B5CF6",
            )
            plotly_figure(fig_bar)
        else:
            empty_state("Day chart unavailable", "Load dataset first.")
