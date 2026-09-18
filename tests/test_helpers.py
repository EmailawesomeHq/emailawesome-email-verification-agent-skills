import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


preflight = load("ea4_preflight", "skills/emailawesome-list-cleaner/scripts/preflight_csv.py")
segmenter = load("ea4_segment", "skills/emailawesome-list-cleaner/scripts/segment_results.py")
reconcile = load("ea4_reconcile", "skills/emailawesome-api-validation/scripts/reconcile_jobs.py")


class CsvTests(unittest.TestCase):
    def test_preflight_preserves_multiline_rows_and_formula_safety(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "input.csv"
            output = Path(temp) / "working.csv"
            source.write_text('Email,Notes\na@example.com,"line one\nline two"\nb@example.com,=SUM(1)\n', encoding="utf-8")
            result = preflight.preflight(source, output)
            self.assertEqual(result["selected_email_column"], "Email")
            with output.open(encoding="utf-8-sig", newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["Notes"], "line one\nline two")
            self.assertEqual(rows[1]["Notes"], "'=SUM(1)")

    def test_preflight_requires_choice_when_columns_tie(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "input.csv"
            output = Path(temp) / "working.csv"
            source.write_text("primary,secondary\na@example.com,b@example.com\n", encoding="utf-8")
            result = preflight.preflight(source, output)
            self.assertTrue(result["requires_email_column_selection"])

    def test_segmenter_preserves_every_row(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "results.csv"
            output = Path(temp) / "segments"
            source.write_text(
                "id,email_address_status\n1,VALID\n2,INVALID\n3,CATCH_ALL\n4,UNKNOWN\n5,FAILED\n",
                encoding="utf-8",
            )
            summary = segmenter.segment(source, output, "email_address_status")
            self.assertTrue(summary["reconciled"])
            self.assertEqual(summary["segments"]["unresolved"], 1)


class AsyncTests(unittest.TestCase):
    def test_reconciliation_reports_missing_duplicates_and_unmapped(self):
        result = reconcile.reconcile(
            ["1", "2"],
            [
                {"source_id": "1", "status": "COMPLETE"},
                {"source_id": "1", "status": "COMPLETE"},
                {"status": "FAILED"},
            ],
        )
        self.assertEqual(result["missing"], ["2"])
        self.assertEqual(result["duplicates"], ["1"])
        self.assertEqual(result["records_without_source_id"], 1)
        self.assertFalse(result["reconciled"])


if __name__ == "__main__":
    unittest.main()
