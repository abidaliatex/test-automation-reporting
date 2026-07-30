# Build Failure Report — automationrunCAI-RIALTO-B2A-trunk #345

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 345 |
| **Date** | 2026-07-30 21:09:18 UTC |
| **Status** | UNSTABLE |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/345/ |
| **Total Tests** | 17 |
| **Passed** | 14 |
| **Failed** | 3 |
| **Skipped** | 0 |
| **Pass Rate** | 82.4% |

---

## Failing Tests / Steps

| Feature | Test Case | Scenario | Failure |
|---|---|---|---|
| `rialtoB2A(CASS).feature` | `tc_getRialtoB2A05` | Returns StoreStatus of Order | `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]` |
| `rialtoB2A(CASS).feature` | `tc_getRialtoB2A06` | Returns StoreStatus of Update Order | `expected [N200] but found [N202]` |
| `rialtoB2A(CASS).feature` | `tc_postRialtoB2A03` | Calculate price for self service | `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]` |
