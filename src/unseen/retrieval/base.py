"""Information retrieval interfaces for event-to-article candidate matching."""

from __future__ import annotations

import abc

from unseen.data.schemas import NewsArticle, RealWorldEvent


class BaseEventArticleRetriever(abc.ABC):
    """Abstract interface for candidate article retrieval given a real-world event."""

    @abc.abstractmethod
    def index_articles(self, articles: list[NewsArticle]) -> None:
        """Build or update the searchable index from article corpus."""
        raise NotImplementedError

    @abc.abstractmethod
    def retrieve_candidates(
        self,
        event: RealWorldEvent,
        top_k: int = 50,
    ) -> list[tuple[NewsArticle, float]]:
        """Retrieve candidate articles for an event ranked by retrieval score.

        Args:
            event: The query real-world event.
            top_k: Maximum number of candidates to return.

        Returns:
            List of (NewsArticle, score) tuples ranked in descending relevance.
        """
        raise NotImplementedError
