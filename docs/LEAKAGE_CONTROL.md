# Leakage-control design

This study uses the term **leakage-controlled**, not leakage-proof.

## Controls implemented

1. Sentinel-1 flood masks are used only as retrospective evaluation labels.
2. Raw centroid longitude/latitude are isolated to M1 geography-only diagnostics.
3. M2, M3 and M4 exclude raw coordinates.
4. Historical road snapshots strictly predate each event.
5. Network-consequence descriptors are computed without label information.
6. Leave-one-event-out testing never trains on the held-out flood event.
7. Spatial validation retrains models while holding out grouped geographic blocks.

## What the design does not claim

- The SAR-derived target is not a confirmed road-closure record.
- LOEO is not transfer to a completely unseen road system; road identities recur across years.
- CHIRPS/ERA5 source latency is not simulated as a real-time operational system.
- The public repository is not evidence of field deployment.

The OSM identity audit is committed at `results/frozen/P9_V10_1_osm_identity_overlap_audit.csv`.
