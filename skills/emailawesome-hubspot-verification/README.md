# Automatically Verify New HubSpot Leads Before Outreach

This model-neutral HubSpot email validation workflow connects a new form submission to EmailAwesome through Zapier, records four explicit result states, and controls the next action before outreach. It supports HubSpot email verification with visible audit fields and duplicate protection, while the Zapier email validation design keeps consent, suppression, and provider status separate.

## What it does

The skill maps a HubSpot trigger to EmailAwesome validation, then routes `VALID`, `INVALID`, `CATCH_ALL`, and `UNKNOWN` without inventing a generic risky status. It produces a dry-run map for reads, writes, branches, failures, retries, and rollback before any live Zap is enabled.

## Why it is valuable

New leads often move through several tools before anyone notices a bad or inconclusive address. This workflow makes the verification result and timestamp reviewable near the point of entry, while preserving uncertainty and preventing duplicate processing.

## Outputs

- A trigger-to-action workflow map
- HubSpot field mappings and four result branches
- Stable record IDs, timestamps, provider IDs, and workflow version fields
- An exception queue, retry owner, rollback plan, and test matrix

Example route: `HubSpot form submission -> EmailAwesome result -> audit fields -> approved next action`. This is a dry-run contract until the user authorizes and tests a live Zap.

## Use it when

Use this skill for new HubSpot form submissions or leads that should be checked before downstream outreach. Use bulk verification for an existing export. Do not claim the workflow prevents HubSpot from creating the original record, and never overwrite consent or delete a contact automatically.

## How the workflow works

1. Select the HubSpot form or object, source email field, and stable record ID.
2. Choose realtime validation when the next Zap step needs an immediate branch.
3. Write the provider result and audit fields without changing consent.
4. Test normal, duplicate, missing, malformed, outage, and write-failure paths.
5. Ask for approval before enabling, changing, or backfilling a live workflow.

## Example request

`Design a dry-run HubSpot and EmailAwesome Zapier workflow for new form submissions. Map all four results, prevent duplicate processing, and show every field write and rollback step.`

## Installation and product connection

Load this `SKILL.md` with the [shared EmailAwesome guidance](../emailawesome/SKILL.md). The workflow can be used by any LLM harness that supports Markdown skills; no OpenAI-specific command is required.

Connect HubSpot and EmailAwesome inside Zapier only after reviewing the fields and permissions. See the [official HubSpot integration guide](https://www.emailawesome.com/integrations/hubspot) for the current actions and templates.

## Limitations and FAQ

**Is this a native HubSpot connector?** No. It is a Zapier-based workflow.

**Does an unknown result mean invalid?** No. It is inconclusive and needs an explicit policy.

**Will the skill enable the Zap?** Not without approval immediately before the live change.
