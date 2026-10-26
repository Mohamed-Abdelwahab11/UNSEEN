"""Feature engineering interfaces for expected coverage modeling."""

from __future__ import annotations

import abc
import math
from typing import Any

from unseen.data.schemas import MediaOutlet, RealWorldEvent


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate the great-circle distance between two points on Earth in kilometers.

    Args:
        lat1, lon1: First coordinate in decimal degrees.
        lat2, lon2: Second coordinate in decimal degrees.

    Returns:
        Distance in kilometers.
    """
    r = 6371.0  # Earth radius in kilometers
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (
        math.sin(delta_phi / 2.0) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
    )
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return r * c


class BaseFeatureExtractor(abc.ABC):
    """Abstract interface for extracting covariate vectors for (event, outlet) pairs."""

    @abc.abstractmethod
    def extract_features(
        self,
        event: RealWorldEvent,
        outlet: MediaOutlet,
        context: dict[str, Any] | None = None,
    ) -> dict[str, float]:
        """Extract a structured feature dictionary for a single observation pair.

        Args:
            event: Ground-truth real-world event.
            outlet: Media organization.
            context: Additional environmental context (e.g., global news congestion).

        Returns:
            Dictionary mapping feature names to numerical values.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def feature_names(self) -> list[str]:
        """Return the complete ordered list of feature names produced by this extractor."""
        raise NotImplementedError
