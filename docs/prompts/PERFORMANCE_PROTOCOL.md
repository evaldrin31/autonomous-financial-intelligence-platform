# PERFORMANCE PROTOCOL: OpenCode

**Version**: 1.0

## Scope

Performance optimization and monitoring.

## When to Optimize

Optimize when:
- [ ] Bottleneck identified
- [ ] User experience affected
- [ ] Cost implications
- [ ] Load testing shows issues

Don't optimize:
- Prematurely
- Without profiling
- Without measuring

## Profiling

```python
# Time function
import time
start = time.time()
result = function()
print(f"Took {time.time() - start}s")

# Profile with cProfile
python -m cProfile -o profile.stats script.py
```

## Database Performance

- Index frequently queried columns
- Avoid N+1 queries
- Use select_related / joinedload
- Batch operations
- Connection pooling

## API Performance

| Metric | Target |
|--------|--------|
| Response time (p95) | < 200ms |
| Response time (p99) | < 500ms |
| Throughput | 1000 req/s |
| Error rate | < 0.1% |

## Frontend Performance

- Code splitting
- Lazy loading
- Image optimization
- Bundle size < 200KB
- Lighthouse score > 90

## Caching

```python
# Redis cache
@cache(ttl=300)
async def expensive_operation():
    return result
```

## Monitoring

- Response times
- Database queries
- Cache hit rates
- Memory usage
- CPU usage

## Common Tasks

| Task | Tool |
|------|------|
| Profile Python | cProfile, py-spy |
| Profile Frontend | Lighthouse, DevTools |
| Load test | k6, Locust |
| Monitor | Prometheus, Grafana |
