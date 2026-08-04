# Investigation — Build 161

**Source Report:** [build-161.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-161.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Build:** 161 | **Date:** 2026-08-04 21:03:15 UTC | **Status:** UNSTABLE

---

## Build Summary

Build: 161
Total Tests: 514
Passed: 459
Failed: 55
Pass Rate: 89.3%

---

## Root Cause Groups

---

## Root Cause 1 — `discountType` Incorrectly Set to `RIALTO` Instead of `null` / `NONE`

**Affected Features:**
- CASS TC11 change to UPPSLAG from Rialto
- CASS TC15 2 products change date MH on head order line
- CASS TC37 - 2 Products Magazine - changes the size in MH
- CASS TC4 Change Placement
- CASS TC27 Magazine (change date)

**Affected Scenarios:**
- User perform CASS GET API — discountType null mismatch (TC11)
- User perform CASS GET API — discountType null/null mismatch (TC15)
- MEDIAHOUSE - Verify original order state in MediaHouse (TC37)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC37)
- User perform CASS GET API — discountType NONE mismatch (TC4)
- MEDIAHOUSE - Verify updated MediaHouse basket state — discountType RIALTO vs NONE (TC27)

**Failure Pattern:**
`orders[0].printDetails.discountType expected [[null]] but found [[RIALTO]]`
`orders.printDetails.discountType expected [[null, null]] but found [[RIALTO, RIALTO]]`
`discountType expected [[NONE]] but found [[RIALTO]]`

**Evidence:**
- TC11 GET: `discountType expected [[null]] but found [[RIALTO]]`
- TC15 GET: `discountType expected [[null, null]] but found [[RIALTO, RIALTO]]`
- TC4 GET: `discountType expected [[NONE]] but found [[RIALTO]]`
- TC27 MH basket: `discountType expected [[RIALTO]] but found [[NONE]]` (inverted — RIALTO not applied when expected)
- TC37 original state: `discountType expected [[null, null]] but found [[RIALTO, RIALTO]]`

**Impact:** 6 failures

**Confidence:** High — consistent pattern across multiple test cases; `discountType` field is being populated with `RIALTO` for orders where no Rialto discount should apply (or vice versa for TC27).

---

## Root Cause 2 — `orderHeader.statusFlags` Missing `PRELIMINARY` Flag

**Affected Features:**
- CASS TC1 and TC2
- CASS TC3 change Size
- CASS TC4 Change Placement
- CASS TC5 change to Uppslag/Spread/Panorama
- CASS TC6 change date and size on order line

**Affected Scenarios:**
- User perform CASS POST API (TC1/TC2)
- User perform CASS POST API (TC3)
- User perform CASS POST API (TC4)
- User perform CASS POST API (TC5)
- User perform CASS POST API (TC6)

**Failure Pattern:**
`orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

**Evidence:**
- TC1: `statusFlags expected [[PRELIMINARY]] but found [[]]`
- TC3: `statusFlags expected [[PRELIMINARY]] but found [[]]`
- TC4: `statusFlags expected [[PRELIMINARY]] but found [[]]`
- TC5: `statusFlags expected [[PRELIMINARY]] but found [[]]`
- TC6: `statusFlags expected [[PRELIMINARY]] but found [[]]`

**Impact:** 5 failures (within broader POST API failures)

**Confidence:** High — same field missing across all basic order mutation scenarios; possibly a regression in order state management.

---

## Root Cause 3 — Magazine `orderDiscount` / `sumDiscount` Unexpectedly Non-Zero

**Affected Features:**
- CASS TC26 Basic order for magazines
- CASS TC32 Magazine (change date from Rialto)
- CASS TC33 Magazine (change size from Rialto)
- CASS TC34 Magazine (change to UPPSLAG from Rialto)
- CASS TC35 Magazine (change Date Size & Placement from Rialto)
- CASS TC36 Magazine (change Product Size Placement & Date from Rialto)
- CASS TC31 Magazine (change Date, Size & Placement)

**Affected Scenarios:**
- Verify reverted MediaHouse basket state (TC26)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC32)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC33)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC34)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse (TC35)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse (TC36)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC36)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse (TC31)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC31)

**Failure Pattern:**
`orderBasketPriceSummary.orderDiscount expected [0.00] but found [3600.00]`
`orderBasketPriceSummary.sumDiscount expected [0.00] but found [3600.00]`

**Evidence:**
- TC26: `orderDiscount expected [0.00] found [3600.00]`, `sumDiscount expected [0.00] found [3600.00]`
- TC32: same pattern — `orderDiscount [0.00] found [3600.00]`
- TC33: `orderDiscount [0.00] found [4000.00]`
- TC34: `orderDiscount [0.00] found [8800.00]`
- TC35/TC36: `orderDiscount expected [3600.00] found [4800.00]`

**Impact:** 9 failures

**Confidence:** High — discount unexpectedly applied (or wrong amount) on magazine orders across all Rialto-originated change flows. Possibly a pricing rule or discount flag regression in the magazine order processing path.

---

## Root Cause 4 — Magazine Commission / Price Calculation Mismatch

**Affected Features:**
- CASS TC28 Magazine (change size)
- CASS TC30 Magazine (change Date & Size)
- CASS TC31 Magazine (change Date, Size & Placement)
- CASS TC35 Magazine (change Date Size & Placement from Rialto)

**Affected Scenarios:**
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC28)
- RIALTO - Verify Rialto reflects reverted full-page state (TC28)
- RIALTO - Verify Rialto reflects reverted full-page state (TC30)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC31)
- RIALTO - Verify Rialto reflects reverted full-page state (TC31)
- RIALTO - Verify updated Agency order after Rialto change (TC35)

**Failure Pattern:**
`orderBasketPriceSummary.commission expected [155.00] but found [250.00]`
`orderAdDetails.priceNet expected [[4845.0]] but found [[4969.0]]`
`orderAdDetails.commissionAmount expected [[155.0]] but found [[31.0]]`

**Evidence:**
- TC28 MH basket: `commission expected [155.00] found [250.00]`, `orderbasketSum expected [4845.00]`
- TC28 Rialto: `priceNet expected [[4845.0]] found [[4969.0]]`, `commissionAmount expected [[155.0]] found [[31.0]]`
- TC30 Rialto: `priceNet expected [[6000.0]] found [[5962.8]]`, `commissionAmount expected [[0.0]] found [[37.2]]`
- TC31: commission/priceNet wrong values

**Impact:** 6 failures

**Confidence:** High — commission computation inconsistent between Rialto and MediaHouse for magazine size/date change scenarios.

---

## Root Cause 5 — Floating-Point Precision Mismatches in Price Fields

**Affected Features:**
- CASS TC11 change to UPPSLAG from Rialto
- CASS TC14 change Product, Size, Placement & Date from Rialto
- CASS TC15 2 products change date MH on head order line
- CASS TC21 2 products change from draft to reserved
- CASS TC23 in MH change from Full page to uppslag (two orderlines)
- CASS TC24 in MH change from uppslag to Full page

**Affected Scenarios:**
- User perform CASS POST API — priceNetExComm precision (TC11)
- User perform CASS POST API — priceNetExComm precision (TC14, #1)
- User perform CASS POST API — priceNet precision (TC14, #2)
- User perform CASS POST API — priceNetExComm precision (TC15)
- User perform CASS POST API — priceNet precision (TC21, #1 and #2)
- Verify created Rialto order — priceNet precision (TC23)
- Verify created Rialto order — priceNet precision (TC24)

**Failure Pattern:**
`priceNetExComm expected [66451.59999999998] but found [66451.6]`
`priceNet expected [32131.849999999988] but found [32131.85]`

**Evidence:**
- TC11: `priceNetExComm expected [66451.59999999998] found [66451.6]`
- TC14: `priceNetExComm expected [38140.399999999994] found [38140.4]`
- TC21: `priceNet expected [32131.849999999988] found [32131.85]`
- TC23: `priceNet expected [32131.849999999988] found [32131.85]`

**Impact:** 7 failures

**Confidence:** High — test data contains raw floating-point values that differ from rounded API responses by rounding only; test assertions may need updating to use approximate comparisons or the API is now rounding differently.

---

## Root Cause 6 — Order Line Sequencing / Ordering Mismatch (`paCode`, `packageId`, `productId`)

**Affected Features:**
- CASS TC15 2 products change date MH on head order line
- CASS TC23 in MH change from Full page to uppslag (two orderlines)
- CASS TC24 in MH change from uppslag to Full page

**Affected Scenarios:**
- User perform CASS POST API — packageId/productId ordering (TC15)
- Verify updated MediaHouse basket state — paCode ordering (TC23)
- Verify reverted MediaHouse basket state — paCode ordering (TC23)
- Verify reverted MediaHouse basket state — paCode ordering (TC24)

**Failure Pattern:**
`orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]`
`orders.printDetails.paCode expected [[SVDTI, SVDTI, AB, AB, AB, SVDTI]] but found [[AB, AB, AB, SVDTI, SVDTI, SVDTI]]`

**Evidence:**
- TC15: `packageId expected [[AB, SVD]] found [[SVD, AB]]`
- TC23 updated: `paCode expected [[SVDTI, SVDTI, AB, AB, AB, SVDTI]] found [[AB, AB, AB, SVDTI, SVDTI, SVDTI]]`
- TC24 reverted: `paCode expected [[SVDTI, AB, SVDTI, AB, AB, SVDTI]] found [[SVDTI, SVDTI, SVDTI, AB, AB, AB]]`

**Impact:** 4 failures

**Confidence:** High — consistent ordering reversal pattern; possibly a change in sort/grouping of order lines returned by the API.

---

## Root Cause 7 — Server Error 500 (Transaction Rolled Back)

**Affected Features:**
- CASS TC18 2 products change size on not registered as head order line
- CASS TC23 in MH change from Full page to uppslag (two orderlines)

**Affected Scenarios:**
- User perform CASS POST API (#1) (TC18)
- Revert two MediaHouse order lines to full page (TC23)

**Failure Pattern:**
`500: Transaction rolled back because it has been marked as rollback-only`

**Evidence:**
- TC18: `500 "Transaction rolled back because it has been marked as rollback-only"`
- TC23 Revert: `500 "Transaction rolled back because it has been marked as rollback-only"`

**Impact:** 2 failures (plus cascading downstream steps)

**Confidence:** High — server-side exception during write operations; likely a backend bug triggered by specific order state combinations.

---

## Root Cause 8 — `totalOrderNetPrice` Gross Calculation Error (TC22)

**Affected Features:**
- CASS TC22 in MH change from Full page to uppslag

**Affected Scenarios:**
- User perform CASS GET API — totalOrderNetPrice mismatch (TC22, #1)
- User perform CASS GET API — printDetails.netAmount mismatch (TC22, #2 and #3)

**Failure Pattern:**
`orders[0].totalOrderNetPrice expected [485073.51] but found [1073973.00]`

**Evidence:**
- TC22 GET #1: `totalOrderNetPrice expected [485073.51] found [1073973.00]` — value is more than double expected
- TC22 GET #2/#3: `printDetails.netAmount` values differ (e.g. `158000.0` instead of `33159.8`)

**Impact:** 3 failures

**Confidence:** High — total price ~2.2x expected; possibly order lines being double-counted or a price summation bug for multi-line uppslag orders.

---

## Root Cause 9 — Integration Mismatch: MH Basket ID ≠ Agency Prisa ID / Path Parameter Error

**Affected Features:**
- CASS TC35 Magazine (change Date Size & Placement from Rialto)
- CASS TC24 in MH change from uppslag to Full page

**Affected Scenarios:**
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC35)
- Verify Rialto reflects the reverted full-page state (TC24)

**Failure Pattern:**
`INTEGRATION MISMATCH: MH basket ID (orBoxid) [7284] does not match Agency Prisa ID [7285]`
`Redundant path parameters: agencyPrisaId=7272. Undefined path parameters: uuid`

**Evidence:**
- TC35: `MH basket ID [7284] ≠ Agency Prisa ID [7285]` — IDs are off by 1; ID synchronisation between systems broken
- TC24: path parameter `uuid` undefined but `agencyPrisaId` present — API call mis-configured after a revert step

**Impact:** 2 failures

**Confidence:** Medium — TC35 may indicate a data sync timing issue; TC24 path parameter error suggests a test data or API URL configuration regression.

---

## Summary

| Root Cause | Failures | Confidence |
|---|---|---|
| discountType incorrectly set to RIALTO / wrong value | 6 | High |
| statusFlags PRELIMINARY missing | 5 | High |
| Magazine orderDiscount/sumDiscount unexpected non-zero | 9 | High |
| Magazine commission/price calculation mismatch | 6 | High |
| Floating-point precision mismatches | 7 | High |
| Order line sequencing/ordering mismatch | 4 | High |
| 500 Transaction rolled back | 2 | High |
| totalOrderNetPrice gross calculation error | 3 | High |
| Integration ID mismatch / path parameter error | 2 | Medium |

**Total accounted failures: 44 direct + 11 cascading = 55**
