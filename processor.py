import pandas as pd
import csv
import os
from config import COMPANY_ACCOUNT_ID, get_output_filename


def process(excel_path: str) -> str:
    df = pd.read_excel(excel_path, dtype={"ID": str})

    required_columns = {"IBAN", "Salary", "ID", "Employee Name"}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise ValueError(f"Missing columns in Excel file: {missing}")

    df = df[df["Salary"] != 0]

    if df.empty:
        raise ValueError("No employees with a non-zero salary found.")

    output_dir = os.path.dirname(excel_path)
    output_path = os.path.join(output_dir, get_output_filename())

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["HDR", "", "", "", "", ""])
        for _, row in df.iterrows():
            writer.writerow([
                "DTL",
                COMPANY_ACCOUNT_ID,
                row["IBAN"],
                row["Salary"],
                row["ID"],
                row["Employee Name"]
            ])
        writer.writerow(["TRL", "", "", "", "", ""])

    return output_path