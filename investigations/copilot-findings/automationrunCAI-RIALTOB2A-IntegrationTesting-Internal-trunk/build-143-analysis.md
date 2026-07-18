# Root Cause Analysis — `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` Build #143

**Source Report:** [build-143.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-143.md)

## Summary

- Build #143 finished `UNSTABLE` with **86 failures** out of 513 tests (83.2% pass rate).
- The failure mix matches the same six recurring groups already visible in builds #141 and #142; no new build-specific failure family stands out in Jenkins.
- The largest contributors remain `discountType=null` responses, pricing/status drift, and multi-product MediaHouse step cascades.

## Root Cause

1. **`discountType` propagation regression (39 failures):** GET validations repeatedly return `orders[].printDetails.discountType=null` where `RIALTO` is expected, with matching basket total drift.
2. **Pricing/status regression (21 failures):** POST/GET validations show missing `PRELIMINARY` status and mismatched `discountAmount`, `commissionAmount`, `priceNet`, `vat`, and `totalInclVat`.
3. **Two-product MH dependency failure (11 failures):** `Index 13 out of bounds for length 13` blocks `odIds` storage, so downstream steps fail with missing TestContext identifiers.
4. **Array-order sensitivity (3 failures):** `packageId`/`productId` values arrive in a different order than the fixture expects.
5. **Identifier binding errors (5 failures):** `agencyPrisaId` and `uuid` are missing or swapped in TC24/TC29, causing follow-on `NullPointerException` failures.
6. **Patch/revert instability (7 failures):** update/revert validations show unchanged field values and one explicit rollback-only transaction.

## Affected Components

- MH/Rialto response mapping for `printDetails.discountType`
- Pricing and order-status generation for CASS POST/GET responses
- Two-product MediaHouse GET step that persists shared `odIds`
- Request-template/path-parameter binding for `agencyPrisaId` and `uuid`
- Patch/revert execution for date, module, and placement updates

## Recommended Fix

- Validate why `discountType` is emitted as `null` and why the same responses also shift basket totals.
- Fix the two-product `odIds` capture path before re-running TC16–TC20 and TC29.
- Correct TC24/TC29 path-parameter bindings and investigate the rollback-only revert in TC23.

## Prevention

- Add a lightweight contract check for `discountType`, `statusFlags`, and key pricing fields before the full suite runs.
- Fail fast when required TestContext IDs or path parameters are missing.
- Use order-agnostic assertions, or stabilize service ordering, for `packageId`/`productId` arrays.
