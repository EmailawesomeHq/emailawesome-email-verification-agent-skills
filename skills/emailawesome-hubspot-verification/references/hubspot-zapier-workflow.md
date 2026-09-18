# HubSpot and Zapier workflow

## Recommended flow

`HubSpot submission or lead event -> stable source ID -> EmailAwesome validation -> four explicit branches -> audit fields -> permitted next action`

## Minimum audit fields

- `emailawesome_status`
- `emailawesome_verified_at`
- `emailawesome_provider_id` when available
- `emailawesome_workflow_version`
- `emailawesome_review_reason`

Use dedicated custom properties or a clearly documented external audit table. Do not overwrite consent, subscription, legal suppression, or the original email value.

## Default routing

- `VALID`: continue only to the next separately authorized step.
- `INVALID`: hold outreach; request correction or route to reversible suppression review.
- `CATCH_ALL`: route to a review queue or declared cautious policy.
- `UNKNOWN`: retry later or route to review.
- Failure or timeout: exception queue; do not invent a final result.

## Duplicate protection

Use the HubSpot record ID plus a workflow/version key. A status write must not retrigger the same verification indefinitely. Record who owns manual retries and how failed writes are replayed.
