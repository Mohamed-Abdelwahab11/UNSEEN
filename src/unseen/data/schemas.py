"""Core data models and schemas for the UNSEEN framework."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class RealWorldEvent:
    """Represents a verified occurrence from an independent ground-truth registry."""

    event_id: str
    name: str
    event_type: str  # e.g., 'earthquake', 'flood', 'wildfire'
    timestamp: datetime
    country_code: str  # ISO-3166-1 alpha-2 or alpha-3
    latitude: float
    longitude: float
    severity_score: float  # Normalized 0.0 to 1.0 or Richter / hazard scale
    fatalities: int = 0
    affected_population: int = 0
    source_registry: str = "EM-DAT"  # e.g., 'EM-DAT', 'GDACS', 'ReliefWeb'
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert event object to dictionary."""
        data = asdict(self)
        data["timestamp"] = self.timestamp.isoformat()
        return data


@dataclass(frozen=True)
class NewsArticle:
    """Represents an ingested news report from a monitored media organization."""

    article_id: str
    outlet_id: str
    published_at: datetime
    headline: str
    lead_paragraph: str = ""
    url: str = ""
    language: str = "en"
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert article object to dictionary."""
        data = asdict(self)
        data["published_at"] = self.published_at.isoformat()
        return data


@dataclass(frozen=True)
class MediaOutlet:
    """Represents a monitored news organization and its structural profile."""

    outlet_id: str
    name: str
    home_country: str
    geographic_scope: str = "international"  # 'international', 'national', 'regional'
    topical_focus: list[str] = field(default_factory=lambda: ["general"])
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert outlet object to dictionary."""
        return asdict(self)


@dataclass(frozen=True)
class CoverageObservation:
    """Observation record pairing an event with an outlet's coverage response."""

    event_id: str
    outlet_id: str
    covered: bool
    matched_article_ids: list[str] = field(default_factory=list)
    max_similarity_score: float = 0.0
    observation_window_days: int = 7
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert coverage observation to dictionary."""
        return asdict(self)


@dataclass(frozen=True)
class BlindSpotCandidate:
    """Result of an anomaly audit for an unobserved event-outlet pair."""

    event_id: str
    outlet_id: str
    expected_probability: float
    calibrated_probability: float
    anomaly_score: float
    confidence_interval_low: float
    confidence_interval_high: float
    counterfactual_twins: list[str] = field(default_factory=list)
    is_statistically_significant: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert blind spot candidate record to dictionary."""
        return asdict(self)
