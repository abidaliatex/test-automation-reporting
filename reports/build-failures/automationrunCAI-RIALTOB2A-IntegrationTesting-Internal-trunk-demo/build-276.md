# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #276
Date: 2026-07-10 12:13 UTC
Status: UNSTABLE
Total Tests: 14
Passed: 11
Failed: 3
Pass Rate: 78.6%

---

## Root Cause Groups

### discountType and pricing mismatch in MediaHouse order validation

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`

**Affected Scenarios:**
- verify that order arrived in MH from rilato - placement (tc_getMHTC03)
- verify that order arrived in MH from rilato - placement - after change (tc_getMHTC03a)

**Failure Pattern:**
`orders[0].printDetails.discountType` is `null` instead of `RIALTO` on initial placement arrival; after placement change the discount type is `RIALTO` instead of the expected `NONE`. Pricing totals (totalInclVat, vat, orderTotalInclVat) and commission values diverge from fixture expectations in both steps.

**Evidence:**
- `tc_getMHTC03`: `orders[0].printDetails.discountType` expected `[RIALTO]` found `[null]`; `orderBasketPriceSummary.totalInclVat` expected `155683.63` found `171598.78`; `orders[0].vat` expected `31136.73` found `47051.88`
- `tc_getMHTC03a`: `orders[0].printDetails.discountType` expected `[NONE]` found `[RIALTO]`; `orderBasketPriceSummary.commission` expected `7750.00` found `12500.00`; `orderBasketPriceSummary.totalInclVat` expected `302812.50` found `296875.00`

**Impact:** 2 failures (failing since build #246)

**Confidence:** High

---

### Rialto order not updated after placement change

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`

**Affected Scenarios:**
- get order in rialto using prisa id - check if placement updated (tc_getIntegrationRialto05b)

**Failure Pattern:**
After the placement change is applied, the Rialto order does not reflect the expected state: `statusFlags` is empty instead of `[PRELIMINARY]`, `depth` is `372` instead of `184`, and commission/pricing values are incorrect.

**Evidence:**
- `orderHeader.statusFlags` expected `[PRELIMINARY]` found `[]`
- `orderAdDetails[0].depth` expected `184` found `372`
- `orderHeader.commissionAmount` expected `7750.00` found `620.0`
- `orderAdDetails[0].priceNet` expected `250000.00` found `249380.0`

**Impact:** 1 failure (failing since build #246)

**Confidence:** High

---

## Failing Tests / Steps

| Test Case | Scenario | Status |
|---|---|---|
| `tc_getMHTC03` | verify that order arrived in MH from rilato - placement | FAILED |
| `tc_getMHTC03a` | verify that order arrived in MH from rilato - placement - after change | FAILED |
| `tc_getIntegrationRialto05b` | get order in rialto using prisa id - check if placement updated | FAILED |
