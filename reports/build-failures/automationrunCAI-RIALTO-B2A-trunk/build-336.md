# Build Failure Report — automationrunCAI-RIALTO-B2A-trunk #336

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 336 |
| **Date** | 2026-07-26 21:09:17 UTC |
| **Status** | UNSTABLE |
| **Triggered By** | AutomationManager-Rialto-APIs-AI-Assisted #45 (timer) |
| **Commit** | `29dc5af001ff347cd07782f72c5d94c34c027394` |
| **Commit Message** | `updated testcase29 data tc_getMHTC_MZN04a` |
| **Total Tests** | 17 |
| **Passed** | 7 |
| **Failed** | 10 |
| **Skipped** | 0 |
| **Pass Rate** | 41.2% |

---

## Failing Tests / Steps

### rialtoB2A(CASS).feature — POST scenarios

| Test Case | Scenario | Error |
|---|---|---|
| `tc_postRialtoB2A01` | Attempts to log in a user | HTTP 404 — `/cass/users/login` not available |
| `tc_postRialtoB2A02` | Create ad for self service | HTTP 404 — `/cass/orders/orders` not available |
| `tc_postRialtoB2A03` | Calculate price for self service | HTTP 404 — `/cass/orders/calculatePrice` not available |
| `tc_postRialtoB2A04` | Queries space availability | HTTP 404 — `/cass/orders/spaceAvailability` not available |
| `tc_patchRialtoB2A01` | Update ad(Order) for self service | `Failed to parse the JSON document` (HTML 404 returned) |

### rialtoB2A(CASS).feature — GET scenarios

| Test Case | Scenario | Error |
|---|---|---|
| `tc_getRialtoB2A01` | get order details using order ID | HTTP 404 — `/cass/orders/orders/1620` not available |
| `tc_getRialtoB2A02` | Returns package and placement data | HTTP 404 — `/cass/staticData/validPackagesAndPlacements` not available |
| `tc_getRialtoB2A04` | Returns OrderHeader objects for orders associated with the user | HTTP 404 — `/cass/orders/orderHeaders` not available |
| `tc_getRialtoB2A05` | Returns StoreStatus of Order | `Invalid number of path parameters. Undefined path parameters are: uuid` |
| `tc_getRialtoB2A06` | Returns StoreStatus of Update Order | `Invalid number of path parameters. Undefined path parameters are: uuid` |
