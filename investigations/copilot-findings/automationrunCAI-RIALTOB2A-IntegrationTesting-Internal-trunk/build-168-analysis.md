# Build 168 Analysis

Source report: [build-168.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-168.md)

## Summary

- Build 168 finished **UNSTABLE** with **37 failures out of 514 tests**.
- Failures cluster around four recurring patterns: multi-line order sequencing drift, revert/identifier handling failures, magazine pricing propagation drift, and single-order placement/pricing drift.

## Build Summary

Build: 168  
Total Tests: 514  
Passed: 477  
Failed: 37  
Pass Rate: 92.8%

## Root Cause Groups

## Order-Line Sequencing / Mapping Drift

**Affected Features:**
- rialtoB2A(CASS TC15 2 products change date MH on head order line)
- rialtoB2A(CASS TC22 in MH change from Full page to uppslag)
- rialtoB2A(CASS TC23 in MH change from Full page to uppslag - two orderlines change)
- rialtoB2A(CASS TC24 in MH change in MH change from uppslag to Full page)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC15)
- User perform CASS GET API - #1.1 (TC15)
- User perform CASS GET API - #1.1 (TC22)
- Verify updated MediaHouse basket state - #1.1 (TC23)
- Verify reverted MediaHouse basket state - #1.1 (TC23)
- Verify reverted MediaHouse basket state - #1.1 (TC24)

**Failure Pattern:**
`packageId expected [[AB, SVD]] found [[SVD, AB]]`

**Evidence:**
- TC15 reverses `packageId`, `productId`, `paCode`, and `issueDate` between the two order lines.
- TC22 and TC23 reorder `paCode`, `prodCode`, `plaCode`, `issueDate`, and the related amount arrays across six order lines.

**Impact:** 8 failures

**Confidence:** High

## Revert Flow / Identifier Propagation Failure

**Affected Features:**
- rialtoB2A(CASS TC23 in MH change from Full page to uppslag - two orderlines change)
- rialtoB2A(CASS TC24 in MH change in MH change from uppslag to Full page)
- rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto))

**Affected Scenarios:**
- Revert two MediaHouse order lines to full page - #1.1 (TC23)
- Revert two MediaHouse order lines to full page - #1.1 (TC24)
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC35)

**Failure Pattern:**
`Transaction rolled back because it has been marked as rollback-only`

**Evidence:**
- TC23 revert returns HTTP 500 with `rollback-only` instead of the expected success response.
- TC24 still carries Uppslag `placementId`/`issueDate` values during the revert and later fails with missing `uuid` plus redundant `agencyPrisaId`.
- TC35 reports `MH basket ID (orBoxid) [7623] does not match Agency Prisa ID [7624]`.

**Impact:** 4 failures

**Confidence:** High

## Magazine Pricing / Discount / Status Drift

**Affected Features:**
- rialtoB2A(CASS TC26 Basic order for magazines)
- rialtoB2A(CASS TC27 Magazine (change date))
- rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama))
- rialtoB2A(CASS TC30 Magazine (change Date & Size))
- rialtoB2A(CASS TC31 Magazine (change Date, Size & Placement))
- rialtoB2A(CASS TC32 Magazine (change date from Rialto))
- rialtoB2A(CASS TC33 Magazine (change size from Rialto))
- rialtoB2A(CASS TC34 Magazine (change to UPPSLAG from Rialto))
- rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto))
- rialtoB2A(CASS TC36 Magazine (change Product Size Placement & Date from Rialto))
- rialtoB2A(CASS TC37 - 2 Products Magazine - changes the size in MH)

**Affected Scenarios:**
- Verify reverted MediaHouse basket state - #1.1 (TC26)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC27, TC29, TC31)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC27, TC29, TC30, TC31)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC32, TC33, TC34, TC36)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC35, TC36)
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35)
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 (TC37)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC37)
- RIALTO - Verify Rialto reflects the updated state - #1.1 (TC37)

**Failure Pattern:**
`orderDiscount expected [0.00] found [3600.00]`

**Evidence:**
- TC26, TC32, TC33, TC34, and TC36 keep non-zero `orderDiscount`, reduced `netPrice`, and unexpected commission after magazine updates or reverts.
- TC27, TC30, and TC37 still carry `statusFlags [[PRELIMINARY]]` or `discountType [[NONE]]` when the reverted/updated order should already be normalized.
- TC29, TC31, TC35, and TC37 show the same drift on Rialto-facing price and commission fields (`priceNet`, `commissionAmount`, `orderbasketSum`).

**Impact:** 19 failures

**Confidence:** High

## Single-Order Placement / Pricing Drift

**Affected Features:**
- rialtoB2A(CASS TC3 change Size)
- rialtoB2A(CASS TC4 Change Placement)
- rialtoB2A(CASS TC5 change to Uppslag/Spread/Panorama)
- rialtoB2A(CASS TC6 change to changes the date and the size on the order line.)
- rialtoB2A(CASS TC9 change size from Rialto)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC3)
- User perform CASS POST API - #1.1 (TC4)
- User perform CASS POST API - #1.1 (TC5)
- User perform CASS POST API - #1.1 (TC6)
- User perform CASS POST API - #1.1 (TC9)
- User perform CASS GET API - #1.1 (TC9)

**Failure Pattern:**
`discountAmount expected [0.0] found [63660.63]`

**Evidence:**
- TC5 returns `placementId [TEXT]`, `columns [5]`, and `width [251]` after an Uppslag change that should remain `UPPSLAG`, `10`, and `530`.
- TC9 GET still reports `depth [372]`, `moduleCode [58]`, and `discountType [[RIALTO]]` instead of the expected full-price values after the size change.

**Impact:** 6 failures

**Confidence:** High

## Affected Components

- CASS multi-line order update mapping for `packageId` / `paCode` / `issueDate`
- MediaHouse ↔ Rialto revert flow payload construction and path-parameter binding
- Magazine discount, commission, and status propagation
- Single-order placement/size recalculation in POST/GET verification paths

## Recommended Fix

- Trace the mapper that builds multi-line order arrays and preserve original order-line alignment across `packageId`, `paCode`, `prodCode`, and amount fields.
- Inspect the revert flow for TC23/TC24 to ensure the generated payload switches placements back to full-page values and keeps `uuid` / basket identifiers in sync.
- Review magazine pricing logic for stale discount, commission, and `PRELIMINARY` flags after update/revert operations.

## Prevention

- Add targeted regression coverage for multi-line order sequencing and revert payload generation before publishing build data.
- Add assertions that compare basket/identifier propagation and magazine discount-state transitions immediately after each update step.
