# Build Failure Report — automationrunCAI-RIALTO-B2A-trunk #343

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 343 |
| **Date** | 2026-07-29 22:36:36 UTC |
| **Status** | UNSTABLE |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/343/ |
| **Total Tests** | 17 |
| **Passed** | 15 |
| **Failed** | 2 |
| **Skipped** | 0 |
| **Pass Rate** | 88.2% |

---

## Failing Tests / Steps

| Feature | Test Case | Scenario | Failure |
|---|---|---|---|
| `rialtoB2A(CASS).feature` | `tc_getRialtoB2A05` | Returns StoreStatus of Order | `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]` |
| `rialtoB2A(CASS).feature` | `tc_postRialtoB2A03` | Calculate price for self service | `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]` |
