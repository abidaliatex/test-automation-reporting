# Build 163 — Investigation Analysis

**Source report:** [build-163.md](../../../reports/build-failures/automationRunReports-trunk/build-163.md)

## Summary

- Build 163 was **UNSTABLE**: 51 of 53 tests passed (96.2%).
- Jenkins reported two failures: one offer-report data mismatch and one stock-orders filter dialog timeout.

## Root Cause

- **Offer report:** The report data mismatch is confirmed by the assertion, but Jenkins evidence does not establish whether test data or report filtering caused the wrong value.
- **Stock Orders:** The OK button did not become clickable within 10 seconds. Jenkins evidence confirms the timeout but not why the dialog state prevented readiness.

## Affected Components

- `report_offer.feature` — `User verifying offer reports` (TC not exposed).
- `reports_stockoforders.feature` — `Perform Filter Actions for Stock of Order` (tc_pfa01).

## Recommended Fix

- Verify the offer report's expected account data and filter inputs.
- Check the stock-orders save dialog and OK-button readiness before the 10-second wait expires.

## Prevention

- Keep offer-report fixtures deterministic.
- Keep stock-orders dialog synchronization aligned with the UI state.
