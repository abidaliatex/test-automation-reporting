# Root Cause Analysis — Build #250

**Source report:** [reports/build-failures/build-250.md](../../reports/build-failures/build-250.md)  
**Analysis date:** 2026-06-25  
**Analyst:** GitHub Copilot

---

## Summary

Build #250 failed due to timeout-related assertion errors in the `PaymentServiceTests` and `IntegrationTests` suites. All failures occurred immediately after commit `a3f9c12`, which modified the payment service timeout configuration.

## Root Cause

The commit `a3f9c12` reduced the connection timeout for the payment service from **5 000 ms** to **3 000 ms**. The test stubs used in `PaymentServiceTests` were still configured to simulate a response after **3 500 ms**, causing every timeout assertion to fail.

- The production code change was valid (tightening the timeout to improve user experience).
- The test doubles (mocks/stubs) were **not updated** to reflect the new timeout boundary.

## Affected Components

| Component | File | Issue |
|---|---|---|
| Payment service config | `src/main/resources/payment-config.yaml` | Timeout lowered to 3 000 ms |
| Payment test stub | `src/test/resources/stubs/payment-stub.json` | Still delays 3 500 ms |
| `PaymentServiceTests` | `src/test/java/PaymentServiceTests.java` | Assertions based on old 5 000 ms threshold |
| `IntegrationTests` | `src/test/java/IntegrationTests.java` | Depends on payment step completing within new threshold |

## Recommended Fix

1. Update `src/test/resources/stubs/payment-stub.json` — set the simulated response delay to ≤ 2 500 ms (safely within the new 3 000 ms timeout).
2. Review `PaymentServiceTests.java` lines 142 and 198 — update any hard-coded timeout values to match the new configuration.
3. Add a shared constant (e.g., `PAYMENT_TIMEOUT_MS`) imported by both production config and test setup to prevent this drift in the future.

## Prevention

- Introduce a lint/validation step that checks test stub delay values against the configured service timeout on every PR.
- Add a comment in `payment-config.yaml` referencing the stub file, so developers know to update both together.

---

*Generated automatically by GitHub Copilot.*
