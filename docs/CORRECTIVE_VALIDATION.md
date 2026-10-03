# V10.1 corrective validation

V10.1 was introduced after an audit of the accelerated P5-P10 run.

## Issue corrected

The original V10 non-unit-cost evaluator described score/cost selection but ranked by raw score before truncating at the budget. V10.1 corrected the implementation to rank by score density for the base-plus-length cost.

## Additional validation added

V10.1 also added:

- true grouped-spatial retraining rather than spatial reporting of existing predictions;
- OSM road-identity recurrence auditing across event holdouts;
- score calibration and risk/uncertainty equivalence auditing;
- 20 sparse hazard-observation replicates per observation fraction;
- refreshed 5,000-resample event bootstrap statistics.

## Scientific consequence

The correction changed the non-unit-cost interpretation materially. At the 10% base-plus-length budget, bridge-first is marginally above the proposed policy. The event-bootstrap interval crosses zero, so no superiority claim is supported.

V10.1 preserved the original V10 outputs for audit and did not retune the predictive models after the correction.
