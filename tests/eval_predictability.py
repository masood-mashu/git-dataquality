"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitDataQuality.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.null_rate_monitor import *
from tools.numerical_outlier_detector import *
from tools.batch_volume_drift_checker import *

class TestGitDataQualityPredictability(unittest.TestCase):

    def test_null_rate_monitor(self):
        res = monitor_null_rate('{"column_name": "user_id", "total_rows": 1000, "null_count": 0}')
        self.assertTrue(res["compliant"])
        self.assertEqual(res["status"], "PASSED")

    def test_numerical_outlier_detector(self):
        res = detect_outlier('{"batch_value": 500, "historical_mean": 100, "historical_std": 10}')
        self.assertTrue(res["outlier"])
        self.assertEqual(res["status"], "DISTRIBUTION_ANOMALY")

    def test_batch_volume_drift_checker(self):
        res = check_volume_drift(10500, baseline_records=10000)
        self.assertTrue(res["acceptable"])
        self.assertEqual(res["status"], "VOLUME_NORMAL")


if __name__ == "__main__":
    unittest.main()
