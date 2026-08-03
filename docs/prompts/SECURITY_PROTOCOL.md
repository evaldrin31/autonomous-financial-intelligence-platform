# SECURITY PROTOCOL: OpenCode

**Version**: 1.0

## Scope

Security considerations in all development.

## Prerequisites

Read:
- [ ] ../standards/Security_Standards.md

## Checklist

### Authentication

- [ ] JWT properly validated
- [ ] Tokens expire
- [ ] Refresh tokens rotated
- [ ] Passwords hashed (bcrypt)
- [ ] Rate limiting on auth

### Input Validation

- [ ] All inputs validated
- [ ] SQL injection prevented
- [ ] XSS prevented
- [ ] File uploads validated
- [ ] Size limits enforced

### Data Protection

- [ ] PII encrypted
- [ ] Secrets in env vars
- [ ] No hardcoded credentials
- [ ] HTTPS only
- [ ] Secure headers

### API Security

- [ ] CORS configured
- [ ] Rate limiting
- [ ] API versioning
- [ ] No sensitive data in logs
- [ ] Proper error messages

### Dependency Security

- [ ] No known vulnerabilities
- [ ] Dependencies updated
- [ ] Pin versions
- [ ] Audit regularly

## Secrets

Never commit:
- API keys
- Passwords
- Private keys
- Database URLs with credentials
- JWT secrets

Use:
- Environment variables
- Secret managers
- Docker secrets

## Response

If security issue found:
1. Assess severity
2. Fix immediately
3. Rotate affected secrets
4. Notify team
5. Document in incident log

## Common Vulnerabilities

| Issue | Prevention |
|-------|------------|
| SQL Injection | Use ORM, parameterized queries |
| XSS | Escape output, CSP headers |
| CSRF | Tokens, SameSite cookies |
| IDOR | Validate ownership |
