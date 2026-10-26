"""Visualization utilities for diagnostic audit reporting and reliability diagrams."""

from __future__ import annotations

from pathlib import Path
from typing import Sequence


def plot_reliability_diagram(
    y_true: Sequence[int],
    y_prob: Sequence[float],
    n_bins: int = 10,
    save_path: str | Path | None = None,
) -> None:
    """Generate and optionally save an empirical reliability diagram.

    Args:
        y_true: Ground truth binary targets.
        y_prob: Predicted model probabilities in [0.0, 1.0].
        n_bins: Bin granularity.
        save_path: Destination file path (e.g., 'reports/figures/calibration_curve.png').
    """
    try:
        import matplotlib
        matplotlib.use("Agg")  # Non-interactive headless backend
        import matplotlib.pyplot as plt
    except ImportError:
        return

    bin_boundaries = [i / n_bins for i in range(n_bins + 1)]
    bin_confs = []
    bin_accs = []

    for i in range(n_bins):
        lower = bin_boundaries[i]
        upper = bin_boundaries[i + 1]
        indices = [
            idx for idx, p in enumerate(y_prob)
            if (lower <= p < upper) or (i == n_bins - 1 and lower <= p <= upper)
        ]
        if indices:
            bin_accs.append(sum(y_true[idx] for idx in indices) / len(indices))
            bin_confs.append(sum(y_prob[idx] for idx in indices) / len(indices))

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Perfect Calibration")
    ax.plot(bin_confs, bin_accs, marker="o", linewidth=2, color="#1f77b4", label="Model")
    ax.set_xlabel("Mean Predicted Probability (Confidence)")
    ax.set_ylabel("Empirical True Positive Frequency (Accuracy)")
    ax.set_title("Reliability Diagram (Calibration Curve)")
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.grid(True, alpha=0.3)
    ax.legend()

    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
