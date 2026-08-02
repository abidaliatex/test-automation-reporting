# Build Failure Report — automationrunCAI-RIALTO-B2A-trunk #350

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 350 |
| **Date** | 2026-08-02 21:02:17 UTC |
| **Status** | UNSTABLE |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/350/ |
| **Total Tests** | 17 |
| **Passed** | 13 |
| **Failed** | 4 |
| **Skipped** | 0 |
| **Pass Rate** | 76.5% |

---

## Failing Tests / Steps

| Feature | Test Case | Scenario | Failure |
|---|---|---|---|
| `rialtoB2A(CASS).feature` | `tc_getRialtoB2A05` | Returns StoreStatus of Order | `expected [N200] but found [N202]` |
| `rialtoB2A(CASS).feature` | `tc_patchRialtoB2A01` | Update ad(Order) for self service | `Failed to parse the JSON document` |
| `rialtoB2A(CASS).feature` | `tc_getRialtoB2A06` | Returns StoreStatus of Update Order | `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.` |
| `rialtoB2A(CASS).feature` | `tc_postRialtoB2A03` | Calculate price for self service | `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]` |
