# Email verification result policy

| Result | Interpretation | Default reversible action |
|---|---|---|
| `VALID` | Available checks support using the address at verification time | Eligible for the next separately authorized step, subject to consent and business rules |
| `INVALID` | Available checks found a clear delivery problem | Preserve the record; route for correction or suppression review |
| `CATCH_ALL` | The domain broadly accepts mailbox patterns | Keep separate for review or a cautious policy |
| `UNKNOWN` | Available evidence is inconclusive | Retry later or review; do not force into valid or invalid |

Store verification result, verification time, consent, engagement, source, and suppression reason as separate fields. Preview affected counts before any write.
