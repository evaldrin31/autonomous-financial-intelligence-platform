# BACKEND PROTOCOL: OpenCode

**Version**: 1.0

## Scope

Backend development with FastAPI, Python, PostgreSQL.

## Prerequisites

Read:
- [ ] ../standards/Python_Coding_Standards.md
- [ ] ../standards/FastAPI_Standards.md
- [ ] ../standards/Database_Standards.md

## Project Structure

```
backend/
├── api/           # Routes
├── core/          # Config
├── database/      # DB setup
├── models/        # SQLAlchemy
├── schemas/       # Pydantic
├── services/      # Business logic
├── repositories/  # Data access
├── agents/        # AI agents
├── rag/           # RAG
├── utils/         # Helpers
└── tests/         # Tests
```

## Development Workflow

### New Endpoint

1. Define schema in `schemas/`
2. Create service in `services/`
3. Create route in `api/v1/`
4. Add tests in `tests/`
5. Update API docs

### Pattern

```python
# schemas/portfolio.py
class PortfolioCreate(BaseModel):
    name: str
    description: Optional[str]

# services/portfolio.py
class PortfolioService:
    async def create(self, data: PortfolioCreate) -> Portfolio:
        # Business logic
        pass

# api/v1/portfolios.py
@router.post("", response_model=PortfolioResponse)
async def create_portfolio(data: PortfolioCreate):
    return await service.create(data)
```

## Standards

### Python

- Type hints required
- Async by default
- Black formatting (88 chars)
- Ruff linting
- Docstrings for public APIs

### FastAPI

- Use dependencies
- Validate inputs
- Handle errors
- Return consistent responses

### Database

- Use SQLAlchemy 2.0
- Async sessions
- Repository pattern
- Alembic migrations

## Testing

```python
# Test structure
def test_create_portfolio(client):
    # Arrange
    data = {"name": "Test"}
    
    # Act
    response = client.post("/portfolios", json=data)
    
    # Assert
    assert response.status_code == 201
    assert response.json()["name"] == "Test"
```

## Debugging

```python
# Add breakpoint
import pdb; pdb.set_trace()

# Or use logging
logger.debug(f"Value: {value}")
```

## Common Tasks

| Task | Command |
|------|---------|
| Run server | `python main.py` |
| Run tests | `pytest` |
| Format | `black .` |
| Lint | `ruff check .` |
| Migrate | `alembic upgrade head` |
