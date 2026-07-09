# Root Cause Analysis — Build #133

**Source Report:** [build-133.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-133.md)

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #133
Date: 2026-07-09 21:03 UTC
Status: UNSTABLE
Total Tests: 513
Passed: 427
Failed: 86
Pass Rate: 83.2%

---

## Root Cause Groups

---

## 1. discountType Not Propagated from Rialto

**Affected Features:**
- rialtoB2A_CASS_print_orders.feature (TC3, TC4, TC5, TC9, TC11, TC14, TC15, TC22, TC23, TC24, TC26)
- rialtoB2A_CASS_magazine_orders.feature (TC27, TC28, TC30, TC31, TC32, TC33, TC34, TC35, TC36)

**Affected Scenarios:**
- User perform CASS GET API – CASS TC3 change Size
- User perform CASS GET API – CASS TC4 Change Placement
- User perform CASS GET API – CASS TC5 change to Uppslag/Spread/Panorama
- User perform CASS GET API – CASS TC9 change size from Rialto (×2)
- User perform CASS GET API – CASS TC11 change to UPPSLAG from Rialto
- User perform CASS GET API – CASS TC14 change Product, Size, Placement & Date from Rialto (×2)
- User perform CASS GET API – CASS TC15 2 products change date MH on head order line (×2)
- User perform CASS GET API – CASS TC22 in MH change from Full page to uppslag (×3)
- Verify original/updated/reverted MH basket state – CASS TC23 in MH change from Full page to uppslag (×3)
- Verify original/updated/reverted MH basket state – CASS TC24 in MH change from uppslag to Full page (×3)
- Verify reverted MediaHouse basket state – CASS TC26 Basic order for magazines
- MEDIAHOUSE - Verify original full-page order state in MediaHouse – CASS TC27 Magazine (change date)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse – CASS TC28 Magazine (change size)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse – CASS TC30 Magazine (change Date & Size)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse – CASS TC31 Magazine (change Date, Size & Placement)
- MEDIAHOUSE - Verify original/updated magazine order state – CASS TC32 Magazine (change date from Rialto) (×2)
- MEDIAHOUSE - Verify original/updated magazine order state – CASS TC33 Magazine (change size from Rialto) (×2)
- MEDIAHOUSE - Verify original/updated magazine order state – CASS TC34 Magazine (change to UPPSLAG from Rialto) (×2)
- MEDIAHOUSE - Verify original magazine order state – CASS TC35 Magazine (change Date Size & Placement from Rialto)
- MEDIAHOUSE - Verify original/updated magazine order state – CASS TC36 Magazine (change Product Size Placement & Date from Rialto) (×2)

**Failure Pattern:**
`orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`

**Evidence:**
- TC11: `Mismatch on field: orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`
- TC14: `Mismatch on field: orders[0].printDetails.discountType expected [[RIALTO, RIALTO, RIALTO, RIALTO]] but found [[null, null, null, null]]`
- TC32/TC33/TC34: Consistently `discountType expected [[RIALTO]] found [[null]]` across all magazine order state verifications
- Affects both Newspaper (TC3–TC26) and Magazine (TC26–TC36) test scenarios — indicates a cross-cutting regression

**Impact:** 33 failures

**Confidence:** High

---

## 2. MediaHouse Order Line Retrieval Failure

**Affected Features:**
- rialtoB2A_CASS_MH_2product_orders.feature (TC16, TC17, TC18, TC19, TC20)
- rialtoB2A_CASS_magazine_orders.feature (TC29)

**Affected Scenarios:**
- User perform CASS GET API – CASS TC16 2 products change date on non-head order line from MH
- User perform CASS POST API – CASS TC16 (cascading: No MH odIds found)
- User perform CASS GET API – CASS TC17 2 products change size on head order line from MH
- User perform CASS POST API – CASS TC17 (cascading: No MH odIds found)
- User perform CASS GET API – CASS TC18 2 products change size on non-head order line from MH
- User perform CASS POST API – CASS TC18 (cascading: No MH odIds found)
- User perform CASS GET API – CASS TC19 2 products change placement on head order from MH
- User perform CASS POST API – CASS TC19 (cascading: No MH odIds found)
- User perform CASS GET API – CASS TC20 2 products change placement order for non head from MH
- User perform CASS POST API – CASS TC20 (cascading: No MH odIds found)
- MEDIAHOUSE - Update two MediaHouse order lines to uppslag – CASS TC29 Magazine (change to Uppslag/Spread/Panorama)

**Failure Pattern:**
`Index 13 out of bounds for length 13` → `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`

**Evidence:**
- TC16–TC20 all fail on GET with identical `Index 13 out of bounds for length 13` — the 14th order line is expected but the response only has 13 entries
- The failed GET step means `TestContext` is never populated with MH odIds, causing every subsequent POST step to fail with: `No MH odIds found in TestContext`
- All 5 two-product MH scenarios fail identically — points to a systemic data or API response change (possibly one fewer order line returned by the MH API)

**Impact:** 11 failures

**Confidence:** High

---

## 3. Pricing / Financial Calculation Discrepancy

**Affected Features:**
- rialtoB2A_CASS_print_orders.feature (TC3, TC5, TC9, TC11, TC15)
- rialtoB2A_CASS_magazine_orders.feature (TC27, TC28, TC30, TC31, TC35, TC37)

**Affected Scenarios:**
- User perform CASS GET API – CASS TC3 change Size
- User perform CASS GET API / POST API – CASS TC5 change to Uppslag/Spread/Panorama
- User perform CASS POST API – CASS TC9 change size from Rialto
- User perform CASS GET API – CASS TC11 change to UPPSLAG from Rialto
- User perform CASS POST API – CASS TC15 2 products change date MH on head order line
- RIALTO - Verify created Rialto order – CASS TC27 Magazine (change date)
- RIALTO - Verify created Rialto order / MEDIAHOUSE - Verify updated MH state / Verify reverted state – CASS TC28 Magazine (change size)
- RIALTO - Verify reverted full-page state – CASS TC30 Magazine (change Date & Size)
- MEDIAHOUSE - Verify updated MH state / RIALTO - Verify reverted state – CASS TC31 Magazine (change Date, Size & Placement)
- RIALTO - Verify updated Agency order after Rialto change – CASS TC35 Magazine (change Date Size & Placement from Rialto)
- MEDIAHOUSE - Verify original/updated order state – CASS TC37 2 Products Magazine - changes the size in MH

**Failure Pattern:**
`orderBasketPriceSummary.totalInclVat expected [X] but found [Y]` / `commission` / `netAmount` / `vat` values off

**Evidence:**
- TC11: `totalInclVat expected [169660.46] found [171598.78]`, `vat expected [46664.22] found [47051.88]`
- TC15: `discountAmount expected [[99479.4, 63660.63]] found [[132639.2, 63660.63]]`
- TC37: `totalInclVat expected [7368.00] found [7614.00]`, `vat expected [[2913.60]] found [[2962.80]]`
- TC28/TC30/TC31: commission and orderbasketSum mismatches on reverted states — possibly a rounding or discount-rate change

**Impact:** 16 failures

**Confidence:** Medium

---

## 4. statusFlags PRELIMINARY Not Set

**Affected Features:**
- rialtoB2A_CASS_print_orders.feature (TC1/TC2, TC3, TC4, TC6)
- rialtoB2A_CASS_magazine_orders.feature (TC27)

**Affected Scenarios:**
- User perform CASS POST API – CASS TC1 and TC2
- User perform CASS POST API – CASS TC3 change Size
- User perform CASS POST API – CASS TC4 Change Placement
- User perform CASS POST API – CASS TC6 change to changes the date and the size on the order line
- RIALTO - Verify reverted full-page state – CASS TC27 Magazine (change date)

**Failure Pattern:**
`orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

**Evidence:**
- TC1/TC2: `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`
- TC3, TC4, TC6: Same empty statusFlags on CASS POST validation
- The `PRELIMINARY` status flag is not being set on newly posted orders — may indicate an order state machine regression or missing initialization logic in the B2A integration layer

**Impact:** 5 failures

**Confidence:** High

---

## 5. Order Detail Value / Field Ordering Mismatch

**Affected Features:**
- rialtoB2A_CASS_MH_2product_orders.feature (TC16–TC20 POST steps)
- rialtoB2A_CASS_print_orders.feature (TC22, TC24)
- rialtoB2A_CASS_magazine_orders.feature (TC27, TC29, TC35)

**Affected Scenarios:**
- User perform CASS POST API – CASS TC16 (issueDate mismatch: expected 2026-07-21 found 2026-07-01)
- User perform CASS POST API – CASS TC17 (moduleCode expected [54,58] found [58,58])
- User perform CASS POST API – CASS TC18 (moduleCode expected [58,54] found [58,58])
- User perform CASS POST API – CASS TC19 (packageId/productId expected [AB,SVD] found [SVD,AB])
- User perform CASS POST API – CASS TC20 (placementId expected [TEXT,SIDAN3] found [TEXT,TEXT])
- User perform CASS POST API – CASS TC22 (packageId array order mismatch)
- Revert two MediaHouse order lines to full page / Verify Rialto reflects reverted state – CASS TC24
- MEDIAHOUSE - Update two MH order lines to uppslag – CASS TC27 (issueDate expected 2026-08-19 found 2026-08-26)
- RIALTO - Verify created Rialto order / cascading null context – CASS TC29 (undefined path param agencyPrisaId)
- MEDIAHOUSE - Verify updated magazine order state – CASS TC35 (INTEGRATION MISMATCH: MH basket ID [6149] ≠ Agency Prisa ID [6150])

**Failure Pattern:**
Wrong values or ordering in array fields (`packageId`, `placementId`, `moduleCode`, `issueDate`); integration ID mismatch; missing path parameter `agencyPrisaId`

**Evidence:**
- TC16 POST: `issueDate expected [[2026-07-01, 2026-07-21]] found [[2026-07-01, 2026-07-01]]`
- TC19 POST: `packageId expected [[AB, SVD]] found [[SVD, AB]]` — array element order swapped
- TC29: `Redundant path parameters: uuid=..., Undefined path parameters: agencyPrisaId` — API call configuration bug
- TC35: `MH basket ID (orBoxid) [6149] does not match Agency Prisa ID [6150]` — basket ID desync between systems

**Impact:** 15 failures

**Confidence:** Medium

---

## Affected Components

- **CASS B2A Integration Layer** — discountType propagation, statusFlags initialization
- **MediaHouse API** — order line count change (Index OOB: TC16–TC20), basket ID sync (TC35)
- **Rialto Pricing Engine** — financial calculation discrepancies across print and magazine orders
- **MH/Rialto Path Parameter Handling** — missing `agencyPrisaId` in TC29 request

## Recommended Fix

- Investigate why `discountType` is returning `null` instead of `RIALTO` in the B2A GET response — likely a missing field mapping or regression in the discount propagation service.
- Check if MH API response now returns 13 order lines instead of 14 for 2-product orders — update test data or fix the retrieval index.
- Review order state initialization to ensure `PRELIMINARY` flag is set on POST.
- Verify pricing formula changes — commission and VAT values are consistently off, possibly due to a rate or rounding change.

## Prevention

- Add contract test to assert `discountType` is never `null` for RIALTO-originated orders.
- Guard MH order line retrieval with bounds-checking and a clear test setup error message.
- Pin expected financial values to a known pricing rule version to detect formula changes early.
