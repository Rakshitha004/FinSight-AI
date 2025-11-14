def run(data: dict) -> dict:
    """
    Estimate ₹ impact and timeline from the detected pattern.
    Simple heuristic now; you can swap with a model later.
    """
    pattern = data.get("pattern", {})
    deviation = float(pattern.get("deviation_percent", 0) or 0)

    if deviation <= 0:
        data["impact"] = {
            "type": "none",
            "estimated_amount": 0.0,
            "timeline_days": 0,
            "probability": 0.5
        }
        return data

    # Heuristic: scale impact with deviation (tune later)
    base_rupees = 18_00_000  # ₹18L baseline from our examples
    amount = round(base_rupees * (deviation / 50.0), 2)
    data["impact"] = {
        "type": "cash_delay",
        "estimated_amount": amount,
        "timeline_days": 45,
        "probability": 0.8
    }
    return data
