"""Evaluation metrics for retrieval, expected coverage prediction, and calibration."""

from __future__ import annotations

import math
from typing import Sequence

from unseen.calibration.base import compute_expected_calibration_error


def brier_score(y_true: Sequence[int], y_prob: Sequence[float]) -> float:
    """Compute the Brier Score (Mean Squared Error of predicted probabilities).

    BS = (1 / N) * sum_{i=1}^N (p_i - y_i)^2
    """
    if len(y_true) != len(y_prob):
        raise ValueError("y_true and y_prob must have identical lengths.")
    if len(y_true) == 0:
        return 0.0
    return sum((p - y) ** 2 for y, p in zip(y_true, y_prob)) / len(y_true)


def log_loss_score(
    y_true: Sequence[int],
    y_prob: Sequence[float],
    eps: float = 1e-15,
) -> float:
    """Compute binary cross-entropy (Log Loss) with probability clipping."""
    if len(y_true) != len(y_prob):
        raise ValueError("y_true and y_prob must have identical lengths.")
    if len(y_true) == 0:
        return 0.0

    total_loss = 0.0
    for y, p in zip(y_true, y_prob):
        p_clipped = max(eps, min(1.0 - eps, p))
        total_loss += - (y * math.log(p_clipped) + (1 - y) * math.log(1.0 - p_clipped))
    return total_loss / len(y_true)


def mean_reciprocal_rank(ranked_hits: Sequence[Sequence[int]]) -> float:
    """Compute Mean Reciprocal Rank (MRR) across a collection of queries.

    Args:
        ranked_hits: List of binary relevance indicators for retrieved ranks per query
                     (e.g., [[0, 1, 0], [1, 0, 0]]).

    Returns:
        MRR score in [0.0, 1.0].
    """
    if not ranked_hits:
        return 0.0

    reciprocal_ranks = []
    for hits in ranked_hits:
        rr = 0.0
        for rank, is_relevant in enumerate(hits, start=1):
            if is_relevant:
                rr = 1.0 / rank
                break
        reciprocal_ranks.append(rr)

    return sum(reciprocal_ranks) / len(reciprocal_ranks)


def recall_at_k(ranked_hits: Sequence[Sequence[int]], k: int) -> float:
    """Compute Recall@K across queries with at least one relevant document.

    Args:
        ranked_hits: Binary relevance lists per query.
        k: Cutoff rank.

    Returns:
        Recall@K fraction in [0.0, 1.0].
    """
    if not ranked_hits or k <= 0:
        return 0.0

    hits_at_k = 0
    total_valid_queries = 0

    for hits in ranked_hits:
        total_relevant = sum(hits)
        if total_relevant > 0:
            total_valid_queries += 1
            if any(hits[:k]):
                hits_at_k += 1

    return hits_at_k / total_valid_queries if total_valid_queries > 0 else 0.0
