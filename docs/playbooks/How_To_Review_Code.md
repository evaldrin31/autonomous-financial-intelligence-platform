# How To: Review Code

**Version**: 1.0

## Overview

Conduct effective code reviews.

## Before Review

- [ ] Understand the change
- [ ] Read requirements
- [ ] Review tests

## Review Checklist

### Code Quality

- [ ] Follows standards
- [ ] Properly typed
- [ ] Well named
- [ ] No duplication
- [ ] Error handling

### Functionality

- [ ] Does what it says
- [ ] Edge cases handled
- [ ] Tests comprehensive
- [ ] No obvious bugs

### Documentation

- [ ] Code commented
- [ ] Complex logic explained
- [ ] API documented
- [ ] CHANGELOG updated

## Review Process

1. **Scan** - Quick read
2. **Understand** - What does it do?
3. **Check** - Against standards
4. **Test** - Run if needed
5. **Comment** - Note issues
6. **Decide** - Approve/Request changes

## Comment Format

```
[Major] Issue that must be fixed
[Minor] Should be fixed
[Suggestion] Nice to have
[Nit] Style preference
```

## Approval Levels

| Level | Meaning |
|-------|---------|
| Approve | Ready to merge |
| Comment | Minor issues |
| Request Changes | Must fix |

## Timing

- Review within 4 hours
- Urgent: Within 1 hour

## References

- [Engineering Review Protocol](../../prompts/ENGINEERING_REVIEW_PROTOCOL.md)
