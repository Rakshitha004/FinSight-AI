import random

def run(data: dict) -> dict:
    """
    Performs lightweight reasoning to explain WHY a pattern anomaly occurred.
    (In a real build, this will connect to an LLM.)
    """

    pattern = data.get("pattern", {})
    cause_text = "No clear cause detected."

    if pattern.get("status") == "anomaly_detected":
        # Simple placeholder reasoning rules
        reasons = [
            "Liquidity tightening in key customer sectors.",
            "Delayed collections due to festive-season credit extensions.",
            "Reduced early-payment incentives offered by sales teams.",
            "Vendor price increases affecting downstream cash flow.",
            "Higher discount push by sales reps impacting margin."
        ]
        cause_text = random.choice(reasons)
    elif pattern.get("status") == "normal":
        cause_text = "Financial behavior remains consistent with historical norms."

    data["cause"] = {
        "explanation": cause_text,
        "confidence": 0.85 if pattern.get("status") == "anomaly_detected" else 0.6
    }

    return data
