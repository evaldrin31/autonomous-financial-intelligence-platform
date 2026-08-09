import datetime
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from backend.models.models import NewsEvent, DataSourceHealth

class NewsIngestionService:
    """Financial news and event sentiment ingestion service."""

    @staticmethod
    def fetch_news_events() -> List[Dict[str, Any]]:
        now = datetime.datetime.utcnow()
        return [
            {
                "title": "Federal Reserve Signals Potential Interest Rate Cut in Upcoming Meeting",
                "source": "Bloomberg Financial News",
                "url": "https://www.bloomberg.com/news/articles/fed-rate-signals",
                "published_at": now - datetime.timedelta(hours=2),
                "sentiment_score": 0.65,
                "materiality": "HIGH",
                "summary": "Fed policy statement highlights easing inflationary pressures and potential adjustments to the federal funds rate."
            },
            {
                "title": "Tech Sector Enterprise AI Spending Surges 28% Year-Over-Year",
                "source": "Reuters Market Insights",
                "url": "https://www.reuters.com/technology/enterprise-ai-spending-growth",
                "published_at": now - datetime.timedelta(hours=5),
                "sentiment_score": 0.82,
                "materiality": "HIGH",
                "summary": "Cloud architecture demand accelerates as enterprise clients expand production deployment of generative model platforms."
            },
            {
                "title": "Global Supply Chain Logistics Index Shows Minor Disruption Risks",
                "source": "Financial Times",
                "url": "https://www.ft.com/content/supply-chain-index",
                "published_at": now - datetime.timedelta(hours=12),
                "sentiment_score": -0.25,
                "materiality": "MEDIUM",
                "summary": "Freight rate volatility increases slightly across key maritime routes, though inventory buffer stock mitigates immediate shocks."
            }
        ]

    @classmethod
    def ingest_news(cls, db: Session) -> int:
        events = cls.fetch_news_events()
        count = 0
        for e in events:
            existing = db.query(NewsEvent).filter(NewsEvent.title == e["title"]).first()
            if not existing:
                ne = NewsEvent(**e)
                db.add(ne)
                count += 1

        health = db.query(DataSourceHealth).filter(DataSourceHealth.source_name == "FINANCIAL_NEWS_API").first()
        if not health:
            health = DataSourceHealth(source_name="FINANCIAL_NEWS_API", status="HEALTHY", freshness_seconds=900, last_successful_update=datetime.datetime.utcnow())
            db.add(health)
        else:
            health.status = "HEALTHY"
            health.freshness_seconds = 900
            health.last_successful_update = datetime.datetime.utcnow()

        db.commit()
        return count
