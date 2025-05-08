import unittest
import os
import json
import time
from reconciler import reconcile, save_report

class TestReconciler(unittest.TestCase):
    
    def setUp(self):
        self.sample_records = [
            {
                "transaction_id": "TX1001",
                "amount": "10.00",
                "date": "2023-01-01",
                "description": "Test A"
            },
            {
                "transaction_id": "TX1002",
                "amount": "15.00",
                "date": "2023-01-02",
                "description": "Test B"
            },
            {
                "transaction_id": "TX1003",
                "amount": "",  # This will be parsed as 0.0
                "date": "2023-01-03",
                "description": "Test C"
            }
        ]
        self.report_path = "test_report.json"

    def test_reconcile_structure(self):
        report = reconcile(self.sample_records)
        self.assertIn("matched", report)
        self.assertIn("mismatched", report)
        self.assertIn("missing", report)

    def test_matched_and_mismatched_logic(self):
        report = reconcile(self.sample_records, threshold=0.02)

        # Expect TX1001 and TX1002 to be matched
        self.assertIn("TX1001", report["matched"])
        self.assertIn("TX1002", report["matched"])

        # Expect TX1003 to be mismatched due to empty amount
        mismatched_ids = [r["transaction_id"] for r in report["mismatched"]]
        self.assertIn("TX1003", mismatched_ids)

    def test_save_report_creates_file(self):
        report = reconcile(self.sample_records)
        save_report(report, self.report_path)
        self.assertTrue(os.path.exists(self.report_path))

        with open(self.report_path) as f:
            data = json.load(f)
            self.assertIn("matched", data)
            self.assertIsInstance(data["matched"], list)

    def test_performance(self):
        large_dataset = [
            {
                "transaction_id": f"TX{i:05}",
                "amount": "100.00",
                "date": "2023-01-01",
                "description": f"Test {i}"
            }
            for i in range(10000)
        ]

        start_time = time.time()
        report = reconcile(large_dataset)
        duration = time.time() - start_time

        print(f"\n🕒 Reconciliation time for 10,000 records: {duration:.4f} seconds")
        self.assertLess(duration, 2.0, "Reconciliation took too long")

    def tearDown(self):
        if os.path.exists(self.report_path):
            os.remove(self.report_path)

if __name__ == '__main__':
    unittest.main()
