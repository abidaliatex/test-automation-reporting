# QA Triage Report — Build #252

**Source report:** [reports/build-failures/build-252.md](../../reports/build-failures/build-252.md)
**Analysis date:** 2026-07-03
**Analyst:** GitHub Copilot

---

## Build Summary

Build: automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #252
Total Tests: Unknown (3 failures reported)
Passed: 0
Failed: 3
Pass Rate: 0 % (of reported tests)

---

## Root Cause Groups

### Null discountType Field Returned by Pricing/Discount Service

**Affected Features:**
- DiscountTypeTests.feature
- PricingIntegrationTests.feature

**Affected Scenarios:**
- Validate discount type on RIALTO product (TC01)
- Validate discount type on bundle order (TC05)
- End-to-end pricing with discountType field (TC14)

**Failure Pattern:**
```
discountType expected [RIALTO] found [null]
```

**Evidence:**
- TC01: `AssertionError: discountType expected [RIALTO] found [null]` at `DiscountTypeTests.java:88`
- TC05: `AssertionError: discountType expected [RIALTO] found [null]` at `DiscountTypeTests.java:134`
- TC14: `NullPointerException: discountType is null — downstream pricing calculation aborted` at `PricingIntegrationTests.java:201`

**Impact:** 3 failures (100 % of reported failing tests)

**Confidence:** High — identical `discountType → null` pattern across all three failures; TC14 NPE is a downstream consequence of the same null value.
