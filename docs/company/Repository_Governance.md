# Repository Governance: AFIP

**Version**: 1.0

## Structure

```
repo/
├── README.md                 # Entry point
├── LICENSE                   # MIT
├── .gitignore               # Ignore rules
├── .env.example             # Env template
├── docker-compose.yml       # Local dev
├── backend/                 # FastAPI app
├── frontend/                # Next.js app
├── docs/                    # Documentation
├── docker/                  # Dockerfiles
└── scripts/                 # Automation
```

## Branches

| Branch | Purpose | Protection |
|--------|---------|------------|
| main | Production | Force push blocked |
| develop | Integration | PR required |
| feature/* | Features | PR required |
| hotfix/* | Fixes | PR required |

## Commit Messages

Format: `type(scope): subject`

Types: feat, fix, docs, style, refactor, test, chore

Example: `feat(auth): add JWT token refresh`

## PR Requirements

- [ ] Tests pass
- [ ] Docs updated
- [ ] Review approved
- [ ] No conflicts
- [ ] Squash if needed

## File Ownership

| Area | Owner |
|------|-------|
| Backend/ | Backend Lead |
| Frontend/ | Frontend Lead |
| Docs/architecture/ | Principal Architect |
| Docs/company/ | CTO |
| Infrastructure/ | DevOps |

## Access Control

| Role | Access |
|------|--------|
| Maintainer | Write to protected |
| Developer | Write to feature |
| Contributor | PR only |
| Read | View only |

## Maintenance

- Monthly dependency updates
- Quarterly structure review
- Annual archive old branches
