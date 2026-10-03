# Results freeze

The public numerical state is frozen at **P10 V10.1**.

V10.1 was a corrective validation stage, not a result-tuning stage. It:

- corrected non-unit-cost selection to score/cost density;
- preserved the original V10 outputs for audit;
- added true grouped-spatial retraining;
- audited OSM identity recurrence;
- audited score calibration and risk/uncertainty ranking equivalence;
- increased sparse hazard-observation testing to 20 replicates per fraction.

No model was retuned after these corrective results were observed.

## Frozen claim gate

- `unit_cost_proposed_superiority_supported = false`
- `length_cost_proposed_superiority_supported = false`

Future repository maintenance should not change frozen numbers simply to make the method appear stronger.
