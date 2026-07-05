# QA Triage Report — Build #262

**Source report:** [../../reports/build-failures/build-262.md](../../reports/build-failures/build-262.md)
**Source build:** [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #262](https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/262/)
**Analysis date:** 2026-07-05

---

## Build Summary

Build: automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #262
Total Tests: 14
Passed: 11
Failed: 3
Pass Rate: 78.6%

---

## Root Cause Groups

### Discount type not propagated from Rialto → MediaHouse on initial placement read

**Affected Scenarios:**
- `tc_getMHTC03` — verify that order arrived in MH from rilato - placement

**Evidence:**
- `orders[0].printDetails.discountType` expected `[RIALTO]`, found `[null]`
- `orderBasketPriceSummary.totalInclVat` expected `155683.63`, found `171598.78`
- `orders[0].vat` expected `31136.73`, found `47051.88`
- `orders[0].orderTotalInclVat` expected `155683.63`, found `171598.78`

**Note:** `discountType` arriving as `null` in MH causes downstream VAT and total calculations to be wrong. Failing since build #246.

---

### Stale discount type and incorrect commission after MH applies placement change

**Affected Scenarios:**
- `tc_getMHTC03a` — verify that order arrived in MH from rilato - placement - after change

**Evidence:**
- `orders[0].printDetails.discountType` expected `[NONE]`, found `[RIALTO]` (discount not cleared after patch)
- `orderBasketPriceSummary.commission` expected `7750.00`, found `8000.00`
- `orderBasketPriceSummary.orderbasketSum` expected `242250.00`, found `242000.00`
- `orderBasketPriceSummary.totalInclVat` expected `302812.50`, found `302500.00`

**Note:** After MH patches the placement, `discountType` is still set to `RIALTO` instead of being cleared to `NONE`, which cascades into wrong commission and totals. Failing since build #246.

---

### Order state not updated on Rialto readback after placement change

**Affected Scenarios:**
- `tc_getIntegrationRialto05b` — get order in rialto using prisa id- check if placement updated

**Evidence:**
- `orderHeader.statusFlags` expected `[PRELIMINARY]`, found `[]` (status missing)
- `orderHeader.commissionAmount` expected `7750.00`, found `620.0`
- `orderAdDetails[0].depth` expected `184`, found `372` (placement depth not updated)
- `orderAdDetails[0].priceNet` expected `250000.00`, found `249380.0`

**Note:** Rialto order state is not reflecting the placement update. `statusFlags` is empty and commission/depth values are stale. Failing since build #246.

---

## Summary

- 3 of 14 tests fail in the `CASS TC4 Change Placement` suite — all related to cross-system data sync between Rialto and MediaHouse.
- All 3 failures have persisted since build #246; commit "updated api version from 87 to 88" (build #262) did not resolve them.

## Root Cause

- Cross-system field mapping for `discountType`, `commissionAmount`, and `statusFlags` is broken in the Rialto ↔ MediaHouse placement-change flow. The `discountType` is not set on initial MH read, not cleared after MH patches placement, and `statusFlags` are not synced back to Rialto.

## Affected Components

- MediaHouse readback (`getMHB2A.csv` — `tc_getMHTC03`, `tc_getMHTC03a`)
- Rialto readback (`getRialtoB2A.csv` — `tc_getIntegrationRialto05b`)

## Recommended Fix

- Verify and fix the `discountType` mapping in the Rialto→MH placement sync handler.
- Ensure `discountType` is cleared to `NONE` when MH applies a placement change patch.
- Confirm `statusFlags` and `commissionAmount` are correctly written back to Rialto after placement update.

## Prevention

- Add targeted contract assertions for `discountType` and `statusFlags` in the pre-merge pipeline for placement-change flows.
