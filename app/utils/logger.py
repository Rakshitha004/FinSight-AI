import json, os
from datetime import datetime, date
from decimal import Decimal
import numpy as np

LOG_FILE = os.path.join(os.getcwd(), "trace_log.json")

def _jsonify(obj):
    # Pandas Timestamp / datetime / date
    if hasattr(obj, "isoformat"):
        try:
            return obj.isoformat()
        except Exception:
            pass
    # NumPy types
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, (np.ndarray,)):
        return obj.tolist()
    # Decimal
    if isinstance(obj, Decimal):
        return float(obj)
    # Sets
    if isinstance(obj, set):
        return list(obj)
    # Fallback: string
    return str(obj)

def log_step(agent_name: str, data: dict):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "agent": agent_name,
        "data": data
    }

    try:
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

        with open(LOG_FILE, "r+", encoding="utf-8") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
            logs.append(entry)
            f.seek(0)
            json.dump(logs, f, indent=4, default=_jsonify)

        print(f"✅ Log written to: {LOG_FILE}")
    except Exception as e:
        print(f"⚠️ Log write failed: {e}")
