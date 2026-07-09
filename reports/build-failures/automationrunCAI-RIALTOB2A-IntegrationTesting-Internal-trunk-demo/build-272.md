# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #272  
Date: 2026-07-09 20:49 UTC  
Status: UNSTABLE  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

### MediaHouse discountType inversion and downstream pricing mismatch

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`

**Affected Scenarios:**
- `tc_getMHTC03` — verify that order arrived in MH from rialto - placement
- `tc_getMHTC03a` — verify that order arrived in MH from rialto - placement - after change

**Failure Pattern:**
`discountType` is `null` before the placement change (expected `RIALTO`) and `RIALTO` after the change (expected `NONE`). This inversion cascades into incorrect VAT, commission, and basket total values in MH.

**Evidence:**
- `tc_getMHTC03`: `orders[0].printDetails.discountType` expected `[RIALTO]` found `[null]`; `orderBasketPriceSummary.totalInclVat` expected `155683.63` found `171598.78`; `orders[0].vat` expected `31136.73` found `47051.88`; `orders[0].orderTotalInclVat` expected `155683.63` found `171598.78`.
- `tc_getMHTC03a`: `orders[0].printDetails.discountType` expected `[NONE]` found `[RIALTO]`; `orderBasketPriceSummary.commission` expected `7750.00` found `12500.00`; `orderBasketPriceSummary.orderbasketSum` expected `242250.00` found `237500.00`; `orderBasketPriceSummary.totalInclVat` expected `302812.50` found `296875.00`; `orders[0].commissions` expected `7750.00` found `12500.00`; `orders[0].sum` expected `242250.00` found `237500.00`; `orders[0].vat` expected `60562.50` found `59375.00`; `orders[0].orderTotalInclVat` expected `302812.50` found `296875.00`.

**Impact:** 2 failures

**Confidence:** High

---

### Rialto order state, commission, and placement dimension mismatch after placement change

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`

**Affected Scenarios:**
- `tc_getIntegrationRialto05b` — get order in rialto using prisa id - check if placement updated

**Failure Pattern:**
After the placement change, the Rialto order returns an empty `statusFlags` (expected `[PRELIMINARY]`), a significantly lower `commissionAmount` (620.0 vs 7750.00), wrong `depth` (372 vs 184), and a `priceNet` that is short by ~620 — matching the unexpected commission deduction from the gross price. Decimal format mismatches (`250000.0` vs `250000.00`) are additional minor fixture issues.

**Evidence:**
- `orderHeader.statusFlags` expected `[PRELIMINARY]` found `[]`.
- `orderHeader.commissionAmount` expected `7750.00` found `620.0`; `orderAdDetails[0].commissionAmount` expected `7750.00` found `620.0`.
- `orderAdDetails[0].depth` expected `184` found `372`.
- `orderAdDetails[0].priceNet` expected `250000.00` found `249380.0` (250000 − 620 = 249380 — commission incorrectly subtracted from net price).
- Decimal format differences: `priceGross`, `orderHeader.priceNetExComm`, `orderAdDetails[0].priceGross`, `orderAdDetails[0].priceNetExComm` all return `250000.0` vs `250000.00`.

**Impact:** 1 failure

**Confidence:** High

---

## Failing Tests / Steps

- `tc_getMHTC03` — verify that order arrived in MH from rialto - placement
- `tc_getMHTC03a` — verify that order arrived in MH from rialto - placement - after change
- `tc_getIntegrationRialto05b` — get order in rialto using prisa id - check if placement updated

## Error Output

```text
--- tc_getMHTC03 ---
java.lang.AssertionError: The following asserts failed:
  Mismatch on field: orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]
  Mismatch on field: orderBasketPriceSummary.totalInclVat expected [155683.63] but found [171598.78]
  Mismatch on field: orders[0].vat expected [31136.73] but found [47051.88]
  Mismatch on field: orders[0].orderTotalInclVat expected [155683.63] but found [171598.78]
  at stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)

--- tc_getMHTC03a ---
java.lang.AssertionError: The following asserts failed:
  Mismatch on field: orders[0].printDetails.discountType expected [[NONE]] but found [[RIALTO]]
  Mismatch on field: orderBasketPriceSummary.commission expected [7750.00] but found [12500.00]
  Mismatch on field: orderBasketPriceSummary.orderbasketSum expected [242250.00] but found [237500.00]
  Mismatch on field: orderBasketPriceSummary.totalInclVat expected [302812.50] but found [296875.00]
  Mismatch on field: orders[0].commissions expected [7750.00] but found [12500.00]
  Mismatch on field: orders[0].sum expected [242250.00] but found [237500.00]
  Mismatch on field: orders[0].vat expected [60562.50] but found [59375.00]
  Mismatch on field: orders[0].orderTotalInclVat expected [302812.50] but found [296875.00]
  at stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)

--- tc_getIntegrationRialto05b ---
java.lang.AssertionError: The following asserts failed:
  Mismatch on field: priceGross expected [250000.00] but found [250000.0]
  Mismatch on field: orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]
  Mismatch on field: orderHeader.priceNetExComm expected [250000.00] but found [250000.0]
  Mismatch on field: orderHeader.commissionAmount expected [7750.00] but found [620.0]
  Mismatch on field: orderAdDetails[0].depth expected [184] but found [372]
  Mismatch on field: orderAdDetails[0].priceGross expected [250000.00] but found [250000.0]
  Mismatch on field: orderAdDetails[0].commissionAmount expected [7750.00] but found [620.0]
  Mismatch on field: orderAdDetails[0].priceNetExComm expected [250000.00] but found [250000.0]
  Mismatch on field: orderAdDetails[0].priceNet expected [250000.00] but found [249380.0]
  at stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)
```
