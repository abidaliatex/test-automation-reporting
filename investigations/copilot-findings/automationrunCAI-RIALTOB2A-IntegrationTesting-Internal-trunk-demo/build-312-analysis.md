# Root Cause Analysis — Build 312

**Source Report:** [build-312.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-312.md)

---

## Build Summary

Build: automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #312
Total Tests: 14
Passed: 13
Failed: 1
Pass Rate: 92.9%

---

## Root Cause Groups

## discountType Field Not Propagated from Rialto to MediaHouse

**Affected Features:**
- rialtoB2A (CASS TC7 Change Date, Size & Placement)

**Affected Scenarios:**
- verify that order arrived in MH from Rialto - Change Date, Size & Placement (tc_getMHTC06)

**Failure Pattern:**
`orders[0].printDetails.discountType` expected `[RIALTO]` but found `[null]`

**Evidence:**
- `Mismatch on field: orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]` — caught by `SoftAssert.assertAll` in `ApiStepDefinition.tearDown` (line 69)
- The GET request to the MediaHouse basket order endpoint (`tc_getMHTC06`) returns the order but `discountType` is null instead of `RIALTO`
- All upstream steps passed: Rialto order was created, posted to Agency, synced to MH (70 s wait), initial GET confirmed order arrived (with correct fields), PATCH applied by MH, 60 s wait — the failure occurs on the first GET after the initial sync, not after the PATCH
- `failedSince: 312` — this is a new regression; prior builds of this suite did not fail on this assertion

**Impact:** 1 failure

**Confidence:** High

---

## Summary

Build 312 is UNSTABLE with 1 failure. The end-to-end flow for "Change Date, Size & Placement" (TC7) completes successfully up to and including the initial MH basket GET; however, `orders[0].printDetails.discountType` is returned as `null` from MediaHouse instead of the expected value `RIALTO`. This indicates that the discount type set in the Rialto order is either not being forwarded in the integration message to MH or is being dropped/not mapped on the MH side during order ingestion.

---

## Root Cause

The `discountType` field (`orders[0].printDetails.discountType`) is null in the MediaHouse response. Possible causes:
- The B2A integration layer that transforms and forwards the Rialto order to MediaHouse is not mapping or populating `discountType` in the outbound payload.
- A recent change to the Rialto or MH data model may have renamed or removed the field used to carry discount type information.
- The MH basket order endpoint may have a defect in deserialising or persisting this field.

---

## Affected Components

- Rialto → MediaHouse B2A integration message mapping (`discountType` field in `printDetails`)
- MediaHouse basket order GET endpoint (`getMHB2A.csv` / `tc_getMHTC06`)
- Test data file: `MediaHouse/getMHB2A.csv` — assertion on `orders[0].printDetails.discountType`

---

## Recommended Fix

- Inspect the B2A integration payload sent from Rialto to MH for TC7 and confirm whether `discountType` is present.
- Check MH order ingestion logic for mapping of `printDetails.discountType` from the incoming integration message.
- If a field rename occurred, align the mapping on both sides.

---

## Prevention

- Add a pre-assertion log step that dumps the full `printDetails` object to stdout before soft-assert evaluation, to aid faster diagnosis.
- Monitor `discountType` propagation in integration smoke tests to catch this regression class earlier in the pipeline.
