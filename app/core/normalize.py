import pandas as pd
import numpy as np

def normalize_records(data: dict) -> dict:
    """Clean and standardize incoming financial records."""
    records = data.get("records", [])
    if not records:
        return {"records": [], "notes": "No records provided"}

    df = pd.DataFrame(records)
    df.columns = [c.strip().lower() for c in df.columns]

    # Parse date columns safely
    for col in ("issue_date", "paid_date", "due_date"):
        if col in df:
            df[col] = pd.to_datetime(df[col], errors="coerce", dayfirst=True)

    # Clean numeric columns
    for col in ("amount", "discount"):
        if col in df:
            df[col] = (
                df[col].astype(str)
                .str.replace(",", "", regex=False)
                .astype(float)
                .fillna(0.0)
            )

    # Derive Days-Sales-Outstanding (DSO)
    if "issue_date" in df and "paid_date" in df:
        df["dso"] = (df["paid_date"] - df["issue_date"]).dt.days

    if "invoice_id" in df.columns:
        df = df.drop_duplicates(subset=["invoice_id"])
    if "issue_date" in df.columns:
        df = df.sort_values(by="issue_date")

    return {"records": df.to_dict(orient="records")}
