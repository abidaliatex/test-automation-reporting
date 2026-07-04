# QA Triage Report — Build #260

**Source report:** [../../reports/build-failures/build-260.md](../../reports/build-failures/build-260.md)  
**Source build:** [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #260](https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/260/)  
**Analysis date:** 2026-07-04

---

## Build Summary

Build: automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #260  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

### Cross-system pricing/discount values diverged after placement flow

**Affected Features:**
- `MediaHouse/getMHB2A.csv`
- `CASS TC4 Change Placement`

**Affected Scenarios:**
- verify that order arrived in MH from Rialto - placement (`tc_getMHTC03`)
- verify that order arrived in MH from Rialto - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
- `orders[0].printDetails.discountType` and related totals/commission fields differ from expected values in MH readback.

**Evidence:**
- `tc_getMHTC03`: expected `discountType=[[RIALTO]]`, found `[[null]]`; expected `totalInclVat=[155683.63]`, found `[171598.78]`
- `tc_getMHTC03a`: expected `discountType=[[NONE]]`, found `[[RIALTO]]`; expected `commission=[7750.00]`, found `[8000.00]`

**Impact:** 2 failures

**Confidence:** High

### Rialto post-update order payload not aligned with expected placement state

**Affected Features:**
- `Rialto/RialtoB2A/getRialtoB2A.csv`
- `CASS TC4 Change Placement`

**Affected Scenarios:**
- get order in Rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
- Rialto response returned mismatched status, depth, commission, and net pricing fields after update.

**Evidence:**
- expected `orderHeader.statusFlags=[[PRELIMINARY]]`, found `[[]]`
- expected `orderHeader.commissionAmount=[7750.00]`, found `[620.0]`
- expected `orderAdDetails[0].depth=[184]`, found `[372]`
- expected `orderAdDetails[0].priceNet=[250000.00]`, found `[249380.0]`

**Impact:** 1 failure

**Confidence:** Medium

## Summary

- Build #260 is unstable due to 3 assertion failures in the same `CASS TC4 Change Placement` flow.
- The strongest signal is pricing/discount transformation drift between expected and actual payload values.

## Root Cause

- Possible data-contract or transformation mismatch in placement-change handling across Rialto and MediaHouse responses.

## Affected Components

- MediaHouse readback validation (`getMHB2A.csv`)
- Rialto readback validation (`getRialtoB2A.csv`)
- Shared placement-change pricing/discount calculation path

## Recommended Fix

- Validate expected mapping for `discountType`, commission, and totals in placement-update responses before next rerun.

## Prevention

- Add focused contract assertions for placement-change response fields before full end-to-end verification.
