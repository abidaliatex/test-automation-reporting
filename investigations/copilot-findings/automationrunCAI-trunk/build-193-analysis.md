# Build 193 Investigation

Source report: [build-193.md](../../../reports/build-failures/automationrunCAI-trunk/build-193.md)

## Summary

Build 193 was UNSTABLE: 260 tests, 244 passed, and 16 failed.

## Root Cause

The failures group into:

1. Missing adapter/adspace or invalid order fixture data (5 failures). Adapter and MC-order requests receive N400/N500 responses because variant/adspace data is unavailable or order fields are invalid.
2. Hibernate lazy-loading failure (3 failures). Print-order POST requests fail when `FChargeses` is accessed outside a session.
3. Stale or changed API response fixtures (8 failures). Returned lists, database values, timestamps, record counts, and result order differ from test expectations.

## Affected Components

- `adapters.feature`: 3 failures
- `mc_orders.feature`: 2 failures
- `print_orders.feature`: 4 failures
- `base.feature`: 2 failures
- `customerapi.feature`: 3 failures
- `dwl.feature`: 2 failures

The 16 affected scenarios are listed in the source report.

## Recommended Fix

- Restore or isolate the adspace/adapter fixture data used by MC and adapter scenarios.
- Correct the MC PATCH test fixture or production validation for the `ono` field.
- Initialize print-order service relationships within an active Hibernate session.
- Refresh fixture datasets and, where ordering is not guaranteed, update response comparisons to avoid irrelevant order differences.

## Prevention

- Seed dependent test data before adapter and order scenarios.
- Add data assertions that fail with a specific setup error before API requests.
- Treat API payloads and database result sets as time-sensitive fixtures and refresh them in a controlled test environment.
