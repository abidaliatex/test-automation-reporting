# Build 181 — Root Cause Analysis

**Source report:** [build-181.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-181.md)

---

## Build Summary

Build: 181  
Total Tests: 514  
Passed: 467  
Failed: 47  
Pass Rate: 90.9%

---

## Root Cause Groups

## Ordering/state alignment mismatch across CASS multi-line flows

**Affected Features:**
- rialtoB2A.feature
- rialtoB2A-magazine.feature

**Affected Scenarios:**
- CASS TC6 change to changes the date and the size on the order line.
- CASS TC14 change Product, Size, Placement & Date from Rialto
- CASS TC15 2 products change date MH on head order line
- CASS TC16 2 products change date on order line which is not head order line from MH
- CASS TC17 2 products change size on head order line from MH
- CASS TC18 2 products change size on not registered as head order line from MH
- CASS TC19 2 products change placement on head order from MH
- CASS TC20 2 products change placement order for non head from MH
- CASS TC22 in MH change from Full page to uppslag
- CASS TC23 in MH change from Full page to uppslag - two orderlines change
- CASS TC24 in MH change from uppslag to Full page
- CASS TC35 Magazine (change Date Size & Placement from Rialto)
- CASS TC37 - 2 Products Magazine - changes the size in MH

**Failure Pattern:**
`orders[0].printDetails.paCode expected [[SVDTI, AB]] but found [[AB, SVDTI]]`

**Evidence:**
- `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]`
- `orderAdDetails.placementId expected [[TEXT, SIDAN3]] but found [[SIDAN3, TEXT]]`

**Impact:** 21 failures

**Confidence:** High

## Transaction rollback-only errors in CASS POST/update steps

**Affected Features:**
- rialtoB2A.feature
- rialtoB2A-magazine.feature

**Affected Scenarios:**
- CASS TC14 change Product, Size, Placement & Date from Rialto
- CASS TC22 in MH change from Full page to uppslag
- CASS TC23 in MH change from Full page to uppslag - two orderlines change
- CASS TC24 in MH change from uppslag to Full page
- CASS TC37 - 2 Products Magazine - changes the size in MH

**Failure Pattern:**
`Transaction rolled back because it has been marked as rollback-only`

**Evidence:**
- `500 ... expected [N200] but found [N400]`
- `{"errorCode":1,"message":null} expected [N200] but found [N500]`

**Impact:** 8 failures

**Confidence:** High

## Discount/pricing regression after order changes

**Affected Features:**
- rialtoB2A.feature
- rialtoB2A-magazine.feature

**Affected Scenarios:**
- CASS TC5 change to Uppslag/Spread/Panorama
- CASS TC9 change size from Rialto
- CASS TC15 2 products change date MH on head order line
- CASS TC22 in MH change from Full page to uppslag
- CASS TC23 in MH change from Full page to uppslag - two orderlines change
- CASS TC24 in MH change from uppslag to Full page
- CASS TC36 Magazine (change Product Size Placement & Date from Rialto)
- CASS TC37 - 2 Products Magazine - changes the size in MH

**Failure Pattern:**
`discountAmount expected [0.0] but found [63660.63]`

**Evidence:**
- `discountType expected [NONE] but found [RIALTO]`
- `orderBasketPriceSummary.orderDiscount expected [0.00] but found [4000.00]`

**Impact:** 13 failures

**Confidence:** High

## Missing PRELIMINARY order status after mutation/revert

**Affected Features:**
- rialtoB2A.feature
- rialtoB2A-magazine.feature

**Affected Scenarios:**
- CASS TC4 Change Placement
- CASS TC28 Magazine (change size)
- CASS TC29 Magazine (change to Uppslag/Spread/Panorama)

**Failure Pattern:**
`orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

**Evidence:**
- Same mismatch repeated in TC4, TC28, and TC29.

**Impact:** 3 failures

**Confidence:** High

## Path parameter contract mismatch (`agencyPrisaId` vs `uuid`)

**Affected Features:**
- rialtoB2A.feature

**Affected Scenarios:**
- CASS TC24 in MH change from uppslag to Full page

**Failure Pattern:**
`Path parameters were not correctly defined ... agencyPrisaId ... uuid`

**Evidence:**
- `Redundant path parameters are: agencyPrisaId=8158. Undefined path parameters are: uuid.`

**Impact:** 1 failure

**Confidence:** High

## MH ↔ Rialto identifier sync mismatch

**Affected Features:**
- rialtoB2A-magazine.feature

**Affected Scenarios:**
- CASS TC35 Magazine (change Date Size & Placement from Rialto)

**Failure Pattern:**
`MH basket ID (orBoxid) does not match Agency Prisa ID`

**Evidence:**
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [8168] does not match Agency Prisa ID [8169]`

**Impact:** 1 failure

**Confidence:** Medium
