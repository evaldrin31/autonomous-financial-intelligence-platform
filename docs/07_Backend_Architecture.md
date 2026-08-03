# Backend Architecture: Autonomous Financial Intelligence Platform

## Executive Summary

This document defines the backend architecture for AFIP, built on FastAPI with a modular, layered design that supports the platform's autonomous AI capabilities while maintaining high performance, security, and maintainability.

---

## 1. Backend Overview

### 1.1 Technology Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| Web Framework | FastAPI | 0.104+ | High-performance API |
| Language | Python | 3.11+ | Modern async support |
| ORM | SQLAlchemy | 2.0+ | Database abstraction |
| Validation | Pydantic | 2.5+ | Data validation |
| Migrations | Alembic | 1.12+ | Database versioning |
| Server | Uvicorn | 0.24+ | ASGI server |
| Testing | Pytest | 7.4+ | Test framework |
| Linting | Ruff | 0.1+ | Fast Python linter |
| Formatting | Black | 23+ | Code formatter |

### 1.2 Architecture Principles

1. **Async-First**: Native async/await throughout
2. **Type Safety**: Comprehensive type hints
3. **Dependency Injection**: FastAPI DI container
4. **Repository Pattern**: Clean data access
5. **Service Layer**: Business logic isolation
6. **API Versioning**: URL-based versioning (/api/v1/)

---

## 2. Project Structure

```
backend/
├── alembic/              # Database migrations
│   ├── env.py
│   ├── versions/
│   └── script.py.mako
│
├── api/                  # API layer
│   ├── __init__.py
│   ├── routes.py        # Route aggregation
│   ├── deps.py          # Dependencies
│   └── v1/
│       ├── __init__.py
│       ├── auth.py      # Auth endpoints
│       ├── users.py     # User endpoints
│       ├── portfolios.py
│       ├── assets.py
│       └── analytics.py
│
├── core/                # Core configuration
│   ├── __init__.py
│   ├── config.py        # Settings
│   ├── security.py      # JWT, hashing
│   └── logging.py       # Logging config
│
├── database/            # Database layer
│   ├── __init__.py
│   ├── session.py       # DB session management
│   ├── base.py          # Base model
│   └── migrations.py    # Migration utilities
│
├── models/              # SQLAlchemy models
│   ├── __init__.py
│   ├── user.py
│   ├── portfolio.py
│   ├── asset.py
│   ├── transaction.py
│   └── price.py
│
├── schemas/             # Pydantic schemas
│   ├── __init__.py
│   ├── user.py
│   ├── portfolio.py
│   ├── asset.py
│   └── common.py
│
├── services/            # Business logic
│   ├── __init__.py
│   ├── user.py
│   ├── portfolio.py
│   ├── asset.py
│   └── analytics.py
│
├── repositories/          # Data access
│   ├── __init__.py
│   ├── base.py
│   ├── user.py
│   └── portfolio.py
│
├── agents/               # AI agents
│   ├── __init__.py
│   ├── orchestrator.py
│   ├── base.py
│   ├── portfolio_analyzer.py
│   ├── market_researcher.py
│   └── risk_manager.py
│
├── rag/                  # RAG system
│   ├── __init__.py
│   ├── ingest.py
│   ├── retrieve.py
│   └── generate.py
│
├── prompts/              # LLM prompts
│   ├── __init__.py
│   ├── portfolio_analysis.txt
│   └── market_research.txt
│
├── utils/                # Utilities
│   ├── __init__.py
│   ├── datetime.py
│   └── validation.py
│
├── tests/                # Test suite
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   └── test_portfolios.py
│
├── main.py              # Application entry
├── requirements.txt     # Dependencies
└── pyproject.toml       # Project config
```

---

## 3. Layer Architecture

### 3.1 API Layer

**Responsibility**: HTTP request handling, validation, response formatting

```python
# Pattern: Router-based organization
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from schemas.portfolio import PortfolioCreate, PortfolioResponse
from services.portfolio import PortfolioService
from api.deps import get_current_user, get_db

router = APIRouter(prefix="/portfolios", tags=["portfolios"])

@router.post("", response_model=PortfolioResponse)
async def create_portfolio(
    portfolio_in: PortfolioCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Create a new portfolio for the authenticated user.
    """
    service = PortfolioService(db)
    portfolio = await service.create(
        user_id=current_user.id,
        data=portfolio_in
    )
    return portfolio
```

### 3.2 Service Layer

**Responsibility**: Business logic, orchestration, transaction management

```python
# Pattern: Service class with dependency injection
class PortfolioService:
    """
    Business logic for portfolio management.
    """
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repo = PortfolioRepository(db)
        self.agent = PortfolioAnalysisAgent()
    
    async def create(
        self,
        user_id: UUID,
        data: PortfolioCreate
    ) -> Portfolio:
        """
        Create portfolio with validation and initial analysis.
        """
        # Validate
        await self._validate_create(user_id, data)
        
        # Create
        portfolio = await self.repo.create(
            user_id=user_id,
            data=data
        )
        
        # Initial analysis
        await self._run_initial_analysis(portfolio)
        
        return portfolio
    
    async def analyze(
        self,
        portfolio_id: UUID
    ) -> PortfolioAnalysis:
        """
        Run comprehensive portfolio analysis.
        """
        portfolio = await self.repo.get(portfolio_id)
        
        # Agent analysis
        analysis = await self.agent.analyze(portfolio)
        
        # Store results
        await self._save_analysis(portfolio_id, analysis)
        
        return analysis
```

### 3.3 Repository Layer

**Responsibility**: Database operations, query optimization

```python
# Pattern: Repository pattern for data access
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class PortfolioRepository:
    """
    Data access for portfolios.
    """
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get(self, id: UUID) -> Optional[Portfolio]:
        """Get portfolio by ID."""
        result = await self.db.execute(
            select(Portfolio).where(Portfolio.id == id)
        )
        return result.scalar_one_or_none()
    
    async def create(self, data: PortfolioCreate) -> Portfolio:
        """Create new portfolio."""
        portfolio = Portfolio(**data.model_dump())
        self.db.add(portfolio)
        await self.db.commit()
        await self.db.refresh(portfolio)
        return portfolio
    
    async def list_by_user(
        self,
        user_id: UUID,
        skip: int = 0,
        limit: int = 100
    ) -> List[Portfolio]:
        """List user portfolios with pagination."""
        result = await self.db.execute(
            select(Portfolio)
            .where(Portfolio.user_id == user_id)
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()
```

### 3.4 Model Layer

**Responsibility**: Database schema, relationships, constraints

```python
# Pattern: SQLAlchemy 2.0 declarative models
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Numeric, DateTime
from database.base import Base

class Portfolio(Base):
    """
    Portfolio model.
    """
    __tablename__ = "portfolios"
    
    id: Mapped[UUID] = mapped_column(primary_key=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(String(500))
    currency: Mapped[str] = mapped_column(String(3), default="USD")
    total_value: Mapped[Decimal] = mapped_column(Numeric(19, 4), default=0)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    
    # Relationships
    user: Mapped["User"] = relationship(back_populates="portfolios")
    assets: Mapped[List["Asset"]] = relationship(back_populates="portfolio")
```

---

## 4. Dependency Injection

### 4.1 FastAPI Dependencies

```python
# deps.py - Centralized dependency definitions
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db_session
from core.security import decode_token
from models.user import User

security = HTTPBearer()

async def get_db() -> AsyncSession:
    """Database session dependency."""
    async with get_db_session() as session:
        yield session

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db),
) -> User:
    """
    Get current authenticated user from JWT token.
    """
    token = credentials.credentials
    payload = decode_token(token)
    
    user = await db.get(User, payload["sub"])
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User inactive"
        )
    
    return user

async def get_current_active_superuser(
    current_user: User = Depends(get_current_user),
) -> User:
    """Get current user with superuser check."""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Superuser required"
        )
    return current_user
```

---

## 5. Error Handling

### 5.1 Exception Hierarchy

```python
# exceptions.py
class AFIPException(Exception):
    """Base exception for AFIP."""
    pass

class ValidationError(AFIPException):
    """Input validation error."""
    pass

class NotFoundError(AFIPException):
    """Resource not found."""
    pass

class AuthenticationError(AFIPException):
    """Authentication failed."""
    pass

class AuthorizationError(AFIPException):
    """Permission denied."""
    pass

class BusinessLogicError(AFIPException):
    """Business rule violation."""
    pass
```

### 5.2 Global Exception Handler

```python
# middleware/error_handler.py
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

@app.exception_handler(AFIPException)
async def afip_exception_handler(
    request: Request,
    exc: AFIPException
):
    """Handle application exceptions."""
    status_code = 500
    
    if isinstance(exc, ValidationError):
        status_code = 400
    elif isinstance(exc, NotFoundError):
        status_code = 404
    elif isinstance(exc, AuthenticationError):
        status_code = 401
    elif isinstance(exc, AuthorizationError):
        status_code = 403
    
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "error": {
                "type": exc.__class__.__name__,
                "message": str(exc)
            }
        }
    )
```

---

## 6. Configuration Management

### 6.1 Settings Pattern

```python
# core/config.py
from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application configuration.
    
    Loads from environment variables with sensible defaults.
    """
    # Application
    APP_NAME: str = "AFIP"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    
    # Server
    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_PORT: int = 8000
    
    # Database
    DATABASE_URL: str = "postgresql://localhost/afip"
    DB_POOL_SIZE: int = 20
    
    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # AI/LLM
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
```

---

## 7. Document Information

| Field | Value |
|-------|-------|
| Document ID | AFIP-DOC-007 |
| Version | 1.0.0 |
| Status | Draft |

---

## Next Document

**→ Continue to**: [08_Frontend_Architecture.md](./08_Frontend_Architecture.md)  
**← Back to**: [06_RAG_Architecture.md](./06_RAG_Architecture.md)
