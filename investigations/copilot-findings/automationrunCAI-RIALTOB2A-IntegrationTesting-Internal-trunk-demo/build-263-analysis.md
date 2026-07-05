[Source report](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-263.md)

## Summary

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #263`  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

## Root Cause

### Placement-change pricing and discount propagation mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`

**Affected Scenarios:**
- verify that order arrived in MH from rilato - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rilato - placement - after change (`tc_getMHTC03a`)
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
- `discountType` flips between `null`, `RIALTO`, and `NONE`
- Placement update returns mismatched placement, depth, commission, VAT, and total values

**Evidence:**
- `tc_getMHTC03`: `orders[0].printDetails.discountType expected [RIALTO] but found [null]`
- `tc_getMHTC03a`: `orders[0].printDetails.discountType expected [NONE] but found [RIALTO]`
- `tc_getIntegrationRialto05b`: `orderAdDetails[0].placementId expected [SIDAN3] but found [TEXT]`

**Impact:** 3 failures  
**Confidence:** High

## Affected Components

- Rialto B2A placement-change flow
- MediaHouse order basket pricing fields
- Discount and placement field propagation in GET validation responses

## Recommended Fix

- Check the placement-change path that feeds MediaHouse and Rialto GET assertions, especially `discountType`, placement mapping, and recalculated commercial totals.

## Prevention

- Keep a focused regression on placement-change scenarios that validates both field mapping and downstream price totals after the update step.
