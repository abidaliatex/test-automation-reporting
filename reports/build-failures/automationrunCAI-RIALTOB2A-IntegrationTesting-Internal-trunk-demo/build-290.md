# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #290
Date: 2026-07-14 21:10:06 UTC
Status: `UNSTABLE`
Total Tests: 14
Passed: 11
Failed: 3
Pass Rate: 78.6%

---

## Root Cause Groups

## MediaHouse discount and basket total mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`

**Affected Scenarios:**
- verify that order arrived in MH from rialto - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rialto - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
`orders[0].printDetails.discountType` and MH basket totals (commission/VAT/totalInclVat) mismatch expected values.

**Evidence:**
- `tc_getMHTC03`: `discountType` expected `[RIALTO]` found `[null]`; `totalInclVat` expected `[155683.63]` found `[171598.78]`; `vat` expected `[31136.73]` found `[47051.88]`.
- `tc_getMHTC03a`: `discountType` expected `[NONE]` found `[RIALTO]`; `commission` expected `[7750.00]` found `[12500.00]`; `orderbasketSum` expected `[242250.00]` found `[237500.00]`.

**Impact:** 2 failures

**Confidence:** High

## Rialto placement update payload mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`

**Affected Scenarios:**
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
Rialto post-update GET response returns mismatched order state and pricing fields.

**Evidence:**
- `orderHeader.statusFlags` expected `[PRELIMINARY]` found `[]`; `orderAdDetails[0].depth` expected `[184]` found `[372]`.
- `orderHeader.commissionAmount` expected `[7750.00]` found `[620.0]`; `orderAdDetails[0].priceNet` expected `[250000.00]` found `[249380.0]`.

**Impact:** 1 failure

**Confidence:** High
