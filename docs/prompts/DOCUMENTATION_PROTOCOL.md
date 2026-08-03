# DOCUMENTATION PROTOCOL: OpenCode

**Version**: 1.0

## Scope

Creating and maintaining documentation.

## Prerequisites

Read:
- [ ] ../../docs/company/Knowledge_Management.md
- [ ] ../../docs/standards/Documentation_Standards.md

## When to Document

| Change | Documentation Required |
|--------|----------------------|
| New API endpoint | OpenAPI + Guide |
| Architecture change | ADR + Arch doc |
| New process | Playbook |
| New standard | Standards doc |
| Bug fix | Changelog |
| Feature | User docs + Changelog |

## Documentation Types

### Code Documentation

```python
"""
Brief description.

Longer explanation if needed.

Args:
    param: Description

Returns:
    Description

Example:
    >>> function(example)
    result
"""
```

### Architecture Documentation

See templates for format.

### Process Documentation

Step-by-step instructions.

## Review

- [ ] Accurate
- [ ] Complete
- [ ] Clear
- [ ] Links work
- [ ] Format correct

## Common Tasks

| Task | Location |
|------|----------|
| API docs | Inline (FastAPI) |
| Architecture | docs/architecture/ |
| Process | docs/playbooks/ |
| Standards | docs/standards/ |
| Decisions | docs/decisions/ |
