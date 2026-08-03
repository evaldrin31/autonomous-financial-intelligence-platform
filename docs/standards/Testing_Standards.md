# Testing Standards: AFIP

**Version**: 1.0

## Coverage

| Component | Target |
|-----------|--------|
| Critical paths | 90% |
| Services | 85% |
| APIs | 80% |
| Utils | 70% |

## Structure

```python
# Arrange
input = setup()

# Act
result = function(input)

# Assert
assert result == expected
```

## Naming

`test_{function}_{scenario}`

Example: `test_create_portfolio_success`

## Types

| Type | Purpose |
|------|---------|
| Unit | Single function |
| Integration | Multiple components |
| E2E | Full flow |

## Fixtures

```python
@pytest.fixture
def portfolio():
    return Portfolio(name="Test")
```

## Mocking

```python
# Mock external calls
with patch('module.function') as mock:
    mock.return_value = expected
    result = function()
```

## Running

```bash
# All tests
pytest

# With coverage
pytest --cov=backend --cov-report=html

# Specific file
pytest tests/test_portfolio.py

# Specific test
pytest -k test_name
```

## Anti-patterns

- ❌ Tests that don't fail
- ❌ Testing implementation
- ❌ No assertions
- ❌ Flaky tests
- ❌ Slow tests
