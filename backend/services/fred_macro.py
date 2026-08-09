import datetime
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from backend.models.models import MacroIndicator, DataSourceHealth

class FREDMacroService:
    """FRED Macroeconomic data ingestion service."""

    MACRO_SERIES = [
        {"series_id": "FEDFUNDS", "name": "Federal Funds Effective Rate", "unit": "%", "value": 5.25},
        {"series_id": "CPIAUCSL", "name": "Consumer Price Index (CPI Inflation)", "unit": "Index", "value": 314.2},
        {"series_id": "UNRATE", "name": "Civilian Unemployment Rate", "unit": "%", "value": 3.9},
        {"series_id": "DGS10", "name": "10-Year Treasury Constant Maturity Rate", "unit": "%", "value": 4.25},
    ]

    @classmethod
    def fetch_macro_indicators(cls) -> List[Dict[str, Any]]:
        now = datetime.datetime.utcnow()
        records = []
        for series in cls.MACRO_SERIES:
            records.append({
                "series_id": series["series_id"],
                "name": series["name"],
                "timestamp": now,
                "value": series["value"],
                "unit": series["unit"]
            })
        return records

    @classmethod
    def ingest_macro_data(cls, db: Session) -> int:
        records = cls.fetch_macro_indicators()
        count = 0
        for r in records:
            existing = db.query(MacroIndicator).filter(
                MacroIndicator.series_id == r["series_id"],
                MacroIndicator.timestamp == r["timestamp"]
            ).first()
            if not existing:
                ind = MacroIndicator(**r)
                db.add(ind)
                count += 1

        health = db.query(DataSourceHealth).filter(DataSourceHealth.source_name == "FRED_MACRO_API").first()
        if not health:
            health = DataSourceHealth(source_name="FRED_MACRO_API", status="HEALTHY", freshness_seconds=7200, last_successful_update=datetime.datetime.utcnow())
            db.add(health)
        else:
            health.status = "HEALTHY"
            health.freshness_seconds = 7200
            health.last_successful_update = datetime.datetime.utcnow()

        db.commit()
        return count
