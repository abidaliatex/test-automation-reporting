# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #275  
Date: 2026-07-10 11:00 UTC  
Status: UNSTABLE  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

## MediaHouse post-placement discount and pricing values diverge from expected fixtures

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`

**Affected Scenarios:**
- verify that order arrived in MH from rialto - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rialto - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
MediaHouse GET validations returned different `discountType`, commission, VAT, and total values than the expected CSV fixtures after placement creation/change.

**Evidence:**
- `tc_getMHTC03`: `orders[0].printDetails.discountType` expected `[RIALTO]` found `[null]`; `orderBasketPriceSummary.totalInclVat` expected `155683.63` found `171598.78`; `orders[0].orderTotalInclVat` expected `155683.63` found `171598.78`.
- `tc_getMHTC03a`: `orders[0].printDetails.discountType` expected `[NONE]` found `[RIALTO]`; `orderBasketPriceSummary.commission` expected `7750.00` found `12500.00`; `orders[0].orderTotalInclVat` expected `302812.50` found `296875.00`.

**Impact:** 2 failures

**Confidence:** High

---

## Rialto placement-change retrieval returned different state and pricing values

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`

**Affected Scenarios:**
- get order in rialto using prisa id - check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
Rialto GET validation after the placement update returned different `statusFlags`, `depth`, commission, and net pricing values than expected.

**Evidence:**
- `orderHeader.statusFlags` expected `[PRELIMINARY]` found `[]`; `orderHeader.commissionAmount` expected `7750.00` found `620.0`; `orderHeader.priceNetExComm` expected `250000.00` found `250000.0`.
- `orderAdDetails[0].depth` expected `184` found `372`; `orderAdDetails[0].commissionAmount` expected `7750.00` found `620.0`; `orderAdDetails[0].priceNet` expected `250000.00` found `249380.0`.

**Impact:** 1 failure

**Confidence:** High

## Failing Tests / Steps

- `tc_getMHTC03` — verify that order arrived in MH from rialto - placement
- `tc_getMHTC03a` — verify that order arrived in MH from rialto - placement - after change
- `tc_getIntegrationRialto05b` — get order in rialto using prisa id - check if placement updated
