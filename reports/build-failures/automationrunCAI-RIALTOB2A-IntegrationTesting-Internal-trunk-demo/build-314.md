# Build Failure Report — automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #314

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 314 |
| **Date** | 2026-07-26T12:50:09 UTC |
| **Status** | UNSTABLE |
| **Duration** | ~205 s |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/314/ |

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #314  
Total Tests: 15  
Passed: 12  
Failed: 3  
Pass Rate: 80.0%

---

## Root Cause Groups

## `discountType` missing in original MediaHouse order readback

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- verify that order arrived in MH from rilato - magzine order original state (`tc_getMHTC_MZN04a`)

**Failure Pattern:**
`orders.printDetails.discountType` expected `[RIALTO]` found `[null]`

**Evidence:**
- `Mismatch on field: orders.printDetails.discountType expected [[RIALTO]] but found [[null]]`
- The scenario reached the MediaHouse GET verification step and failed on field assertion rather than transport/status checks

**Impact:** 1 failure

**Confidence:** High

---

## Reverted full-page state was not reflected after the MediaHouse size-change flow

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- verify that order arrived in MH from rilato - magzine order after Uppslag/Spread/Panorama change (`tc_getMHTC_MZN04b`)
- confirms order created in Agency for testcase 29 - after size change (`tc_getIntegrationRialtoMZN04b`)

**Failure Pattern:**
Expected reverted full-page values (`HALVLIGG`, original dimensions, and ~5000 pricing), but both MH and Rialto responses still returned `UPPSLAG`/expanded dimensions with ~11000 pricing.

**Evidence:**
- MH assertion mismatches include `orders.printDetails.plaCode expected [[HALVLIGG]] but found [[UPPSLAG]]` plus width/depth and price summary mismatches
- Rialto assertion mismatches include `orderAdDetails.placementId expected [[HALVLIGG]] but found [[UPPSLAG]]` plus the same dimension and pricing drift

**Impact:** 2 failures

**Confidence:** High
