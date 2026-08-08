# Build 165 Analysis

Source report: [build-165.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-165.md)

---

## Build Summary

Build: 165  
Total Tests: 514  
Passed: 457  
Failed: 57  
Pass Rate: 88.9%

---

## Root Cause Groups

### Discount / Price Calculation Mismatch

**Affected Features:**
- rialtoB2A(CASS TC1 and TC2)
- rialtoB2A(CASS TC3/6/9/11/14/15/21/23/24)
- rialtoB2A(CASS TC26/27/29/31/32/33/34/35/36/37)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1 and TC2)
- User perform CASS GET API - #1.1 (TC11)
- User perform CASS POST API - #1.1 (TC14)
- User perform CASS POST API - #1.1 (TC15)
- User perform CASS GET API - #1.1 (TC15)
- User perform CASS POST API - #1.1 (TC21)
- Verify original full-page order state in MediaHouse - #1.1 (TC23)
- Verify updated MediaHouse basket state - #1.1 (TC23)
- Verify reverted MediaHouse basket state - #1.1 (TC23)
- Verify created Rialto order and capture shared identifiers - #1.1 (TC24)
- Verify original full-page order state in MediaHouse - #1.1 (TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC26)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC27)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC29)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC29)
- User perform CASS POST API - #1.1 (TC3)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (TC31)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC31)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC31)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC32)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC33)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC34)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC35)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC36)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC36)
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 (TC37)
- User perform CASS POST API - #1.1 (TC6)
- User perform CASS POST API - #1.1 (TC9)

**Failure Pattern:**
- `discountAmount expected [0.0] found [63660.63]`
- `orderBasketPriceSummary.orderDiscount expected [0.00] found [4000.00]`
- `orderBasketPriceSummary.totalInclVat expected [169660.46] found [155683.63]`

**Evidence:**
- TC1 and TC2: `discountAmount expected [0.0] but found [63660.63]`
- TC31: `commission expected [465.00] but found [155.00]`
- TC37: `totalInclVat expected [7368.00] but found [5814.00]`

**Impact:** 32 failures

**Confidence:** High

### Order-Line Mapping / Sequencing Mismatch

**Affected Features:**
- rialtoB2A(CASS TC4/5/9/15/18/19/20/22/24/35/37)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC15)
- User perform CASS POST API - #1.1 (TC18)
- User perform CASS POST API - #1.1 (TC19)
- User perform CASS POST API - #1.1 (TC20)
- User perform CASS GET API - #1.1 (TC22)
- Verify updated MediaHouse basket state - #1.1 (TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC24)
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC37)
- User perform CASS POST API - #1.1 (TC4)
- User perform CASS POST API - #1.1 (TC5)
- User perform CASS GET API - #1.1 (TC9)

**Failure Pattern:**
- `packageId expected [[AB, SVD]] found [[SVD, AB]]`
- `moduleCode expected [[58, 54]] found [[58, 58]]`

**Evidence:**
- TC15: packageId/productId sequence reversed
- TC22/TC24: paCode/plaCode ordering does not match expected order-line mapping

**Impact:** 13 failures

**Confidence:** Medium

### Basket ID / Path Parameter Propagation Failure

**Affected Features:**
- rialtoB2A(CASS TC1 and TC2)
- rialtoB2A(CASS TC24 in MH change in MH change from uppslag to Full page)

**Affected Scenarios:**
- User perform CASS POST API (TC1 and TC2)
- User perform CASS GET API - #1.1 (TC1 and TC2)
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)

**Failure Pattern:**
- `Basket not found for campaign`
- `Invalid number of path parameters... mhBasketOrderId`

**Evidence:**
- TC1/2: basket not found followed by missing `mhBasketOrderId`
- TC24: redundant `agencyPrisaId` and undefined `uuid`

**Impact:** 4 failures

**Confidence:** High

### Backend Transaction Rollback (HTTP 500)

**Affected Features:**
- rialtoB2A(CASS TC18)
- rialtoB2A(CASS TC22)
- rialtoB2A(CASS TC24)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC18)
- User perform CASS POST API - #1.1 (TC22)
- Revert two MediaHouse order lines to full page - #1.1 (TC24)

**Failure Pattern:**
- `Transaction rolled back because it has been marked as rollback-only`

**Evidence:**
- TC18 POST returns HTTP 500 rollback-only
- TC22 POST returns HTTP 500 rollback-only
- TC24 revert step returns HTTP 500 rollback-only

**Impact:** 3 failures

**Confidence:** High

### Order Status Propagation Mismatch

**Affected Features:**
- rialtoB2A(CASS TC27)
- rialtoB2A(CASS TC30)
- rialtoB2A(CASS TC37)

**Affected Scenarios:**
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC27)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC30)
- RIALTO - Verify Rialto reflects the updated state - #1.1 (TC37)

**Failure Pattern:**
- `statusFlags expected [[]] found [[PRELIMINARY]]`

**Evidence:**
- TC27: reverted order still has `PRELIMINARY`
- TC30/TC37: reverted/updated state checks show stale state markers with price-side mismatches

**Impact:** 3 failures

**Confidence:** Medium

### MH Basket ID / Agency ID Mismatch

**Affected Features:**
- rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto))

**Affected Scenarios:**
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC35)

**Failure Pattern:**
- `MH basket ID (orBoxid) [7454] does not match Agency Prisa ID [7455]`

**Evidence:**
- TC35: integration mismatch reported explicitly in assertion output

**Impact:** 1 failure

**Confidence:** High
