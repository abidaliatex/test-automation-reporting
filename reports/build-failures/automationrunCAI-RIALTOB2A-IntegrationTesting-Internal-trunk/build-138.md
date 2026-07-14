# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #138  
Date: 2026-07-13 21:03 UTC  
Status: UNSTABLE  
Total Tests: 513  
Passed: 427  
Failed: 86  
Pass Rate: 82.7%

---

## Root Cause Groups

## discountType=null and basket pricing drift

**Affected Features:**
- `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase7.feature`
- `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase14.feature`, `rialtoB2A(CASS)TestCase15.feature`
- `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase26.feature`
- `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`
- `rialtoB2A(CASS)TestCase32.feature`, `rialtoB2A(CASS)TestCase33.feature`, `rialtoB2A(CASS)TestCase34.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase36.feature`

**Affected Scenarios:**
- TC3 change Size — User perform CASS GET API
- TC4 Change Placement — User perform CASS GET API (×2: discountType null then found RIALTO when NONE expected)
- TC5 change to Uppslag/Spread/Panorama — User perform CASS GET API
- TC6 changes the date and the size — User perform CASS GET API
- TC7 Change Date, Size & Placement — User perform CASS GET API
- TC9 change size from Rialto — User perform CASS GET API
- TC11 change to UPPSLAG from Rialto — User perform CASS GET API
- TC14 change Product, Size, Placement & Date from Rialto — User perform CASS GET API (×2)
- TC15 2 products change date MH on head order line — User perform CASS GET API
- TC22 in MH change from Full page to uppslag — User perform CASS GET API (×2)
- TC23 in MH change from Full page to uppslag - two orderlines — Verify original full-page order state in MediaHouse
- TC24 in MH change from uppslag to Full page — Verify original / Verify updated MediaHouse basket state
- TC26 Basic order for magazines — Verify reverted MediaHouse basket state
- TC27 Magazine (change date) — MEDIAHOUSE Verify original full-page order state
- TC28 Magazine (change size) — MEDIAHOUSE Verify original full-page order state
- TC30 Magazine (change Date & Size) — MEDIAHOUSE Verify original full-page order state
- TC31 Magazine (change Date, Size & Placement) — MEDIAHOUSE Verify original full-page order state
- TC32 Magazine (change date from Rialto) — MEDIAHOUSE Verify original / updated magazine order state
- TC33 Magazine (change size from Rialto) — MEDIAHOUSE Verify original / updated magazine order state
- TC34 Magazine (change to UPPSLAG from Rialto) — MEDIAHOUSE Verify original / updated magazine order state
- TC35 Magazine (change Date Size & Placement from Rialto) — MEDIAHOUSE Verify original magazine order state
- TC36 Magazine (change Product Size Placement & Date from Rialto) — MEDIAHOUSE Verify original / updated magazine order state

**Failure Pattern:**
`orders.printDetails.discountType` expected `[RIALTO]` found `[null]`; downstream `orderDiscount`, `sumDiscount`, `netPrice`, `vat`, and `totalInclVat` deviate from fixtures accordingly.

**Evidence:**
- TC3: `orders[0].printDetails.discountType` expected `[RIALTO]` found `[null]`; `totalInclVat` expected `155683.63` found `171598.78`
- TC14: `orders[0].printDetails.discountType` expected `[RIALTO, RIALTO, RIALTO, RIALTO]` found `[null, null, null, null]`
- TC32: `discountType` expected `[RIALTO]` found `[null]`; `orderDiscount` expected `0.00` found `3600.00`

**Impact:** 31 failures

**Confidence:** High

---

## PRELIMINARY statusFlags not returned

**Affected Features:**
- `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`

**Affected Scenarios:**
- TC3 change Size — User perform CASS POST API
- TC4 Change Placement — User perform CASS POST API
- TC5 change to Uppslag/Spread/Panorama — User perform CASS POST API
- TC6 changes the date and the size — User perform CASS POST API

**Failure Pattern:**
`orderHeader.statusFlags` expected `[[PRELIMINARY]]` found `[[]]`; commission and net amounts also deviate on affected calls.

**Evidence:**
- TC3 POST: `orderHeader.statusFlags` expected `[[PRELIMINARY]]` found `[[]]`; `commissionAmount` expected `3574.92` found `3984.47`
- TC4 POST: `orderHeader.statusFlags` expected `[[PRELIMINARY]]` found `[[]]`; `commissionAmount` expected `7750.00` found `620.0`
- TC5 POST: `discountAmount` expected `[0.0]` found `[63660.63]`; `priceGross` expected `[250000.00]` found `[192192.0]`

**Impact:** 4 failures

**Confidence:** High

---

## Two-product MH index out of bounds → TestContext cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase17.feature`, `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase20.feature`

**Affected Scenarios:**
- TC16 2 products change date on order line (not head) from MH — GET (index error); POST (no odIds); POST (issueDate mismatch)
- TC17 2 products change size on head order line from MH — GET (index error); POST (no odIds); POST (moduleCode mismatch)
- TC18 2 products change size on non-head from MH — GET (index error); POST (no odIds); POST (moduleCode mismatch)
- TC19 2 products change placement on head order from MH — GET (index error); POST (no odIds); POST (packageId/placementId mismatch)
- TC20 2 products change placement for non-head from MH — GET (index error); POST (no odIds); POST (placementId mismatch)

**Failure Pattern:**
`Index 13 out of bounds for length 13` in GET step prevents `odIds` from being stored; all subsequent POST/patch steps fail with `No MH odIds found in TestContext`.

**Evidence:**
- TC16: `Index 13 out of bounds for length 13`
- TC16 POST: `No MH odIds found in TestContext. Run the MH GET storage step before the patch step. expected object to not be null`
- TC17: same index error → same cascade

**Impact:** 15 failures

**Confidence:** High

---

## Array ordering mismatches

**Affected Features:**
- `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`

**Affected Scenarios:**
- TC15 2 products change date MH on head order line — User perform CASS POST API (packageId, productId, issueDate order)
- TC22 in MH change from Full page to uppslag — User perform CASS POST API (packageId, placementId, prodCode order)
- TC23 in MH change from Full page to uppslag - two orderlines — Verify updated MediaHouse basket state; Verify reverted MediaHouse basket state
- TC24 in MH change from uppslag to Full page — Revert two order lines (placementId, issueDate arrays); Verify reverted MediaHouse basket state

**Failure Pattern:**
Array fields (`packageId`, `placementId`, `paCode`, `plaCode`, `prodCode`, `issueDate`) returned in a different order than fixture expectations.

**Evidence:**
- TC15 POST: `packageId` expected `[AB, SVD]` found `[SVD, AB]`
- TC22 POST: `packageId` expected `[SVDTI, SVDTI, SVDTI, AB, AB, AB]` found `[SVDTI, AB, SVDTI, AB, AB, SVDTI]`
- TC24 revert: `placementId` expected `[TEXT×6]` found `[UPPSLAG×6]`

**Impact:** 6 failures

**Confidence:** High

---

## Path parameter errors

**Affected Features:**
- `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- TC23 in MH change from Full page to uppslag - two orderlines — Revert two MediaHouse order lines to full page (HTTP 500)
- TC24 in MH change from uppslag to Full page — Verify Rialto reflects the reverted full-page state (agencyPrisaId/uuid swap)
- TC29 Magazine (change to Uppslag/Spread/Panorama) — RIALTO Verify created order (uuid/agencyPrisaId swap); MEDIAHOUSE cascade; RIALTO Verify reverted state (missing agencyPrisaId)

**Failure Pattern:**
Rialto GET steps have swapped or missing path parameters (`agencyPrisaId`/`uuid`). TC23 revert produces HTTP 500 rolled-back transaction.

**Evidence:**
- TC24 Rialto: `Redundant path parameters: agencyPrisaId=6331. Undefined path parameters: uuid`
- TC29 Rialto: `Redundant path parameters: uuid=a740c86f-... Undefined path parameters: agencyPrisaId`
- TC23 revert: HTTP 500 `Transaction rolled back because it has been marked as rollback-only`

**Impact:** 9 failures

**Confidence:** High

**Note:** The TC1 basket-not-found issue observed in build #137 (which added 3 additional failures to this group) is not present in this build; TC1 passed successfully.

---

## Residual pricing and identity mismatches

**Affected Features:**
- `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`
- `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`
- `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- TC3 change Size — User perform CASS GET API (post-change commission/pricing drift)
- TC5 change to Uppslag/Spread/Panorama — User perform CASS GET API (post-change commission drift)
- TC9 change size from Rialto — User perform CASS POST API (discountAmount cascade); User perform CASS GET API (depth/moduleCode/netAmount)
- TC11 change to UPPSLAG from Rialto — User perform CASS GET API (post-change totalInclVat/vat)
- TC15 2 products change date MH on head order line — User perform CASS POST API; User perform CASS GET API (post-change pricing)
- TC22 in MH change from Full page to uppslag — User perform CASS GET API (final pricing step)
- TC27 Magazine (change date) — RIALTO Verify created order (`[[v]]` vs `[v]`); MEDIAHOUSE Update order lines (issueDate); MEDIAHOUSE Verify updated basket; RIALTO Verify reverted state
- TC28 Magazine (change size) — RIALTO Verify created order (assertion format); MEDIAHOUSE Verify updated basket (commission); RIALTO Verify reverted state
- TC30 Magazine (change Date & Size) — RIALTO Verify reverted state (priceNet, commission)
- TC31 Magazine (change Date, Size & Placement) — MEDIAHOUSE Verify updated basket; RIALTO Verify reverted state
- TC35 Magazine (change Date Size & Placement from Rialto) — RIALTO Verify updated Agency order; MEDIAHOUSE Verify updated state (basket ID mismatch)
- TC37 2 Products Magazine — MEDIAHOUSE Verify original / updated basket state

**Failure Pattern:**
Post-change GET validations show commission, priceNet, and totalInclVat deviations. TC27/TC28 Rialto steps fail on nested assertion format (`[[v]]` vs `[v]`). TC35 shows MH basket ID vs Agency Prisa ID mismatch.

**Evidence:**
- TC11 post-change: `totalInclVat` expected `136225.78` found `146941.10`
- TC27 Rialto: `discountAmount` expected `[[3600.0]]` found `[3600.0]`
- TC28 updated: `commission` expected `155.00` found `250.00`
- TC35: `MH basket ID (orBoxid) [6341] does not match Agency Prisa ID [6342]`

**Impact:** 21 failures

**Confidence:** Medium

---

## Failing Tests / Steps

- 86 failing validations grouped above across MH GET checks, MH/Rialto POST/PATCH steps, and Rialto follow-up GET checks.
