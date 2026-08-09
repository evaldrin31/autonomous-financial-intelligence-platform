from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database.session import get_db
from backend.models.models import MarketData
from backend.services.data_ingestion import MarketDataService

router = APIRouter(prefix="/market", tags=["Market Intelligence"])

@router.get("/ohlcv")
def get_market_data(ticker: str = "AAPL", days: int = Query(30, ge=1, le=365), db: Session = Depends(get_db)):
    """Retrieves OHLCV market price history for a given asset ticker."""
    records = db.query(MarketData).filter(MarketData.ticker == ticker).order_by(MarketData.timestamp.desc()).limit(days).all()
    if not records:
        MarketDataService.ingest_market_data(db, ticker=ticker, days=days)
        records = db.query(MarketData).filter(MarketData.ticker == ticker).order_by(MarketData.timestamp.desc()).limit(days).all()
    return {"ticker": ticker, "count": len(records), "data": records}
