## Build Summary

Build: automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #252
Total Tests: 3 (reported failing tests)
Passed: 0
Failed: 3
Pass Rate: 0%

---

## Root Cause Groups

### Null `discountType` returned by pricing response

**Affected Features:**
- `DiscountTypeTests`
- `PricingIntegrationTests`

**Affected Scenarios:**
- Validate discount type on RIALTO product (TC01)
- Validate discount type on bundle order (TC05)
- End-to-end pricing with discountType field (TC14)

**Failure Pattern:**
`discountType expected [RIALTO] found [null]`

**Evidence:**
- TC01/TC05 both fail with `AssertionError: discountType expected [RIALTO] found [null]` at `DiscountTypeTests.java:88` and `DiscountTypeTests.java:134`.
- TC14 fails with `NullPointerException: discountType is null — downstream pricing calculation aborted` at `PricingIntegrationTests.java:201`.

**Impact:** 3 failures

**Confidence:** High
