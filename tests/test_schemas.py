"""Unit tests for UNSEEN data schemas."""

import dataclasses
from datetime import datetime, timezone

from unseen.data.schemas import (
    BlindSpotCandidate,
    CoverageObservation,
    MediaOutlet,
    NewsArticle,
    RealWorldEvent,
)


def _get_sample_event() -> RealWorldEvent:
    return RealWorldEvent(
        event_id="EQ-2026-TUR-01",
        name="Eastern Mediterranean Earthquake",
        event_type="earthquake",
        timestamp=datetime(2026, 2, 6, 4, 17, tzinfo=timezone.utc),
        country_code="TR",
        latitude=37.174,
        longitude=37.032,
        severity_score=7.8,
        fatalities=50000,
        affected_population=14000000,
        source_registry="EM-DAT",
        metadata={"depth_km": 17.9},
    )


def _get_sample_article() -> NewsArticle:
    return NewsArticle(
        article_id="art_reuters_001",
        outlet_id="reuters",
        published_at=datetime(2026, 2, 6, 6, 0, tzinfo=timezone.utc),
        headline="Major 7.8 Magnitude Earthquake Strikes Southern Turkey and Syria",
        lead_paragraph="A devastating 7.8-magnitude earthquake rocked southern Turkey and northern Syria early Monday.",
        url="https://www.reuters.com/world/middle-east/major-earthquake-hits-turkey-2026-02-06/",
        language="en",
    )


def _get_sample_outlet() -> MediaOutlet:
    return MediaOutlet(
        outlet_id="reuters",
        name="Reuters",
        home_country="GB",
        geographic_scope="international",
        topical_focus=["general", "breaking_news", "international"],
    )


def test_real_world_event_schema(sample_event=None):
    event = sample_event or _get_sample_event()
    assert event.event_id == "EQ-2026-TUR-01"
    assert event.event_type == "earthquake"
    assert event.fatalities == 50000

    data = event.to_dict()
    assert data["event_id"] == "EQ-2026-TUR-01"
    assert "timestamp" in data
    assert isinstance(data["timestamp"], str)

    # Immutability check
    try:
        event.fatalities = 100
        raise AssertionError("RealWorldEvent should be frozen/immutable")
    except dataclasses.FrozenInstanceError:
        pass


def test_news_article_schema(sample_article=None):
    article = sample_article or _get_sample_article()
    assert article.article_id == "art_reuters_001"
    assert article.outlet_id == "reuters"

    data = article.to_dict()
    assert data["article_id"] == "art_reuters_001"
    assert isinstance(data["published_at"], str)


def test_media_outlet_schema(sample_outlet=None):
    outlet = sample_outlet or _get_sample_outlet()
    assert outlet.outlet_id == "reuters"
    assert outlet.home_country == "GB"
    assert "international" in outlet.topical_focus


def test_coverage_observation_schema():
    obs = CoverageObservation(
        event_id="EQ-2026-TUR-01",
        outlet_id="reuters",
        covered=True,
        matched_article_ids=["art_reuters_001"],
        max_similarity_score=0.92,
    )
    assert obs.covered is True
    assert len(obs.matched_article_ids) == 1
    assert obs.max_similarity_score == 0.92


def test_blind_spot_candidate_schema():
    cand = BlindSpotCandidate(
        event_id="EQ-2026-TUR-01",
        outlet_id="some_outlet",
        expected_probability=0.88,
        calibrated_probability=0.85,
        anomaly_score=2.65,
        confidence_interval_low=0.78,
        confidence_interval_high=0.92,
        is_statistically_significant=True,
    )
    assert cand.is_statistically_significant is True
    assert cand.anomaly_score == 2.65
