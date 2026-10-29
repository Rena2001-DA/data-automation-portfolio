import pandas as pd

from src.data_validation import validate_financial_data


def test_detects_missing_values_and_invalid_revenue():
    df = pd.DataFrame(
        {
            "company_id": ["A001", "A002", "A003"],
            "revenue": [1000, None, -100],
            "net_income": [100, 200, None],
        }
    )

    result = validate_financial_data(df)

    assert result["missing_columns"] == []
    assert result["missing_values"]["revenue"] == 1
    assert result["missing_values"]["net_income"] == 1
    assert result["negative_revenue_rows"] == 1


def test_detects_duplicate_rows():
    df = pd.DataFrame(
        {
            "company_id": ["A001", "A001"],
            "revenue": [1000, 1000],
            "net_income": [100, 100],
        }
    )

    result = validate_financial_data(df)

    assert result["duplicate_rows"] == 1


def test_detects_missing_required_columns():
    df = pd.DataFrame(
        {
            "company_id": ["A001"],
            "revenue": [1000],
        }
    )

    result = validate_financial_data(df)

    assert result["missing_columns"] == ["net_income"]