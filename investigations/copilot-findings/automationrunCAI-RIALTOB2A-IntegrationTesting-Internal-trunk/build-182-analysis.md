# Build 182 — Investigation Analysis

**Source report:** [build-182.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-182.md)

---

## Build Summary

| Field | Value |
|-------|-------|
| Build | 182 |
| Total Tests | 514 |
| Passed | 456 |
| Failed | 58 |
| Pass Rate | 88.7% |

---

## Root Cause Groups

---

## Root Cause 1 — Order Line Field Value Ordering / Sequencing Mismatch

**Affected Features:**
- rialtoB2A(CASS)TestCase4.feature
- rialtoB2A(CASS)TestCase5.feature
- rialtoB2A(CASS)TestCase6.feature
- rialtoB2A(CASS)TestCase9.feature
- rialtoB2A(CASS)TestCase14.feature
- rialtoB2A(CASS)TestCase15.feature
- rialtoB2A(CASS)TestCase16.feature
- rialtoB2A(CASS)TestCase17.feature
- rialtoB2A(CASS)TestCase18.feature
- rialtoB2A(CASS)TestCase19.feature
- rialtoB2A(CASS)TestCase20.feature
- rialtoB2A(CASS)TestCase22.feature
- rialtoB2A(CASS)TestCase23.feature
- rialtoB2A(CASS)TestCase24.feature
- rialtoB2A(CASS)TestCase28.feature
- rialtoB2A(CASS)TestCase29.feature
- rialtoB2A(CASS)TestCase35.feature
- rialtoB2A(CASS)TestCase36.feature
- rialtoB2A(CASS)TestCase37.feature

**Affected Scenarios:**
- User perform CASS POST API (TC4)
- User perform CASS POST API (TC5)
- User perform CASS POST API (TC6)
- User perform CASS POST API / GET API (TC9)
- User perform CASS POST API / GET API (TC14)
- User perform CASS POST API / GET API (TC15)
- User perform CASS POST API / GET API (TC16)
- User perform CASS POST API / GET API (TC17)
- User perform CASS POST API / GET API (TC18)
- User perform CASS POST API / GET API (TC19)
- User perform CASS POST API / GET API (TC20)
- User perform CASS POST API / GET API (TC22)
- Verify original/updated/reverted MediaHouse basket state (TC23)
- Verify original/updated/reverted MediaHouse basket state (TC24)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC28)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC29)
- RIALTO - Verify updated Agency order after Rialto change (TC35)
- MEDIAHOUSE - Verify original/updated magazine order state in MediaHouse (TC36)
- MEDIAHOUSE - Verify original/updated order state / RIALTO - Verify updated state (TC37)

**Failure Pattern:**
```
Mismatch on field: orderAdDetails.packageId expected [[SVD, AB, SVD, AB]] but found [[AB, SVD, AB, SVD]]
Mismatch on field: orderAdDetails.productId expected [[SVD, AB, SVD, AB]] but found [[AB, SVD, AB, SVD]]
Mismatch on field: orderAdDetails.issueDate expected [[2026-12-01, 2026-12-21]] but found [[2026-12-01, 2026-12-01]]
Mismatch on field: orders[0].printDetails.paCode expected [[SVDTI, SVDTI, AB, AB]] but found [[AB, SVDTI, AB, SVDTI]]
```

**Evidence:**
- Array values are present but in the wrong order (e.g., `[SVD, AB, SVD, AB]` vs `[AB, SVD, AB, SVD]`)
- Affects `packageId`, `productId`, `placementId`, `issueDate`, `materialId`, `depth`, `paCode`, `plaCode`, `prodCode`, `discountAmount`
- Impacts both POST (write) and GET (read-back verification) steps, indicating the data is stored incorrectly or returned in non-deterministic order
- Scope is broad: 19 TCs across Newspaper, Magazine, and multi-product scenarios; all involve multi-line orders or order modifications

**Impact:** 86 failures

**Confidence:** High

---

## Root Cause 2 — Transaction Rollback on MH Order Line Update (N400)

**Affected Features:**
- rialtoB2A(CASS)TestCase22.feature
- rialtoB2A(CASS)TestCase23.feature
- rialtoB2A(CASS)TestCase24.feature
- rialtoB2A(CASS)TestCase37.feature

**Affected Scenarios:**
- User perform CASS POST API (TC22)
- Update two MediaHouse order lines to uppslag (TC23)
- Revert two MediaHouse order lines to full page (TC23)
- Update two MediaHouse order lines to uppslag (TC24)
- Revert two MediaHouse order lines to full page (TC24)
- MEDIAHOUSE - Update MediaHouse order head line to change date (TC37)

**Failure Pattern:**
```
500: Transaction rolled back because it has been marked as rollback-only
expected [N200] but found [N400]
```

**Evidence:**
- All failures are MH-side update operations (uppslag ↔ full page conversions, magazine size changes)
- The backend marks the transaction as rollback-only before the commit, returning HTTP 400 to the caller
- Consistent across TC22, TC23, TC24, TC37 — all involve multi-line uppslag/size change operations in MediaHouse
- CAI version: `8.8.x-CI.80-rd84a301f` — possibly a regression introduced in CI.80

**Impact:** 14 failures

**Confidence:** High

---

## Root Cause 3 — Path Parameter Misconfiguration (TC24)

**Affected Features:**
- rialtoB2A(CASS)TestCase24.feature

**Affected Scenarios:**
- Verify Rialto reflects the reverted full-page state (TC24)

**Failure Pattern:**
```
Path parameters were not correctly defined.
Redundant path parameters are: agencyPrisaId=8201. Undefined path parameters are: uuid.
```

**Evidence:**
- The test step passes `agencyPrisaId` as a path parameter, but the endpoint now expects `uuid`
- Possibly a test configuration issue following an API contract change in the target endpoint

**Impact:** 2 failures

**Confidence:** High

---

## Root Cause 4 — Integration ID Mismatch (orBoxid vs. agencyPrisaId)

**Affected Features:**
- rialtoB2A(CASS)TestCase35.feature

**Affected Scenarios:**
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC35)

**Failure Pattern:**
```
INTEGRATION MISMATCH: MH basket ID (orBoxid) [8211] does not match Agency Prisa ID [8212]
expected [8212] but found [8211]
```

**Evidence:**
- MH basket ID and Agency Prisa ID are off by 1 — suggests an ID allocation or synchronisation issue between systems
- Possibly related to the same rollback root cause (Root Cause 2) causing partial writes that leave IDs de-synced

**Impact:** 2 failures

**Confidence:** Medium

---

## Root Cause 5 — Internal Server Error (N500) on Initial POST

**Affected Features:**
- rialtoB2A(CASS)TestCase14.feature

**Affected Scenarios:**
- User perform CASS POST API (TC14)

**Failure Pattern:**
```
{"errorCode":1,"message":null} expected [N200] but found [N500]
```

**Evidence:**
- Isolated to TC14 initial POST step; other TC14 steps fail with field mismatch errors instead
- `errorCode:1` with null message suggests an unhandled exception in the CASS API
- May be a transient infrastructure issue or a cascading effect from the rollback problem

**Impact:** 2 failures

**Confidence:** Low

---

## Summary

| Root Cause | Failures | Confidence |
|------------|----------|------------|
| Field value ordering / sequencing mismatch in multi-line orders | 86 | High |
| Transaction rollback on MH order line update | 14 | High |
| Path parameter `agencyPrisaId` vs `uuid` mismatch (TC24) | 2 | High |
| Integration ID mismatch orBoxid vs agencyPrisaId (TC35) | 2 | Medium |
| Internal Server Error (N500) on CASS POST (TC14) | 2 | Low |

The dominant failure (86/106 test failures, spread across 19 TCs) is the **array field ordering mismatch** in order details. Given the breadth of impact — all multi-product and multi-line modification scenarios — this likely points to a change in how the backend sorts or returns order line arrays in CAI build `8.8.x-CI.80-rd84a301f`.
