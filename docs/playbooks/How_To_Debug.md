# How To: Debug

**Version**: 1.0

## Overview

Systematic debugging approach.

## Process

### 1. Reproduce

- [ ] Find reproduction steps
- [ ] Create minimal case
- [ ] Document environment

### 2. Investigate

```python
# Add logging
import logging
logger = logging.getLogger(__name__)
logger.debug(f"Value: {value}")

# Or use debugger
import pdb; pdb.set_trace()

# Check stack trace
traceback.print_exc()
```

### 3. Isolate

- Remove unrelated code
- Check recent changes
- Check dependencies
- Check environment

### 4. Fix

- Write test reproducing bug
- Fix the root cause
- Verify fix works
- Check for regression

### 5. Document

- Update CHANGELOG
- Add regression test
- Document if complex

## Tools

| Tool | Use |
|------|-----|
| pdb | Python debugger |
| VS Code | Integrated debugger |
| Logging | Add context |
| Pytest | Reproduce bugs |

## Common Issues

| Issue | Check |
|-------|-------|
| Import error | Path, dependencies |
| NoneType error | Validation |
| Async error | await, event loop |
| DB error | Connection, query |

## References

- [Bugfix Protocol](../../prompts/BUGFIX_PROTOCOL.md)
