from __future__ import annotations

import pandas as pd


def validate_required_columns(df: pd.DataFrame, required: list[str]) -> None:
    """Validate that a DataFrame contains all required columns.

    Args:
        df: Input DataFrame.
        required: Required column names.

    Raises:
        ValueError: If any required columns are missing.
    """

    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

