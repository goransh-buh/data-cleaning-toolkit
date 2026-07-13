"""Column normalization utilities."""

import re
import pandas as pd


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to snake_case and strip whitespace."""
    df = df.copy()
    new_columns = []
    for col in df.columns:
        col = col.strip()
        col = re.sub(r"[^\w\s]", "", col)
        col = re.sub(r"\s+", "_", col)
        new_columns.append(col.lower())
    df.columns = new_columns
    return df
