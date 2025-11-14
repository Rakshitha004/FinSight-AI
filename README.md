🚀 FinSight-AI
AI-powered financial pattern detection system that analyzes DSO (Days Sales Outstanding), identifies anomalies, forecasts impact, and generates CFO-level alerts.
🏗️ Project Status: In Progress

FinSight-AI is under active development. Currently working on:

Improving agent-level reasoning

Enhancing accuracy of anomaly detection

Adding dashboards & UI for CFO alerts

Building n8n automation workflows

Deployment setup (Render / Railway / Docker)
🤖 Current Working Agents

These agents are fully implemented and running in the backend:

Pattern Watcher Agent → Detects DSO deviation

Causal Reasoning Agent → Explains the possible root cause

Impact Forecast Agent → Estimates financial impact (amount + timeline)

Risk Severity Agent → Calculates risk score + severity level

CFO Alert Agent → Generates final summary alert for CFOs

All agents are connected in a chain and produce combined output via /api/ingest.

