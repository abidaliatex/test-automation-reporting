# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #284  
Date: 2026-07-10 21:10 UTC  
Status: UNSTABLE  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

### MediaHouse discountType and pricing mismatch

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`

**Affected Scenarios:**
- `tc_getMHTC03` — verify that order arrived in MH from rialto - placement
- `tc_getMHTC03a` — verify that order arrived in MH from rialto - placement - after change

**Failure Pattern:**
MediaHouse GET validations fail after placement creation/change because `discountType`, pricing totals, VAT, and commission values differ from expected CSV fixture values.

**Evidence:**
- `tc_getMHTC03`: `orders[0].printDetails.discountType` expected `[RIALTO]` found `[null]`; `orderBasketPriceSummary.totalInclVat` expected `155683.63` found `171598.78`; `orders[0].vat` expected `31136.73` found `47051.88`; `orders[0].orderTotalInclVat` expected `155683.63` found `171598.78`.
- `tc_getMHTC03a`: `orders[0].printDetails.discountType` expected `[NONE]` found `[RIALTO]`; `orderBasketPriceSummary.commission` expected `7750.00` found `12500.00`; `orderBasketPriceSummary.orderbasketSum` expected `242250.00` found `237500.00`; `orderBasketPriceSummary.totalInclVat` expected `302812.50` found `296875.00`; `orders[0].commissions` expected `7750.00` found `12500.00`; `orders[0].sum` expected `242250.00` found `237500.00`; `orders[0].vat` expected `60562.50` found `59375.00`; `orders[0].orderTotalInclVat` expected `302812.50` found `296875.00`.

**Impact:** 2 failures

**Confidence:** High

---

### Rialto placement state, commission, and order status mismatch

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`

**Affected Scenarios:**
- `tc_getIntegrationRialto05b` — get order in rialto using prisa id - check if placement updated

**Failure Pattern:**
Rialto GET validation after placement update returns wrong `depth`, missing `statusFlags`, incorrect `commissionAmount`, and decimal format mismatches in pricing fields.

**Evidence:**
- `orderAdDetails[0].depth` expected `184` found `372`; `orderHeader.statusFlags` expected `[PRELIMINARY]` found `[]`.
- `orderHeader.commissionAmount` expected `7750.00` found `620.0`; `orderAdDetails[0].commissionAmount` expected `7750.00` found `620.0`.
- `orderAdDetails[0].priceNet` expected `250000.00` found `249380.0`; `priceGross` expected `250000.00` found `250000.0` (decimal precision).

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
