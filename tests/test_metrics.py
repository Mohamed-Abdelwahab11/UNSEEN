"""Unit tests for statistical evaluation metrics and calibration."""

import math
from unseen.anomaly.base import ResidualAnomalyDetector
from unseen.calibration.base import compute_expected_calibration_error
from unseen.evaluation.metrics import (
    brier_score,
    log_loss_score,
    mean_reciprocal_rank,
    recall_at_k,
)


def test_brier_score_perfect_predictions():
    y_true = [1, 0, 1, 1, 0]
    y_prob = [1.0, 0.0, 1.0, 1.0, 0.0]
    assert math.isclose(brier_score(y_true, y_prob), 0.0, abs_tol=1e-6)


def test_brier_score_worst_predictions():
    y_true = [1, 0]
    y_prob = [0.0, 1.0]
    assert math.isclose(brier_score(y_true, y_prob), 1.0, abs_tol=1e-6)


def test_expected_calibration_error():
    # Perfectly calibrated case
    y_true = [1, 1, 0, 0]
    y_prob = [0.5, 0.5, 0.5, 0.5]
    ece = compute_expected_calibration_error(y_true, y_prob, n_bins=2)
    assert math.isclose(ece, 0.0, abs_tol=1e-6)

    # Empty case
    assert compute_expected_calibration_error([], []) == 0.0


def test_log_loss_score():
    y_true = [1, 0]
    y_prob = [0.9, 0.1]
    loss = log_loss_score(y_true, y_prob)
    expected = - (math.log(0.9) + math.log(0.9)) / 2.0
    assert math.isclose(loss, expected, rel_tol=1e-3)


def test_mean_reciprocal_rank():
    # Query 1: hit at rank 1 (1.0), Query 2: hit at rank 2 (0.5), Query 3: no hit (0.0)
    ranked_hits = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
    expected_mrr = (1.0 + 0.5 + 0.0) / 3.0
    assert math.isclose(mean_reciprocal_rank(ranked_hits), expected_mrr, abs_tol=1e-6)


def test_recall_at_k():
    ranked_hits = [[0, 1, 0], [0, 0, 1]]
    assert math.isclose(recall_at_k(ranked_hits, k=1), 0.0, abs_tol=1e-6)
    assert math.isclose(recall_at_k(ranked_hits, k=2), 0.5, abs_tol=1e-6)
    assert math.isclose(recall_at_k(ranked_hits, k=3), 1.0, abs_tol=1e-6)


def test_residual_anomaly_detector():
    detector = ResidualAnomalyDetector(min_expected_prob=0.70, significance_threshold=2.0)

    # Covered event should have 0 anomaly score
    score_covered = detector.compute_anomaly_score(expected_prob=0.85, observed_coverage=True)
    assert score_covered == 0.0
    assert detector.is_anomalous_omission(0.85, observed_coverage=True) is False

    # Uncovered event with high expectation
    score_omitted = detector.compute_anomaly_score(expected_prob=0.90, observed_coverage=False)
    assert score_omitted > 2.0
    assert detector.is_anomalous_omission(0.90, observed_coverage=False) is True

    # Low expectation event is ordinary non-coverage, not an anomalous omission
    assert detector.is_anomalous_omission(0.30, observed_coverage=False) is False
