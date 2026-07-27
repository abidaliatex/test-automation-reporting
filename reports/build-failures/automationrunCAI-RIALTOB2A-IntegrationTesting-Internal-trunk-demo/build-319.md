# Jenkins Build Failure Report

## Build Details

- **Build ID:** 319
- **Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo
- **Date:** 2026-07-27 13:13 UTC
- **Status:** UNSTABLE
- **URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/319/

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #319  
Total Tests: 16  
Passed: 12  
Failed: 4  
Pass Rate: 75.0%

---

## Root Cause Groups

## Cross-system ID drift between MediaHouse basket ID and Agency Prisa ID

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (TC29 / `tc_getMHTC_MZN04a`)
- MEDIAHOUSE - Update two MediaHouse order lines to uppslag - #1.1 (TC29 / `tc_patchIntegrationMH_MZN03`)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC29 / `tc_getMHTC_MZN04b`)

**Failure Pattern:**
`INTEGRATION MISMATCH: MH basket ID (orBoxid) [6863] does not match Agency Prisa ID [6868]`

**Evidence:**
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6863] does not match Agency Prisa ID [6868] expected [6868] but found [6863]`
- `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`
- Both MH verification scenarios fail at `User verify the Prisa ID matches with the Prisa ID from Agency`.

**Impact:** 3 failures

**Confidence:** High

---

## Reverted-state validation mismatch in Rialto order fields

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC29 / `tc_getIntegrationRialtoMZN04b`)

**Failure Pattern:**
Reverted full-page expectations do not match returned order state (placement, dimensions, and monetary fields).

**Evidence:**
- `orderAdDetails.placementId expected [[UPPSLAG]] but found [[TEXT]]`
- `orderAdDetails.columns expected [[2]] but found [[1]]`
- `orderAdDetails.priceGross expected [[11000.0]] but found [[6000.0]]`
- `orderHeader.statusFlags expected [[]] but found [[PRELIMINARY]]`

**Impact:** 1 failure

**Confidence:** High
