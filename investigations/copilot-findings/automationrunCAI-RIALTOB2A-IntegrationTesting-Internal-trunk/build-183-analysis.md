# Build 183 — Investigation Analysis

**Source report:** [build-183.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-183.md)

---

## Build Summary

Build: 183  
Total Tests: 514  
Passed: 458  
Failed: 56  
Pass Rate: 89.1%

---

## Root Cause Groups

### Order line field/state mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase9.feature`
- `rialtoB2A(CASS)TestCase14.feature` through `rialtoB2A(CASS)TestCase24.feature`
- `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase29.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase36.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS POST API (TC4, TC5, TC6, TC9, TC14-TC22)
- User perform CASS GET API (TC9, TC14-TC20, TC22)
- Verify created Rialto order and capture shared identifiers (TC23)
- Verify original full-page order state in MediaHouse (TC23, TC24)
- Verify updated MediaHouse basket state (TC23, TC24, TC37)
- Verify reverted MediaHouse basket state (TC23, TC24)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC28, TC29)
- RIALTO - Verify updated Agency order after Rialto change (TC35)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse (TC36)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC36)
- MEDIAHOUSE - Verify original order state in MediaHouse (TC37)
- RIALTO - Verify Rialto reflects the updated state (TC37)

**Failure Pattern:**
`Mismatch on field: orderAdDetails.packageId expected [[SVD, AB, SVD, AB]] but found [[AB, SVD, AB, SVD]]`

**Evidence:**
- The same ordering drift appears in both write-time and read-back assertions for `packageId`, `productId`, `paCode`, `prodCode`, `issueDate`, `placementId`, and related fields.
- Several failures show correct values attached to the wrong order-line position, which points to unstable ordering or wrong line-to-line mapping rather than missing data.
- TC37 also shows stale `placementId`, `materialId`, and price totals after MH changes, consistent with line-state propagation errors.

**Impact:** 45 failures

**Confidence:** High

### Transaction rollback on MediaHouse updates

**Affected Features:**
- `rialtoB2A(CASS)TestCase22.feature`
- `rialtoB2A(CASS)TestCase23.feature`
- `rialtoB2A(CASS)TestCase24.feature`
- `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS POST API (TC22)
- Update two MediaHouse order lines to uppslag (TC23, TC24)
- Revert two MediaHouse order lines to full page (TC23, TC24)
- MEDIAHOUSE - Update MediaHouse order head line to change date (TC37)

**Failure Pattern:**
`Transaction rolled back because it has been marked as rollback-only`

**Evidence:**
- All update calls fail with HTTP 400 and a rollback-only backend error payload.
- The failures are limited to MH update/revert flows, not the initial setup calls.
- The rollback payload consistently reports CAI version `8.8.x-CI.87-r3a178be8`.

**Impact:** 7 failures

**Confidence:** High

### Internal server error on API POST

**Affected Features:**
- `rialtoB2A(CASS)TestCase14.feature`
- `rialtoB2A(CASS)TestCase21.feature`

**Affected Scenarios:**
- User perform CASS POST API (TC14)
- User perform CASS POST API (TC21)

**Failure Pattern:**
`{"errorCode":1,"message":null} expected [N200] but found [N500]`

**Evidence:**
- Both failures occur on the POST step before downstream verification.
- The response body provides no business error detail, which suggests an unhandled server-side exception.

**Impact:** 2 failures

**Confidence:** Low

### Path parameter misconfiguration

**Affected Features:**
- `rialtoB2A(CASS)TestCase24.feature`

**Affected Scenarios:**
- Verify Rialto reflects the reverted full-page state (TC24)

**Failure Pattern:**
`Redundant path parameters are: agencyPrisaId=8238. Undefined path parameters are: uuid.`

**Evidence:**
- The verification step still passes `agencyPrisaId` where the endpoint expects `uuid`.
- The error is isolated to the final Rialto validation call in TC24.

**Impact:** 1 failure

**Confidence:** High

### Integration ID mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC35)

**Failure Pattern:**
`MH basket ID (orBoxid) [8248] does not match Agency Prisa ID [8249]`

**Evidence:**
- The IDs differ by one, which points to a synchronization or wrong-record lookup issue.
- This appears only in the MH verification step for TC35.

**Impact:** 1 failure

**Confidence:** Medium
