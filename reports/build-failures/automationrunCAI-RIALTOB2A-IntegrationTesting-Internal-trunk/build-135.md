# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #135  
Date: 2026-07-11 15:10 UTC  
Status: UNSTABLE  
Total Tests: 513  
Passed: 427  
Failed: 86  
Pass Rate: 83.2%

---

## Root Cause Groups

## discountType=null and basket pricing drift

**Affected Features:**
- `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`
- `rialtoB2A(CASS)TestCase14.feature`, `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`
- `rialtoB2A(CASS)TestCase26.feature`, `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`
- `rialtoB2A(CASS)TestCase32.feature`, `rialtoB2A(CASS)TestCase33.feature`, `rialtoB2A(CASS)TestCase34.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase36.feature`

**Affected Scenarios:**
- TC3 change Size — User perform CASS GET API
- TC4 Change Placement — User perform CASS GET API
- TC5 change to Uppslag/Spread/Panorama — User perform CASS GET API
- TC9 change size from Rialto — User perform CASS GET API
- TC11 change to UPPSLAG from Rialto — User perform CASS GET API
- TC14 change Product, Size, Placement & Date from Rialto — User perform CASS GET API
- TC15 2 products change date MH on head order line — User perform CASS GET API (both steps)
- TC22 in MH change from Full page to uppslag — User perform CASS GET API
- TC23 in MH change from Full page to uppslag - two orderlines change — Verify original full-page order state in MediaHouse
- TC24 in MH change from uppslag to Full page — Verify original full-page order state / Verify updated MediaHouse basket state
- TC26 Basic order for magazines — Verify reverted MediaHouse basket state
- TC27 Magazine (change date) — MEDIAHOUSE Verify original / updated basket state
- TC28 Magazine (change size) — MEDIAHOUSE Verify original basket state
- TC30 Magazine (change Date & Size) — MEDIAHOUSE Verify original basket state
- TC31 Magazine (change Date, Size & Placement) — MEDIAHOUSE Verify original basket state
- TC32 Magazine (change date from Rialto) — MEDIAHOUSE Verify original / updated magazine order state
- TC33 Magazine (change size from Rialto) — MEDIAHOUSE Verify original / updated magazine order state
- TC34 Magazine (change to UPPSLAG from Rialto) — MEDIAHOUSE Verify original / updated magazine order state
- TC35 Magazine (change Date Size & Placement from Rialto) — MEDIAHOUSE Verify original magazine order state
- TC36 Magazine (change Product Size Placement & Date from Rialto) — MEDIAHOUSE Verify original / updated magazine order state

**Failure Pattern:**
`orders.printDetails.discountType` expected `[RIALTO]` found `[null]`; basket-level `orderDiscount`, `sumDiscount`, `netPrice`, `vat`, and `totalInclVat` deviate from fixtures accordingly.

**Evidence:**
- TC3: `orders[0].printDetails.discountType` expected `[RIALTO]` found `[null]`; `totalInclVat` expected `155683.63` found `171598.78`
- TC14: `orders[0].printDetails.discountType` expected `[RIALTO, RIALTO, RIALTO, RIALTO]` found `[null, null, null, null]`
- TC32: `orders.printDetails.discountType` expected `[RIALTO]` found `[null]`; `netPrice` expected `6000.00` found `2400.00`

**Impact:** 35 failures

**Confidence:** High

---

## PRELIMINARY statusFlags not returned

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase6.feature`

**Affected Scenarios:**
- TC1 and TC2 — User perform CASS POST API
- TC3 change Size — User perform CASS POST API
- TC4 Change Placement — User perform CASS POST API
- TC6 changes the date and the size — User perform CASS POST API

**Failure Pattern:**
`orderHeader.statusFlags` expected `[[PRELIMINARY]]` but found `[[]]`; commission and net amounts also drift on some steps.

**Evidence:**
- TC1: `orderHeader.statusFlags` expected `[[PRELIMINARY]]` found `[[]]`
- TC4 POST: `statusFlags` empty; `commissionAmount` expected `7750.00` found `620.0`
- TC6 POST: `statusFlags` empty; `commissionAmount` expected `3574.92` found `2390.78`

**Impact:** 5 failures

**Confidence:** High

---

## Two-product MH index out-of-bounds and TestContext cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase17.feature`, `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase20.feature`

**Affected Scenarios:**
- TC16 2 products change date on order line (not head) from MH — User perform CASS GET API (index error); User perform CASS POST API (no odIds); User perform CASS POST API (issueDate mismatch)
- TC17 2 products change size on head order line from MH — User perform CASS GET API (index error); CASS POST API (no odIds); CASS POST API (moduleCode mismatch)
- TC18 2 products change size on non-head from MH — User perform CASS GET API (index error); CASS POST API (no odIds); CASS POST API (moduleCode mismatch)
- TC19 2 products change placement on head order from MH — User perform CASS GET API (index error); CASS POST API (no odIds); CASS POST API (packageId/placementId mismatch)
- TC20 2 products change placement for non-head from MH — User perform CASS GET API (index error); CASS POST API (no odIds); CASS POST API (placementId mismatch)

**Failure Pattern:**
`Index 13 out of bounds for length 13` in GET step prevents `odIds` from being stored in `TestContext`; all subsequent patch steps then fail with `No MH odIds found in TestContext`.

**Evidence:**
- TC16: `Index 13 out of bounds for length 13`
- TC16 next step: `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`
- TC17: `Index 13 out of bounds for length 13` → same cascade

**Impact:** 15 failures

**Confidence:** High

---

## Array ordering and state drift

**Affected Features:**
- `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`

**Affected Scenarios:**
- TC15 2 products change date MH on head order line — User perform CASS POST API (`packageId`, `productId`, `issueDate` order mismatch)
- TC22 in MH change from Full page to uppslag — User perform CASS GET API (`paCode`, `plaCode`, `prodCode` order mismatch) x2
- TC23 in MH change from Full page to uppslag - two orderlines — Verify updated MediaHouse basket state; Verify reverted MediaHouse basket state
- TC24 in MH change from uppslag to Full page — Revert two order lines step (`placementId`, `issueDate` arrays wrong); Verify reverted MediaHouse basket state

**Failure Pattern:**
Array fields (`paCode`, `plaCode`, `prodCode`, `packageId`, `placementId`, `issueDate`) are returned in a different order than expected, or state after revert does not match original fixture.

**Evidence:**
- TC15 POST: `packageId` expected `[AB, SVD]` found `[SVD, AB]`; `issueDate` expected `[2026-07-01, 2026-07-21]` found `[2026-07-01, 2026-07-01]`
- TC22 GET: `paCode` expected `[AB, SVDTI, AB, AB, SVDTI, SVDTI]` found `[SVDTI, AB, SVDTI, AB, AB, SVDTI]`
- TC24 revert: `placementId` expected `[TEXT x6]` found `[UPPSLAG x6]`; `issueDate` array entirely wrong

**Impact:** 7 failures

**Confidence:** Medium

---

## Request construction / path parameter errors

**Affected Features:**
- `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- TC24 in MH change from uppslag to Full page — Verify Rialto reflects the reverted full-page state
- TC29 Magazine (change to Uppslag/Spread/Panorama) — RIALTO Verify created Rialto order; RIALTO Verify Rialto reflects the reverted full-page state

**Failure Pattern:**
Follow-up Rialto GET steps have swapped or undefined path parameters; TC23 revert also triggers a server-side rollback-only error (HTTP 500).

**Evidence:**
- TC24 Rialto follow-up: `Redundant path parameters: agencyPrisaId=6224. Undefined path parameters: uuid`
- TC29 Rialto (initial): `Redundant path parameters: uuid=2bc0bb31-74bb-4719-99e3-8ab8de7cba45. Undefined path parameters: agencyPrisaId`
- TC29 Rialto (revert): `Invalid number of path parameters. Expected 1, was 0. Undefined: agencyPrisaId`
- TC23 revert: HTTP 500 `Transaction rolled back because it has been marked as rollback-only`

**Impact:** 4 failures

**Confidence:** High

---

## Residual magazine pricing and identity mismatches

**Affected Features:**
- `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- TC11 change to UPPSLAG from Rialto — User perform CASS GET API (post-change pricing)
- TC27 Magazine (change date) — MEDIAHOUSE Update two order lines; MEDIAHOUSE Verify updated basket state; RIALTO Verify reverted state; RIALTO Verify created order (assertion format)
- TC28 Magazine (change size) — MEDIAHOUSE Verify updated basket state; RIALTO Verify reverted state; RIALTO Verify created order (assertion format)
- TC30 Magazine (change Date & Size) — RIALTO Verify reverted state
- TC31 Magazine (change Date, Size & Placement) — MEDIAHOUSE Verify updated basket state; RIALTO Verify reverted state
- TC35 Magazine (change Date Size & Placement from Rialto) — RIALTO Verify updated Agency order; MEDIAHOUSE Verify updated magazine order state (basket ID mismatch)
- TC37 2 Products Magazine — MEDIAHOUSE Verify original / updated basket state

**Failure Pattern:**
Post-change GET validations show commission, priceNet, and totalInclVat values that differ from fixtures without the `discountType=null` signature. TC35 shows an MH basket ID vs Agency Prisa ID correlation mismatch. TC27/TC28 Rialto steps show assertion format mismatch (nested list `[[v]]` vs scalar `[v]`).

**Evidence:**
- TC11 post-change: `totalInclVat` expected `136225.78` found `146941.10`
- TC28 updated state: `commission` expected `155.00` found `250.00`; `totalInclVat` expected `6056.25` found `5937.50`
- TC35: `MH basket ID (orBoxid) [6234] does not match Agency Prisa ID [6235]`
- TC27 Rialto: `discountAmount` expected `[[3600.0]]` found `[3600.0]` (nested list vs scalar)

**Impact:** 15 failures

**Confidence:** Medium

---

## Failing Tests / Steps

- 86 failing validations grouped above across MH GET checks, MH/Rialto POST/PATCH steps, and Rialto follow-up GET checks.
