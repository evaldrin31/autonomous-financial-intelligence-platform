from fastapi import APIRouter
from backend.api import health
from backend.api import auth

router = APIRouter(prefix="/api/v1")

router.include_router(health.router)
router.include_router(auth.router)
