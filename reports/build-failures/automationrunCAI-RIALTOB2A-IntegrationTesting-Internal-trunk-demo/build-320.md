# Build Failure Report — automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #320

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 320 |
| **Date** | 2026-07-27 13:19:29 UTC |
| **Status** | UNSTABLE |
| **Duration** | ~261 s |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/320/ |

---

## Build Summary

Build: 320
Total Tests: 16
Passed: 12
Failed: 4
Pass Rate: 75%

---

## Root Cause Groups

## MediaHouse basket lookup returned a different order than the Agency order

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (`tc_getMHTC_MZN04a`)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (`tc_getMHTC_MZN04b`)

**Failure Pattern:**
`MH basket ID (orBoxid) [6863] does not match Agency Prisa ID [6869]`

**Evidence:**
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6863] does not match Agency Prisa ID [6869]`
- The same cross-system identifier mismatch failed both MH verification reads in the TC29 flow

**Impact:** 2 failures

**Confidence:** High

---

## Missing MH order-line IDs caused the update flow to abort and left Rialto in the pre-update state

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- MEDIAHOUSE - Update two MediaHouse order lines to uppslag - #1.1 (`tc_patchIntegrationMH_MZN03`)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (`tc_getIntegrationRialtoMZN04b`)

**Failure Pattern:**
`No MH odIds found in TestContext` followed by Rialto returning the original `TEXT` layout instead of the expected `UPPSLAG` state

**Evidence:**
- `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`
- `orderAdDetails.placementId expected [[UPPSLAG]] but found [[TEXT]]`
- Additional Rialto mismatches stayed on original-state values: columns `1` vs `2`, width `230` vs `460`, `priceGross` `6000.0` vs `11000.0`

**Impact:** 2 failures

**Confidence:** High
