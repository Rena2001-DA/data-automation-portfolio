import pandas as pd


REQUIRED_COLUMNS = [
    "company_id",
    "revenue",
    "net_income",
]


def validate_financial_data(
    df: pd.DataFrame,
) -> dict:
    """Validate basic data quality in financial records."""

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        return {
            "missing_columns": missing_columns,
            "missing_values": {},
            "duplicate_rows": 0,
            "negative_revenue_rows": 0,
        }

    return {
        "missing_columns": [],
        "missing_values": (
            df[REQUIRED_COLUMNS]
            .isna()
            .sum()
            .to_dict()
        ),
        "duplicate_rows": int(
            df.duplicated().sum()
        ),
        "negative_revenue_rows": int(
            (df["revenue"] < 0).sum()
        ),
    }