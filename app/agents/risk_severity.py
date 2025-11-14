def run(data: dict) -> dict:
    """
    Evaluates the financial severity level based on pattern deviation and impact.
    Assigns a score 0–10 and labels it as Low / Medium / High risk.
    """
    pattern = data.get("pattern", {})
    impact = data.get("impact", {})

    deviation = float(pattern.get("deviation_percent", 0) or 0)
    est_amount = float(impact.get("estimated_amount", 0) or 0)
    prob = float(impact.get("probability", 0.5))

    # Simple scoring heuristic (customizable later)
    score = min(10.0, (deviation / 10.0) + (est_amount / 1_000_000) * prob * 2)
    if score < 3:
        level = "Low"
    elif score < 7:
        level = "Medium"
    else:
        level = "High"

    data["severity"] = {
        "score": round(score, 2),
        "level": level,
        "notes": f"Deviation={deviation:.1f}%, Impact≈₹{est_amount/1_00_000:.1f}L, Probability={prob}"
    }

    return data
