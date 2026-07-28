# Build 326 — Root Cause Analysis

**Source Report:** [build-326.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-326.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo
**Date:** 2026-07-28

---

## Build Summary

Build: 326  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

## Missing discount type metadata in MH/Rialto GET verification

**Affected Features:**
- MediaHouse/getMHB2A.csv

**Affected Scenarios:**
- verify order created in Rialto from MH (`tc_getMHTC01`)
- get order created in Rialto from MH - after change (`tc_getMHTC01a`)

**Failure Pattern:**
`orders[0].printDetails.discountType expected [RIALTO/NONE] found [null]`

**Evidence:**
- `tc_getMHTC01`: `orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`
- `tc_getMHTC01a`: `orders[0].printDetails.discountType expected [[NONE]] but found [[null]]`

**Impact:** 2 failures

**Confidence:** High

## Discount and total calculations drift after change flow

**Affected Features:**
- MediaHouse/getMHB2A.csv
- Rialto/RialtoB2A/getRialtoB2A.csv

**Affected Scenarios:**
- get order created in Rialto from MH - after change (`tc_getMHTC01a`)
- get order in rialto using risa id - check if issue date updated (`tc_getIntegrationRialto02`)

**Failure Pattern:**
`Expected zero-discount/full-price totals, but response contains discountAmount=63660.63 and reduced net/total values`

**Evidence:**
- `tc_getMHTC01a`: `orderBasketPriceSummary.orderDiscount expected [0.00] but found [63660.63]`, `netPrice expected [192192.00] but found [128531.37]`
- `tc_getIntegrationRialto02`: `discountAmount expected [0.0] but found [63660.63]`, `orderHeader.priceNetExComm expected [192192.0] but found [128531.37]`

**Impact:** 2 failures

**Confidence:** High

## Summary

- Build 326 is unstable with 3 failed checks concentrated in MH/Rialto order validation.
- Failures cluster around missing discount metadata and inconsistent discount/total calculations.

## Root Cause

- MH/Rialto retrieval responses may be returning null `discountType` and recalculated monetary totals inconsistent with expected baseline values.

## Affected Components

- `orders[0].printDetails.*`
- `orderBasketPriceSummary.*`
- `orderHeader.*`
- `orderAdDetails[0].*`

## Recommended Fix

- Validate discount-type mapping and price-summary calculation logic in MH-to-Rialto retrieval path used after order changes.

## Prevention

- Keep contract assertions for non-null `discountType` and cross-field price consistency in both MH and Rialto GET validation flows.
