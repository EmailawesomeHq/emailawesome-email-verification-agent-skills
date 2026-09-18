# Email Verification Skills for List Cleaning, HubSpot, and APIs

This model-neutral EmailAwesome skill pack turns three practical email verification needs into auditable workflows: cleaning CSV lists before campaigns, verifying new HubSpot leads through Zapier, and adding an asynchronous validation boundary to forms or lead pipelines. It works with Claude, Codex, GLM, DeepSeek, and other harnesses that can load Markdown instructions and Python helpers. The pack preserves uncertainty, separates validation from consent, and requires approval before sending, CRM writes, suppression changes, or deployment.

## Included email verification skills

- [Clean and Verify an Email List Before Your Next Campaign](skills/emailawesome-list-cleaner/README.md)
- [Automatically Verify New HubSpot Leads Before Outreach](skills/emailawesome-hubspot-verification/README.md)
- [Add Email Validation to Forms and Lead Pipelines with an API](skills/emailawesome-api-validation/README.md)
- `emailawesome`, the shared product, result-policy, credential, and routing foundation

## Why this pack is useful

Most email validation examples stop at an API response. These skills preserve source rows, reconcile asynchronous jobs, distinguish `VALID`, `INVALID`, `CATCH_ALL`, and `UNKNOWN`, and make the next business action explicit. That makes the output easier to review, test, and hand from marketing operations to engineering without hiding unresolved records.

## Install and use

Follow [INSTALL.md](INSTALL.md) for harness-neutral loading and [COMPATIBILITY.md](COMPATIBILITY.md) for the portability contract. Use [SECURITY.md](SECURITY.md) before connecting credentials or production data.

The included tests are local and do not consume EmailAwesome credits. Live verification requires an EmailAwesome account, an authorized data set, and explicit approval.

## Discover the right workflow

Use the list cleaner for CSV email verification and bulk list preparation. Use the HubSpot workflow for Zapier-based lead routing. Use the API workflow for signup forms, applications, callbacks, and developer-managed pipelines.

Learn more at the [official EmailAwesome website](https://www.emailawesome.com/).
