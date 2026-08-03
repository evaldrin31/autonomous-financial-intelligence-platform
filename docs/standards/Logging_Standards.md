# Logging Standards: AFIP

**Version**: 1.0

## Levels

| Level | Use |
|-------|-----|
| DEBUG | Detailed info |
| INFO | General events |
| WARNING | Unexpected but handled |
| ERROR | Errors, handled |
| CRITICAL | System failure |

## Format

```python
logger.info("User logged in", extra={"user_id": user_id})
logger.error("Database connection failed", extra={"error": str(e)})
```

## Structure

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Processing portfolio", extra={
    "portfolio_id": portfolio_id,
    "action": "rebalance"
})
```

## What to Log

- ✅ Request/response (at debug)
- ✅ Errors with context
- ✅ Business events
- ✅ Performance metrics
- ❌ Sensitive data
- ❌ Passwords
- ❌ PII

## Configuration

```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

## JSON Logging (Production)

```python
{
  "timestamp": "2024-01-01T00:00:00Z",
  "level": "INFO",
  "logger": "module.function",
  "message": "Event",
  "context": {}
}
```
