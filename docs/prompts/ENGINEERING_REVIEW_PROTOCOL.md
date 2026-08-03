# ENGINEERING REVIEW PROTOCOL: OpenCode

**Version**: 1.0

## Purpose

Review code, architecture, documentation for quality.

## Review Types

| Type | Scope | Time |
|------|-------|------|
| Quick | Single file | 5 min |
| Standard | PR | 15 min |
| Deep | Architecture | 30 min |
| Emergency | Critical path | 10 min |

## Review Checklist

### Code Quality

- [ ] Follows standards
- [ ] Properly typed
- [ ] Well named
- [ ] No duplication
- [ ] Error handling
- [ ] No security issues
- [ ] Performance acceptable

### Functionality

- [ ] Does what it says
- [ ] Edge cases handled
- [ ] No obvious bugs
- [ ] Tests exist
- [ ] Tests pass

### Documentation

- [ ] Code commented
- [ ] Complex logic explained
- [ ] API documented
- [ ] Changes documented

### Architecture

- [ ] Fits existing patterns
- [ ] No scope creep
- [ ] Dependencies appropriate
- [ ] Backward compatible (or versioned)

## Review Comments

### Format

```
[Severity] [Category]: Message

Example:
[Major] Security: User input not validated
[Minor] Style: Use constant instead of magic number
[Suggestion] Design: Consider extracting to function
```

### Severities

| Severity | Action Required |
|----------|-----------------|
| Critical | Must fix before merge |
| Major | Should fix before merge |
| Minor | Nice to have |
| Suggestion | Optional |

### Categories

- Security
- Performance
- Correctness
- Maintainability
- Testing
- Documentation
- Style

## Review Process

1. **Scan**: Read through quickly
2. **Understand**: What is this doing?
3. **Check**: Against standards
4. **Test**: Run if needed
5. **Comment**: Note issues
6. **Approve**: If acceptable
7. **Follow up**: Verify fixes

## Approval Levels

| Level | Meaning |
|-------|---------|
| Approve | Ready to merge |
| Comment | Minor issues, author decides |
| Request Changes | Must fix before merge |

## Emergency Reviews

When speed matters:
- Focus on critical issues only
- Skip style nits
- Trust author for minor fixes
- Document skipped checks
- Follow up later
