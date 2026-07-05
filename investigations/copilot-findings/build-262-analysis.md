# QA Triage Report — Build #262

**Source report:** [../../reports/build-failures/build-262.md](../../reports/build-failures/build-262.md)  
**Source build:** [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #262](https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/262/)  
**Analysis date:** 2026-07-05

---

## Build Summary

Build: automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #262  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

### Discount type and pricing mismatch in MH readback after placement creation

**Affected Features:**
- `MediaHouse/getMHB2A.csv`
- `CASS TC4 Change Placement`

**Affected Scenarios:**
- verify that order arrived in MH from rilato - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rilato - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
`discountType` not propagated correctly between Rialto and MediaHouse; pricing totals (VAT, commission, totalInclVat) differ from expected values on MH GET readback.

**Evidence:**
- `tc_getMHTC03`: `orders[0].printDetails.discountType` expected `[RIALTO]` found `[null]`; `totalInclVat` expected `155683.63` found `171598.78`
- `tc_getMHTC03a`: `orders[0].printDetails.discountType` expected `[NONE]` found `[RIALTO]`; `commission` expected `7750.00` found `8000.00`

**Impact:** 2 failures  
**Confidence:** High

---

### Rialto order state not reflecting placement update (Agency readback)

**Affected Features:**
- `Rialto/RialtoB2A/getRialtoB2A.csv`
- `CASS TC4 Change Placement`

**Affected Scenarios:**
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
After a placement change patched via MH, the Agency-side Rialto order still shows stale/incorrect values for `statusFlags`, `commissionAmount`, `depth`, and `priceNet`.

**Evidence:**
- `orderHeader.statusFlags` expected `[PRELIMINARY]` found `[]`
- `orderHeader.commissionAmount` expected `7750.00` found `620.0`
- `orderAdDetails[0].depth` expected `184` found `372`
- `orderAdDetails[0].priceNet` expected `250000.00` found `249380.0`

**Impact:** 1 failure  
**Confidence:** Medium
