# Root Cause Analysis — `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` Build #142

**Source Report:** [build-142.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-142.md)

## Summary

- Build #142 finished `UNSTABLE` with **86 failures** out of 513 tests (83.2% pass rate).
- Failures are concentrated in six recurring groups: `discountType=null`, pricing/status drift, two-product MH index/TestContext cascade, array ordering mismatches, path-parameter errors with TC29 null pointers, and patch/revert-state failures.
- The same high-frequency patterns seen in recent builds remain active.

## Root Cause

1. **discountType propagation regression (36 failures):** GET validations repeatedly show `orders[].printDetails.discountType` as `null` where `RIALTO` is expected.
2. **Financial/status drift (24 failures):** POST/GET checks show missing `PRELIMINARY` status and pricing deltas (`discountAmount`, `commissionAmount`, `priceNet`, `totalInclVat`).
3. **Two-product MH step dependency failure (11 failures):** `Index 13 out of bounds` prevents `odIds` persistence; downstream steps fail with missing TestContext IDs.
4. **Array-order sensitivity (3 failures):** `packageId`/`productId` order differs from fixture expectation.
5. **Identifier routing errors (5 failures):** `agencyPrisaId`/`uuid` path parameters are swapped or missing; TC29 follow-up checks include `NullPointerException`.
6. **Patch/revert execution instability (7 failures):** update/revert payload validation mismatches and one explicit rollback-only HTTP 500.

## Affected Components

- MH/Rialto response mapping for `printDetails.discountType`
- CASS pricing + status flag generation (`PRELIMINARY`, commission/discount totals)
- Two-product MH GET-to-POST TestContext handoff (`odIds`)
- Rialto GET path parameter binding (`agencyPrisaId`, `uuid`)
- MediaHouse patch/revert transaction and payload application

## Recommended Fix

- Validate why `discountType` is emitted as `null` for affected MH/Rialto GET flows.
- Trace missing `PRELIMINARY` flag and pricing drift in CASS POST/GET responses.
- Fix the multi-product index handling that blocks `odIds` capture.
- Correct path parameter mapping for TC24/TC29 Rialto follow-up requests.
- Review revert/patch transaction handling for rollback-only and stale-state outcomes.

## Prevention

- Add a post-deploy contract check for `discountType`, `statusFlags`, and key pricing fields.
- Add guardrails to fail fast when `odIds` is not written to TestContext.
- Add request-template validation for path parameters before execution.
