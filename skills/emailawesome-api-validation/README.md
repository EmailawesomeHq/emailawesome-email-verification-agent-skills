# Add Email Validation to Forms and Lead Pipelines with an API

Use this model-neutral email validation API workflow to add EmailAwesome checks to forms, applications, CRMs, and automation services. The email verification API design supports secure server-side secrets, signup form validation, asynchronous callbacks, idempotent reconciliation, and explicit lead pipeline decisions. It does not guess undocumented endpoints or expose API keys in browser code.

## What it does

The skill defines a durable request record before submission, associates it with the provider ID, validates callbacks, handles retries, and separates provider job state from the final email result and business decision.

## Why it is valuable

Production integrations fail in more ways than a simple request example shows. Duplicate callbacks, timeouts, out-of-order delivery, rate limits, and uncertain submissions can create lost results or duplicate credit use. This workflow makes those cases testable and reviewable.

## Outputs

- An entry-point and latency policy
- A request, provider-job, callback, and business-decision state model
- Server-side credential and callback controls
- A reconciliation report for missing, unexpected, and duplicate mappings
- A failure matrix with bounded retries and approval gates

Example state path: `created -> submitted -> provider accepted -> callback validated -> result recorded -> business policy evaluated`. The included local tests validate the state-handling helpers; this is not a live API result.

## Use it when

Use this skill for developer-managed forms, applications, or lead systems that need an auditable validation boundary. Do not use it to promise synchronous-only behavior, guaranteed delivery, consent, or identity proof.

## How the workflow works

1. Define stable internal IDs, latency limits, retention, and result policies.
2. Persist the internal request before calling the provider.
3. Submit server-side and retain the returned provider ID.
4. Authenticate, validate, and apply callbacks idempotently.
5. Reconcile jobs and review failures before deployment.

## Example request

`Design an EmailAwesome integration for this signup form. Keep the key server-side, model the asynchronous callback, prevent replay and duplicate application, and include a reconciliation plan that can be checked with the provided helper.`

## Installation and product connection

Load this `SKILL.md` with the [shared EmailAwesome guidance](../emailawesome/SKILL.md). Run `scripts/reconcile_jobs.py` with Python 3 when mapping evidence must be checked. The skill is portable across compatible LLM and agent harnesses.

Recheck the [official EmailAwesome API use case](https://www.emailawesome.com/use-cases/email-validation-api) and current developer documentation before creating deployable transport code.

## Limitations and FAQ

**Can the API key be used in a browser?** No. Keep it server-side.

**Does an accepted job mean the email is valid?** No. Submission state and verification result are different.

**Will the skill deploy the integration?** Only after explicit authorization and production-specific review.
