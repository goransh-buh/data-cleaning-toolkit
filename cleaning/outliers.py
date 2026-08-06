"""Outlier detection utilities."""

import pandas as pd
import numpy as np


def detect_outliers_iqr(df: pd.DataFrame, column: str, multiplier: float = 1.5) -> pd.Series:
    """Return a boolean mask of outlier rows using the IQR method."""
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - multiplier * iqr
    upper = q3 + multiplier * iqr
    return (df[column] < lower) | (df[column] > upper)


def remove_outliers(df: pd.DataFrame, columns: list, multiplier: float = 1.5) -> pd.DataFrame:
    """Remove rows that are outliers in any of the given columns."""
    mask = pd.Series(False, index=df.index)
    for col in columns:
        mask |= detect_outliers_iqr(df, col, multiplier)
    return df[~mask]
