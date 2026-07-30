# Root Cause Analysis — Build #155

**Source report:** [build-155.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-155.md)

## Summary
- Build #155 (`automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`) finished **UNSTABLE** on 2026-07-30 21:03 UTC (duration ~93 min).
- 79 failures out of 514 tests (84.6% pass rate).
- Four distinct failure clusters: floating-point precision drift (dominant, 54 failures), `discountType` polarity inversion (13), transaction rollbacks + path-parameter errors (4), and basket ID synchronisation mismatches (3).

## Root Cause

- **Floating-point precision drift (54 failures):** Financial calculation fields across the CASS POST/GET flow return IEEE-754 double-precision residuals (e.g., `63660.630000000005` instead of `63660.63`, `38140.399999999994` instead of `38140.4`). This suggests the API or a downstream computation layer is not rounding/truncating to the expected decimal scale before serialising responses. May be a regression in the price-calculation or serialisation path introduced in `caiVersion 8.8.x-CI.39-r79762950`.

- **`discountType` polarity inversion (13 failures):** The field `orders[*].printDetails.discountType` returns `RIALTO` where tests expect `null`. This is the reverse of the failure seen in build #154 (`null` found where `RIALTO` expected), strongly suggesting that a fix or toggle applied between builds overcorrected the assignment condition.

- **Transaction rollback / path-parameter failures (4 failures):** TC18 and TC22 CASS POST calls return HTTP 500 with `Transaction rolled back because it has been marked as rollback-only`. TC24 revert and verify steps fail with a parameter-binding error (`agencyPrisaId` provided but `uuid` missing), implying the test state from a prior step was not carried forward correctly.

- **Basket ID synchronisation mismatch (3 failures):** The MediaHouse `orBoxid` value captured after basket creation diverges from the Agency Prisa ID used by the test in the subsequent GET verification. This may indicate a race condition or stale ID capture during test setup.

## Affected Components
- CASS POST/GET API response serialisation (price/discount calculation).
- Rialto → MediaHouse `discountType` mapping and propagation logic.
- Multi-line order update and basket revert flows (TC18, TC22, TC24).
- Cross-system basket ID binding between MediaHouse and Agency Prisa.

## Recommended Fix
- Investigate the price serialisation layer in `caiVersion 8.8.x-CI.39-r79762950` for the source of precision residuals; apply `BigDecimal` rounding or equivalent before response serialisation.
- Review the `discountType` assignment change applied between builds #154 and #155; the condition controlling whether `RIALTO` or `null` is set appears toggled in the wrong direction.
- Add diagnostic logging to TC18/TC22 POST calls to capture the underlying rollback trigger; review whether a prior step's transaction is not being committed before these calls execute.
- Verify that the basket ID capture step in TC1/TC35 waits for the synchronised ID from Agency Prisa before proceeding to GET verification.

## Prevention
- Add a precision contract test that asserts financial fields are serialised to exactly two decimal places.
- Add a regression test that covers the `discountType` assigned value for each discount-source variant (RIALTO, null) to catch polarity regressions.
- Ensure test-step state propagation for `uuid` and `agencyPrisaId` is validated before dependent steps execute.
