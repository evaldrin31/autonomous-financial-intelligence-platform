# TESTING PROTOCOL: OpenCode

**Version**: 1.0

## Scope

Writing and running tests.

## Prerequisites

Read:
- [ ] ../../docs/20_Testing_Strategy.md

## Test Pyramid

```
    E2E (10%)
    Integration (30%)
    Unit (60%)
```

## Writing Tests

### Unit Test

```python
def test_calculate_returns():
    # Arrange
    start = 100
    end = 110
    
    # Act
    result = calculate_returns(start, end)
    
    # Assert
    assert result == 10.0
```

### Integration Test

```python
def test_create_portfolio_api(client):
    response = client.post("/portfolios", json={"name": "Test"})
    assert response.status_code == 201
    assert response.json()["name"] == "Test"
```

## Standards

- Test behavior, not implementation
- One assertion per test (ideal)
- Descriptive names
- Setup in fixtures
- Cleanup after

## Coverage

| Component | Target |
|-----------|--------|
| Critical paths | 90% |
| Services | 85% |
| API routes | 80% |
| Utils | 70% |

## Running Tests

```bash
# All tests
pytest

# Specific file
pytest tests/test_portfolio.py

# With coverage
pytest --cov=backend --cov-report=html

# Specific test
pytest -k test_name
```

## When to Test

- [ ] Before commit
- [ ] Before PR
- [ ] Before merge
- [ ] After bug fix
- [ ] After refactor

## Common Tasks

| Task | Approach |
|------|----------|
| New feature | Write tests first |
| Bug fix | Write test reproducing bug |
| Refactor | Ensure tests pass before/after |
