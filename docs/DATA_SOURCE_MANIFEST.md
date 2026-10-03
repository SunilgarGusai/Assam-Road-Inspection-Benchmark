# Data-source manifest

| Evidence layer | Source | Frozen study use | Redistribution |
|---|---|---|---|
| Flood mapping | Sentinel-1 GRD / Copernicus | Four event-specific pre/event SAR pairs | No raw scenes redistributed |
| Terrain | SRTM 1 arc-second HGT | Terrain correction and road-environment features | No raw tiles redistributed |
| Rainfall | ERA5 hourly total precipitation | Primary dynamic rainfall features | No raw archive redistributed |
| Rainfall sensitivity | CHIRPS daily rainfall | Secondary rainfall sensitivity | No raw archive redistributed |
| Roads | Geofabrik dated OpenStreetMap PBF snapshots | Strictly pre-event road reconstruction | No raw PBF snapshots redistributed |

## Event road snapshots

| Event | Flood date | Frozen OSM snapshot | Lag |
|---|---|---|---:|
| ASSAM_2020_MONSOON | 2020-07-18 | 2020-01-01 | 199 d |
| ASSAM_2021_AUG | 2021-08-28 | 2021-01-01 | 239 d |
| ASSAM_2022_JUNE | 2022-06-16 | 2022-01-01 | 166 d |
| ASSAM_2023_JUNE | 2023-06-22 | 2023-01-01 | 172 d |

## Rainfall-source amendment

GSMaP-ISRO was an initial target source but was not used after automated acquisition proved unavailable. ERA5 plus CHIRPS was frozen before downstream outcome modelling.

Users should obtain current access URLs and provider terms directly from the original services.
