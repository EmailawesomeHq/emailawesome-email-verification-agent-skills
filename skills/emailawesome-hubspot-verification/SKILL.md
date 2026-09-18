---
name: emailawesome-hubspot-verification
description: Design and verify Zapier workflows that check new HubSpot form submissions or leads with EmailAwesome, write auditable status fields, prevent duplicate processing, and route every result. Use for HubSpot data-quality automation; not for claiming a native connector or enabling a live Zap without approval.
---

# Automatically Verify New HubSpot Leads Before Outreach

Create a reversible HubSpot and EmailAwesome workflow that makes uncertainty visible before downstream outreach.

## Workflow

1. Identify the HubSpot trigger, form or object, source email field, stable record ID, current consent/suppression fields, and the first downstream action that depends on verification.
2. Read the [shared EmailAwesome guidance](../emailawesome/SKILL.md) and [references/hubspot-zapier-workflow.md](references/hubspot-zapier-workflow.md).
3. Choose Realtime Email Validation when the next Zap step needs an immediate branch. Use saved single validation when an asynchronous record is acceptable; use bulk verification for existing exports.
4. Map all four results explicitly. Never create a `RISKY` pseudo-status or merge `CATCH_ALL` and `UNKNOWN` into `VALID`.
5. Add duplicate-trigger protection, verification timestamp, provider result, provider/job ID where available, workflow version, retry owner, and an exception queue.
6. Produce a dry-run map of every read, write, branch, failure path, and rollback step.
7. Test valid, invalid, catch-all, unknown, missing email, malformed input, duplicate trigger, provider outage, and downstream-write failure.
8. Require approval immediately before enabling the Zap, changing a live workflow, backfilling records, or writing to HubSpot.

## Boundaries

- This is a Zapier workflow, not a proprietary native HubSpot connector.
- A HubSpot form submission may already exist before validation. Say `verify before outreach or downstream use`, not `prevent HubSpot from creating the contact`.
- Never delete contacts or overwrite consent automatically.
