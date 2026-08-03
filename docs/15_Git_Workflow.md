# Git Workflow: Autonomous Financial Intelligence Platform

## Executive Summary

This document defines the Git branching strategy, commit conventions, and collaboration workflows for AFIP.

---

## 1. Branching Strategy

### 1.1 Git Flow

```
main (production)
  │
  ├─── develop (integration)
  │      │
  │      ├─── feature/auth
  │      ├─── feature/portfolio-crud
  │      └─── feature/market-data
  │
  ├─── hotfix/security-patch
  │
  └─── release/v1.0.0
```

### 1.2 Branch Types

| Branch | Purpose | Protection |
|--------|---------|------------|
| **main** | Production code | Force push blocked |
| **develop** | Integration branch | PR required |
| **feature/*** | New features | PR required |
| **hotfix/*** | Critical fixes | PR required |
| **release/*** | Release preparation | PR required |

---

## 2. Commit Conventions

### 2.1 Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### 2.2 Commit Types

| Type | Description | Example |
|------|-------------|---------|
| **feat** | New feature | feat(auth): add JWT authentication |
| **fix** | Bug fix | fix(api): resolve CORS issue |
| **docs** | Documentation | docs(readme): update setup instructions |
| **style** | Code style | style(frontend): fix indentation |
| **refactor** | Refactoring | refactor(db): optimize queries |
| **test** | Tests | test(auth): add login tests |
| **chore** | Maintenance | chore(deps): update packages |

### 2.3 Example Commit

```
feat(portfolio): add portfolio creation endpoint

- Implement POST /portfolios
- Add validation with Pydantic
- Create database migrations
- Add unit tests

Closes #123
```

---

## 3. Pull Request Process

### 3.1 PR Requirements

- [ ] Descriptive title
- [ ] Detailed description
- [ ] Linked issues
- [ ] Tests passing
- [ ] Code reviewed
- [ ] No conflicts
- [ ] Documentation updated

### 3.2 PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing complete

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No console warnings
```

---

## 4. Commands Reference

```bash
# Create feature branch
git checkout -b feature/portfolio-analytics develop

# Make changes and commit
git add .
git commit -m "feat(portfolio): add analytics endpoint"

# Push and create PR
git push -u origin feature/portfolio-analytics

# Update branch
git checkout develop
git pull origin develop
git checkout feature/portfolio-analytics
git rebase develop

# Merge PR
git checkout develop
git merge --no-ff feature/portfolio-analytics
git push origin develop

# Delete feature branch
git branch -d feature/portfolio-analytics
git push origin --delete feature/portfolio-analytics
```

---

## 5. Document Information

| Field | Value |
|-------|-------|
| Document ID | AFIP-DOC-015 |
| Version | 1.0.0 |
| Status | Draft |

---

## Next Document

**→ Continue to**: [16_OpenCode_Workflow.md](./16_OpenCode_Workflow.md)  
**← Back to**: [14_Project_Workflow.md](./14_Project_Workflow.md)
