from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database.session import get_db
from backend.services.data_quality import DataQualityEngine
from backend.services.data_ingestion import MarketDataService
from backend.services.sec_edgar import SECEdgarService
from backend.services.fred_macro import FREDMacroService
from backend.services.news_ingestion import NewsIngestionService

router = APIRouter(prefix="/data-health", tags=["Data Health & Ingestion"])

@router.get("/")
def get_data_health(db: Session = Depends(get_db)):
    """Returns real-time health and freshness status for all registered data sources."""
    return {"sources": DataQualityEngine.evaluate_source_health(db)}

@router.post("/refresh")
def trigger_data_refresh(ticker: str = "AAPL", db: Session = Depends(get_db)):
    """Triggers on-demand data ingestion and refreshes quality health status."""
    market_count = MarketDataService.ingest_market_data(db, ticker=ticker, days=30)
    sec_count = SECEdgarService.ingest_filings(db, ticker=ticker)
    macro_count = FREDMacroService.ingest_macro_data(db)
    news_count = NewsIngestionService.ingest_news(db)

    return {
        "success": True,
        "records_ingested": {
            "market_data": market_count,
            "sec_filings": sec_count,
            "macro_indicators": macro_count,
            "news_events": news_count
        },
        "health": DataQualityEngine.evaluate_source_health(db)
    }
