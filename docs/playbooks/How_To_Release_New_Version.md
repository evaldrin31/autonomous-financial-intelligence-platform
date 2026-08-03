# How To: Release New Version

**Version**: 1.0

## Overview

Complete release process.

## Checklist

### Pre-Release (Day -3)

- [ ] All features merged
- [ ] Tests passing
- [ ] Documentation updated
- [ ] CHANGELOG updated
- [ ] Version bumped

### Release Day

1. **Create Branch**
   ```bash
   git checkout -b release/v1.1.0 develop
   ```

2. **Final Testing**
   ```bash
   pytest
   npm test
   ```

3. **Version Bump**
   ```bash
   # Update version in package.json, pyproject.toml
   ```

4. **Merge to Main**
   ```bash
   git checkout main
   git merge release/v1.1.0
   git tag v1.1.0
   git push origin main --tags
   ```

5. **Deploy**
   ```bash
   docker build -t afip:v1.1.0 .
   kubectl apply -f k8s/
   ```

6. **Verify**
   - Health check
   - Smoke tests
   - Monitor metrics

### Post-Release

- [ ] Announce in #releases
- [ ] Update documentation
- [ ] Monitor for 24 hours

## Template

```markdown
## Release v1.1.0

**Date**: 2024-01-01

### Features
- Feature 1

### Fixes
- Fix 1

### Breaking Changes
- None
```

## References

- [Release Process](../../company/Release_Process.md)
