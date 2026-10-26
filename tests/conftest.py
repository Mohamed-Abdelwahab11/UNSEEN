"""Shared test fixtures for the UNSEEN test suite."""

from __future__ import annotations

from datetime import datetime, timezone

import pytest
from unseen.data.schemas import (
    MediaOutlet,
    NewsArticle,
    RealWorldEvent,
)


@pytest.fixture
def sample_event() -> RealWorldEvent:
    """Fixture providing a verified real-world disaster event."""
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


@pytest.fixture
def sample_article() -> NewsArticle:
    """Fixture providing a mock news article."""
    return NewsArticle(
        article_id="art_reuters_001",
        outlet_id="reuters",
        published_at=datetime(2026, 2, 6, 6, 0, tzinfo=timezone.utc),
        headline="Major 7.8 Magnitude Earthquake Strikes Southern Turkey and Syria",
        lead_paragraph="A devastating 7.8-magnitude earthquake rocked southern Turkey and northern Syria early Monday.",
        url="https://www.reuters.com/world/middle-east/major-earthquake-hits-turkey-2026-02-06/",
        language="en",
    )


@pytest.fixture
def sample_outlet() -> MediaOutlet:
    """Fixture providing a mock international news agency."""
    return MediaOutlet(
        outlet_id="reuters",
        name="Reuters",
        home_country="GB",
        geographic_scope="international",
        topical_focus=["general", "breaking_news", "international"],
    )
