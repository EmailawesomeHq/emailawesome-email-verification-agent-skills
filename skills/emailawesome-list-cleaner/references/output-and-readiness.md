# Output and list-quality rules

## Required outputs

- An unchanged source file or its recorded hash and location.
- A complete reconciled dataset with stable source IDs.
- Separate `VALID`, `INVALID`, `CATCH_ALL`, `UNKNOWN`, excluded, and unresolved views.
- Duplicate relationships that point to the retained source row.
- A machine-readable summary and a short human-readable quality report.

## List-quality decision

Return `LIST QUALITY READY`, `LIST QUALITY READY WITH CONDITIONS`, or `LIST QUALITY NOT READY` using thresholds supplied by the user. When none exist, propose provisional thresholds and label them as assumptions.

Consider verification coverage, list age, duplicates, malformed rows, consent/suppression completeness, and unresolved work. This decision describes data quality only. A valid result is not permission to contact the address and does not guarantee delivery.
