# Build 162 — Investigation Analysis

**Source report:** [build-162.md](../../../reports/build-failures/automationRunOrderCreation-trunk/build-162.md)

## Summary

- Build 162 was **UNSTABLE**: 241 of 282 tests passed; 41 failed (85.5%).
- Jenkins results show 12 distinct failure patterns across online job notes, order creation, job notes, revised orders, Sales Forecast, and placement-column scenarios.

## Root Cause

- Six online-job-notes cases directly fail because `onlinejobNotes.csv` is missing.
- Two Cucumber steps are reported undefined, and one customer-selection step fails with a database result-set exception.
- The remaining failures are UI timeouts/click interception or assertions showing absent order/job-note data. Jenkins identifies these symptoms but does not establish their underlying causes.

## Affected Components

- `onlineJobNotes.feature`, `toporder.feature`, `createorder.feature`, `jobNotes.feature`
- `revisedOrder.feature`, `salesForecast.feature`, `onlineJob.feature`
- `minmaxplacementcol.feature`, `commissionorders.feature`, `duplicateOrders.feature`

## Recommended Fix

- Verify the missing fixture and undefined step bindings; inspect the reported UI and data-state failures without assuming a shared cause.

## Prevention

- Check test fixtures and step bindings before execution, and retain scenario-level UI/data evidence for intermittent failures.
