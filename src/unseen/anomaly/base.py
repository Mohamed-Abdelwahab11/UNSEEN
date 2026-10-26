"""Anomaly detection interfaces for media omission auditing."""

from __future__ import annotations

import abc
import math
from typing import Any

from unseen.data.schemas import BlindSpotCandidate


class BaseAnomalyDetector(abc.ABC):
    """Abstract interface for detecting statistically unusual non-coverage."""

    def __init__(
        self,
        min_expected_prob: float = 0.70,
        significance_threshold: float = 2.0,
    ) -> None:
        self.min_expected_prob = min_expected_prob
        self.significance_threshold = significance_threshold

    @abc.abstractmethod
    def compute_anomaly_score(
        self,
        expected_prob: float,
        observed_coverage: bool | int,
        variance: float = 0.0,
    ) -> float:
        """Compute deviation score for an observation.

        Args:
            expected_prob: Calibrated model expectation P(Y=1).
            observed_coverage: Ground truth binary coverage (0 or 1).
            variance: Estimated prediction variance or epistemic uncertainty.

        Returns:
            Normalized anomaly score (higher implies more anomalous omission).
        """
        raise NotImplementedError

    def is_anomalous_omission(
        self,
        expected_prob: float,
        observed_coverage: bool | int,
        variance: float = 0.0,
    ) -> bool:
        """Evaluate if an event-outlet pair constitutes a statistically anomalous omission."""
        if observed_coverage:
            return False
        if expected_prob < self.min_expected_prob:
            return False
        score = self.compute_anomaly_score(expected_prob, observed_coverage, variance)
        return score >= self.significance_threshold


class ResidualAnomalyDetector(BaseAnomalyDetector):
    """Standardized residual anomaly detector based on binomial variance."""

    def compute_anomaly_score(
        self,
        expected_prob: float,
        observed_coverage: bool | int,
        variance: float = 0.0,
    ) -> float:
        observed_val = 1.0 if observed_coverage else 0.0
        # If event was covered, omission anomaly is 0
        if observed_val == 1.0:
            return 0.0

        # Binomial standard deviation plus epistemic uncertainty
        denom = math.sqrt(expected_prob * (1.0 - expected_prob) + variance + 1e-6)
        residual = (expected_prob - observed_val) / denom
        return max(0.0, residual)
