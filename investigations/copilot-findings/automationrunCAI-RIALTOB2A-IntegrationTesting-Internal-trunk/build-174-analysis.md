# Investigation: Build 174 — Root Cause Analysis

**Source Report:** [build-174.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-174.md)  
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk  
**Build:** 174  
**Date:** 2026-08-17  
**Status:** UNSTABLE

## Summary

---

## Build Summary

Build: 174  
Total Tests: 514  
Passed: 484  
Failed: 30  
Pass Rate: 94.2%

---

## Root Cause

## Root Cause Groups

## Multi-line mapping/order mismatches in print/order details

**Affected Features:**
- rialtoB2A(CASS TC14 change Product, Size, Placement & Date from Rialto)
- rialtoB2A(CASS TC15 2 products change date MH on head order line)
- rialtoB2A(CASS TC18/TC19/TC20/TC22/TC23/TC24)
- rialtoB2A(CASS TC37 - 2 Products Magazine - changes the size in MH)

**Affected Scenarios:**
- User perform CASS GET API - #1.1 (TC14)
- User perform CASS GET API - #1.1 (TC15)
- User perform CASS POST API - #1.1 (TC18)
- User perform CASS POST API - #1.1 (TC19)
- User perform CASS POST API - #1.1 (TC20)
- User perform CASS GET API - #1.1 (TC22, 3 failures)
- Verify updated MediaHouse basket state - #1.1 (TC23)
- Verify reverted MediaHouse basket state - #1.1 (TC23)
- Revert two MediaHouse order lines to full page - #1.1 (TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC24)
- RIALTO - Verify Rialto reflects the updated state - #1.1 (TC37)

**Failure Pattern:**
`paCode/prodCode/packageId/productId/placementId` values are present but incorrect in order or mapped to wrong line/item.

**Evidence:**
- `orders[0].printDetails.paCode expected [[SVDTI, AB]] but found [[AB, SVDTI]]` (TC15)
- `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]` (TC19)
- `body.orderAdDetailUpdates.placementId expected [[TEXT,...]] but found [[UPPSLAG,...]]` (TC24)

**Impact:** 13 failures

**Confidence:** High

## Pricing/discount calculation mismatches

**Affected Features:**
- rialtoB2A(CASS TC5)
- rialtoB2A(CASS TC6)
- rialtoB2A(CASS TC9)
- rialtoB2A(CASS TC31)
- rialtoB2A(CASS TC36)
- rialtoB2A(CASS TC37)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC5)
- User perform CASS POST API - #1.1 (TC6)
- User perform CASS POST API - #1.1 (TC9)
- User perform CASS GET API - #1.1 (TC9)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC31)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC36)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC36)
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 (TC37)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC37)

**Failure Pattern:**
`discountAmount/orderDiscount/netPrice/priceNet/priceGross/commission/totalInclVat/vat` expected values differ from returned calculation outputs.

**Evidence:**
- `discountAmount expected [0.0] but found [63660.63]` (TC5)
- `orderBasketPriceSummary.orderDiscount expected [3600.00] but found [4800.00]` (TC36)
- `totalInclVat expected [7368.00] but found [5814.00]` (TC37)

**Impact:** 9 failures

**Confidence:** High

## Missing PRELIMINARY status flag after updates

**Affected Features:**
- rialtoB2A(CASS TC4 Change Placement)
- rialtoB2A(CASS TC28 Magazine (change size))
- rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama))

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC4)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC28)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC29)

**Failure Pattern:**
`orderHeader.statusFlags` expected `[PRELIMINARY]` but found `[]`.

**Evidence:**
- `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]` (TC4/TC28/TC29)

**Impact:** 3 failures

**Confidence:** High

## Revert-path instability (rollback + invalid path parameters)

**Affected Features:**
- rialtoB2A(CASS TC23 in MH change from Full page to uppslag - two orderlines change)
- rialtoB2A(CASS TC24 in MH change from uppslag to Full page)

**Affected Scenarios:**
- Revert two MediaHouse order lines to full page - #1.1 (TC23)
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)

**Failure Pattern:**
Revert flow fails with transaction rollback and downstream request uses invalid path parameters.

**Evidence:**
- `errorMessage: Transaction rolled back because it has been marked as rollback-only` (TC23)
- `Redundant path parameters: agencyPrisaId=7856; Undefined path parameters: uuid` (TC24)

**Impact:** 2 failures

**Confidence:** High

## Rialto ↔ MediaHouse order identity mismatch

**Affected Features:**
- rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto))

**Affected Scenarios:**
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC35)

**Failure Pattern:**
Updated data appears applied to a different order/basket than expected.

**Evidence:**
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [7866] does not match Agency Prisa ID [7867]`
- `placementId expected [[SIDAN2]] but found [[HALVLIGG]]`

**Impact:** 2 failures

**Confidence:** High

## API response code regression on CASS POST (TC14)

**Affected Features:**
- rialtoB2A(CASS TC14 change Product, Size, Placement & Date from Rialto)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC14)

**Failure Pattern:**
API returns `N500` where test expects `N200`.

**Evidence:**
- `{"errorCode":1,"message":null} expected [N200] but found [N500]`

**Impact:** 1 failure

**Confidence:** Medium

## Affected Components

- CASS POST/GET order update and mapping logic for multi-line orders
- Pricing and discount calculation pipeline (Rialto + MediaHouse views)
- Order status flag propagation (`PRELIMINARY`)
- Revert transaction handling and path parameter construction
- Cross-system order identity synchronization (Agency Prisa ID vs MH basket ID)

## Recommended Fix

- Prioritize mapping/order alignment defects and pricing calculation regressions; these account for 22/30 failures.
- Validate rollback transaction boundaries in revert flows before building follow-up Rialto requests.
- Add targeted regression checks for basket/order identity consistency in TC35 path.

## Prevention

- Add contract checks for ordered arrays (`paCode/prodCode/packageId/productId`) where sequence matters.
- Add API-level assertions for `statusFlags` and response-code expectations after change/revert operations.
- Add pre-assertion guard that compares Agency Prisa ID and MH `orBoxid` before downstream validations.
