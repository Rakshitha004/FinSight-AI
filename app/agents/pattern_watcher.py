import pandas as pd
import numpy as np

def run(data: dict) -> dict:
    """
    Detects behavioral shifts (anomalies) in payment timing / DSO.
    Input:  {"records": [ {invoice_id, issue_date, paid_date, amount, ... }, ... ]}
    Output: adds a 'pattern' object describing deviation.
    """

    # Convert incoming records to a DataFrame
    df = pd.DataFrame(data.get("records", []))
    if df.empty:
        data["pattern"] = {"status": "no_data", "notes": "No records received"}
        return data

    # Parse dates safely
    for col in ("issue_date", "paid_date"):
        if col in df:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Calculate Days Sales Outstanding (DSO)
    df["dso"] = (df["paid_date"] - df["issue_date"]).dt.days

    # Compute average DSO and compare to baseline
    current_avg = df["dso"].mean()
    baseline = data.get("baseline_dso", current_avg)
    deviation = ((current_avg - baseline) / baseline) * 100 if baseline else 0

    # Detect pattern shift
    status = "anomaly_detected" if deviation > 15 else "normal"

    data["pattern"] = {
        "metric": "DSO",
        "current_value": round(current_avg, 2),
        "baseline_value": round(baseline, 2),
        "deviation_percent": round(deviation, 2),
        "status": status,
        "confidence": 0.9 if status == "anomaly_detected" else 0.7,
        "notes": f"Avg DSO {current_avg:.1f} days (baseline {baseline:.1f}) → deviation {deviation:.1f}%"
    }

    return data
