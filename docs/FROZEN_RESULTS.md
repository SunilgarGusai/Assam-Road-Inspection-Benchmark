# Frozen result inventory

The scientific state is frozen at **P10 V10.1**.

## Event scale

| Event | Road edges | SAR-supported observations | Primary positive rate |
|---|---:|---:|---:|
| 2020 monsoon | 37,474 | 19,710 | 0.370% |
| 2021 Aug | 55,933 | 49,791 | 0.349% |
| 2022 Jun | 58,155 | 48,748 | 2.868% |
| 2023 Jun | 106,998 | 92,926 | 0.906% |
| **Total** | **258,560** | **211,175** | **2,487 positives** |

## Leave-one-event-out mean performance

| Regime | Mean AUPRC | Mean AUROC |
|---|---:|---:|
| M1 geography only | **0.1625** | 0.8309 |
| M2 road/network/environment | 0.0839 | 0.8329 |
| M3 dynamic hazard only | 0.0196 | 0.5586 |
| M4 combined | 0.0297 | 0.7257 |

## Grouped spatial validation

| Regime | Mean AUPRC | SD | Mean AUROC |
|---|---:|---:|---:|
| M1 geography only | 0.1161 | 0.1353 | 0.8401 |
| M2 road/network/environment | 0.0668 | 0.0539 | 0.8419 |
| M3 dynamic hazard only | **0.1607** | 0.1420 | 0.8701 |
| M4 combined | 0.1474 | 0.0747 | **0.8978** |

The reversal between event transfer and spatial transfer is a core result.

## 10% inspection budget

### Unit cost

- proposed: **0.36897**
- risk: **0.35294**
- difference: **+0.01603**
- 95% interval: **[-0.05129, 0.08336]**

### Base-plus-length cost

- bridge: **0.10439**
- proposed: **0.10312**
- difference: **-0.00127**
- 95% interval: **[-0.07660, 0.11049]**

Neither comparison supports a resolved superiority claim.

## Sparse hazard-observation stress test

| Observed ERA5 cells | AUPRC mean ± SD | 10% utility mean ± SD |
|---:|---:|---:|
| 10% | 0.0405 ± 0.0288 | 0.4384 ± 0.1331 |
| 30% | 0.0353 ± 0.0255 | 0.4133 ± 0.1280 |
| 50% | 0.0333 ± 0.0240 | 0.3876 ± 0.1361 |
| 70% | 0.0312 ± 0.0233 | 0.3847 ± 0.1430 |
| 90% | 0.0297 ± 0.0226 | 0.3729 ± 0.1608 |

This non-monotonic pattern is a robustness result, not evidence that fewer observations should be preferred operationally.
