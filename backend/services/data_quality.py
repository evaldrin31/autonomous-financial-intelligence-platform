import datetime
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from backend.models.models import DataSourceHealth, MarketData

class DataQualityEngine:
    """Engine for validating data freshness, identifying stale records, and monitoring data source health."""

    STALE_THRESHOLDS = {
        "MARKET_DATA_API": 300,        # 5 minutes
        "SEC_EDGAR_API": 86400,        # 24 hours
        "FRED_MACRO_API": 604800,      # 7 days
        "FINANCIAL_NEWS_API": 3600,    # 1 hour
    }

    @classmethod
    def evaluate_source_health(cls, db: Session) -> List[Dict[str, Any]]:
        """Evaluates health, freshness, and stale status across all registered data sources."""
        sources = db.query(DataSourceHealth).all()
        now = datetime.datetime.utcnow()
        results = []

        for src in sources:
            elapsed = (now - src.last_successful_update).total_seconds()
            threshold = cls.STALE_THRESHOLDS.get(src.source_name, 3600)
            
            status = "HEALTHY"
            if elapsed > threshold * 2 or src.error_count > 5:
                status = "DEGRADED"
            elif elapsed > threshold:
                status = "STALE"

            results.append({
                "source_name": src.source_name,
                "status": status,
                "freshness_seconds": int(elapsed),
                "last_successful_update": src.last_successful_update.isoformat(),
                "error_count": src.error_count,
            })
        return results

    @staticmethod
    def validate_market_record(record: MarketData) -> bool:
        """Validates market data record integrity (e.g. non-negative prices, high >= low)."""
        if record.open < 0 or record.high < 0 or record.low < 0 or record.close < 0:
            return False
        if record.high < record.low:
            return False
        if record.volume < 0:
            return False
        return True
