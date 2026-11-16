# Build 161 — Investigation Analysis

**Source report:** [build-161.md](../../../reports/build-failures/automationRunReports-trunk/build-161.md)

## Summary

- Build 161 was **UNSTABLE**: 51 of 53 tests passed (96.2%).
- Two scenarios failed, with distinct symptoms.

## Root Cause

- **Stock Orders filter save:** The test timed out waiting for the dialog's OK button to become clickable. Jenkins evidence identifies the failed wait and page-object method, but does not establish why the button was unavailable.
- **Offer report:** The generated data contained a different user value than expected. The result establishes a data mismatch, not its underlying cause.

## Affected Components

- `reports_stockoforders.feature` — saving a created filter as CSV.
- `report_offer.feature` — `User verifying offer reports` (`tc_offer01`).

## Recommended Fix

- Check the stock-orders dialog state when the save action runs and verify the OK button is available and enabled.
- Verify the offer report's filter and expected test data against the generated report.

## Prevention

- Keep the filter-save UI state and readiness checks deterministic.
- Use stable report test data and assertions that identify the mismatched field without exposing personal data.
