"""Centralized dataset loader for Smart City Traffic Analytics.

Auto-loads data/raw/train.csv on first call and caches it in
st.session_state['df'] so all pages share the same dataframe without
re-reading from disk on every rerun.

Columns expected:
    DateTime  – hourly timestamps  (str -> parsed to datetime)
    Junction  – junction id         (int 1-4)
    Vehicles  – vehicle count       (int)
    ID        – composite row ID    (ignored for analytics)
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import pandas as pd
import streamlit as st

# Absolute path to the primary dataset
_REPO_ROOT = Path(__file__).resolve().parents[2]
_TRAIN_CSV = _REPO_ROOT / "data" / "raw" / "train.csv"
_TEST_CSV  = _REPO_ROOT / "data" / "raw" / "test.csv"

SESSION_KEY = "df"


def _parse_csv(path: Path) -> pd.DataFrame:
    """Read and clean the traffic CSV."""
    df = pd.read_csv(path, parse_dates=["DateTime"])
    df = df.sort_values("DateTime").reset_index(drop=True)

    # Derived time features
    df["Hour"]       = df["DateTime"].dt.hour
    df["DayOfWeek"]  = df["DateTime"].dt.dayofweek   # 0=Mon
    df["Month"]      = df["DateTime"].dt.month
    df["Date"]       = df["DateTime"].dt.date
    df["WeekDay"]    = df["DateTime"].dt.day_name()
    df["IsWeekend"]  = df["DayOfWeek"].isin([5, 6]).astype(int)

    # Junction labels
    junction_names = {1: "Junction 1 (North)", 2: "Junction 2 (East)",
                      3: "Junction 3 (Central)", 4: "Junction 4 (South)"}
    df["JunctionName"] = df["Junction"].map(junction_names).fillna(df["Junction"].astype(str))

    return df


def load_dataset(force: bool = False) -> Optional[pd.DataFrame]:
    """Return the cached dataframe from session_state.

    Loads from train.csv automatically if not already loaded.
    Returns None only if both CSVs are missing.
    """
    if SESSION_KEY in st.session_state and not force:
        return st.session_state[SESSION_KEY]

    if _TRAIN_CSV.exists():
        try:
            df = _parse_csv(_TRAIN_CSV)
            st.session_state[SESSION_KEY] = df
            return df
        except Exception:
            pass

    return None


def get_df() -> Optional[pd.DataFrame]:
    """Shorthand alias used by pages."""
    return load_dataset()


def dataset_is_loaded() -> bool:
    return SESSION_KEY in st.session_state and st.session_state[SESSION_KEY] is not None


def dataset_info() -> dict:
    """Return summary stats for navbar / sidebar display."""
    df = get_df()
    if df is None:
        return {"status": "Not connected", "rows": 0, "junctions": 0, "date_range": "—"}
    return {
        "status": "Connected",
        "rows": len(df),
        "junctions": df["Junction"].nunique(),
        "date_range": f"{df['DateTime'].min().strftime('%b %Y')} – {df['DateTime'].max().strftime('%b %Y')}",
    }
