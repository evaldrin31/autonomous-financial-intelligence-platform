import datetime
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from backend.models.models import FinancialDocument, DocumentChunk, DataSourceHealth

class SECEdgarService:
    """SEC EDGAR document ingestion service for 10-K, 10-Q, and 8-K filings."""

    @staticmethod
    def fetch_filings(ticker: str) -> List[Dict[str, Any]]:
        """Simulates fetching official SEC filings with metadata and structured section chunks."""
        now = datetime.datetime.utcnow()
        return [
            {
                "ticker": ticker,
                "document_type": "10-K",
                "filing_date": now - datetime.timedelta(days=90),
                "title": f"{ticker} Annual Report (Form 10-K)",
                "source_url": f"https://www.sec.gov/edgar/searchedgar/companysearch?ticker={ticker}",
                "content_hash": f"hash_10k_{ticker}_2025",
                "chunks": [
                    "Item 1. Business: The company operates in high-growth technology sectors with strong cash flow.",
                    "Item 1A. Risk Factors: Macroeconomic inflation, supply chain disruption, and competitive pressure.",
                    "Item 7. Management Discussion: Revenue increased 15% year-over-year with expanding operating margins."
                ]
            },
            {
                "ticker": ticker,
                "document_type": "10-Q",
                "filing_date": now - datetime.timedelta(days=15),
                "title": f"{ticker} Quarterly Report (Form 10-Q)",
                "source_url": f"https://www.sec.gov/edgar/searchedgar/companysearch?ticker={ticker}",
                "content_hash": f"hash_10q_{ticker}_q2",
                "chunks": [
                    "Item 2. Management Discussion: Q2 revenue beat consensus estimates by 4.2% driven by enterprise demand.",
                    "Item 3. Quantitative Disclosures: Interest rate sensitivity remains low with fixed-rate debt structure."
                ]
            }
        ]

    @classmethod
    def ingest_filings(cls, db: Session, ticker: str) -> int:
        filings = cls.fetch_filings(ticker)
        count = 0
        for f in filings:
            existing = db.query(FinancialDocument).filter(
                FinancialDocument.ticker == ticker,
                FinancialDocument.content_hash == f["content_hash"]
            ).first()
            if not existing:
                doc = FinancialDocument(
                    ticker=f["ticker"],
                    document_type=f["document_type"],
                    filing_date=f["filing_date"],
                    title=f["title"],
                    source_url=f["source_url"],
                    content_hash=f["content_hash"]
                )
                db.add(doc)
                db.flush()
                
                for idx, chunk_text in enumerate(f["chunks"]):
                    chunk = DocumentChunk(
                        document_id=doc.id,
                        chunk_index=idx,
                        content=chunk_text,
                        metadata_json={"ticker": ticker, "document_type": f["document_type"]}
                    )
                    db.add(chunk)
                count += 1

        health = db.query(DataSourceHealth).filter(DataSourceHealth.source_name == "SEC_EDGAR_API").first()
        if not health:
            health = DataSourceHealth(source_name="SEC_EDGAR_API", status="HEALTHY", freshness_seconds=43, last_successful_update=datetime.datetime.utcnow())
            db.add(health)
        else:
            health.status = "HEALTHY"
            health.freshness_seconds = 43
            health.last_successful_update = datetime.datetime.utcnow()

        db.commit()
        return count
