
import pandas as pd

def validate_data(file_path):

    df = pd.read_csv(file_path)

    required_columns = [
        "customerID",
        "tenure",
        "MonthlyCharges",
        "TotalCharges",
        "Churn"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    if df.empty:
        raise ValueError("Dataset is empty")

    if df["customerID"].duplicated().any():
        raise ValueError("Duplicate customer IDs found")

    if not df["Churn"].isin(["Yes", "No"]).all():
        raise ValueError("Unexpected target values")

    print("Data validation successful!")

    print("Records:", len(df))
    print("Columns:", len(df.columns))

    return True
