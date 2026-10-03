from pathlib import Path
import json
import math
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / "results" / "frozen"
A = ROOT / "audits"

def close(a, b, tol=1e-10):
    return math.isclose(float(a), float(b), rel_tol=0.0, abs_tol=tol)

def main():
    p4 = pd.read_csv(R / "P4_V9_event_summary.csv")
    p5 = pd.read_csv(R / "P5_V10_event_summary.csv")
    p7 = pd.read_csv(R / "P7_V10_leave_one_event_out_metrics.csv")
    spatial = pd.read_csv(R / "P10_V10_1_spatial_validation_summary.csv")
    policy = pd.read_csv(R / "P10_V10_1_policy_summary.csv")
    ident = pd.read_csv(R / "P9_V10_1_osm_identity_overlap_audit.csv")
    calib = pd.read_csv(R / "P9_V10_1_probability_calibration_audit.csv")
    sparse = pd.read_csv(R / "P10_V10_1_sparse_summary_20reps.csv")
    stats = json.loads((R / "P10_V10_1_STATISTICS.json").read_text())
    claims = json.loads((R / "P10_V10_1_CLAIM_AUDIT.json").read_text())
    p4audit = json.loads((A / "P4_V9_5_3_2020_COMPLETENESS_AUDIT.json").read_text())

    assert len(p4) == len(p5) == 4
    assert int(p4["topological_edges"].sum()) == 258560
    assert int(p5["support_eligible_edges"].sum()) == 211175

    positives = (p5["support_eligible_edges"] * p5["primary_positive_rate"]).sum()
    assert close(positives, 2487.0, 1e-6)

    means = p7.groupby("regime")["auprc"].mean()
    assert close(means["M1_geography_only"], 0.16250367424914286)
    assert close(means["M4_combined"], 0.02974313487920546)

    ss = spatial.set_index("regime")
    assert close(ss.loc["M3_dynamic_hazard_only", "auprc_mean"], 0.16066084940079212)
    assert close(ss.loc["M4_combined", "auroc_mean"], 0.8978007466644226)

    ten_unit = policy[(policy.cost_model == "unit") & (policy.budget_fraction == 0.1)].set_index("policy")
    ten_len = policy[(policy.cost_model == "length") & (policy.budget_fraction == 0.1)].set_index("policy")
    assert close(ten_unit.loc["proposed", "mean"], 0.3689707702575886)
    assert close(ten_unit.loc["risk", "mean"], 0.3529367395340928)
    assert close(ten_len.loc["bridge", "mean"], 0.10438954034635807)
    assert close(ten_len.loc["proposed", "mean"], 0.10311930570476481)

    assert close(ident["row_overlap_fraction"].mean(), 0.6950127926942564)
    assert bool(calib["risk_uncertainty_rank_identical"].all())
    assert (calib["p_max"] < 0.5).all()
    assert list(sparse["observed_fraction"]) == [0.1, 0.3, 0.5, 0.7, 0.9]

    assert stats["bootstrap_resamples"] == 5000
    assert stats["cost_models"]["unit"]["event_bootstrap_95ci"][0] < 0 < stats["cost_models"]["unit"]["event_bootstrap_95ci"][1]
    assert stats["cost_models"]["length"]["event_bootstrap_95ci"][0] < 0 < stats["cost_models"]["length"]["event_bootstrap_95ci"][1]

    assert claims["spatial_blocks"] == 135
    assert claims["sparse_replicates_per_fraction"] == 20
    assert claims["unit_cost_proposed_superiority_supported"] is False
    assert claims["length_cost_proposed_superiority_supported"] is False

    assert p4audit["pass_gate"] is True
    assert p4audit["grid_candidate_sets_equal"] is True
    assert p4audit["candidate_symmetric_difference_count"] == 0
    assert p4audit["prior_recovery_grid_4x4"] >= 0.9999
    assert p4audit["prior_recovery_grid_5x3"] >= 0.9999

    print("PASS: frozen PAPER004 evidence is internally consistent.")

if __name__ == "__main__":
    main()
