# DEPLOYMENT PROTOCOL: OpenCode

**Version**: 1.0

## Scope

Deployment procedures for AFIP.

## Prerequisites

Read:
- [ ] ../../docs/company/Release_Process.md

## Environments

| Env | URL | Purpose |
|-----|-----|---------|
| Local | localhost | Development |
| Staging | staging.afip.com | Testing |
| Production | app.afip.com | Live |

## Deployment Workflow

### To Staging

1. Merge feature to develop
2. Verify tests pass
3. Deploy: `docker-compose -f docker-compose.staging.yml up -d`
4. Smoke tests
5. Notify team

### To Production

1. Create release branch
2. Final testing
3. Create GitHub release
4. Deploy with zero downtime
5. Verify health checks
6. Monitor metrics

## Pattern

```bash
# Build
docker build -t afip-backend:latest .

# Tag
docker tag afip-backend:latest registry.com/afip-backend:v1.0.0

# Push
docker push registry.com/afip-backend:v1.0.0

# Deploy
kubectl apply -f k8s/
```

## Rollback

```bash
# Identify last good version
docker pull afip-backend:v0.9.0

# Deploy previous
docker-compose up -d

# Verify rollback
```

## Monitoring

- Check logs: `docker logs <container>`
- Check health: `curl /health`
- Check metrics: Dashboard
- Check alerts: PagerDuty

## Safety

- Never deploy on Friday
- Always have rollback plan
- Monitor for 24 hours
- Keep previous version ready
