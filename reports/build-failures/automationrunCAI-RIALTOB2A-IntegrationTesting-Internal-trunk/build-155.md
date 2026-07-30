# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #155  
Total Tests: 514  
Passed: 435  
Failed: 79  
Pass Rate: 84.6%

---

## Root Cause Groups

## Numeric precision / floating-point calculation drift

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`
- `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase9.feature`
- `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase14.feature`, `rialtoB2A(CASS)TestCase15.feature`
- `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase21.feature`, `rialtoB2A(CASS)TestCase22.feature`
- `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase26.feature`
- `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`
- `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase32.feature`, `rialtoB2A(CASS)TestCase33.feature`
- `rialtoB2A(CASS)TestCase34.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase36.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1, TC3, TC4, TC5, TC6, TC9, TC11, TC14, TC15, TC18, TC21, TC22)
- User perform CASS GET API - #1.1 (TC3, TC5, TC11)
- Verify created Rialto order and capture shared identifiers - #1.1 (TC23, TC24)
- Verify original full-page order state in MediaHouse - #1.1 (TC23, TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC26)
- RIALTO - Verify created Rialto order and capture shared identifiers - #1.1 (TC27, TC28)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (TC27, TC28, TC30, TC31)
- MEDIAHOUSE - Update two MediaHouse order lines to uppslag - #1.1 (TC27)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC27, TC30, TC31)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC28, TC31)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC32, TC33, TC34, TC35, TC36)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC32, TC33, TC34, TC36)
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35)

**Failure Pattern:**
Financial fields (`discountAmount`, `priceNet`, `priceNetExComm`, `commissionAmount`, `vat`, `totalInclVat`, `netAmount`, `grossAmount`) return values with IEEE-754 double precision residuals instead of the expected rounded values.

**Evidence:**
- `orderAdDetails[0].discountAmount expected [63660.63] but found [63660.630000000005]`
- `orderAdDetails[0].priceNetExComm expected [66451.59999999998] but found [66451.6]`
- `orderAdDetails.priceNet expected [[19380.0, 36958.049999999996, ...]] but found [[19380.0, 36958.05, ...]]`
- `orderBasketPriceSummary.totalInclVat expected [169660.46] but found [155683.63]`

**Impact:** 54 failures

**Confidence:** High

---

## `discountType` polarity inversion (`null` returned instead of expected `RIALTO`)

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`
- `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase23.feature`
- `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS GET API - #1.1 (TC4, TC9, TC11, TC15, TC22)
- Verify updated MediaHouse basket state - #1.1 (TC23, TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC23, TC24)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC27)
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 (TC37)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC37)

**Failure Pattern:**
`orders[*].printDetails.discountType` is returned as `null` where `RIALTO` is expected. Note: build #154 showed the inverse polarity (`RIALTO` found where `null` expected), suggesting a discount-type assignment toggle between deployments.

**Evidence:**
- `orders[0].printDetails.discountType expected [[null]] but found [[RIALTO]]`
- `orders[0].printDetails.discountType expected [[null, null]] but found [[RIALTO, RIALTO]]`

**Impact:** 13 failures

**Confidence:** High

---

## Transaction rollback and path-parameter binding failures

**Affected Features:**
- `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase24.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC18, TC22)
- Revert two MediaHouse order lines to full page - #1.1 (TC24)
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)

**Failure Pattern:**
Backend returns HTTP 500 with `Transaction rolled back because it has been marked as rollback-only`; separately TC24 fails with `Redundant path parameters are: agencyPrisaId=7025. Undefined path parameters are: uuid`.

**Evidence:**
- `500: errorMessage: Transaction rolled back because it has been marked as rollback-only (caiVersion 8.8.x-CI.39-r79762950, 2026-07-30 23:28–23:41)`
- `Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=7025. Undefined path parameters are: uuid`

**Impact:** 4 failures

**Confidence:** High

---

## MH/Agency basket ID synchronisation mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- User perform CASS GET API - #1.1 (TC1)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC35)

**Failure Pattern:**
After basket creation, the MediaHouse `orBoxid` diverges from the Agency Prisa ID used in subsequent GET verification.

**Evidence:**
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6872] does not match Agency Prisa ID [7006] expected [7006] but found [6872]`
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [7035] does not match Agency Prisa ID [7036] expected [7036] but found [7035]`

**Impact:** 3 failures

**Confidence:** Medium

---

## Multi-line update ordering mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase22.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC15, TC22)

**Failure Pattern:**
Order-line arrays are returned in a different sequence than expected (`packageId`, `productId`, `placementId`, `issueDate` order inverted).

**Evidence:**
- `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]`
- `body.orderAdDetailUpdates.packageId expected [[SVDTI, SVDTI, SVDTI, AB, AB, AB]] but found [[SVDTI, AB, SVDTI, AB, AB, SVDTI]]`

**Impact:** 2 failures

**Confidence:** Medium
