# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #285  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

## MediaHouse discountType and pricing mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`

**Affected Scenarios:**
- verify that order arrived in MH from rialto - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rialto - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
`orders[0].printDetails.discountType` expected `RIALTO/NONE` found `null/RIALTO` with corresponding basket totals, VAT, and commission mismatches.

**Evidence:**
- `tc_getMHTC03`: `discountType` expected `RIALTO` found `null`; `totalInclVat` expected `155683.63` found `171598.78`.
- `tc_getMHTC03a`: `discountType` expected `NONE` found `RIALTO`; `commission` expected `7750.00` found `12500.00`; `totalInclVat` expected `302812.50` found `296875.00`.

**Impact:** 2 failures

**Confidence:** High

## Rialto placement update state/pricing mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`

**Affected Scenarios:**
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
Placement update validation returned mismatched state and pricing values (`statusFlags`, `depth`, `commissionAmount`, price fields).

**Evidence:**
- `statusFlags` expected `PRELIMINARY` found empty.
- `orderAdDetails[0].depth` expected `184` found `372`.
- `commissionAmount` expected `7750.00` found `620.0`.

**Impact:** 1 failure

**Confidence:** High
