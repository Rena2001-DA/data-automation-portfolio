from pathlib import Path

import pandas as pd

from src.data_validation import validate_financial_data


def main():
    project_root = Path(__file__).resolve().parent.parent
    data_path = project_root / "data" / "sample_financial_data.csv"

    df = pd.read_csv(data_path)
    results = validate_financial_data(df)

    print("=== Financial Data Quality Report ===")
    print(f"Rows checked: {len(df)}")
    print(f"Missing columns: {results['missing_columns']}")
    print(f"Missing values: {results['missing_values']}")
    print(f"Duplicate rows: {results['duplicate_rows']}")
    print(
        "Negative revenue rows: "
        f"{results['negative_revenue_rows']}"
    )


if __name__ == "__main__":
    main()