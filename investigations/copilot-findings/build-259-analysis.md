# QA Triage Report — Build #259

**Source build:** [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #259](https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/259/)<br>
**Analysis date:** 2026-07-04<br>
**Local report:** No auto-generated `reports/build-failures/build-259.md` was present in this repository snapshot.

---

## Build Summary

Build: automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #259<br>
Total Tests: 14<br>
Passed: 11<br>
Failed: 3<br>
Pass Rate: 78.6%

---

## Root Cause Groups

### Media House discountType and pricing totals drift after placement change

**Affected Features:**
- `MediaHouse/getMHB2A.csv`
- `CASS TC4 Change Placement`

**Affected Scenarios:**
- verify that order arrived in MH from rilato - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rilato - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
- `orders[0].printDetails.discountType` and related basket totals no longer match expected values in the MH verification response.

**Evidence:**
- `tc_getMHTC03`: expected `orders[0].printDetails.discountType=[[RIALTO]]`, found `[[null]]`; `orderBasketPriceSummary.totalInclVat` expected `155683.63`, found `171598.78`
- `tc_getMHTC03a`: expected `orders[0].printDetails.discountType=[[NONE]]`, found `[[RIALTO]]`; `orderBasketPriceSummary.commission` expected `7750.00`, found `8000.00`
- Both failures occurred in the `MediaHouse\getMHB2A.csv` readback step of the same placement-change flow.

**Impact:** 2 failures

**Confidence:** High

### Rialto placement update returned mismatched order state and financial fields

**Affected Features:**
- `Rialto/RialtoB2A/getRialtoB2A.csv`
- `CASS TC4 Change Placement`

**Affected Scenarios:**
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
- The post-update Rialto order response returned unexpected status, commission, depth, and net values.

**Evidence:**
- expected `orderHeader.statusFlags=[[PRELIMINARY]]`, found `[[]]`
- expected `orderHeader.commissionAmount=[7750.00]`, found `[620.0]`
- expected `orderAdDetails[0].depth=[184]`, found `[372]`
- Failure occurred in the `Rialto\RialtoB2A\getRialtoB2A.csv` verification step after the Media House placement update.

**Impact:** 1 failure

**Confidence:** Medium
