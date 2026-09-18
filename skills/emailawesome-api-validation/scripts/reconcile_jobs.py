#!/usr/bin/env python3
"""Reconcile expected source IDs with asynchronous EmailAwesome job records."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def reconcile(expected: list[str], jobs: list[dict]) -> dict:
    expected_set = set(expected)
    by_source: dict[str, dict] = {}
    duplicates: set[str] = set()
    records_without_source = 0
    for job in jobs:
        source_id = str(job.get("source_id", "") or "")
        if not source_id:
            records_without_source += 1
            continue
        if source_id in by_source:
            duplicates.add(source_id)
        by_source[source_id] = job

    missing = [source_id for source_id in expected if source_id not in by_source]
    unexpected = [source_id for source_id in by_source if source_id not in expected_set]
    states = Counter(str(job.get("status", "MISSING") or "MISSING").upper() for job in by_source.values())
    return {
        "expected": len(expected),
        "received_unique": len(by_source),
        "records_without_source_id": records_without_source,
        "missing": missing,
        "unexpected": unexpected,
        "duplicates": sorted(duplicates),
        "job_states": dict(states),
        "reconciled": not missing and not unexpected and not duplicates and records_without_source == 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("expected_ids", type=Path, help="JSON array of source IDs")
    parser.add_argument("jobs", type=Path, help="JSON array of records containing source_id")
    args = parser.parse_args()
    expected = json.loads(args.expected_ids.read_text(encoding="utf-8"))
    jobs = json.loads(args.jobs.read_text(encoding="utf-8"))
    print(json.dumps(reconcile([str(item) for item in expected], jobs), indent=2))


if __name__ == "__main__":
    main()
