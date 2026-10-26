"""Explainable AI interfaces for contextualizing media omissions."""

from __future__ import annotations

import abc
from typing import Any

from unseen.data.schemas import BlindSpotCandidate


class BaseOmissionExplainer(abc.ABC):
    """Abstract interface for explaining why an event was expected to be covered."""

    @abc.abstractmethod
    def explain_omission(
        self,
        candidate: BlindSpotCandidate,
        features: dict[str, float],
        twin_evidence: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """Generate human-interpretable audit explanation for a detected blind spot.

        Args:
            candidate: Flagged blind spot candidate record.
            features: Numerical feature map for this event-outlet instance.
            twin_evidence: Historical matched twin events and their coverage status.

        Returns:
            Structured dictionary containing narrative summary, top feature drivers,
            and comparative historical evidence.
        """
        raise NotImplementedError


class RuleBasedOmissionExplainer(BaseOmissionExplainer):
    """Transparent baseline explainer articulating statistical coverage expectation."""

    def explain_omission(
        self,
        candidate: BlindSpotCandidate,
        features: dict[str, float],
        twin_evidence: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        twin_evidence = twin_evidence or []
        covered_twins = [t for t in twin_evidence if t.get("covered", False)]

        summary = (
            f"Event '{candidate.event_id}' had a calibrated coverage expectation of "
            f"{candidate.calibrated_probability * 100:.1f}% for outlet '{candidate.outlet_id}'. "
        )

        if twin_evidence:
            summary += (
                f"Historically, this outlet covered {len(covered_twins)} of "
                f"{len(twin_evidence)} comparable events in this domain."
            )

        return {
            "event_id": candidate.event_id,
            "outlet_id": candidate.outlet_id,
            "summary": summary,
            "calibrated_expectation": candidate.calibrated_probability,
            "anomaly_score": candidate.anomaly_score,
            "top_features": sorted(features.items(), key=lambda item: abs(item[1]), reverse=True)[:5],
            "twin_count": len(twin_evidence),
            "twin_covered_count": len(covered_twins),
        }
