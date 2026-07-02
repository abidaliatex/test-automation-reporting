# Build Failure Report — Build #250

| Field | Value |
|---|---|
| **Build ID** | 250 |
| **Date** | 2026-06-25 |
| **Branch** | `main` |
| **Triggered by** | Commit `a3f9c12` — "Update payment service timeout config" |
| **Status** | ❌ FAILED |
| **Duration** | 4m 38s |

## Failing Tests

| Test Suite | Test Name | Result |
|---|---|---|
| `PaymentServiceTests` | `testProcessPayment_timeout` | FAILED |
| `PaymentServiceTests` | `testRefundPayment_timeout` | FAILED |
| `IntegrationTests` | `testCheckoutFlow_endToEnd` | FAILED |

## Error Output

```
[PaymentServiceTests] testProcessPayment_timeout
  AssertionError: Expected response within 3000ms but got timeout after 3000ms
  at PaymentServiceTests.java:142
  Caused by: java.net.SocketTimeoutException: connect timed out

[PaymentServiceTests] testRefundPayment_timeout
  AssertionError: Expected response within 3000ms but got timeout after 3000ms
  at PaymentServiceTests.java:198
  Caused by: java.net.SocketTimeoutException: connect timed out

[IntegrationTests] testCheckoutFlow_endToEnd
  AssertionError: Checkout flow did not complete — payment step failed
  at IntegrationTests.java:87
```

## Environment

- **Runner**: `ubuntu-22.04`
- **Java**: `17.0.10`
- **Build tool**: Maven 3.9.6

## Suggested Next Steps

- Review the timeout configuration change in commit `a3f9c12`.
- Check whether the payment service mock/stub was updated to match the new timeout value.
- See investigation: [build-250-analysis.md](../../investigations/copilot-findings/build-250-analysis.md)
