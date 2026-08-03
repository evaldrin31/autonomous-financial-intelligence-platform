# BUGFIX PROTOCOL: OpenCode

**Version**: 1.0

## Scope

Systematic bug fixing.

## Process

### 1. Reproduce

- [ ] Understand the bug
- [ ] Create minimal reproduction
- [ ] Document steps

### 2. Investigate

- [ ] Find root cause
- [ ] Check related code
- [ ] Review recent changes
- [ ] Check logs

### 3. Fix

- [ ] Write failing test
- [ ] Implement fix
- [ ] Verify test passes
- [ ] Check no regression

### 4. Verify

- [ ] Test in staging
- [ ] Test edge cases
- [ ] Performance check

### 5. Document

- [ ] Update CHANGELOG
- [ ] Document in code if complex
- [ ] Close issue with explanation

## Template

```
Bug: [Description]

Reproduction:
1. Step 1
2. Step 2
3. Expected: ...
4. Actual: ...

Root Cause:
[Explanation]

Fix:
[What was changed]

Test:
[How it was tested]
```

## Severity

| Level | Response |
|-------|----------|
| Critical | Fix immediately, hotfix |
| High | Fix in current sprint |
| Medium | Fix in next sprint |
| Low | Backlog |

## Common Causes

| Cause | Prevention |
|-------|------------|
| Race condition | Proper locking, async patterns |
| Null reference | Type checking, validation |
| Logic error | Tests, code review |
| Environment | Configuration management |
