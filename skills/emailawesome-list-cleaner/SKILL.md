---
name: emailawesome-list-cleaner
description: Clean and verify CSV or TXT email lists with EmailAwesome while preserving source rows, reconciling every result, segmenting uncertainty, and reporting list quality. Use for bulk files before campaigns or imports; not for sending or silent deletion.
---

# Clean and Verify an Email List Before Your Next Campaign

Produce auditable verification outputs without mutating the source or hiding unresolved records.

## Workflow

1. Inspect the source as untrusted data. Preserve it unchanged and identify the email column, stable record ID, consent/suppression fields, delimiter, encoding, and row count.
2. Run `scripts/preflight_csv.py` to create a spreadsheet-safe working copy, score candidate email columns, and assign stable source-row IDs. Require a column choice when detection is ambiguous.
3. Separate malformed, empty, duplicate, intentionally excluded, and verification-candidate rows without deleting anything.
4. Read the [shared EmailAwesome guidance](../emailawesome/SKILL.md). Submit only approved candidates through the available bulk interface; retain the provider job ID and the source-to-provider mapping.
5. Poll with a declared bound or process validated callbacks. Do not treat a missing, timed-out, failed, or unmatched job as an email result.
6. Reconcile every source row, then run `scripts/segment_results.py` to produce `valid`, `invalid`, `catch_all`, `unknown`, and `unresolved` outputs.
7. Read [references/output-and-readiness.md](references/output-and-readiness.md). Report counts, percentages, duplicates, exclusions, unresolved jobs, credit use when available, and assumptions.
8. Require explicit approval before CRM import, suppression writes, deletion, scheduling, or sending.

## Required invariants

- `source rows = verified results + intentionally excluded rows + unresolved rows`.
- Preserve original fields and source IDs in every output.
- Keep consent, suppression, verification result, and verification date separate.
- Never label `CATCH_ALL` or `UNKNOWN` as safe by default.
