#!/usr/bin/env python3
"""Create a stable, non-destructive working CSV and report email-column candidates."""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
from pathlib import Path

EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
RESERVED = {"_ea_source_row_id", "_ea_preflight_issue"}


def formula_safe(value: str) -> str:
    return "'" + value if value.startswith(("=", "+", "-", "@")) else value


def preflight(input_path: Path, output_path: Path, email_column: str | None = None) -> dict:
    raw = input_path.read_text(encoding="utf-8-sig")
    dialect = csv.Sniffer().sniff(raw[:8192], delimiters=",;\t|")
    reader = csv.DictReader(io.StringIO(raw), dialect=dialect)
    headers = list(reader.fieldnames or [])
    if not headers or any(not header for header in headers) or len(headers) != len(set(headers)):
        raise ValueError("CSV headers must be present and unique")
    if RESERVED.intersection(headers):
        raise ValueError("CSV uses reserved _ea_ audit columns")
    rows = list(reader)
    if not rows:
        raise ValueError("CSV contains no data rows")
    if any(None in row for row in rows):
        raise ValueError("CSV contains rows wider than its header")

    scores: dict[str, float] = {}
    for header in headers:
        values = [str(row.get(header, "") or "").strip() for row in rows[:200]]
        nonempty = [value for value in values if value]
        scores[header] = round(
            sum(bool(EMAIL_RE.fullmatch(value)) for value in nonempty) / max(1, len(nonempty)), 3
        )

    selected = email_column
    if selected is None:
        best = max(scores.values(), default=0)
        winners = [header for header, score in scores.items() if score == best and score >= 0.5]
        selected = winners[0] if len(winners) == 1 else None
    if selected is not None and selected not in headers:
        raise ValueError(f"email column not found: {selected}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_headers = ["_ea_source_row_id", "_ea_preflight_issue", *headers]
    with output_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=output_headers)
        writer.writeheader()
        for record_number, row in enumerate(rows, start=2):
            safe_row = {header: formula_safe(str(row.get(header, "") or "")) for header in headers}
            issue = ""
            if selected:
                raw_email = str(row.get(selected, "") or "").strip()
                if raw_email.startswith(("=", "+", "-", "@")):
                    issue = "formula_like_email_requires_review"
                    safe_row[selected] = formula_safe(raw_email)
                else:
                    safe_row[selected] = raw_email
            writer.writerow(
                {"_ea_source_row_id": str(record_number), "_ea_preflight_issue": issue, **safe_row}
            )

    return {
        "rows": len(rows),
        "headers": headers,
        "candidate_scores": scores,
        "selected_email_column": selected,
        "requires_email_column_selection": selected is None,
        "working_copy": str(output_path),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--email-column")
    args = parser.parse_args()
    print(json.dumps(preflight(args.input, args.output, args.email_column), indent=2))


if __name__ == "__main__":
    main()
