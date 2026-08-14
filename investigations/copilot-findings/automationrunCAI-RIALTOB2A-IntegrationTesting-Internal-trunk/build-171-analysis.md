# Build 171 — Root Cause Analysis

**Source Report:** [build-171.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-171.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-14 21:03:18 UTC

---

## Build Summary

**Build:** 171
**Total Tests:** 514
**Passed:** 465
**Failed:** 49
**Pass Rate:** 90.5%

---

## Root Cause Groups

---

## Root Cause 1: Basket Not Found for Campaign (Magazine TCs)

**Affected Features:**
- rialtoB2A CASS Magazine scenarios

**Affected Scenarios:**
- CASS TC31 Magazine (change Date, Size & Placement) — MEDIAHOUSE - User perform CASS POST API
- CASS TC32 Magazine (change date from Rialto) — MEDIAHOUSE - User perform CASS POST API
- CASS TC32 Magazine (change date from Rialto) — MEDIAHOUSE - Refresh basket lookup after Rialto update
- CASS TC34 Magazine (change to UPPSLAG from Rialto) — MEDIAHOUSE - User perform CASS POST API
- CASS TC34 Magazine (change to UPPSLAG from Rialto) — MEDIAHOUSE - Refresh basket lookup after Rialto update
- CASS TC35 Magazine (change Date Size & Placement from Rialto) — MEDIAHOUSE - User perform CASS POST API
- CASS TC35 Magazine (change Date Size & Placement from Rialto) — MEDIAHOUSE - Refresh basket lookup after Rialto update
- CASS TC37 - 2 Products Magazine (changes the size in MH) — MEDIAHOUSE - User connect and authenticate
- CASS TC4 Change Placement — User perform CASS POST API

**Failure Pattern:**
`Basket not found for campaign: TestCase3X expected [false] but found [true]`

**Evidence:**
- TC31: `Basket not found for campaign: TestCase31 expected [false] but found [true]`
- TC32: `Basket not found for campaign: TestCase32 expected [false] but found [true]`
- TC34: `Basket not found for campaign: TestCase34 expected [false] but found [true]`
- TC35: `Basket not found for campaign: TestCase35 expected [false] but found [true]`; then re-check `Basket not found for campaign: TestCase34` (possibly stale campaign ID)
- TC37: `Basket not found for campaign: TestCase37 expected [false] but found [true]`
- TC4: `Basket not found for campaign: TestCase04 expected [false] but found [true]`

**Impact:** 9 failures
**Confidence:** High

---

## Root Cause 2: Undefined Path Parameter `mhBasketOrderId` (Cascading from Basket Not Found)

**Affected Features:**
- rialtoB2A CASS Magazine scenarios (all basket-not-found TCs)

**Affected Scenarios:**
- CASS TC31 Magazine — MEDIAHOUSE - Verify original full-page order state - #1.1
- CASS TC31 Magazine — MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1
- CASS TC32 Magazine — MEDIAHOUSE - Verify original magazine order state - #1.1
- CASS TC32 Magazine — MEDIAHOUSE - Verify updated magazine order state - #1.1
- CASS TC34 Magazine — MEDIAHOUSE - Verify original magazine order state - #1.1
- CASS TC34 Magazine — MEDIAHOUSE - Verify updated magazine order state - #1.1
- CASS TC35 Magazine — MEDIAHOUSE - Verify original magazine order state - #1.1
- CASS TC35 Magazine — MEDIAHOUSE - Verify updated magazine order state - #1.1
- CASS TC37 - 2 Products Magazine — MEDIAHOUSE - Verify original order state - #1.1
- CASS TC37 - 2 Products Magazine — MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1
- CASS TC4 Change Placement — User perform CASS GET API - #1.1 (x2)

**Failure Pattern:**
`Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: mhBasketOrderId.`

**Evidence:**
- All GET/verify steps that depend on basket lookup fail because `mhBasketOrderId` was never stored (basket was not found in the preceding POST step).
- TC37 additionally: `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`

**Impact:** 12 failures (cascade from Root Cause 1)
**Confidence:** High

---

## Root Cause 3: Incorrect Discount / Price Values in Rialto API Response

**Affected Features:**
- rialtoB2A CASS print scenarios

**Affected Scenarios:**
- CASS TC4 Change Placement — User perform CASS POST API - #1.1
- CASS TC5 change to Uppslag/Spread/Panorama — User perform CASS POST API - #1.1
- CASS TC7 Change Date, Size & Placement — User perform CASS POST API - #1.1
- CASS TC9 change size from Rialto — User perform CASS POST API - #1.1
- CASS TC9 change size from Rialto — User perform CASS GET API - #1.1

**Failure Pattern:**
`discountAmount expected [0.0] but found [63660.63]` / `priceGross expected [250000.0] but found [192192.0]`

**Evidence:**
- TC4: `discountAmount expected [0.0] found [63660.63], priceGross expected [250000.0] found [192192.0]`
- TC5: `discountAmount expected [0.0] found [63660.63], priceGross expected [250000.00] found [192192.0]`
- TC7: `discountAmount expected [0.0] found [63660.63], priceGross expected [1090.0] found [192192.0]`
- TC9: `discountAmount expected [0.0] found [38197.97]`, `priceNetExComm expected [115320.00] found [77122.03]`
- The value `192192.0` appears consistently across TC4/TC5/TC7 — possibly a shared discount calculation returning the wrong net amount.

**Impact:** 5 failures
**Confidence:** High

---

## Root Cause 4: Array Ordering Mismatch in Multi-Product CASS Responses

**Affected Features:**
- rialtoB2A CASS multi-product scenarios

**Affected Scenarios:**
- CASS TC15 2 products change date MH on head order line — User perform CASS GET API - #1.1
- CASS TC15 2 products change date MH on head order line — User perform CASS POST API - #1.1
- CASS TC19 2 products change placement on head order from MH — User perform CASS POST API - #1.1
- CASS TC22 in MH change from Full page to uppslag — User perform CASS GET API - #1.1 (x3)
- CASS TC24 in MH change from uppslag to Full page — Verify reverted MediaHouse basket state - #1.1

**Failure Pattern:**
`paCode expected [[SVDTI, AB]] but found [[AB, SVDTI]]` — element ordering in arrays is non-deterministic

**Evidence:**
- TC15 GET: `paCode expected [[SVDTI, AB]] found [[AB, SVDTI]]`, `prodCode expected [[SVD, AB]] found [[AB, SVD]]`
- TC15 POST: `packageId expected [[AB, SVD]] found [[SVD, AB]]`
- TC19 POST: same `packageId` order mismatch
- TC22: six-element array `[SVDTI, AB, SVDTI, AB, AB, SVDTI]` vs `[AB, SVDTI, AB, AB, SVDTI, SVDTI]`

**Impact:** 8 failures
**Confidence:** High

---

## Root Cause 5: Incorrect `netAmount` Values in Multi-Product Scenarios

**Affected Features:**
- rialtoB2A CASS multi-product change scenarios

**Affected Scenarios:**
- CASS TC22 in MH change from Full page to uppslag — User perform CASS GET API - #1.1 (netAmount)
- CASS TC23 in MH change from Full page to uppslag - two orderlines change — Verify updated MediaHouse basket state - #1.1
- CASS TC23 in MH change from Full page to uppslag - two orderlines change — Verify reverted MediaHouse basket state - #1.1

**Failure Pattern:**
`netAmount expected [[128531.37, 33159.8, ...]] but found [[192192.0, 158000.0, ...]]`

**Evidence:**
- TC22: `netAmount expected [128531.37, ...] found [192192.0, ...]`
- TC23 updated: `netAmount expected [300000.0, 300000.0, 128531.37, ...] found [300000.0, 300000.0, 128531.37, ...]` (partial mismatch in later positions)
- TC23 reverted: `netAmount expected [33159.8, 128531.37, ...] found [158000.0, 128531.37, ...]`

**Impact:** 3 failures
**Confidence:** Medium (possibly same root cause as RC3 — discount/price calculation error)

---

## Root Cause 6: Missing `PRELIMINARY` statusFlag in Magazine Orders

**Affected Features:**
- rialtoB2A CASS Magazine scenarios

**Affected Scenarios:**
- CASS TC28 Magazine (change size) — RIALTO - Verify Rialto reflects the reverted full-page state - #1.1
- CASS TC29 Magazine (change to Uppslag/Spread/Panorama) — RIALTO - Verify Rialto reflects the reverted full-page state - #1.1

**Failure Pattern:**
`orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

**Evidence:**
- TC28: `statusFlags expected [[PRELIMINARY]] but found [[]]`
- TC29: `statusFlags expected [[PRELIMINARY]] but found [[]]`
- Both are "revert" verification steps, suggesting the revert operation does not re-set the PRELIMINARY flag.

**Impact:** 2 failures
**Confidence:** High

---

## Root Cause 7: Incorrect Placement / Product Data in Magazine Scenarios (TC33, TC36, TC37)

**Affected Features:**
- rialtoB2A CASS Magazine scenarios

**Affected Scenarios:**
- CASS TC33 Magazine (change size from Rialto) — MEDIAHOUSE - Verify updated magazine order state - #1.1
- CASS TC36 Magazine (change Product Size Placement & Date from Rialto) — MEDIAHOUSE - Verify original magazine order state - #1.1
- CASS TC36 Magazine (change Product Size Placement & Date from Rialto) — MEDIAHOUSE - Verify updated magazine order state - #1.1
- CASS TC37 - 2 Products Magazine — RIALTO - Verify Rialto reflects the updated state - #1.1

**Failure Pattern:**
Placement code / product code mismatch between expected and actual state

**Evidence:**
- TC33: `plaCode expected [HALVLIGG] found [TEXT]`, `depth expected [146] found [297]`
- TC36 original: `orderDiscount expected [3600.00] found [4800.00]`
- TC36 updated: `paCode expected [ANA] found [KOT]`, `plaCode expected [HALVLIGG] found [SIDAN]`
- TC37: `placementId expected [HALVLIGG, TEXT] found [TEXT, TEXT]`

**Impact:** 5 failures
**Confidence:** Medium (possibly test data or sync issue between Rialto and MediaHouse)

---

## Root Cause 8: Redundant / Undefined Path Parameters (TC24, TC6)

**Affected Features:**
- rialtoB2A CASS print scenarios

**Affected Scenarios:**
- CASS TC24 in MH change from uppslag to Full page — Verify Rialto reflects the reverted full-page state - #1.1
- CASS TC6 change date and size — User perform CASS POST API - #1.1

**Failure Pattern:**
Path parameter configuration error / decimal format mismatch

**Evidence:**
- TC24: `Redundant path parameters are: agencyPrisaId=7741. Undefined path parameters are: uuid.`
- TC6: `priceNetExComm expected [115320.00] but found [115320.0]` — trailing zero formatting difference

**Impact:** 2 failures
**Confidence:** High (TC24 = step config bug; TC6 = decimal format assertion strictness)
