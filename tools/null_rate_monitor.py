"""
null_rate_monitor.py - Calculates column null percentage and verifies compliance against maximum allowed SLA
"""
import sys
import json


def monitor_null_rate(column_stats_json: str, max_allowed_pct: float = 1.0):
    import json
    data = json.loads(column_stats_json) if isinstance(column_stats_json, str) else column_stats_json
    total = max(data.get("total_rows", 1), 1)
    nulls = data.get("null_count", 0)
    pct = (nulls / total) * 100.0
    passed = pct <= max_allowed_pct
    return {
        "column": data.get("column_name", "unknown"),
        "total_rows": total,
        "null_count": nulls,
        "null_pct": round(pct, 2),
        "compliant": passed,
        "status": "PASSED" if passed else "NULL_THRESHOLD_EXCEEDED"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "null-rate-monitor"}))
