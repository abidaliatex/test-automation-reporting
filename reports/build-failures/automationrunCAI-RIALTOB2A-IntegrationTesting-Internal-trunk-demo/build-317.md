# Build Failure Report — automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #317

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 317 |
| **Date** | 2026-07-27 11:56 UTC |
| **Status** | UNSTABLE |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/317/ |

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #317  
Total Tests: 15  
Passed: 11  
Failed: 4  
Pass Rate: 73.3%

---

## Root Cause Groups

## MediaHouse basket/order correlation mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- verify that order arrived in MH from rialto - magazine order original state (`tc_getMHTC_MZN04a`)
- for Magazine change to Uppslag/Spread/Panorama in MH (`tc_patchIntegrationMH_MZN03`)
- verify that order arrived in MH from rialto - magazine order after Uppslag/Spread/Panorama change (`tc_getMHTC_MZN04b`)

**Failure Pattern:**
MH basket ID lookup returned `orBoxid=6821`, but the Agency Prisa ID captured earlier was `6841`; the follow-on MH patch step then had no stored order-line IDs to update.

**Evidence:**
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6821] does not match Agency Prisa ID [6841]`
- `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`
- The same Prisa/orBoxid mismatch failed both MH verification scenarios.

**Impact:** 3 failures

**Confidence:** High

---

## Rialto order did not match the expected reverted full-page state

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- confirms order created in Agency for testcase 29 - after size change (`tc_getIntegrationRialtoMZN04b`)

**Failure Pattern:**
Expected reverted full-page values (`HALVLIGG`, depth `146`, gross `5000.0`, no discount) but Rialto still returned a different state (`TEXT`, depth `297`, gross `6000.0`, discount `3600.0`, `PRELIMINARY`).

**Evidence:**
- `Mismatch on field: orderAdDetails.placementId expected [[HALVLIGG]] but found [[TEXT]]`
- `Mismatch on field: orderAdDetails.priceGross expected [[5000.0]] but found [[6000.0]]`
- `Mismatch on field: orderHeader.statusFlags expected [[]] but found [[PRELIMINARY]]`

**Impact:** 1 failure

**Confidence:** Medium
