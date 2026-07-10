# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #279  
URL: https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/279/  
Date: 2026-07-10 14:43 UTC  
Status: UNSTABLE  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

## MediaHouse discount and pricing assertions mismatch fixture expectations

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`

**Affected Scenarios:**
- verify that order arrived in MH from rialto - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rialto - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
`orders[0].printDetails.discountType` expected `[RIALTO/NONE]` but found `[null/RIALTO]`, with related commission, VAT, and total mismatches.

**Evidence:**
- `tc_getMHTC03`: `orders[0].printDetails.discountType` expected `[[RIALTO]]` found `[[null]]`; `orderBasketPriceSummary.totalInclVat` expected `155683.63` found `171598.78`.
- `tc_getMHTC03a`: `orders[0].printDetails.discountType` expected `[[NONE]]` found `[[RIALTO]]`; `orderBasketPriceSummary.commission` expected `7750.00` found `12500.00`.

**Impact:** 2 failures

**Confidence:** High

## Rialto order state after placement change does not match expected contract

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`

**Affected Scenarios:**
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
Post-change Rialto GET validation returns mismatched formatting/state and pricing fields (status flags, depth, commission, net totals).

**Evidence:**
- `orderHeader.statusFlags` expected `[[PRELIMINARY]]` found `[[]]`; `orderHeader.commissionAmount` expected `7750.00` found `620.0`.
- `orderAdDetails[0].depth` expected `184` found `372`; `orderAdDetails[0].priceNet` expected `250000.00` found `249380.0`.

**Impact:** 1 failure

**Confidence:** High

## Failing Tests / Steps

- `tc_getMHTC03` — verify that order arrived in MH from rialto - placement
- `tc_getMHTC03a` — verify that order arrived in MH from rialto - placement - after change
- `tc_getIntegrationRialto05b` — get order in rialto using prisa id- check if placement updated
