# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #286  
Date: 2026-07-11 14:59:22 UTC  
Status: `UNSTABLE`  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

## MediaHouse discountType and basket pricing drift

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`

**Affected Scenarios:**
- verify that order arrived in MH from rialto - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rialto - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
`orders[0].printDetails.discountType` and related basket totals/commission fields returned values different from the expected MediaHouse assertions.

**Evidence:**
- `tc_getMHTC03`: `discountType` expected `[RIALTO]` found `[null]`; `totalInclVat` expected `[155683.63]` found `[171598.78]`.
- `tc_getMHTC03a`: `discountType` expected `[NONE]` found `[RIALTO]`; `commission` expected `[7750.00]` found `[12500.00]`; `totalInclVat` expected `[302812.50]` found `[296875.00]`.

**Impact:** 2 failures

**Confidence:** High

## Rialto placement update state and pricing mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`

**Affected Scenarios:**
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
Post-update Rialto GET validation returned inconsistent order state and pricing values after the placement change flow.

**Evidence:**
- `statusFlags` expected `[PRELIMINARY]` found `[]`; `depth` expected `[184]` found `[372]`.
- `commissionAmount` expected `[7750.00]` found `[620.0]`; `priceNet` expected `[250000.00]` found `[249380.0]`.

**Impact:** 1 failure

**Confidence:** High
