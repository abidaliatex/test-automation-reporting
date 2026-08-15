# Build 172 — Root Cause Analysis

**Source Report:** [build-172.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-172.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-15 22:43:18 UTC

---

## Build Summary

| Metric | Value |
|--------|-------|
| Build | 172 |
| Total Tests | 514 |
| Passed | 488 |
| Failed | 26 |
| Pass Rate | 94.9% |

---

## Root Cause Groups

---

## 1. Unexpected Discount Applied on Size / Uppslag Change

**Affected Features:**
- rialtoB2A(CASS TC5 change to Uppslag/Spread/Panorama)
- rialtoB2A(CASS TC9 change size from Rialto)

**Affected Scenarios:**
- User perform CASS POST API — CASS TC5 change to Uppslag/Spread/Panorama
- User perform CASS POST API — CASS TC9 change size from Rialto
- User perform CASS GET API — CASS TC9 change size from Rialto

**Failure Pattern:**
`discountAmount` expected `[0.0]` but found `[63660.63]` / `[38197.97]`; corresponding `priceNetExComm` and `priceGross` values are lower than expected because an unexpected discount is being deducted.

**Evidence:**
- TC5 POST: `discountAmount expected [0.0] found [63660.63]`, `priceGross expected [250000.00] found [192192.0]`, `priceNetExComm expected [250000.00] found [128531.37]`
- TC9 POST: `discountAmount expected [0.0] found [38197.97]`, `priceNetExComm expected [115320.00] found [77122.03]`
- TC9 GET: `depth expected [184] found [372]`, `netAmount expected [115320.0] found [128531.37]` — dimension not updated, pricing cascade mismatch

**Impact:** 3 failures across 2 scenarios
**Confidence:** High

---

## 2. Print Detail Array Order Non-Deterministic (Multi-Product)

**Affected Features:**
- rialtoB2A(CASS TC15 2 products change date MH on head order line)
- rialtoB2A(CASS TC22 in MH change from Full page to uppslag)
- rialtoB2A(CASS TC23 in MH change from Full page to uppslag - two orderlines change)
- rialtoB2A(CASS TC24 in MH change in MH change from uppslag to Full page)

**Affected Scenarios:**
- User perform CASS GET API — CASS TC15 (2 products change date MH on head order line)
- User perform CASS POST API — CASS TC15 (2 products change date MH on head order line)
- User perform CASS GET API — CASS TC22 (in MH change from Full page to uppslag) × 3
- Verify updated MediaHouse basket state — CASS TC23
- Verify reverted MediaHouse basket state — CASS TC23
- Verify reverted MediaHouse basket state — CASS TC24

**Failure Pattern:**
Arrays for `paCode`, `prodCode`, `issueDate`, `packageId`, `productId` returned in reversed or shuffled order relative to expected. Values are correct but position differs.

**Evidence:**
- TC15 GET: `paCode expected [[SVDTI, AB]] found [[AB, SVDTI]]`; `issueDate expected [[2026-12-21, 2026-12-01]] found [[2026-12-01, 2026-12-21]]`
- TC22 GET: `paCode expected [[SVDTI, AB, SVDTI, AB, AB, SVDTI]] found [[AB, SVDTI, AB, AB, SVDTI, SVDTI]]`
- TC23: `netAmount expected [[...33159.8...]] found [[...33159.8...]]` — rounding discrepancy also present (`33159.79999...` vs `33159.8`)
- TC24: `plaCode expected [[TEXT×6]] found [[TEXT, UPPSLAG×5]]` — revert did not restore placement

**Impact:** 9 failures across 4 scenarios
**Confidence:** High

---

## 3. PRELIMINARY Status Flag Missing After Revert

**Affected Features:**
- rialtoB2A(CASS TC4 Change Placement)
- rialtoB2A(CASS TC28 Magazine (change size))
- rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama))

**Affected Scenarios:**
- User perform CASS POST API — CASS TC4 Change Placement
- RIALTO - Verify Rialto reflects the reverted full-page state — CASS TC28 Magazine (change size)
- RIALTO - Verify Rialto reflects the reverted full-page state — CASS TC29 Magazine (change to Uppslag/Spread/Panorama)

**Failure Pattern:**
`orderHeader.statusFlags` expected `[PRELIMINARY]` but found `[]` — Rialto does not flag the order as preliminary after a revert or change operation.

**Evidence:**
- TC4 POST: `statusFlags expected [[PRELIMINARY]] found [[]]`
- TC28 RIALTO revert check: `statusFlags expected [[PRELIMINARY]] found [[]]`
- TC29 RIALTO revert check: `statusFlags expected [[PRELIMINARY]] found [[]]`

**Impact:** 3 failures across 3 scenarios
**Confidence:** High

---

## 4. Magazine Pricing / Commission Calculation Errors

**Affected Features:**
- rialtoB2A(CASS TC31 Magazine (change Date, Size & Placement))
- rialtoB2A(CASS TC36 Magazine (change Product Size Placement & Date from Rialto))
- rialtoB2A(CASS TC37 - 2 Products Magazine - changes the size in MH)

**Affected Scenarios:**
- RIALTO - Verify Rialto reflects the reverted full-page state — CASS TC31
- MEDIAHOUSE - Verify original magazine order state — CASS TC36
- MEDIAHOUSE - Verify updated magazine order state — CASS TC36
- MEDIAHOUSE - Verify original order state in MediaHouse — CASS TC37
- MEDIAHOUSE - Verify updated MediaHouse basket state — CASS TC37
- RIALTO - Verify Rialto reflects the updated state — CASS TC37

**Failure Pattern:**
Commission and discount amounts are computed incorrectly for magazine orders. `priceNet` / `commissionAmount` / `orderDiscount` differ from expected; `PRELIMINARY` statusFlag missing in TC37.

**Evidence:**
- TC31: `priceNet expected [5000.0] found [4845.0]`, `commissionAmount expected [0.0] found [155.0]`
- TC36 original: `orderDiscount expected [3600.00] found [4800.00]`, `netPrice expected [2400.00] found [1200.00]`
- TC36 updated: `orderDiscount expected [0.00] found [4000.00]`, `netPrice expected [5000.00] found [1000.00]`
- TC37 original: `totalInclVat expected [7368.00] found [5814.00]`, `vat expected [[2913.60]] found [[1162.80]]`
- TC37 updated: `commission expected [234.40] found [229.40]`, `totalInclVat expected [9734.00] found [8963.25]`

**Impact:** 6 failures across 3 scenarios
**Confidence:** High

---

## 5. TC24 Transaction Rollback / Path Parameter Error

**Affected Features:**
- rialtoB2A(CASS TC24 in MH change in MH change from uppslag to Full page)

**Affected Scenarios:**
- Revert two MediaHouse order lines to full page — CASS TC24
- Verify Rialto reflects the reverted full-page state — CASS TC24

**Failure Pattern:**
Server returns HTTP 500 (`Transaction rolled back because it has been marked as rollback-only`) on the revert call; subsequent Rialto verification fails because `uuid` path parameter is undefined while `agencyPrisaId` is redundant.

**Evidence:**
- TC24 Revert: `500 Transaction rolled back...`, `expected [N200] found [N400]`
- TC24 Rialto check: `Redundant path parameters: agencyPrisaId=7778. Undefined path parameters: uuid`

**Impact:** 2 failures (cascaded from rollback)
**Confidence:** High

---

## 6. TC35 Basket ID / Placement Mismatch

**Affected Features:**
- rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto))

**Affected Scenarios:**
- RIALTO - Verify updated Agency order after Rialto change — CASS TC35
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse — CASS TC35

**Failure Pattern:**
After Rialto triggers a change, the expected placement (`SIDAN2`) and date (`2026-08-05`) do not match what was saved; additionally the MH basket ID (`orBoxid=7788`) differs from the Agency Prisa ID (`7789`), indicating a data synchronisation mismatch.

**Evidence:**
- TC35 Rialto: `placementId expected [SIDAN2] found [HALVLIGG]`, `issueDate expected [2026-08-05] found [2026-08-12]`, `depth expected [297] found [146]`
- TC35 MH: `INTEGRATION MISMATCH: MH basket ID (orBoxid) [7788] does not match Agency Prisa ID [7789]`

**Impact:** 2 failures
**Confidence:** Medium

---

## 7. TC6 Numeric Format / Precision Mismatch

**Affected Features:**
- rialtoB2A(CASS TC6 change to changes the date and the size on the order line.)

**Affected Scenarios:**
- User perform CASS POST API — CASS TC6

**Failure Pattern:**
Numeric fields serialised as integer-style (`115320.0`) instead of decimal (`115320.00`), and `priceNet` slightly lower than expected (`111745.08` vs `115320.00`), possibly due to a commission deduction being applied unexpectedly.

**Evidence:**
- TC6 POST: `priceNetExComm expected [115320.00] found [115320.0]`, `priceNet expected [115320.00] found [111745.08]`

**Impact:** 1 failure
**Confidence:** Medium
