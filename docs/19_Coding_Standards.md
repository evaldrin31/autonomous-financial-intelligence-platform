# Coding Standards: Autonomous Financial Intelligence Platform

## Executive Summary

This document defines the coding standards and style guidelines for AFIP to ensure consistency, readability, and maintainability across the codebase.

---

## 1. Python Standards

### 1.1 Style Guide

**Tool**: Black (formatting) + Ruff (linting)

```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py311']

[tool.ruff]
target-version = "py311"
line-length = 88
select = ["E", "F", "I", "N", "W", "UP", "B", "C4", "SIM"]
```

### 1.2 Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| **Classes** | PascalCase | `PortfolioService` |
| **Functions** | snake_case | `calculate_returns` |
| **Variables** | snake_case | `total_value` |
| **Constants** | UPPER_SNAKE_CASE | `MAX_RETRY_COUNT` |
| **Private** | Leading underscore | `_internal_method` |
| **Modules** | snake_case | `portfolio_service.py` |

### 1.3 Type Hints

```python
from typing import Optional, List, Dict, Any
from decimal import Decimal

# Functions must have type hints
def calculate_portfolio_value(
    assets: List[Asset],
    prices: Dict[str, Decimal]
) -> Decimal:
    """
    Calculate total portfolio value.
    
    Args:
        assets: List of portfolio assets
        prices: Current price dictionary
    
    Returns:
        Total portfolio value
    """
    return sum(
        asset.quantity * prices.get(asset.symbol, Decimal('0'))
        for asset in assets
    )
```

### 1.4 Documentation

```python
class PortfolioService:
    """
    Service for portfolio management operations.
    
    This service handles CRUD operations for portfolios,
    asset tracking, and performance calculations.
    
    Attributes:
        db: Database session
        cache: Redis cache client
    
    Example:
        >>> service = PortfolioService(db)
        >>> portfolio = await service.create(user_id, data)
    """
    
    def __init__(self, db: AsyncSession) -> None:
        """
        Initialize service with database session.
        
        Args:
            db: SQLAlchemy async session
        """
        self.db = db
```

---

## 2. TypeScript Standards

### 2.1 Style Guide

**Tool**: ESLint + Prettier

```json
// .eslintrc.json
{
  "extends": ["next/core-web-vitals", "plugin:@typescript-eslint/recommended"],
  "rules": {
    "@typescript-eslint/explicit-function-return-type": "error",
    "@typescript-eslint/no-explicit-any": "error"
  }
}
```

### 2.2 Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| **Interfaces** | PascalCase | `PortfolioData` |
| **Types** | PascalCase | `TransactionType` |
| **Functions** | camelCase | `getPortfolioValue` |
| **Variables** | camelCase | `totalValue` |
| **Constants** | UPPER_SNAKE_CASE | `MAX_ASSETS` |
| **Components** | PascalCase | `PortfolioCard` |
| **Hooks** | camelCase, prefix | `usePortfolio` |

### 2.3 Type Safety

```typescript
// Always define types
interface Portfolio {
  id: string;
  name: string;
  totalValue: number;
  assets: Asset[];
}

// Use strict typing
function calculateReturn(
  startValue: number,
  endValue: number
): number {
  return ((endValue - startValue) / startValue) * 100;
}

// Avoid 'any'
// Bad
const data: any = fetchData();

// Good
const data: Portfolio = fetchData();
```

---

## 3. General Principles

### 3.1 Code Organization

```
backend/
├── api/              # API routes only
├── services/         # Business logic
├── models/           # Database models
├── schemas/          # Pydantic schemas
├── utils/            # Pure functions
└── tests/            # Test files

frontend/
├── app/              # Next.js pages
├── components/       # React components
├── hooks/            # Custom hooks
├── lib/              # Utilities
├── store/            # State management
└── types/            # TypeScript types
```

### 3.2 Error Handling

```python
# Python
from fastapi import HTTPException

async def get_portfolio(portfolio_id: UUID) -> Portfolio:
    portfolio = await db.get(Portfolio, portfolio_id)
    if not portfolio:
        raise HTTPException(
            status_code=404,
            detail=f"Portfolio {portfolio_id} not found"
        )
    return portfolio
```

```typescript
// TypeScript
try {
  const portfolio = await api.portfolios.get(id);
  setPortfolio(portfolio);
} catch (error) {
  if (error.response?.status === 404) {
    toast.error('Portfolio not found');
  } else {
    toast.error('Failed to load portfolio');
  }
}
```

---

## 4. Document Information

| Field | Value |
|-------|-------|
| Document ID | AFIP-DOC-019 |
| Version | 1.0.0 |
| Status | Draft |

---

## Next Document

**→ Continue to**: [20_Testing_Strategy.md](./20_Testing_Strategy.md)  
**← Back to**: [18_Deployment_Guide.md](./18_Deployment_Guide.md)
