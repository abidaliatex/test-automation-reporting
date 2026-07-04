# QA Triage Report — Build #258

**Source build:** [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #258](https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/258/)  
**Analysis date:** 2026-07-04  
**Local report:** No auto-generated `reports/build-failures/build-258.md` was present in this repository snapshot.

---

## Build Summary

Build: automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #258  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6 %

---

## Root Cause Groups

### Discount and pricing response drift in Media House verification

**Affected Features:**
- `MediaHouse/getMHB2A.csv`
- `CASS TC4 Change Placement`

**Affected Scenarios:**
- verify that order arrived in MH from rilato - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rilato - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
- `orders[0].printDetails.discountType` returned the wrong value (`null` or `RIALTO`)
- price summary fields drifted with the same response (`commission`, `vat`, `totalInclVat`)

**Evidence:**
- `tc_getMHTC03`: expected `orders[0].printDetails.discountType=[[RIALTO]]`, found `[[null]]`; `orderBasketPriceSummary.totalInclVat` was `171598.78` instead of `155683.63`
- `tc_getMHTC03a`: expected `orders[0].printDetails.discountType=[[NONE]]`, found `[[RIALTO]]`; `orderBasketPriceSummary.commission` was `8000.00` instead of `7750.00`
- Jenkins checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` with commit message `updated api version from 87 to 88`

**Impact:** 2 failures

**Confidence:** High

### Rialto order field mismatch after placement update

**Affected Features:**
- `Rialto/RialtoB2A/getRialtoB2A.csv`
- `CASS TC4 Change Placement`

**Affected Scenarios:**
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
- post-update Rialto order fields no longer matched expected financial and state values

**Evidence:**
- expected `orderHeader.statusFlags=[[PRELIMINARY]]`, found `[[]]`
- expected `orderHeader.commissionAmount=[7750.00]`, found `[620.0]`
- expected `orderAdDetails[0].depth=[184]`, found `[372]`
- Jenkins checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` with commit message `updated api version from 87 to 88`

**Impact:** 1 failure

**Confidence:** Medium
