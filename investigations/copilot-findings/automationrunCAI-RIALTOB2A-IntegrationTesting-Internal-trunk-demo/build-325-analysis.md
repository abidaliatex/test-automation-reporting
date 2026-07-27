# Build 325 — Root Cause Analysis

**Source Report:** [build-325.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-325.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo
**Date:** 2026-07-27

---

## Build Summary

Build: 325  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

## Missing `discountType` in MH/Rialto verification payload

**Affected Features:**
- MediaHouse GET order verification (`MediaHouse/getMHB2A.csv`)

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

## Discount and total-price drift after order change flow

**Affected Features:**
- MediaHouse changed-order validation (`MediaHouse/getMHB2A.csv`)
- Rialto order retrieval validation (`Rialto/RialtoB2A/getRialtoB2A.csv`)

**Affected Scenarios:**
- get order created in Rialto from MH - after change (`tc_getMHTC01a`)
- get order in rialto using risa id - check if issue date updated (`tc_getIntegrationRialto02`)

**Failure Pattern:**
`Expected zero-discount/full-price totals but response shows discountAmount=63660.63 and reduced net totals`

**Evidence:**
- `tc_getMHTC01a`: `orderBasketPriceSummary.orderDiscount expected [0.00] but found [63660.63]` and `netPrice expected [192192.00] but found [128531.37]`
- `tc_getIntegrationRialto02`: `discountAmount expected [0.0] but found [63660.63]`, `orderHeader.priceNetExComm expected [192192.0] but found [128531.37]`, `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

**Impact:** 2 failures

**Confidence:** High

## Summary

- Build 325 is unstable with 3 assertion failures concentrated in MH/Rialto order validation.
- Failures group into missing discount type metadata and consistent discount/net total drift values.

## Root Cause

- Responses in MH/Rialto verification path possibly return incomplete discount metadata (`discountType=null`) and inconsistent recalculated totals after change flow.

## Affected Components

- `orders[0].printDetails.*`
- `orderBasketPriceSummary.*`
- `orderHeader.*`
- `orderAdDetails[0].*`

## Recommended Fix

- Compare payload generation between initial create flow and changed-order retrieval flow for `discountType`, `discountAmount`, and net/total fields.
- Verify status-flag mapping in the retrieval path returning `orderHeader.statusFlags`.

## Prevention

- Add contract checks for non-null `discountType` and cross-field arithmetic consistency (`discount`, `net`, `totalInclVat`) across MH and Rialto GET validations.
