"""
Health check endpoints.
"""

from datetime import datetime
from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    """Health check response model."""

    status: str
    version: str
    timestamp: datetime


@router.get("", response_model=dict[str, Any])
async def health_check() -> dict[str, Any]:
    """
    Health check endpoint.

    Returns the current health status of the API.
    """
    return {
        "success": True,
        "data": HealthResponse(
            status="healthy",
            version="1.0.0",
            timestamp=datetime.utcnow(),
        ).model_dump(),
        "timestamp": datetime.utcnow().isoformat(),
    }
