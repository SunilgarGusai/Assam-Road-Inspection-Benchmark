# Frozen public method protocol

## Scope

This document describes the public computational logic behind the frozen PAPER004 evidence. It is a reviewer-facing protocol, not a replacement for the multi-gigabyte historical raw-data workspace.

## Event design

Four Assam flood events were fixed before downstream modelling: 18 July 2020, 28 August 2021, 16 June 2022 and 22 June 2023. Dated pre-event OpenStreetMap/Geofabrik road snapshots were used for each event.

## Flood-exposure target

Sentinel-1 event masks were created independently of road/network outcomes. The primary edge target is positive when at least 10% of valid along-edge samples intersect the medium flood mask. Strict and liberal masks are retained as target-sensitivity checks.

## Predictor firewall

- Flood masks are evaluation-only targets.
- Raw longitude/latitude appear only in the M1 geography-control experiment.
- M2/M3/M4 exclude raw coordinates.
- Road/network features are static or pre-event.
- Rainfall features are kept separate from the retrospective flood labels.

## Network consequence

The public decision layer uses a transparent heuristic consequence score combining graph bridges, bridge split fraction, approximate edge betweenness, articulation-endpoint information and road hierarchy. It is not traffic assignment or emergency-facility accessibility simulation.

## Model regimes

Four Extra-Trees regimes are compared: geography only; road/network/environment; dynamic hazard only; and combined road/environment + hazard.

## Transfer validation

Two questions are kept separate:

- leave-one-event-out transfer across the four floods;
- true grouped spatial retraining over 135 0.25-degree blocks using five folds.

## Inspection policies

Eight fixed ranking policies are evaluated under 1%, 2.5%, 5%, 10%, 15% and 20% budgets.

The non-unit cost was corrected in V10.1 to use score/cost density before enforcing the budget. The procedure is a transparent greedy heuristic and is not claimed as an exact 0-1 knapsack optimizer.

## Robustness

The frozen V10.1 package includes OSM identity-overlap auditing, calibration auditing, risk-versus-uncertainty rank-equivalence auditing, strict/medium/liberal target sensitivity, 20-replicate sparse hazard-observation stress tests and 5,000 event-level bootstrap resamples.
