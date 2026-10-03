from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / "results" / "frozen"

p5 = pd.read_csv(R / "P5_V10_event_summary.csv")
p7 = pd.read_csv(R / "P7_V10_leave_one_event_out_metrics.csv")
sp = pd.read_csv(R / "P10_V10_1_spatial_validation_summary.csv")
policy = pd.read_csv(R / "P10_V10_1_policy_summary.csv")
stats = json.loads((R / "P10_V10_1_STATISTICS.json").read_text())

print("ASSAM ROAD INSPECTION BENCHMARK")
print("=" * 40)
print(f"Supported edge-event observations: {int(p5.support_eligible_edges.sum()):,}")
print(f"Primary positives: {(p5.support_eligible_edges*p5.primary_positive_rate).sum():.0f}")

print("\nLeave-one-event-out mean AUPRC")
print(p7.groupby("regime")["auprc"].mean().round(4).to_string())

print("\nGrouped-spatial mean AUPRC")
print(sp.set_index("regime")["auprc_mean"].round(4).to_string())

for cost in ("unit", "length"):
    q = policy[(policy.cost_model == cost) & (policy.budget_fraction == 0.1)]
    print(f"\n10% {cost} budget utility")
    print(q.sort_values("mean", ascending=False)[["policy","mean"]].to_string(index=False))

print("\nBootstrap conclusion")
for cost, d in stats["cost_models"].items():
    lo, hi = d["event_bootstrap_95ci"]
    print(f"{cost}: difference={d['difference_mean']:.4f}, 95% CI=[{lo:.4f}, {hi:.4f}]")
