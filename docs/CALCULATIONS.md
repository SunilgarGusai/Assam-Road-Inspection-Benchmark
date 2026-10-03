# Calculations

## Primary road-exposure target

For edge (e),

[
y_e = 1\{f_e^{(medium)} \ge 0.10\},
]

where (f_e^{(medium)}) is the fraction of valid along-edge samples intersecting the medium Sentinel-1 flood mask.

## Network-consequence proxy

[
C_e = \operatorname{clip}(0.35B_e + 0.25S_e + 0.20Q_e + 0.10A_e + 0.10H_e, 0, 1).
]

The component weights are fixed heuristic design choices, not calibrated agency costs.

## Risk and uncertainty

Let (p_e) be the frozen M4 model score:

[
h_e = 4p_e(1-p_e).
]

All frozen M4 scores are below 0.5, so (h_e) is monotone in (p_e) over the observed range. Risk and uncertainty therefore produce the same unit-cost ranking in every event.

## Proposed inspection score

[
s_e = (p_e + 0.35h_e)(0.25 + 0.75C_e).
]

This is a fixed heuristic decision score, not a fitted causal utility model.

## Retrospective evaluation utility

[
U_e = y_e L_e(0.25 + 0.75C_e),
]

where (L_e) is road-edge length. The oracle quantity is used only after ranking.

## Inspection costs

Unit cost:

[
c_e = 1.
]

Base-plus-length cost:

[
c_e = 1 + L_e/\operatorname{median}(L).
]

For non-unit cost, V10.1 ranks by score density (s_e/c_e) and adds links greedily while the total budget remains feasible.

## 10% bootstrap conclusion

Unit cost:

- proposed = 0.36897
- risk = 0.35294
- difference = +0.01603
- 95% event-bootstrap interval = [-0.05129, 0.08336]

Base-plus-length:

- proposed = 0.10312
- bridge = 0.10439
- difference = -0.00127
- 95% event-bootstrap interval = [-0.07660, 0.11049]

Both intervals cross zero. No statistically resolved superiority claim is made.
