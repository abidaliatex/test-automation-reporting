# Build 177 — Root Cause Analysis

**Source Report:** [build-177.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-177.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-21 22:03:09 UTC

---

## Build Summary

Build: 177
Total Tests: 514
Passed: 481
Failed: 33
Pass Rate: 93.6%

---

## Root Cause Groups

---

## Array Element Ordering — Multi-Product Ad Details Not Sorted Consistently

**Affected Features:**
- rialtoB2A(CASS TC19 2 products change placement on head order from MH).feature
- rialtoB2A(CASS TC20 2 products change placement order for non head from MH).feature
- rialtoB2A(CASS TC22 in MH change from Full page to uppslag).feature
- rialtoB2A(CASS TC24 in MH change in MH change from uppslag to Full page).feature
- rialtoB2A(CASS TC37 - 2 Products Magazine - changes the size in MH).feature

**Affected Scenarios:**
- 2 products change placement on head order from MH (TC19)
- 2 products change placement order for non head from MH (TC20)
- In MH change from Full page to uppslag (TC22)
- In MH change from uppslag to Full page (TC24)
- 2 Products Magazine - changes the size in MH (TC37)

**Failure Pattern:**
```
packageId expected [[AB, SVD]] but found [[SVD, AB]]
productId expected [[AB, SVD]] but found [[SVD, AB]]
placementId expected [[TEXT, SIDAN3]] but found [[TEXT, TEXT]]
paCode expected [[SVDTI, AB, SVDTI, AB, AB, SVDTI]] but found [[AB, SVDTI, AB, AB, SVD, SVDTI]]
placementId expected [[HALVLIGG, TEXT]] but found [[TEXT, TEXT]]
```

**Evidence:**
- TC19: `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]` — order lines returned in reversed sequence
- TC22: `paCode expected [[SVDTI, AB, SVDTI, AB, AB, SVDTI]] but found [[AB, SVDTI, AB, AB, SVD, SVDTI]]` — 6-element array out of expected order
- TC24: `placementId expected [[TEXT, TEXT, TEXT, TEXT, TEXT, TEXT]] but found [[UPPSLAG, UPPSLAG, UPPSLAG, UPPSLAG, UPPSLAG, UPPSLAG]]` — revert to full-page not applied
- TC37: `placementId expected [[HALVLIGG, TEXT]] but found [[TEXT, TEXT]]` — placement update lost for one product line

**Impact:** 10+ failures (multiple cascade steps per TC)

**Confidence:** High

---

## Missing PRELIMINARY Status Flag on Order Header

**Affected Features:**
- rialtoB2A(CASS TC4 Change Placement).feature
- rialtoB2A(CASS TC28 Magazine (change size)).feature
- rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama)).feature

**Affected Scenarios:**
- Change Placement (TC4)
- Magazine change size (TC28)
- Magazine change to Uppslag/Spread/Panorama (TC29)

**Failure Pattern:**
```
orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]
```

**Evidence:**
- TC4: `statusFlags expected [[PRELIMINARY]] but found [[]]` — POST step fails immediately
- TC28: `statusFlags expected [[PRELIMINARY]] but found [[]]` — after Rialto re-authentication step
- TC29: same as TC28

**Impact:** 3 failures (persisting since build 174)

**Confidence:** High

---

## Incorrect Pricing / Discount Calculation

**Affected Features:**
- rialtoB2A(CASS TC5 change to Uppslag/Spread/Panorama).feature
- rialtoB2A(CASS TC9 change size from Rialto).feature
- rialtoB2A(CASS TC31 Magazine (change Date, Size & Placement)).feature
- rialtoB2A(CASS TC36 Magazine (change Product Size Placement & Date from Rialto)).feature
- rialtoB2A(CASS TC37 - 2 Products Magazine - changes the size in MH).feature

**Affected Scenarios:**
- Change to Uppslag/Spread/Panorama (TC5)
- Change size from Rialto (TC9)
- Magazine change Date, Size & Placement (TC31)
- Magazine change Product Size Placement & Date from Rialto (TC36)
- 2 Products Magazine - changes the size in MH (TC37)

**Failure Pattern:**
```
discountAmount expected [0.0] but found [63660.63]
orderHeader.priceNetExComm expected [115320.00] but found [77122.03]
orderAdDetails.priceNet expected [[5000.0]] but found [[4845.0]]
orderBasketPriceSummary.orderDiscount expected [0.00] but found [4000.00]
orderBasketPriceSummary.totalInclVat expected [7368.00] but found [5814.00]
```

**Evidence:**
- TC5: unexpected discount of 63,660.63 applied; `priceNetExComm` drops from 250,000 to 128,531.37
- TC9: `discountAmount` 38,197.97 applied unexpectedly; `commissionAmount` and `vat` all reduced proportionally
- TC31: `commissionAmount` 155.0 wrongly applied (expected 0.0); `priceNet` reduced by 155
- TC36: `orderDiscount` 4,000.00 surplus in updated state
- TC37: `totalInclVat` off by ~1,554; `commission` off by 5.00

**Impact:** 7 failures

**Confidence:** High

---

## Integration Basket ID Mismatch (MH ↔ Agency)

**Affected Features:**
- rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto)).feature

**Affected Scenarios:**
- Magazine change Date Size & Placement from Rialto (TC35)

**Failure Pattern:**
```
INTEGRATION MISMATCH: MH basket ID (orBoxid) [8003] does not match Agency Prisa ID [8004]
```

**Evidence:**
- TC35: After Rialto update propagation the MH lookup returns basket `8003` while the Agency side has advanced to `8004` — indicates a race condition or stale basket reference between systems

**Impact:** 4 failures (TC35 cascades across 3 subsequent verification steps)

**Confidence:** Medium

---

## Server Error (HTTP 500) on CASS POST

**Affected Features:**
- rialtoB2A(CASS TC14 change Product, Size, Placement & Date from Rialto).feature

**Affected Scenarios:**
- Change Product, Size, Placement & Date from Rialto (TC14)

**Failure Pattern:**
```
{"errorCode":1,"message":null} expected [N200] but found [N500]
```

**Evidence:**
- TC14: CASS POST returns HTTP 500 with `errorCode:1, message:null`; GET verification step cascades as failure

**Impact:** 2 failures

**Confidence:** High

---

## Numeric Precision Formatting (Decimal Trailing Zero)

**Affected Features:**
- rialtoB2A(CASS TC6 change date and size).feature

**Affected Scenarios:**
- Change date and size on order line (TC6)

**Failure Pattern:**
```
priceNetExComm expected [115320.00] but found [115320.0]
priceGross expected [115320.00] but found [115320.0]
```

**Evidence:**
- TC6: Values are numerically equal but differ in decimal formatting (`115320.00` vs `115320.0`); likely a serialisation/assertion strictness issue

**Impact:** 1 failure

**Confidence:** High
