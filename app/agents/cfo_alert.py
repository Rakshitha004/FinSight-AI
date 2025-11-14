def run(data: dict) -> dict:
    """
    Generates a CFO-friendly alert summary combining all previous agent outputs.
    Converts technical metrics into human-readable business language.
    """

    pattern = data.get("pattern", {})
    cause = data.get("cause", {})
    impact = data.get("impact", {})
    severity = data.get("severity", {})

    metric = pattern.get("metric", "Unknown Metric")
    deviation = pattern.get("deviation_percent", 0)
    cause_text = cause.get("explanation", "No cause identified")
    est_amount = impact.get("estimated_amount", 0)
    timeline = impact.get("timeline_days", 0)
    severity_level = severity.get("level", "N/A")
    score = severity.get("score", 0)

    alert_summary = (
        f"🚨 Early Risk Alert: {metric} deviation detected ({deviation:.1f}%). "
        f"Cause: {cause_text}. "
        f"Expected impact ≈ ₹{est_amount:,.0f} within {timeline} days. "
        f"Severity: {severity_level} (Score: {score})."
    )

    data["alert"] = {
        "metric": metric,
        "summary": alert_summary,
        "severity": severity_level,
        "score": score
    }

    return data
