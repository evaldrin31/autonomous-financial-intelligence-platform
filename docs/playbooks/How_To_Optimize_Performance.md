# How To: Optimize Performance

**Version**: 1.0

## Overview

Systematic performance optimization.

## Process

### 1. Measure

```python
import time
start = time.time()
result = function()
print(f"Took {time.time() - start}s")
```

### 2. Profile

```bash
# Python profiler
python -m cProfile -o profile.stats script.py

# Memory profiler
python -m memory_profiler script.py
```

### 3. Identify Bottleneck

- Database queries?
- External API calls?
- CPU intensive?
- Memory usage?

### 4. Optimize

#### Database

```python
# Add index
CREATE INDEX idx_name ON table(column);

# Use eager loading
query.options(selectinload(Related))

# Batch queries
query.filter(Model.id.in_(ids))
```

#### API

```python
# Cache responses
@cache(ttl=300)
async def expensive_query():
    ...

# Async processing
results = await asyncio.gather(*tasks)
```

#### Frontend

- Code splitting
- Lazy loading
- Image optimization
- Memoization

### 5. Verify

- Measure again
- Ensure improvement
- Check no regression

## Common Optimizations

| Area | Technique |
|------|-----------|
| Database | Index, query optimization |
| API | Caching, pagination |
| Frontend | Code splitting, lazy loading |
| Memory | Streaming, generators |

## References

- [Performance Protocol](../../prompts/PERFORMANCE_PROTOCOL.md)
