# EmailAwesome product contract

Revalidate these facts against current product and developer documentation before consequential use.

## Confirmed product capabilities

- One-off verification in the product.
- Bulk verification for CSV or TXT lists.
- Asynchronous API verification.
- Zapier-based integrations, including HubSpot workflows.
- Sender-readiness and warm-up guidance as a separate product workflow.

## API facts used by this pack

- Base URL: `https://api.emailawesome.com/api`.
- Authentication header: `x-api-key`.
- Confirmed single-create path: `POST /validations/email_validation`.
- A single request includes `email` and a `results_callback` object.
- Submission/job states and final verification results are separate state machines.
- Final results are `VALID`, `INVALID`, `CATCH_ALL`, or `UNKNOWN`.
- Documented error handling includes malformed requests, conflicts, and rate limits.

Do not infer bulk paths, callback authenticity behavior, retry safety, quotas, or billing rules from the single-create contract. Verify them before generating deployable code.

## Integration facts

HubSpot workflows are currently presented as Zapier integrations, not as a proprietary native HubSpot connector. A HubSpot trigger may already have created a submission or record before validation runs. Do not promise otherwise.
