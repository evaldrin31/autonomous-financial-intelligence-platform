# Git Standards: AFIP

**Version**: 1.0

## Branches

| Type | Pattern | From |
|------|---------|------|
| Feature | `feature/description` | develop |
| Bugfix | `fix/description` | develop |
| Hotfix | `hotfix/description` | main |
| Release | `release/vX.X.X` | develop |

## Commits

Format: `type(scope): subject`

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- style: Formatting
- refactor: Restructuring
- test: Tests
- chore: Maintenance

Example: `feat(auth): add JWT login`

## PRs

- Create from feature branch
- Fill template
- Request review
- Address feedback
- Squash if needed
- Merge with --no-ff

## Workflow

```bash
# Create branch
git checkout -b feature/name develop

# Work
git commit -m "feat: description"

# Push
git push -u origin feature/name

# PR and merge
```

## Protected Branches

- main: No direct push
- develop: PR required

## Anti-patterns

- ❌ Commit to main directly
- ❌ Large PRs (>500 lines)
- ❌ Unclear commit messages
- ❌ Merge without review
