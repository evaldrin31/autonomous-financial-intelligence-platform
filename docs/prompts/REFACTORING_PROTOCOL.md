# REFACTORING PROTOCOL: OpenCode

**Version**: 1.0

## Scope

Safe code refactoring.

## When to Refactor

- [ ] Code is hard to understand
- [ ] Duplication exists
- [ ] Performance issues
- [ ] Technical debt
- [ ] Adding features is hard

## Safety Rules

1. Tests must exist before refactoring
2. Tests must pass after refactoring
3. No behavior changes
4. One change at a time
5. Commit frequently

## Process

### 1. Preparation

- [ ] Identify code to refactor
- [ ] Ensure tests exist
- [ ] Verify tests pass
- [ ] Create branch

### 2. Refactor

```
Extract Method → Rename → Inline → Move
```

### 3. Verify

```bash
# Run tests
pytest

# Check types
mypy

# Check lint
ruff check .
```

### 4. Commit

```bash
git add .
git commit -m "refactor(scope): description"
```

## Patterns

| Pattern | When |
|---------|------|
| Extract Method | Function too long |
| Rename | Unclear names |
| Inline | Unnecessary abstraction |
| Move | Wrong location |
| Replace Conditional | With polymorphism |

## Red Flags

Don't refactor when:
- No tests exist
- Deadline is tight
- Code is working and stable
- Risk > benefit

## Common Tasks

| Task | Approach |
|------|----------|
| Extract function | Cut, paste, test |
| Rename | IDE refactor, test |
| Simplify | Remove duplication |
