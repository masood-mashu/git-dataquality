"""
batch_volume_drift_checker.py - Audits current batch record count against 30-day moving average volume
"""
import sys
import json


def check_volume_drift(current_records: int, baseline_records: int = 10000, max_drift_pct: float = 25.0):
    drift = abs(current_records - baseline_records) / max(baseline_records, 1) * 100.0
    acceptable = drift <= max_drift_pct
    return {
        "current_records": current_records,
        "baseline_records": baseline_records,
        "drift_pct": round(drift, 2),
        "acceptable": acceptable,
        "status": "VOLUME_NORMAL" if acceptable else "VOLUME_SPIKE_OR_DROP"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "batch-volume-drift-checker"}))
