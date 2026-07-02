# Weekly Test Failure Summary

**Period:** 2026-06-20 → 2026-06-26  
**Generated:** 2026-06-27  
**Total builds:** 12 | **Failed builds:** 2 | **Pass rate:** 83.3 %

---

## Failure Counts by Test Suite

| Test Suite | Failures this week | Failures last week | Trend |
|---|---|---|---|
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

---

## Key Observations

- Both failures this week were caused by **dependency/configuration changes that were not reflected in the test layer** — a recurring pattern that suggests a gap in the PR review checklist.
- `PaymentServiceTests` and `HttpClientTests` are the highest-risk suites this week.
- `UserAuthTests` recovered from last week's single failure; the fix introduced in commit `c1a0b33` appears stable.

## Recommended Actions

1. Add a PR checklist item: *"Have test stubs and mocks been updated to match this change?"*
2. Consider pinning major-version dependency upgrades behind a dedicated compatibility branch to allow incremental migration.
3. Schedule a review of `ApiGatewayTests` initialisation logic — the `NullPointerException` in build #251 suggests fragile test setup.

---

*This dashboard is regenerated weekly. Do not edit manually — rerun the weekly summary pipeline instead.*
