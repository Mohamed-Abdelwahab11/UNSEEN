"""Uncertainty estimation and probability calibration interfaces."""

from __future__ import annotations

import abc
import math
from typing import Any


def compute_expected_calibration_error(
    y_true: list[int],
    y_prob: list[float],
    n_bins: int = 10,
) -> float:
    """Compute Expected Calibration Error (ECE) across partitioned probability bins.

    ECE = sum_{m=1}^M (|B_m| / N) * |acc(B_m) - conf(B_m)|

    Args:
        y_true: Ground-truth binary labels (0 or 1).
        y_prob: Predicted probabilities in [0.0, 1.0].
        n_bins: Number of equal-width probability bins.

    Returns:
        Scalar ECE value in [0.0, 1.0].
    """
    if len(y_true) != len(y_prob):
        raise ValueError("y_true and y_prob must have identical lengths.")
    if len(y_true) == 0:
        return 0.0

    bin_boundaries = [i / n_bins for i in range(n_bins + 1)]
    ece = 0.0
    total_samples = len(y_true)

    for i in range(n_bins):
        bin_lower = bin_boundaries[i]
        bin_upper = bin_boundaries[i + 1]

        # Filter items falling in bin [lower, upper) (inclusive of upper for final bin)
        bin_indices = [
            idx
            for idx, p in enumerate(y_prob)
            if (bin_lower <= p < bin_upper) or (i == n_bins - 1 and bin_lower <= p <= bin_upper)
        ]

        bin_size = len(bin_indices)
        if bin_size > 0:
            bin_acc = sum(y_true[idx] for idx in bin_indices) / bin_size
            bin_conf = sum(y_prob[idx] for idx in bin_indices) / bin_size
            ece += (bin_size / total_samples) * abs(bin_acc - bin_conf)

    return ece


class BaseCalibrator(abc.ABC):
    """Abstract interface for post-hoc probability calibration."""

    def __init__(self) -> None:
        self.is_fitted = False

    @abc.abstractmethod
    def fit(self, y_prob: list[float], y_true: list[int]) -> BaseCalibrator:
        """Fit calibration mapping on validation probabilities and labels."""
        raise NotImplementedError

    @abc.abstractmethod
    def calibrate(self, y_prob: list[float]) -> list[float]:
        """Apply calibration mapping to uncalibrated probabilities."""
        raise NotImplementedError
