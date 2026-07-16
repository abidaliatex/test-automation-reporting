# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #141  
Date: 2026-07-16 21:03 UTC  
Status: UNSTABLE  
Total Tests: 513  
Passed: 425  
Failed: 88  
Pass Rate: 82.8%

---

## Root Cause Groups

## discountType=null (MH/Rialto printDetails)

**Affected Features:**
- `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`
- `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase14.feature`, `rialtoB2A(CASS)TestCase15.feature`
- `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase26.feature`
- `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`
- `rialtoB2A(CASS)TestCase32.feature`, `rialtoB2A(CASS)TestCase33.feature`, `rialtoB2A(CASS)TestCase34.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase36.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- TC3 change Size — User perform CASS GET API
- TC4 Change Placement — User perform CASS GET API (discountType expected `[NONE]` found `[RIALTO]`)
- TC5 change to Uppslag/Spread/Panorama — User perform CASS GET API
- TC9 change size from Rialto — User perform CASS GET API
- TC11 change to UPPSLAG from Rialto — User perform CASS GET API
- TC14 change Product, Size, Placement & Date from Rialto — User perform CASS GET API (×2)
- TC15 2 products change date MH on head order line — User perform CASS GET API
- TC22 in MH change from Full page to uppslag — User perform CASS GET API
- TC23 in MH change from Full page to uppslag - two orderlines — Verify original full-page order state in MediaHouse
- TC23 in MH change from Full page to uppslag - two orderlines — Verify updated MediaHouse basket state
- TC23 in MH change from Full page to uppslag - two orderlines — Verify reverted MediaHouse basket state
- TC24 in MH change from uppslag to Full page — Verify original full-page order state in MediaHouse
- TC24 in MH change from uppslag to Full page — Verify updated MediaHouse basket state
- TC24 in MH change from uppslag to Full page — Verify reverted MediaHouse basket state
- TC26 Basic order for magazines — Verify reverted MediaHouse basket state
- TC27 Magazine (change date) — MEDIAHOUSE Verify original full-page order state in MediaHouse
- TC28 Magazine (change size) — MEDIAHOUSE Verify original full-page order state in MediaHouse
- TC30 Magazine (change Date & Size) — MEDIAHOUSE Verify original full-page order state in MediaHouse
- TC31 Magazine (change Date, Size & Placement) — MEDIAHOUSE Verify original full-page order state in MediaHouse
- TC32 Magazine (change date from Rialto) — MEDIAHOUSE Verify original magazine order state in MediaHouse
- TC32 Magazine (change date from Rialto) — MEDIAHOUSE Verify updated magazine order state in MediaHouse
- TC33 Magazine (change size from Rialto) — MEDIAHOUSE Verify original magazine order state in MediaHouse
- TC33 Magazine (change size from Rialto) — MEDIAHOUSE Verify updated magazine order state in MediaHouse
- TC34 Magazine (change to UPPSLAG from Rialto) — MEDIAHOUSE Verify original magazine order state in MediaHouse
- TC34 Magazine (change to UPPSLAG from Rialto) — MEDIAHOUSE Verify updated magazine order state in MediaHouse
- TC35 Magazine (change Date Size & Placement from Rialto) — MEDIAHOUSE Verify original magazine order state in MediaHouse
- TC36 Magazine (change Product Size Placement & Date from Rialto) — MEDIAHOUSE Verify original magazine order state in MediaHouse
- TC36 Magazine (change Product Size Placement & Date from Rialto) — MEDIAHOUSE Verify updated magazine order state in MediaHouse
- TC37 2 Products Magazine - changes the size in MH — MEDIAHOUSE Verify updated MediaHouse basket state

**Failure Pattern:**
`orders[0].printDetails.discountType` expected `[RIALTO]` found `[null]`; downstream basket pricing fields (`netPrice`, `vat`, `totalInclVat`) deviate accordingly. TC4 shows the inverse: `discountType` expected `[NONE]` found `[RIALTO]`.

**Evidence:**
- TC3: `orders[0].printDetails.discountType` expected `[[RIALTO]]` found `[[null]]`
- TC14: `orders[0].printDetails.discountType` expected `[[RIALTO, RIALTO, RIALTO, RIALTO]]` found `[[null, null, null, null]]`
- TC32: `discountType` expected `[RIALTO]` found `[null]`; `totalInclVat` deviates

**Impact:** 34 failures

**Confidence:** High

---

## Financial Calculation Errors (discount / commission / pricing)

**Affected Features:**
- `rialtoB2A(CASS)TestCase1and2.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`
- `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase15.feature`
- `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`
- `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- TC1 and TC2 — User perform CASS POST API (discountAmount expected `0.0` found `63660.63`)
- TC3 change Size — User perform CASS POST API (statusFlags `[PRELIMINARY]` found `[]`); User perform CASS GET API (commission drift)
- TC4 Change Placement — User perform CASS POST API (statusFlags `[PRELIMINARY]` found `[]`; commission `7750.00` found `620.0`)
- TC5 change to Uppslag/Spread/Panorama — User perform CASS POST API (discountAmount `0.0` found `63660.63`); User perform CASS GET API (commission drift)
- TC6 changes the date and the size — User perform CASS POST API (statusFlags `[PRELIMINARY]` found `[]`)
- TC9 change size from Rialto — User perform CASS POST API (discountAmount `0.0` found `38197.97`); User perform CASS GET API
- TC11 change to UPPSLAG from Rialto — User perform CASS GET API (`totalInclVat` expected `136225.78` found `146941.10`)
- TC15 2 products change date MH on head order line — User perform CASS POST API (discountAmount/commissionAmount mismatch)
- TC27 Magazine (change date) — RIALTO Verify created order; RIALTO Verify reverted state (issueDate + pricing)
- TC28 Magazine (change size) — RIALTO Verify created order (assertion format `[[v]]` vs `[v]`); MEDIAHOUSE Verify updated basket (commission `155.00` found `250.00`); RIALTO Verify reverted state
- TC30 Magazine (change Date & Size) — RIALTO Verify reverted state (priceNet `6000.0` found `5962.8`)
- TC31 Magazine (change Date, Size & Placement) — MEDIAHOUSE Verify updated basket (commission `465.00` found `250.00`); RIALTO Verify reverted state
- TC35 Magazine (change Date Size & Placement from Rialto) — RIALTO Verify updated Agency order; MEDIAHOUSE Verify updated state (basket ID mismatch: orBoxid `6377` vs agencyPrisaId `6378`)
- TC37 2 Products Magazine — MEDIAHOUSE Verify original order state; MEDIAHOUSE Verify updated state

**Failure Pattern:**
`discountAmount`, `commissionAmount`, `priceNetExComm`, `totalInclVat`, and `statusFlags` deviate from expected values on POST/GET steps. TC27/TC28 Rialto steps also fail on nested assertion format (`[[v]]` vs `[v]`).

**Evidence:**
- TC1 POST: `discountAmount` expected `0.0` found `63660.63`; `priceNetExComm` expected `192192.0` found `128531.37`
- TC4 POST: `orderHeader.statusFlags` expected `[[PRELIMINARY]]` found `[[]]`; `commissionAmount` expected `7750.00` found `620.0`
- TC11 GET: `totalInclVat` expected `136225.78` found `146941.10`
- TC28 MH: `commission` expected `155.00` found `250.00`

**Impact:** 22 failures

**Confidence:** High

---

## Two-product MH index out of bounds → TestContext cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase17.feature`, `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase20.feature`

**Affected Scenarios:**
- TC16 2 products change date on order line (not head) from MH — User perform CASS GET API (index error); User perform CASS POST API (no odIds); User perform CASS POST API (issueDate `2026-07-21` found `2026-07-01`)
- TC17 2 products change size on head order line from MH — User perform CASS GET API (index error); User perform CASS POST API (no odIds); User perform CASS POST API (moduleCode `[54,58]` found `[58,58]`)
- TC18 2 products change size on non-head from MH — User perform CASS GET API (index error); User perform CASS POST API (no odIds); User perform CASS POST API (moduleCode `[58,54]` found `[58,58]`)
- TC19 2 products change placement on head order from MH — User perform CASS GET API (index error); User perform CASS POST API (no odIds)
- TC20 2 products change placement order for non head from MH — User perform CASS GET API (index error); User perform CASS POST API (no odIds); User perform CASS POST API (placementId `[TEXT, SIDAN3]` found `[TEXT, TEXT]`)

**Failure Pattern:**
`Index 13 out of bounds for length 13` in GET step prevents `odIds` from being stored in TestContext; all subsequent POST/patch steps fail with `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.` Attribute mismatches on the final POST steps indicate the underlying change was not applied.

**Evidence:**
- TC16 GET: `Index 13 out of bounds for length 13`
- TC16 POST: `No MH odIds found in TestContext. Run the MH GET storage step before the patch step. expected object to not be null`
- TC17: same cascade pattern

**Impact:** 13 failures

**Confidence:** High

---

## Array ordering non-determinism (packageId / productId)

**Affected Features:**
- `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase22.feature`

**Affected Scenarios:**
- TC15 2 products change date MH on head order line — User perform CASS POST API (packageId/productId order `[AB, SVD]` found `[SVD, AB]`)
- TC19 2 products change placement on head order from MH — User perform CASS POST API (packageId/productId order `[AB, SVD]` found `[SVD, AB]`)
- TC22 in MH change from Full page to uppslag — User perform CASS POST API (packageId `[SVDTI, SVDTI, SVDTI, AB, AB, AB]` found in mixed order)

**Failure Pattern:**
`packageId` and `productId` arrays returned in a different order than fixture expectations.

**Evidence:**
- TC15 POST: `packageId` expected `[AB, SVD]` found `[SVD, AB]`; `productId` expected `[AB, SVD]` found `[SVD, AB]`
- TC22 POST: `packageId` expected `[SVDTI, SVDTI, SVDTI, AB, AB, AB]` found `[SVDTI, AB, SVDTI, AB, AB, SVDTI]`

**Impact:** 3 failures

**Confidence:** High

---

## Path parameter errors (agencyPrisaId / uuid swap)

**Affected Features:**
- `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- TC24 in MH change from uppslag to Full page — Revert two MediaHouse order lines to full page (placementId `[TEXT×6]` found `[UPPSLAG×6]`); Verify Rialto reflects the reverted full-page state (agencyPrisaId/uuid swap)
- TC29 Magazine (change to Uppslag/Spread/Panorama) — RIALTO Verify created Rialto order (uuid/agencyPrisaId swap); MEDIAHOUSE Update two MediaHouse order lines to uppslag (no odIds); RIALTO Verify Rialto reflects the reverted full-page state (missing agencyPrisaId)

**Failure Pattern:**
Rialto GET steps have swapped or missing path parameters (`agencyPrisaId`/`uuid`). TC29 additionally fails with `No MH odIds found in TestContext` as a cascade from the prior step failure.

**Evidence:**
- TC24 Rialto: `Redundant path parameters: agencyPrisaId=6367. Undefined path parameters: uuid`
- TC29 Rialto (create): `Redundant path parameters: uuid=aa659d7d-... Undefined path parameters: agencyPrisaId`
- TC29 Rialto (revert): `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: agencyPrisaId`

**Impact:** 5 failures

**Confidence:** High

---

## Failing Tests / Steps

- 88 failing validations grouped above across MH GET checks, MH/Rialto POST/PATCH steps, and Rialto follow-up GET checks.
