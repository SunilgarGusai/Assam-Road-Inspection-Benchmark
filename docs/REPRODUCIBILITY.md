# Reproducibility boundary

## Publicly checkable calculations

The repository supports independent checking of:

- total edge-event support and primary prevalence;
- leave-one-event-out metrics;
- grouped-spatial metrics;
- inspection-policy budget curves;
- 10% policy comparisons and bootstrap conclusions;
- sparse hazard-observation summaries;
- OSM identity recurrence;
- calibration and risk/uncertainty equivalence;
- the independent 2020 road-completeness gate.

## What is not redistributed

The repository intentionally excludes multi-gigabyte upstream data archives: Sentinel-1 scenes, ERA5 hourly archives, CHIRPS rasters, SRTM tiles and Geofabrik PBF files. Those sources remain under provider terms and are documented in `DATA_SOURCE_MANIFEST.md`.

## Historical versus reviewer-facing environment

The exact historical package versions of every P0-P10 dependency were not captured as a single lockfile. The repository therefore does **not** invent an exact historical environment.

The committed lightweight validation environment is:

- Python 3.13
- NumPy 2.3.5
- pandas 2.2.3

The original full pipeline additionally used SciPy, scikit-learn, NetworkX, rasterio, Shapely, pyproj, GeoPandas, joblib, Matplotlib and psutil.

## Verification

```bash
python scripts/validate_frozen_package.py
python scripts/summarize_key_results.py
```

GitHub Actions runs the invariant checks automatically on pushes and pull requests.
