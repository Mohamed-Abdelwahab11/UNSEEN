#!/usr/bin/env python3
"""UNSEEN Framework Setup & Integrity Verification Script.

Executes standalone smoke tests across the package without external dependencies.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

# Add src to Python path
repo_root = Path(__file__).resolve().parent.parent
src_dir = repo_root / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))


def run_checks() -> int:
    print("=" * 70)
    print("  UNSEEN: Environment & Package Verification")
    print("=" * 70)

    errors: list[str] = []

    # 1. Package Import & Version
    try:
        import unseen

        print(f"[✓] Successfully imported 'unseen' package (version {unseen.__version__})")
    except Exception as exc:
        errors.append(f"Package import failed: {exc}")
        print(f"[✗] Failed to import 'unseen': {exc}")
        return 1

    # 2. Submodule Imports
    submodules = [
        "unseen.data",
        "unseen.retrieval",
        "unseen.matching",
        "unseen.features",
        "unseen.models",
        "unseen.counterfactual",
        "unseen.anomaly",
        "unseen.calibration",
        "unseen.explainability",
        "unseen.evaluation",
        "unseen.visualization",
    ]
    for mod in submodules:
        try:
            __import__(mod)
            print(f"[✓] Submodule '{mod}' imported cleanly")
        except Exception as exc:
            errors.append(f"Submodule import failed ({mod}): {exc}")
            print(f"[✗] Submodule '{mod}' failed: {exc}")

    # 3. Schema Instantiation
    try:
        from unseen.data.schemas import (
            BlindSpotCandidate,
            CoverageObservation,
            MediaOutlet,
            NewsArticle,
            RealWorldEvent,
        )

        event = RealWorldEvent(
            event_id="TEST-001",
            name="Verification Test Flood",
            event_type="flood",
            timestamp=datetime.now(timezone.utc),
            country_code="EG",
            latitude=30.0444,
            longitude=31.2357,
            severity_score=0.75,
            fatalities=12,
            affected_population=5000,
        )
        assert event.event_id == "TEST-001"
        assert event.to_dict()["country_code"] == "EG"

        outlet = MediaOutlet(
            outlet_id="reuters",
            name="Reuters",
            home_country="GB",
            geographic_scope="international",
        )
        assert outlet.outlet_id == "reuters"

        article = NewsArticle(
            article_id="ART-001",
            outlet_id="reuters",
            published_at=datetime.now(timezone.utc),
            headline="Flooding Reported in Urban Areas",
        )
        assert article.article_id == "ART-001"

        obs = CoverageObservation(
            event_id=event.event_id,
            outlet_id=outlet.outlet_id,
            covered=False,
        )
        assert obs.covered is False

        candidate = BlindSpotCandidate(
            event_id=event.event_id,
            outlet_id=outlet.outlet_id,
            expected_probability=0.88,
            calibrated_probability=0.85,
            anomaly_score=2.75,
            confidence_interval_low=0.78,
            confidence_interval_high=0.92,
            is_statistically_significant=True,
        )
        assert candidate.is_statistically_significant is True
        print("[✓] All data schemas instantiated and validated successfully")
    except Exception as exc:
        errors.append(f"Schema verification failed: {exc}")
        print(f"[✗] Schema verification failed: {exc}")

    # 4. Metric Computations
    try:
        from unseen.anomaly.base import ResidualAnomalyDetector
        from unseen.calibration.base import compute_expected_calibration_error
        from unseen.evaluation.metrics import (
            brier_score,
            log_loss_score,
            mean_reciprocal_rank,
            recall_at_k,
        )
        from unseen.explainability.base import RuleBasedOmissionExplainer

        # Brier Score
        bs = brier_score([1, 0], [1.0, 0.0])
        assert abs(bs - 0.0) < 1e-6

        # ECE
        ece = compute_expected_calibration_error([1, 0], [0.5, 0.5], n_bins=2)
        assert abs(ece - 0.0) < 1e-6

        # Log Loss
        ll = log_loss_score([1, 0], [0.8, 0.2])
        assert ll > 0.0

        # Retrieval MRR & Recall@K
        mrr = mean_reciprocal_rank([[1, 0], [0, 1]])
        assert abs(mrr - 0.75) < 1e-6

        rec = recall_at_k([[0, 1], [1, 0]], k=1)
        assert abs(rec - 0.5) < 1e-6

        # Anomaly scoring
        detector = ResidualAnomalyDetector(min_expected_prob=0.70)
        is_anom = detector.is_anomalous_omission(expected_prob=0.90, observed_coverage=False)
        assert is_anom is True

        # Explainer
        explainer = RuleBasedOmissionExplainer()
        explanation = explainer.explain_omission(
            candidate=candidate,
            features={"severity": 0.75, "distance_km": 1500.0},
            twin_evidence=[{"event_id": "TWIN-1", "covered": True}],
        )
        assert "summary" in explanation
        print("[✓] Metric, anomaly detector, and explainer functions verified")
    except Exception as exc:
        errors.append(f"Evaluation metrics verification failed: {exc}")
        print(f"[✗] Evaluation metrics verification failed: {exc}")

    print("=" * 70)
    if not errors:
        print("  ALL VERIFICATION CHECKS PASSED (100%)")
        print("=" * 70)
        return 0
    else:
        print(f"  VERIFICATION FAILED WITH {len(errors)} ERROR(S)")
        for err in errors:
            print(f"  - {err}")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    sys.exit(run_checks())
