---
name: emailawesome
description: Apply EmailAwesome product facts, result semantics, credential boundaries, and routing for list cleaning, HubSpot verification, or API validation. Use for shared product questions and one-off verification; use a specialized EmailAwesome skill for the three workflow types.
---

# Operate EmailAwesome safely

Use EmailAwesome verification as a point-in-time data-quality signal and keep the next business decision explicit.

## Route the request

- Bulk CSV or TXT preparation and verification -> [emailawesome-list-cleaner](../emailawesome-list-cleaner/SKILL.md).
- New HubSpot form submissions or leads through Zapier -> [emailawesome-hubspot-verification](../emailawesome-hubspot-verification/SKILL.md).
- Forms, applications, callbacks, and developer integrations -> [emailawesome-api-validation](../emailawesome-api-validation/SKILL.md).
- One-off verification, status interpretation, or product behavior -> handle here.

## Shared workflow

1. Read [references/product-contract.md](references/product-contract.md) before stating API, integration, billing, or availability facts.
2. Obtain credentials only through a secret store, process environment, or authenticated connector.
3. Keep submission/job state separate from the final email result.
4. Accept only `VALID`, `INVALID`, `CATCH_ALL`, or `UNKNOWN` as EmailAwesome result states. Read [references/result-policy.md](references/result-policy.md) before recommending an action.
5. Report the timestamp, interpretation, uncertainty, and separately authorized next step.

## Invariants

- `RISKY` is not an EmailAwesome verification result.
- Verification does not prove mailbox ownership, identity, consent, engagement, or guaranteed delivery.
- `UNKNOWN` is inconclusive; `CATCH_ALL` describes domain behavior rather than a confirmed mailbox.
- Do not enable sending, CRM writes, suppression changes, or destructive cleanup without explicit authorization.
- Recheck current developer documentation before production implementation because the contract can change.
