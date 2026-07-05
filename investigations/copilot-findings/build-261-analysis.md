# QA Triage Report — Build #261

**Source report:** [../../reports/build-failures/build-261.md](../../reports/build-failures/build-261.md)  
**Source build:** [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #261](https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/261/)  
**Analysis date:** 2026-07-05

---

## Build Summary

Build: automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #261  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

### Cross-system pricing/discount mismatch in placement flow

**Affected Features:**
- `MediaHouse/getMHB2A.csv`
- `CASS TC4 Change Placement`

**Affected Scenarios:**
- verify that order arrived in MH from rilato - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rilato - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
- `discountType`, commission, VAT, and `totalInclVat` differ from expected values in MH readback.

**Evidence:**
- `tc_getMHTC03`: expected `discountType=[[RIALTO]]`, found `[[null]]`; expected `totalInclVat=[155683.63]`, found `[171598.78]`
- `tc_getMHTC03a`: expected `discountType=[[NONE]]`, found `[[RIALTO]]`; expected `commission=[7750.00]`, found `[8000.00]`

**Impact:** 2 failures

**Confidence:** High

### Rialto readback payload mismatch after placement update

**Affected Features:**
- `Rialto/RialtoB2A/getRialtoB2A.csv`
- `CASS TC4 Change Placement`

**Affected Scenarios:**
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
- Response values for `statusFlags`, `commissionAmount`, `depth`, and `priceNet` diverge from expected order state.

**Evidence:**
- expected `orderHeader.statusFlags=[[PRELIMINARY]]`, found `[[]]`
- expected `orderHeader.commissionAmount=[7750.00]`, found `[620.0]`
- expected `orderAdDetails[0].depth=[184]`, found `[372]`
- expected `orderAdDetails[0].priceNet=[250000.00]`, found `[249380.0]`

**Impact:** 1 failure

**Confidence:** Medium

## Summary

- Build #261 is unstable due to 3 assertion mismatches in `CASS TC4 Change Placement`.

## Root Cause

- Most failures point to contract/value mismatch between expected and actual pricing/discount payload fields.

## Affected Components

- MediaHouse readback validations (`getMHB2A.csv`)
- Rialto readback validations (`getRialtoB2A.csv`)

## Recommended Fix

- Validate and align discount/commission mapping for placement-change responses before re-run.

## Prevention

- Keep targeted assertion checks for discount and pricing fields in pre-merge verification.
