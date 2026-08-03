# Knowledge Management: AFIP

**Version**: 1.0

## Philosophy

Knowledge lives with code. Documentation is code.

## Structure

```
docs/
├── README.md                    # Entry point
├── company/                     # Governance
├── architecture/                # System design
├── standards/                   # How we work
├── playbooks/                   # How to do things
├── templates/                   # Reusable formats
└── decisions/                   # ADRs
```

## Rules

1. **Docs with Code**: Every PR updates docs
2. **One Source**: Link, don't duplicate
3. **Living Docs**: Update when code changes
4. **Accessible**: Clear, concise, searchable

## Documentation Types

| Type | Location | Owner |
|------|----------|-------|
| API | Inline (OpenAPI) | Backend |
| Code | Inline comments | Author |
| Architecture | docs/architecture/ | Architect |
| Process | docs/company/ | CTO |
| How-to | docs/playbooks/ | Team |
| Decisions | docs/decisions/ | Decision maker |

## Review

- Monthly doc audit
- Remove stale docs
- Update broken links
- Consolidate duplicates

## Tools

- Markdown for docs
- Git for versioning
- GitHub for hosting
- VS Code for editing

## Search

- Use GitHub search
- Tag appropriately
- Clear titles
- Good summaries
