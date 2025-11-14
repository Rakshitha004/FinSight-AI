from fastapi import FastAPI, Request
from app.agents import pattern_watcher, causal_reasoning, impact_forecast, risk_severity, cfo_alert
from app.core.normalize import normalize_records
from app.utils.logger import log_step


app = FastAPI(title="CFO Cognitive Risk Radar")

@app.get("/")
def root():
    return {"status": "ok", "message": "CFO Radar backend running successfully"}

@app.post("/api/ingest")
async def ingest_data(request: Request):
    raw = await request.json()
    normalized = normalize_records(raw)
    log_step("Normalizer", normalized)

    pattern_output = pattern_watcher.run(normalized)
    log_step("PatternWatcher", pattern_output)

    cause_output = causal_reasoning.run(pattern_output)
    log_step("CausalReasoning", cause_output)

    impact_output = impact_forecast.run(cause_output)
    log_step("ImpactForecast", impact_output)

    severity_output = risk_severity.run(impact_output)
    log_step("RiskSeverity", severity_output)

    alert_output = cfo_alert.run(severity_output)
    log_step("CFOAlert", alert_output)

    return {"alert": alert_output}



    # Sequentially trigger each agent
    pattern_output = pattern_watcher.run(data)
    cause_output = causal_reasoning.run(pattern_output)
    impact_output = impact_forecast.run(cause_output)
    severity_output = risk_severity.run(impact_output)
    alert_output = cfo_alert.run(severity_output)

    return {"alert": alert_output}
