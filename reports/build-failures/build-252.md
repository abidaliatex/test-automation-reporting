# Build Failure Report — Build #252

| Field | Value |
|---|---|
| **Build ID** | 252 |
| **Date** | 2026-07-03 |
| **Job** | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` |
| **Build URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/252/ |
| **Branch** | `trunk` |
| **Status** | ❌ FAILED |

## Failing Tests

| Test Suite / Feature | Scenario | Test Case | Result |
|---|---|---|---|
| `DiscountTypeTests` | Validate discount type on RIALTO product | TC01 | FAILED |
| `DiscountTypeTests` | Validate discount type on bundle order | TC05 | FAILED |
| `PricingIntegrationTests` | End-to-end pricing with discountType field | TC14 | FAILED |

## Error Output

```
[DiscountTypeTests] Validate discount type on RIALTO product (TC01)
  AssertionError: discountType expected [RIALTO] found [null]
  at DiscountTypeTests.java:88

[DiscountTypeTests] Validate discount type on bundle order (TC05)
  AssertionError: discountType expected [RIALTO] found [null]
  at DiscountTypeTests.java:134

[PricingIntegrationTests] End-to-end pricing with discountType field (TC14)
  NullPointerException: discountType is null — downstream pricing calculation aborted
  at PricingIntegrationTests.java:201
```

## Environment

- **Runner**: Jenkins internal (`crossadv.atex.com`)
- **Pipeline**: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`

## Suggested Next Steps

- Investigate why `discountType` is returning `null` instead of `RIALTO` across all affected scenarios.
- Check whether a recent change to the discount/pricing service or its API contract dropped the `discountType` field.
- See investigation: [build-252-analysis.md](../../investigations/copilot-findings/build-252-analysis.md)
