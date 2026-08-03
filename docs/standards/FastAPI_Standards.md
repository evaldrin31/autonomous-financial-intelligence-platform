# FastAPI Standards: AFIP

**Version**: 1.0

## Structure

```
api/
├── __init__.py
├── deps.py
├── routes.py
└── v1/
    ├── portfolios.py
    ├── assets.py
    └── auth.py
```

## Routes

```python
from fastapi import APIRouter, Depends, HTTPException
from typing import List

router = APIRouter(prefix="/portfolios", tags=["portfolios"])

@router.get("", response_model=List[PortfolioResponse])
async def list_portfolios(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """List user portfolios."""
    return await service.list_by_user(current_user.id)
```

## Responses

```python
@router.get("/{id}", response_model=PortfolioResponse)
async def get_portfolio(id: UUID):
    portfolio = await service.get(id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return portfolio
```

## Dependencies

```python
async def get_current_user(
    token: str = Depends(oauth2_scheme)
) -> User:
    """Get current authenticated user."""
    return await auth_service.verify_token(token)
```

## Error Handling

```python
@app.exception_handler(CustomError)
async def custom_error_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc)}
    )
```

## Middleware

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Testing

```python
def test_get_portfolio(client):
    response = client.get("/api/v1/portfolios/1")
    assert response.status_code == 200
    assert response.json()["id"] == "1"
```
