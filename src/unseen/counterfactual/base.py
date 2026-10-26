"""Counterfactual and matched-event analysis interfaces."""

from __future__ import annotations

import abc
from typing import Any

from unseen.data.schemas import RealWorldEvent


class BaseCounterfactualAuditor(abc.ABC):
    """Abstract interface for matched-event counterfactual analysis."""

    @abc.abstractmethod
    def find_matched_events(
        self,
        target_event: RealWorldEvent,
        candidate_events: list[RealWorldEvent],
        k: int = 5,
    ) -> list[tuple[RealWorldEvent, float]]:
        """Identify the top-k historically most similar counterfactual twin events.

        Args:
            target_event: The unobserved or audited event.
            candidate_events: Historical pool of candidate real-world events.
            k: Number of nearest-neighbor counterfactual twins to return.

        Returns:
            List of (event, distance_or_similarity) tuples.
        """
        raise NotImplementedError

    def estimate_counterfactual_coverage(
        self,
        outlet_id: str,
        matched_events: list[RealWorldEvent],
        coverage_lookup: dict[tuple[str, str], bool],
    ) -> float:
        """Calculate the empirical coverage rate of the outlet across the matched twin cohort.

        Args:
            outlet_id: Target media outlet identifier.
            matched_events: Historical matched twins.
            coverage_lookup: Mapping from (event_id, outlet_id) to boolean covered status.

        Returns:
            Empirical coverage fraction in [0.0, 1.0].
        """
        if not matched_events:
            return 0.0
        covered_count = sum(
            1
            for e in matched_events
            if coverage_lookup.get((e.event_id, outlet_id), False)
        )
        return covered_count / len(matched_events)

    def audit_event_omission(
        self,
        target_event: RealWorldEvent,
        outlet_id: str,
        candidate_events: list[RealWorldEvent],
        coverage_lookup: dict[tuple[str, str], bool],
        k: int = 5,
    ) -> dict[str, Any]:
        """Perform full counterfactual audit for a specific event-outlet observation."""
        twins = self.find_matched_events(target_event, candidate_events, k=k)
        matched_event_list = [twin for twin, _ in twins]
        twin_coverage_rate = self.estimate_counterfactual_coverage(
            outlet_id, matched_event_list, coverage_lookup
        )
        actual_covered = coverage_lookup.get((target_event.event_id, outlet_id), False)

        return {
            "target_event_id": target_event.event_id,
            "outlet_id": outlet_id,
            "actual_covered": actual_covered,
            "twin_coverage_rate": twin_coverage_rate,
            "counterfactual_discrepancy": twin_coverage_rate - (1.0 if actual_covered else 0.0),
            "matched_twins": [
                {
                    "event_id": e.event_id,
                    "name": e.name,
                    "similarity": sim,
                    "covered": coverage_lookup.get((e.event_id, outlet_id), False),
                }
                for e, sim in twins
            ],
        }
