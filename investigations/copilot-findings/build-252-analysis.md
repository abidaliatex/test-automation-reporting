# QA Triage Report — Build #252

**Source report:** [reports/build-failures/build-252.md](../../reports/build-failures/build-252.md)
**Analysis date:** 2026-07-03
**Analyst:** GitHub Copilot

---

## Build Summary

Build: automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #252
Total Tests: 3
Passed: 0
Failed: 3
Pass Rate: 0%

---

## Root Cause Groups

### `discountType` returns `null` instead of `RIALTO`

**Confidence:** High — identical null-value pattern across all three failures; TC14 NPE is a direct downstream consequence.

**Evidence:**
```
AssertionError: discountType expected [RIALTO] found [null]  — DiscountTypeTests.java:88
AssertionError: discountType expected [RIALTO] found [null]  — DiscountTypeTests.java:134
NullPointerException: discountType is null — downstream pricing calculation aborted  — PricingIntegrationTests.java:201
```

**Affected Scenarios:**
- `DiscountTypeTests` — Validate discount type on RIALTO product (TC01)
- `DiscountTypeTests` — Validate discount type on bundle order (TC05)
- `PricingIntegrationTests` — End-to-end pricing with discountType field (TC14)
