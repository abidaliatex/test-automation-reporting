# Build 180 — Root Cause Analysis

**Source report:** [build-180.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-180.md)

---

## Build Summary

| Field | Value |
|---|---|
| Build | 180 |
| Total Tests | 514 |
| Passed | 467 |
| Failed | 47 |
| Pass Rate | 90.9% |

---

## Root Cause Groups

---

## 1. Print Details Array Ordering Mismatch (paCode / prodCode / plaCode)

**Affected Features:**
- rialtoB2A CASS scenarios (MH / Rialto integration)

**Affected Scenarios:**
- CASS TC14 change Product, Size, Placement & Date from Rialto — User perform CASS GET API (#1, #2)
- CASS TC15 2 products change date MH on head order line — User perform CASS GET API (#1, #2)
- CASS TC19 2 products change placement on head order from MH — User perform CASS POST API
- CASS TC20 2 products change placement order for non head from MH — User perform CASS POST API
- CASS TC22 in MH change from Full page to uppslag — User perform CASS GET API (#1, #2, #3)
- CASS TC23 two orderlines change — Verify updated MediaHouse basket state
- CASS TC23 two orderlines change — Verify reverted MediaHouse basket state
- CASS TC24 change from uppslag to Full page — Verify updated MediaHouse basket state
- CASS TC24 change from uppslag to Full page — Verify reverted MediaHouse basket state
- CASS TC37 - 2 Products Magazine - changes size in MH — MEDIAHOUSE - Verify updated basket state

**Failure Pattern:**
`printDetails.paCode expected [[SVDTI, AB]] but found [[AB, SVDTI]]`  
`orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]`

**Evidence:**
- TC14: `paCode expected [[SVDTI, SVDTI, AB, AB]] but found [[AB, SVDTI, AB, SVDTI]]`
- TC19: `packageId expected [[AB, SVD]] but found [[SVD, AB]]`
- TC22: `paCode expected [[SVDTI, AB, SVDTI, AB, AB, SVDTI]] but found [[AB, SVDTI, AB, SVDTI, AB, SVDTI]]`

**Impact:** ~18 failures

**Confidence:** High — consistent across multiple scenarios; the values are correct but the sort order returned by the API is non-deterministic or has changed.

---

## 2. Transaction Rollback — "rollback-only" 500 Error

**Affected Features:**
- rialtoB2A CASS TC22, TC24 (uppslag/full-page changes in MH)

**Affected Scenarios:**
- CASS TC22 in MH change from Full page to uppslag — User perform CASS POST API (#1)
- CASS TC22 in MH change from Full page to uppslag — User perform CASS POST API (#2)
- CASS TC24 change from uppslag to Full page — Revert two MediaHouse order lines to full page
- CASS TC14 change Product, Size, Placement & Date from Rialto — User perform CASS POST API (N500 variant)

**Failure Pattern:**
`Transaction rolled back because it has been marked as rollback-only` → HTTP 400 (expected 200)

**Evidence:**
- `500 : {"errorMessage":"Transaction rolled back because it has been marked as rollback-only","caiVersion":"8.8.x-CI.78-r5108c68e"} expected [N200] but found [N400]` at 23:36:42, 23:36:57, 23:39:03, 23:41:49

**Impact:** 7 failures

**Confidence:** High — server-side transaction management issue in CAI 8.8.x-CI.78-r5108c68e; likely a regression in the current CI build.

---

## 3. Unexpected Discount Applied (discountType / discountAmount)

**Affected Features:**
- rialtoB2A CASS TC5, TC9 (size/spread changes from Rialto)

**Affected Scenarios:**
- CASS TC5 change to Uppslag/Spread/Panorama — User perform CASS POST API
- CASS TC9 change size from Rialto — User perform CASS POST API
- CASS TC9 change size from Rialto — User perform CASS GET API
- CASS TC36 Magazine — MEDIAHOUSE Verify original state
- CASS TC36 Magazine — MEDIAHOUSE Verify updated state
- CASS TC37 - 2 Products Magazine — MEDIAHOUSE Verify original state

**Failure Pattern:**
`discountAmount expected [0.0] but found [63660.63]`  
`discountType expected [NONE] but found [PERCENT_PER_ORDER]`

**Evidence:**
- TC5: `discountAmount expected [0.0] but found [63660.63]`, `priceGross expected [250000.00] but found [192192.0]`
- TC9: `discountAmount expected [0.0] but found [38197.97]`, `discountType expected [NONE] but found [PERCENT_PER_ORDER]`
- TC36: `orderDiscount expected [3600.00] but found [4800.00]`; `orderDiscount expected [0.00] but found [4000.00]`

**Impact:** 8 failures

**Confidence:** High — pricing/discount recalculation logic is returning incorrect values after product/size changes.

---

## 4. Missing `statusFlags: PRELIMINARY` After Order Change

**Affected Features:**
- CASS TC4 (Change Placement), TC28 Magazine, TC29 Magazine

**Affected Scenarios:**
- CASS TC4 Change Placement — User perform CASS POST API
- CASS TC28 Magazine (change size) — RIALTO Verify reverted state
- CASS TC29 Magazine (change to Uppslag/Spread/Panorama) — RIALTO Verify reverted state

**Failure Pattern:**
`orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

**Evidence:**
- TC4: `statusFlags expected [[PRELIMINARY]] but found [[]]`
- TC28: same pattern after revert

**Impact:** 3 failures

**Confidence:** High — order status is not being set to PRELIMINARY after modification/revert operations.

---

## 5. Path Parameter Configuration Error (`agencyPrisaId` vs `uuid`)

**Affected Features:**
- CASS TC24 (verify Rialto after revert)

**Affected Scenarios:**
- CASS TC24 in MH change from uppslag to Full page — Verify Rialto reflects the reverted full-page state

**Failure Pattern:**
`Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=8121. Undefined path parameters are: uuid.`

**Evidence:**
- `java.lang.IllegalArgumentException: Redundant path parameters are: agencyPrisaId=8121. Undefined path parameters are: uuid.`

**Impact:** 1 failure

**Confidence:** High — test or endpoint configuration uses `agencyPrisaId` but the API now expects `uuid`.

---

## 6. MH Basket ID / Agency Prisa ID Mismatch & Rialto State Mismatch

**Affected Features:**
- CASS TC35, TC37 Magazine scenarios

**Affected Scenarios:**
- CASS TC35 Magazine (change Date Size & Placement from Rialto) — RIALTO Verify updated Agency order
- CASS TC35 Magazine — MEDIAHOUSE Verify updated magazine order state
- CASS TC37 - 2 Products Magazine — RIALTO Verify updated state

**Failure Pattern:**
`orBoxid [8131] does not match agencyPrisaId [8132]`  
`placementId / issueDate / depth mismatch between MH and Rialto`

**Evidence:**
- TC35: `INTEGRATION MISMATCH: MH basket ID (orBoxid) [8131] does not match Agency Prisa ID [8132]`
- TC35: `placementId expected [SIDAN2] but found [HALVLIGG]`, `issueDate expected [2026-08-05] but found [2026-08-12]`
- TC37: `placementId expected [[HALVLIGG, TEXT]] but found [[TEXT, TEXT]]`

**Impact:** 5 failures

**Confidence:** Medium — possibly related to the same ordering/state sync issue driving group 1, or a separate data-sync regression between MH and Rialto.
