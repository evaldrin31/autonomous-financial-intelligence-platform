# Release Process: AFIP

**Version**: 1.0

## Release Types

| Type | Frequency | Version Bump |
|------|-----------|--------------|
| Patch | Weekly | 1.0.x |
| Minor | Monthly | 1.x.0 |
| Major | Quarterly | x.0.0 |

## Release Checklist

### Pre-release (Day -3)

- [ ] All features merged
- [ ] Tests passing
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped

### Release Day

- [ ] Create release branch: `release/v1.x.x`
- [ ] Run full test suite
- [ ] Deploy to staging
- [ ] Smoke tests pass
- [ ] Create GitHub release
- [ ] Merge to main
- [ ] Deploy to production
- [ ] Verify in production

### Post-release

- [ ] Monitor for 24 hours
- [ ] Announce in #releases
- [ ] Update documentation
- [ ] Tag deployment

## Hotfix Process

1. Branch from main: `hotfix/description`
2. Fix with minimal changes
3. Fast-track review
4. Deploy immediately
5. Merge to develop

## Rollback

If issues detected:
1. Identify last good version
2. Deploy previous version
3. Fix forward in next release
4. Post-mortem within 48 hours
