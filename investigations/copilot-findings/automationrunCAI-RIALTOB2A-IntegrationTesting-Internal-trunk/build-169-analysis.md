# Build 169 Analysis

Source report: [build-169.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-169.md)

## Summary

- Build 169 finished **UNSTABLE** with **31 failures out of 514 tests**.
- Failures cluster into four recurring patterns: multi-line order mapping drift, revert/identifier propagation failures, magazine pricing/status drift, and single-order placement/pricing drift.

## Build Summary

Build: 169  
Total Tests: 514  
Passed: 483  
Failed: 31  
Pass Rate: 94.0%

## Root Cause Groups

### Order-Line Sequencing / Mapping Drift

**Affected Features:**
- rialtoB2A(CASS)TestCase15.feature
- rialtoB2A(CASS)TestCase19.feature
- rialtoB2A(CASS)TestCase22.feature
- rialtoB2A(CASS)TestCase23.feature
- rialtoB2A(CASS)TestCase24.feature

**Affected Scenarios:**
- User perform CASS GET API - #1.1 (TC15)
- User perform CASS POST API - #1.1 (TC15)
- User perform CASS POST API - #1.1 (TC19)
- User perform CASS GET API - #1.1 (TC22)
- Verify updated MediaHouse basket state - #1.1 (TC23)
- Verify reverted MediaHouse basket state - #1.1 (TC23)
- Verify reverted MediaHouse basket state - #1.1 (TC24)

**Failure Pattern:**
`orderAdDetails.packageId expected [[AB, SVD]] found [[SVD, AB]]`

**Evidence:**
- TC15 and TC19 swap `packageId`, `productId`, and `placementId`/`issueDate` between the two order lines in Rialto verification.
- TC22, TC23, and TC24 reorder `paCode`, `prodCode`, `plaCode`, `issueDate`, and amount arrays across six MediaHouse order lines.

**Impact:** 9 failures

**Confidence:** High

### Revert Flow / Identifier Propagation Failure

**Affected Features:**
- rialtoB2A(CASS)TestCase23.feature
- rialtoB2A(CASS)TestCase24.feature
- rialtoB2A(CASS)TestCase35.feature

**Affected Scenarios:**
- Revert two MediaHouse order lines to full page - #1.1 (TC23)
- Revert two MediaHouse order lines to full page - #1.1 (TC24)
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC35)

**Failure Pattern:**
`Transaction rolled back because it has been marked as rollback-only`

**Evidence:**
- TC23 revert returns HTTP 500 `rollback-only` instead of the expected success response.
- TC24 revert payload keeps `UPPSLAG` placements and wrong issue dates, then the follow-up GET fails because `uuid` is undefined while `agencyPrisaId` is redundant.
- TC35 reports `MH basket ID (orBoxid) [7685] does not match Agency Prisa ID [7686]`.

**Impact:** 4 failures

**Confidence:** High

### Magazine Pricing / Status Drift

**Affected Features:**
- rialtoB2A(CASS)TestCase28.feature
- rialtoB2A(CASS)TestCase29.feature
- rialtoB2A(CASS)TestCase31.feature
- rialtoB2A(CASS)TestCase33.feature
- rialtoB2A(CASS)TestCase34.feature
- rialtoB2A(CASS)TestCase35.feature
- rialtoB2A(CASS)TestCase36.feature
- rialtoB2A(CASS)TestCase37.feature

**Affected Scenarios:**
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC28)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC29)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC31)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC33)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC34)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC35)
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC36)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC36)
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 (TC37)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC37)
- RIALTO - Verify Rialto reflects the updated state - #1.1 (TC37)

**Failure Pattern:**
`orderBasketPriceSummary.orderDiscount expected [0.00] found [4000.00]`

**Evidence:**
- TC33, TC34, and TC36 keep non-zero `orderDiscount` and reduced `netPrice` after Rialto-driven magazine updates that should clear the discount.
- TC28, TC29, and TC31 still report `statusFlags [[PRELIMINARY]]`, stale commissions, or stale net prices after the revert/update flow.
- TC35 and TC37 also drift on placement/date/VAT totals, so both MediaHouse and Rialto views stay out of sync after the magazine change sequence.

**Impact:** 12 failures

**Confidence:** High

### Single-Order Placement / Pricing Drift

**Affected Features:**
- rialtoB2A(CASS)TestCase3.feature
- rialtoB2A(CASS)TestCase4.feature
- rialtoB2A(CASS)TestCase5.feature
- rialtoB2A(CASS)TestCase6.feature
- rialtoB2A(CASS)TestCase9.feature

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
- TC5 returns stale Uppslag pricing and discount values (`priceGross`, `priceNetExComm`, `commissionAmount`) instead of the expected full-price values.
- TC9 GET still reports `depth [372]`, `moduleCode [58]`, and discounted amounts after the size change, while TC4 keeps `statusFlags` empty instead of `PRELIMINARY`.

**Impact:** 6 failures

**Confidence:** High

## Root Cause

- The failures point to state drift after update/revert operations rather than isolated test-data issues.
- Multi-line mapping loses line alignment, revert flows do not fully restore identifiers/payload fields, and downstream pricing/status calculations stay stale in both MediaHouse and Rialto.

## Affected Components

- Multi-line order mapping for `packageId`, `paCode`, `prodCode`, `placementId`, and `issueDate`
- MediaHouse revert payload generation and path-parameter binding
- Magazine discount, commission, VAT, and status propagation
- Single-order size/placement recalculation in POST and GET verification flows

## Recommended Fix

- Trace the mapper that builds multi-line order arrays and preserve original line alignment across identifiers, placements, dates, and amount fields.
- Inspect the TC23/TC24 revert flow so it restores full-page payload values and keeps `uuid`, basket IDs, and Agency IDs in sync.
- Review magazine and single-order recalculation logic for stale discount/status propagation after update and revert operations.

## Prevention

- Add regression coverage for multi-line order sequencing plus revert payload/identifier validation before publishing build data.
- Add targeted assertions that verify discount/status reset behavior immediately after each MediaHouse or Rialto update step.
