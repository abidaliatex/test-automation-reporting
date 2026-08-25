# Build Failure Report

## Build Info

| Field | Value |
|---|---|
| **Build ID** | 181 |
| **Job** | automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk |
| **Date** | 2026-08-25 |
| **Status** | UNSTABLE |
| **Duration** | ~94 min |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/181/ |

## Test Results

| Metric | Count |
|---|---|
| Total Tests | 514 |
| Passed | 467 |
| Failed | 47 |
| Pass Rate | 90.9% |

## Failing Tests / Steps (Grouped)

### 1) Ordering/state mismatch in CASS order details (21)
- Affected scenarios: TC6, TC14, TC15, TC16, TC17, TC18, TC19, TC20, TC22, TC23, TC24, TC35, TC37
- Pattern: `printDetails` / `orderAdDetails` arrays and correlated fields returned in unexpected order or values.

### 2) Transaction rollback / API 500 errors (8)
- Affected scenarios: TC14, TC22, TC23, TC24, TC37
- Pattern: `Transaction rolled back because it has been marked as rollback-only`; expected `N200` but got `N500/N400`.

### 3) Discount/pricing calculation mismatch (13)
- Affected scenarios: TC5, TC9, TC15, TC22, TC23, TC24, TC36, TC37
- Pattern: non-zero discounts and basket totals where zero/expected values were asserted.

### 4) Missing PRELIMINARY status flag after change/revert (3)
- Affected scenarios: TC4, TC28, TC29
- Pattern: `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`.

### 5) Path parameter contract mismatch (1)
- Affected scenario: TC24
- Pattern: redundant `agencyPrisaId` and missing `uuid` path parameter.

### 6) MH/Rialto basket ID mismatch (1)
- Affected scenario: TC35
- Pattern: `orBoxid` does not match `agencyPrisaId`.
