# Root Cause Analysis — `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` Build #139

**Source Report:** [build-139.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-139.md)

---

## Summary

Build #139 (2026-07-14 21:03 UTC) produced **88 failures** across 513 tests (pass rate 82.8%). This is 2 more failures than build #138 (86). All chronic failure groups from prior builds persist; TC1/TC2 have regressed (discountAmount wrong, previously passing in #138), and TC37 now contributes additional failures. No previously failing groups were resolved.

---

## Root Cause

Five independent root causes are responsible for all 88 failures:

1. **MH `discountType` not propagated (34 failures):** The service returns `discountType=null` on MH/Rialto GET validation steps where `RIALTO` (or `NONE` in TC4) is expected. Downstream basket pricing fields (`netPrice`, `vat`, `totalInclVat`) deviate accordingly. This is a persistent regression since build #134, with 3 more failures in this build compared to #138.

2. **Financial calculation errors — discount / commission / pricing drift (22 failures):** CASS POST responses return `statusFlags=[]` instead of `[PRELIMINARY]`; `discountAmount`, `commissionAmount`, `priceNetExComm`, and `totalInclVat` deviate from fixture values. TC1/TC2 regressed this build (discountAmount `0.0` expected, `63660.63` found). TC27/TC28 Rialto steps additionally fail on a nested assertion format mismatch (`[[v]]` vs `[v]`). TC35 has a basket identity mismatch (`orBoxid [6377]` vs `agencyPrisaId [6378]`).

3. **Two-product MH index out-of-bounds — TC16–TC20 (13 failures):** `Index 13 out of bounds for length 13` in the multi-product GET step prevents `odIds` from being stored in TestContext; all downstream POST/patch steps cascade-fail with `No MH odIds found in TestContext`. Attribute mismatches (issueDate, moduleCode, placementId) on the final POST step indicate the underlying change was also not applied. This is a test-framework bug present since build #134.

4. **Array ordering non-determinism — TC15, TC19, TC22 (3 failures):** `packageId` and `productId` arrays are returned in a non-deterministic order that does not match fixture expectations.

5. **Path parameter errors — TC24, TC29 (5 failures):** `agencyPrisaId` and `uuid` are swapped or absent in Rialto GET steps; TC29 additionally cascades to a `No MH odIds` failure.

---

## Affected Components

- MH discountType propagation service (persistent regression since v88)
- Rialto order state update (statusFlags, commissionAmount, discountAmount — includes TC1/TC2 regression)
- Test framework — two-product odIds storage step (TC16–TC20, off-by-one index bound)
- Test fixtures — `getMHB2A.csv`, `getRialtoB2A.csv` (stale post-v88 expected values for pricing fields)
- Rialto API request construction (TC24, TC29 — path parameter mapping agencyPrisaId/uuid)

---

## Recommended Fix

1. **Fixture refresh:** Update `getMHB2A.csv` and `getRialtoB2A.csv` expected values to reflect current service responses for `discountType`, `discountAmount`, commission, VAT, depth, and `statusFlags`. This would resolve the majority of failures (groups 1 and 2).
2. **TC16–TC20 off-by-one fix:** Correct the index bound in the multi-product MH GET step so `odIds` are stored correctly and downstream steps can execute.
3. **TC24/TC29 path parameter mapping:** Swap the `agencyPrisaId` and `uuid` parameter bindings in the Rialto GET step template.
4. **Array ordering:** Use an order-agnostic assertion for `packageId`, `productId`, and related array fields, or ensure the service returns a consistent order.

---

## Prevention

- Introduce a post-deployment fixture validation step that compares live API responses against test CSV fixtures after each version upgrade, to catch value drift before it causes suite-wide failures.
- Add explicit handling for the multi-product index bounds in the test framework to prevent silent cascade failures across TC16–TC20.
- Add a regression gate on TC1/TC2 discountAmount to surface service-side discount calculation changes early.
