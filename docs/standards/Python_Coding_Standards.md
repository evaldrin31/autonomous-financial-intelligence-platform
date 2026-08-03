# Python Coding Standards: AFIP

**Version**: 1.0

## Style

- Black formatter, 88 chars
- Ruff linter
- Type hints required
- Docstrings for public APIs

## Naming

| Type | Convention |
|------|-----------|
| Classes | PascalCase |
| Functions | snake_case |
| Variables | snake_case |
| Constants | UPPER_SNAKE |
| Private | _leading_underscore |

## Imports

```python
# Standard library
import os
from typing import List

# Third party
from fastapi import FastAPI
from sqlalchemy import select

# Local
from backend.core.config import settings
```

## Type Hints

```python
def calculate_value(assets: List[Asset]) -> Decimal:
    ...

async def get_portfolio(id: UUID) -> Optional[Portfolio]:
    ...
```

## Docstrings

```python
def function_name(param: Type) -> ReturnType:
    """
    Brief description.
    
    Longer explanation if needed.
    
    Args:
        param: Description
    
    Returns:
        Description
    """
```

## Error Handling

```python
try:
    result = await operation()
except SpecificError as e:
    logger.error(f"Failed: {e}")
    raise CustomError() from e
```

## Async

- Use async/await
- No sync IO in async functions
- Use asyncio.gather for parallel

## Testing

```python
def test_function():
    # Arrange
    input = ...
    
    # Act
    result = function(input)
    
    # Assert
    assert result == expected
```

## Anti-patterns

- ❌ `except:` (bare except)
- ❌ Mutable default args
- ❌ `print()` (use logging)
- ❌ Global state
- ❌ Circular imports
