# How To: Handle Bugs

**Version**: 1.0

## Overview

Systematic bug handling process.

## Process

### 1. Report

Create issue with:
- Clear title
- Steps to reproduce
- Expected vs actual
- Environment
- Screenshots/logs

### 2. Triage

| Severity | Response Time |
|----------|---------------|
| Critical | 1 hour |
| High | 1 day |
| Medium | 1 week |
| Low | Backlog |

### 3. Investigate

- Find root cause
- Assess impact
- Identify related code

### 4. Fix

```python
# Write test first
def test_bug_reproduction():
    # Arrange
    input = ...
    
    # Act
    result = function(input)
    
    # Assert
    assert result == expected  # Should fail initially

# Fix code
def function(input):
    # Fixed logic
    return result

# Verify test passes
```

### 5. Verify

- [ ] Test passes
- [ ] No regression
- [ ] Code reviewed

### 6. Deploy

- Deploy to staging
- Verify
- Deploy to production
- Monitor

## Template

```markdown
## Bug Report

**Description**: Brief description

**Steps**:
1. Step 1
2. Step 2

**Expected**: What should happen
**Actual**: What happens

**Environment**: Version, browser, OS
```

## References

- [Bugfix Protocol](../../prompts/BUGFIX_PROTOCOL.md)
