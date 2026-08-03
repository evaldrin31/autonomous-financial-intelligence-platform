# How To: Deploy

**Version**: 1.0

## Overview

Deploy AFIP to production.

## Prerequisites

- [ ] Tests passing
- [ ] Code reviewed
- [ ] Documentation updated

## Local Deploy

```bash
docker-compose up -d
```

## Staging Deploy

```bash
# Build
docker build -t afip-backend:staging .

# Deploy
kubectl apply -f k8s/staging/

# Verify
curl https://staging.afip.com/api/v1/health
```

## Production Deploy

### 1. Create Release

```bash
# Create branch
git checkout -b release/v1.1.0 develop

# Update version
# Update CHANGELOG

# Commit
git commit -m "chore: bump version to 1.1.0"
```

### 2. Build

```bash
docker build -t afip-backend:v1.1.0 .
docker push registry/afip-backend:v1.1.0
```

### 3. Deploy

```bash
kubectl apply -f k8s/production/
```

### 4. Verify

```bash
# Health check
curl https://api.afip.com/health

# Smoke tests
pytest tests/e2e/
```

### 5. Monitor

- Watch logs
- Check metrics
- Monitor for 1 hour

## Rollback

```bash
kubectl rollout undo deployment/backend
```

## References

- [Release Process](../../company/Release_Process.md)
- [Deployment Protocol](../../prompts/DEPLOYMENT_PROTOCOL.md)
