# Security Standards: AFIP

**Version**: 1.0

## Authentication

- JWT with expiration
- Refresh token rotation
- Password hashing (bcrypt)
- Rate limiting on auth

## Input Validation

- Validate all inputs
- Use Pydantic/FastAPI validation
- Sanitize user input
- Prevent SQL injection

## Secrets

- Store in environment variables
- Never commit secrets
- Rotate regularly
- Use secret manager in prod

## HTTPS

- TLS 1.3 only
- Secure headers
- HSTS enabled
- No mixed content

## CORS

- Whitelist specific origins
- No wildcards in production
- Credentials restricted

## Dependencies

- Audit regularly
- Pin versions
- Update promptly
- No known vulnerabilities

## Response Headers

```
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000
Content-Security-Policy: default-src 'self'
```

## Secrets Checklist

- [ ] No hardcoded passwords
- [ ] No API keys in code
- [ ] No private keys
- [ ] .env.example only
- [ ] No .env committed
