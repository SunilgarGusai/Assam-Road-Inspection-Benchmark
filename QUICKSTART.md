# Quickstart

The default path validates the committed frozen evidence; it does **not** download multi-gigabyte raw remote-sensing archives.

## 1. Environment

```bash
conda env create -f environment.yml
conda activate assam-road-inspection
```

or:

```bash
python -m pip install -r requirements.txt
```

## 2. Validate the frozen package

```bash
python scripts/validate_frozen_package.py
```

Expected final line:

```text
PASS: frozen PAPER004 evidence is internally consistent.
```

## 3. Print key scientific evidence

```bash
python scripts/summarize_key_results.py
```

This route verifies the public machine-readable evidence. It does not claim byte-identical reconstruction of the historical raw-data pipeline. See `docs/REPRODUCIBILITY.md`.
