# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #298  
Date: 2026-07-22 13:42:02 UTC  
Status: `UNSTABLE`  
Total Tests: 15  
Passed: 10  
Failed: 5  
Pass Rate: 66.7%

---

## Root Cause Groups

## Missing `agencyPrisaId` path parameter in Rialto GET requests

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- RIALTO - Verify created Rialto order and capture shared identifiers (#1.1)
- RIALTO - Verify Rialto reflects the reverted full-page state (#1.1)

**Failure Pattern:**
`agencyPrisaId` path parameter undefined in Rialto GET call; `uuid` is passed as redundant parameter instead.

**Evidence:**
- `RIALTO - Verify created Rialto order and capture shared identifiers`: `Path parameters were not correctly defined. Redundant path parameters are: uuid=1829d8f3-7e33-4bdd-9964-b45c03af5f88. Undefined path parameters are: agencyPrisaId.`
- `RIALTO - Verify Rialto reflects the reverted full-page state`: `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: agencyPrisaId.`

**Impact:** 2 failures

**Confidence:** High

## Cascading NullPointerException — Prisa ID and MH odIds not available in TestContext

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- MEDIAHOUSE - Verify original full-page order state in MediaHouse (#1.1)
- MEDIAHOUSE - Update two MediaHouse order lines to uppslag (#1.1)
- MEDIAHOUSE - Verify updated MediaHouse basket state (#1.1)

**Failure Pattern:**
MediaHouse steps fail due to missing shared state (Prisa ID and MH odIds) that was not stored because earlier Rialto GET steps failed.

**Evidence:**
- `MEDIAHOUSE - Verify original full-page order state in MediaHouse`: `NullPointerException` at `ApiStepDefinition.user_verify_the_prisa_id_matches_with_the_prisa_id_from_agency` (ApiStepDefinition.java:1488)
- `MEDIAHOUSE - Update two MediaHouse order lines to uppslag`: `No MH odIds found in TestContext. Run the MH GET storage step before the patch step. expected object to not be null`
- `MEDIAHOUSE - Verify updated MediaHouse basket state`: `NullPointerException` at `ApiStepDefinition.user_verify_the_prisa_id_matches_with_the_prisa_id_from_agency` (ApiStepDefinition.java:1488)

**Impact:** 3 failures

**Confidence:** High
