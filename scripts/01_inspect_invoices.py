"""Exercise 1: load and inspect fictional invoice data."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
invoices = pd.read_csv(ROOT / "data/raw/invoices.csv")
for column in ("invoice_date", "due_date"):
    invoices[column] = pd.to_datetime(invoices[column], format="%Y-%m-%d", errors="raise")

print(invoices.head())
print(invoices.dtypes)
print("Rows:", len(invoices))
print("Missing values:\n", invoices.isna().sum())
print("Duplicate invoice IDs:", invoices["invoice_id"].duplicated().sum())

# TODO: validate required columns, values and unique invoice IDs.
# TODO: convert amount columns to integer cents and print totals.
# Expected invoiced: 920000 cents; paid: 240000 cents.
