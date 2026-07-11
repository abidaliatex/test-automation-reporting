# Weekly Test Failure Summary

**Period:** 2026-06-20 → 2026-07-03  
**Generated:** 2026-07-03  
**Total builds:** 13 | **Failed builds:** 3 | **Pass rate:** 76.9 %

---

## Failure Counts by Test Suite

| Test Suite | Failures this week | Failures last week | Trend |
|---|---|---|---|
| `DiscountTypeTests` | 2 | 0 | ↑ |
| `PricingIntegrationTests` | 1 | 0 | ↑ |
| `PaymentServiceTests` | 2 | 0 | ↑ |
| `IntegrationTests` | 1 | 0 | ↑ |
| `HttpClientTests` | 2 | 0 | ↑ |
| `ApiGatewayTests` | 1 | 0 | ↑ |
| `UserAuthTests` | 0 | 1 | ↓ |
| `ProductCatalogueTests` | 0 | 0 | → |
| `OrderServiceTests` | 0 | 0 | → |

---

## Failed Builds

| Build | Date | Root Cause Summary | Investigation |
|---|---|---|---|
| [#250](../reports/build-failures/build-250.md) | 2026-06-25 | Test stubs not updated after timeout config change | [analysis](../investigations/copilot-findings/build-250-analysis.md) |
| [#251](../reports/build-failures/build-251.md) | 2026-06-26 | Breaking API change in HTTP client major version bump | — |
| [#252](../reports/build-failures/build-252.md) | 2026-07-03 | `discountType` returning null instead of RIALTO across all scenarios | [analysis](../investigations/copilot-findings/build-252-analysis.md) |

---

## Key Observations

- Build #252 introduced a new failure pattern: `discountType` returning `null` instead of the expected `RIALTO` value — this impacts both direct assertions and downstream pricing flows.
- All three builds this week were caused by **changes to service contracts or configuration that were not reflected in the test layer**.
- `PaymentServiceTests` and `HttpClientTests` remain high-risk from last week's failures; `DiscountTypeTests` is now a new risk area.

## Recommended Actions

1. Add a PR checklist item: *"Have test stubs and mocks been updated to match this change?"*
2. Consider pinning major-version dependency upgrades behind a dedicated compatibility branch to allow incremental migration.
3. Schedule a review of `ApiGatewayTests` initialisation logic — the `NullPointerException` in build #251 suggests fragile test setup.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Triage |
|---|---|---|---|

| [automationrunCAI-RIALTO-B2A-trunk #301](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-301.md) | 2026-07-10 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-301-analysis.md) |

| [automationrunCAI-RIALTO-B2A-trunk #298](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-298.md) | 2026-07-10 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-298-analysis.md) |

| [automationrunCAI-RIALTO-B2A-trunk #295](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-295.md) | 2026-07-10 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-295-analysis.md) |

| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #134](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-134.md) | 2026-07-10 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-134-analysis.md) |

| [automationrunCAI-RIALTO-B2A-trunk #286](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-286.md) | 2026-07-09 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-286-analysis.md) |

| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #271](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-271.md) | 2026-07-09 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-271-analysis.md) |

| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #270](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-270.md) | 2026-07-06 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-270-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #284](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-284.md) | 2026-07-05 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-284-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #269](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-269.md) | 2026-07-05 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-269-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #262](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-262.md) | 2026-07-05 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-262-analysis.md) |

---

*This dashboard is regenerated weekly. Do not edit manually — rerun the weekly summary pipeline instead.*
