# How To: Add New API

**Version**: 1.0

## Overview

Add a new REST API endpoint following AFIP patterns.

## Prerequisites

- [ ] Read FastAPI Standards
- [ ] Understand existing patterns
- [ ] Know the domain

## Steps

### 1. Define Schema

```python
# backend/schemas/portfolio.py
from pydantic import BaseModel

class PortfolioCreate(BaseModel):
    name: str
    description: Optional[str]

class PortfolioResponse(BaseModel):
    id: UUID
    name: str
    total_value: Decimal
```

### 2. Create Service

```python
# backend/services/portfolio.py
class PortfolioService:
    async def create(self, user_id: UUID, data: PortfolioCreate) -> Portfolio:
        portfolio = Portfolio(user_id=user_id, **data.dict())
        await self.db.add(portfolio)
        await self.db.commit()
        return portfolio
```

### 3. Create Route

```python
# backend/api/v1/portfolios.py
from fastapi import APIRouter

router = APIRouter(prefix="/portfolios", tags=["portfolios"])

@router.post("", response_model=PortfolioResponse)
async def create_portfolio(
    data: PortfolioCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = PortfolioService(db)
    return await service.create(current_user.id, data)
```

### 4. Register Route

```python
# backend/api/routes.py
from api.v1 import portfolios

api_router.include_router(portfolios.router)
```

### 5. Write Tests

```python
# backend/tests/test_portfolios.py
def test_create_portfolio(client):
    response = client.post(
        "/api/v1/portfolios",
        json={"name": "Test"}
    )
    assert response.status_code == 201
```

### 6. Update Documentation

- [ ] Add to API docs (auto-generated)
- [ ] Update relevant architecture doc
- [ ] Add to CHANGELOG

## Verification

```bash
# Run tests
pytest tests/test_portfolios.py

# Check lint
ruff check .

# Type check
mypy backend/
```

## Common Patterns

| Pattern | Use When |
|---------|----------|
| CRUD | Standard resource |
| Nested | Sub-resource |
| Action | Custom operation |

## References

- [FastAPI Standards](../standards/FastAPI_Standards.md)
- [API Standards](../standards/REST_API_Standards.md)
