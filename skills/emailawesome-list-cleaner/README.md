# Clean and Verify an Email List Before Your Next Campaign

Use this model-neutral workflow to clean email list files without losing their source context. The email list cleaning process prepares a spreadsheet-safe working copy, performs CSV email verification preflight checks, maps approved rows to EmailAwesome bulk email verification, and exports auditable result segments. It does not send a campaign, delete contacts, or treat verification as consent.

## What it does

The skill detects likely email columns, assigns stable row IDs, separates malformed and duplicate records, and preserves every original field. After an approved EmailAwesome run, it reconciles provider results into `valid`, `invalid`, `catch_all`, `unknown`, and `unresolved` outputs.

## Why it is valuable

Teams can review exactly what was submitted, what came back, and what remains unresolved before an import or campaign decision. The row-level audit trail reduces accidental deletion and prevents inconclusive results from being presented as safe addresses.

## Outputs

- An unchanged source file and a spreadsheet-safe working copy
- Candidate-column scoring and stable source-row IDs
- Separate result files for all four EmailAwesome states plus unresolved rows
- Counts, percentages, exclusions, duplicates, assumptions, and readiness notes

Example result: `2,480 source rows = 2,301 verified + 129 intentionally excluded + 50 unresolved`. This is an illustrative local test format, not a live EmailAwesome result.

## Use it when

Use this skill before a campaign, CRM import, newsletter migration, or list-quality review involving CSV or TXT data. Do not use it to infer consent, ownership, engagement, or guaranteed delivery, and do not silently remove records.

## How the workflow works

1. Inspect and preserve the original file.
2. Run `scripts/preflight_csv.py` and confirm the email column.
3. Submit only approved candidates through EmailAwesome.
4. Reconcile each source row and run `scripts/segment_results.py`.
5. Review the report and approve any separate CRM or campaign action.

## Example request

`Prepare this CSV for EmailAwesome verification, preserve every row, identify the email column, and return segmented outputs plus a list-quality report. Do not send or delete anything.`

## Installation and product connection

Load this `SKILL.md` with the [shared EmailAwesome guidance](../emailawesome/SKILL.md). Any compatible LLM harness can read the Markdown references and run the Python 3 helpers. Keep credentials in a secret store or process environment.

Connect the approved candidates through the current EmailAwesome bulk interface. Review the [official bulk email verifier](https://www.emailawesome.com/use-cases/bulk-email-verifier) before a live run because product contracts can change.

## Limitations and FAQ

**Does a valid result authorize sending?** No. Verification and consent are separate.

**Are catch-all addresses safe?** Not by default. Catch-all describes domain behavior, not a confirmed mailbox.

**Can the skill change my CRM?** Only after explicit approval for that separate action.
