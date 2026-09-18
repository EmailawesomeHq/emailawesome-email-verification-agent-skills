#!/usr/bin/env python3
"""Split reconciled EmailAwesome CSV results into complete auditable segments."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

STATUSES = {
    "VALID": "valid",
    "INVALID": "invalid",
    "CATCH_ALL": "catch_all",
    "UNKNOWN": "unknown",
}


def segment(input_path: Path, output_dir: Path, status_column: str) -> dict:
    with input_path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        headers = reader.fieldnames or []
    if status_column not in headers:
        raise ValueError(f"status column not found: {status_column}")

    output_dir.mkdir(parents=True, exist_ok=True)
    buckets = {name: [] for name in [*STATUSES.values(), "unresolved"]}
    for row in rows:
        status = str(row.get(status_column, "") or "").strip().upper()
        buckets[STATUSES.get(status, "unresolved")].append(row)

    for name, bucket in buckets.items():
        path = output_dir / f"{name}.csv"
        with path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=headers)
            writer.writeheader()
            writer.writerows(bucket)

    counts = Counter({name: len(bucket) for name, bucket in buckets.items()})
    summary = {
        "input_rows": len(rows),
        "segments": dict(counts),
        "reconciled": sum(counts.values()) == len(rows),
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--status-column", default="email_address_status")
    args = parser.parse_args()
    print(json.dumps(segment(args.input, args.output_dir, args.status_column), indent=2))


if __name__ == "__main__":
    main()
