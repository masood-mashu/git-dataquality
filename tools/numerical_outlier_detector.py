"""
numerical_outlier_detector.py - Calculates Z-score deviation for numeric batch averages against historical baseline
"""
import sys
import json


def detect_outlier(zscore_data_json: str, z_threshold: float = 3.0):
    import json
    data = json.loads(zscore_data_json) if isinstance(zscore_data_json, str) else zscore_data_json
    val = data.get("batch_value", 0.0)
    mean = data.get("historical_mean", 0.0)
    std = max(data.get("historical_std", 1.0), 0.001)
    z = abs(val - mean) / std
    is_outlier = z > z_threshold
    return {
        "batch_value": val,
        "mean": mean,
        "z_score": round(z, 2),
        "outlier": is_outlier,
        "status": "DISTRIBUTION_ANOMALY" if is_outlier else "NORMAL_DISTRIBUTION"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "numerical-outlier-detector"}))
