# IMPLEMENTATION PROTOCOL: OpenCode

**Version**: 1.0

## When to Use

Implementing features, fixing bugs, adding functionality.

## Pre-Implementation

### Step 1: Context Gathering

Read:
- [ ] PROJECT_STATE.md (current status)
- [ ] Relevant architecture doc
- [ ] Standards for the area
- [ ] Existing similar code

### Step 2: Scope Definition

Define:
- What needs to change
- What stays the same
- Success criteria
- Files to modify

## Implementation Steps

### Step 3: Scaffold

```python
# Create file structure
# Add imports
# Define interfaces
# Add TODOs
```

### Step 4: Core Logic

```python
# Implement main functionality
# Add error handling
# Add logging
# Follow patterns from similar code
```

### Step 5: Tests

```python
# Write unit tests first
# Test happy path
# Test edge cases
# Test error cases
```

### Step 6: Integration

```python
# Wire into existing system
# Update routes/exports
# Test integration
```

### Step 7: Documentation

- [ ] Update inline comments
- [ ] Update API docs
- [ ] Update relevant .md files
- [ ] Add examples if needed

## Code Quality Checklist

- [ ] Types defined
- [ ] Errors handled
- [ ] Logging added
- [ ] No magic numbers/strings
- [ ] Functions < 50 lines
- [ ] Complexity < 10
- [ ] No duplicate code

## Post-Implementation

### Step 8: Verification

```bash
# Run tests
pytest

# Check lint
ruff check .
black --check .

# Type check
mypy
```

### Step 9: Commit

```bash
git add <files>
git commit -m "type(scope): description"
git push
```

## Patterns

### New Feature

1. Create branch: `feature/name`
2. Implement backend
3. Implement frontend
4. Add tests
5. Update docs
6. Create PR

### Bug Fix

1. Create branch: `fix/description`
2. Write test reproducing bug
3. Fix code
4. Verify test passes
5. Check no regression
6. Create PR

### Refactor

1. Create branch: `refactor/description`
2. Ensure tests exist
3. Refactor code
4. Verify tests pass
5. Check no behavior change
6. Create PR
