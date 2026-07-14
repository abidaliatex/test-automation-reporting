# Root Cause Analysis — `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` Build #138

**Source Report:** [build-138.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-138.md)

---

## Summary

Build #138 (2026-07-13 21:03 UTC) produced **86 failures** across 513 tests (pass rate 82.7%). This is the same failure count as builds #134 and #135. The TC1 basket-not-found issue that added 3 failures in build #137 was not reproduced in this run. All six chronic failure groups identified in earlier builds persist unchanged — no regressions were introduced and none were resolved.

---

## Root Cause

Six independent root causes are responsible for all 86 failures:

1. **MH `discountType` not propagated (31 failures):** The service returns `discountType=null` on MH GET validation steps where `RIALTO` or `NONE` is expected. Downstream basket pricing fields (`netPrice`, `vat`, `totalInclVat`) deviate accordingly. Root cause is a service-side v88 regression that has persisted since build #134.

2. **Rialto `statusFlags` and commission drift (4 failures):** CASS POST responses return `statusFlags=[]` instead of `[PRELIMINARY]`, and commission amounts differ from fixture values. Consistent with the same Rialto state propagation defect present since build #134.

3. **Two-product MH index out-of-bounds — TC16–TC20 (15 failures):** `Index 13 out of bounds for length 13` in the multi-product GET step prevents `odIds` from being stored; all downstream POST/patch steps cascade-fail with `No MH odIds found in TestContext`. This is a test-framework bug that has been present since build #134.

4. **Array ordering mismatches — TC15, TC22, TC23, TC24 (6 failures):** Fields such as `packageId`, `placementId`, and `issueDate` are returned in a non-deterministic order that does not match fixture expectations.

5. **Path parameter errors — TC23, TC24, TC29 (9 failures):** `agencyPrisaId` and `uuid` are swapped or absent in Rialto GET steps; TC23 revert produces an HTTP 500 rolled-back transaction. The TC1 basket-not-found that appeared in build #137 did not recur.

6. **Residual pricing / identity mismatches — TC3, TC5, TC9, TC11, TC15, TC22, TC27, TC28, TC30, TC31, TC35, TC37 (21 failures):** Commission, priceNet, and totalInclVat deviate on post-change steps; TC27/TC28 Rialto steps fail on `[[v]]` vs `[v]` assertion format; TC35 has an MH basket ID / Agency Prisa ID identity mismatch.

---

## Affected Components

- MH discountType propagation service (v88)
- Rialto order state update (statusFlags, commissionAmount)
- Test framework — two-product odIds storage step (TC16–TC20)
- Test fixtures — `getMHB2A.csv`, `getRialtoB2A.csv` (stale post-v88 expected values)
- Rialto API request construction (TC24, TC29 — path parameter mapping)

---

## Recommended Fix

1. **Fixture refresh:** Update `getMHB2A.csv` and `getRialtoB2A.csv` expected values to reflect v88 service responses for `discountType`, commission, VAT, depth, and `statusFlags`. This would resolve the majority of failures (groups 1, 2, and 6).
2. **TC16–TC20 off-by-one fix:** Correct the index bound in the multi-product MH GET step so `odIds` are stored correctly and downstream steps can execute.
3. **TC24/TC29 path parameter mapping:** Investigate and swap the `agencyPrisaId` and `uuid` parameter bindings in the Rialto GET step template.
4. **Array ordering:** Use an order-agnostic assertion for `packageId`, `placementId`, and related array fields, or ensure the service returns a consistent order.

---

## Prevention

- Introduce a post-deployment fixture validation step that compares live API responses against test CSV fixtures after each version upgrade, to catch value drift before it causes suite-wide failures.
- Add explicit handling for the multi-product index bounds in the test framework to prevent silent cascade failures across TC16–TC20.
