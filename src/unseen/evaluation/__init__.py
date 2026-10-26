"""Evaluation metrics and benchmarking routines."""

from unseen.calibration.base import compute_expected_calibration_error
from unseen.evaluation.metrics import (
    brier_score,
    log_loss_score,
    mean_reciprocal_rank,
    recall_at_k,
)

__all__ = [
    "brier_score",
    "log_loss_score",
    "compute_expected_calibration_error",
    "mean_reciprocal_rank",
    "recall_at_k",
]
