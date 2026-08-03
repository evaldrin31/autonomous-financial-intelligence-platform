# Deployment Guide: Autonomous Financial Intelligence Platform

## Executive Summary

This document provides comprehensive deployment procedures for AFIP across development, staging, and production environments.

---

## 1. Deployment Overview

### 1.1 Environments

| Environment | URL | Purpose |
|-------------|-----|---------|
| **Local** | localhost:3000/8000 | Development |
| **Staging** | staging.afip.com | Testing |
| **Production** | app.afip.com | Live users |

### 1.2 Deployment Methods

| Method | Best For | Complexity |
|--------|----------|------------|
| **Docker Compose** | Local, Small deployments | Low |
| **Kubernetes** | Production, Scale | High |
| **Serverless** | Variable load | Medium |

---

## 2. Docker Deployment

### 2.1 Local Development

```bash
# Clone repository
git clone [repo-url]
cd afip

# Copy environment
cp .env.example .env
# Edit .env with your settings

# Start services
docker-compose up -d

# Verify
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### 2.2 Production Docker

```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: always

  backend:
    image: afip-backend:latest
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - SECRET_KEY=${SECRET_KEY}
      - DEBUG=false
    ports:
      - "8000:8000"
    restart: always

  frontend:
    image: afip-frontend:latest
    environment:
      - NEXT_PUBLIC_API_URL=${API_URL}
    ports:
      - "3000:3000"
    restart: always

volumes:
  postgres_data:
```

### 2.3 Build and Push

```bash
# Build images
docker build -t afip-backend:latest -f docker/Dockerfile.backend.prod .
docker build -t afip-frontend:latest -f docker/Dockerfile.frontend.prod .

# Push to registry
docker tag afip-backend:latest registry.com/afip-backend:latest
docker push registry.com/afip-backend:latest
```

---

## 3. Environment Configuration

### 3.1 Required Variables

```bash
# Database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=secure_password
POSTGRES_DB=afip
DATABASE_URL=postgresql://user:pass@db:5432/afip

# Security
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30

# API
BACKEND_URL=https://api.afip.com
FRONTEND_URL=https://app.afip.com

# AI (if using cloud)
OPENAI_API_KEY=sk-...
```

### 3.2 Secret Management

```bash
# Use Docker secrets
docker secret create postgres_password secrets/postgres_pass.txt

# Or use a secret manager (HashiCorp Vault, AWS Secrets Manager)
```

---

## 4. Health Checks

### 4.1 Backend Health

```python
# GET /api/v1/health
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2024-01-01T00:00:00Z",
  "services": {
    "database": "connected",
    "redis": "connected",
    "ai_services": "available"
  }
}
```

### 4.2 Frontend Health

```javascript
// Health check endpoint
export default function HealthPage() {
  return new Response('OK', { status: 200 });
}
```

---

## 5. Rollback Procedures

### 5.1 Quick Rollback

```bash
# Rollback to previous version
docker-compose pull
docker-compose up -d --build

# Or use specific tag
docker-compose down
docker tag afip-backend:previous afip-backend:latest
docker-compose up -d
```

---

## 6. Document Information

| Field | Value |
|-------|-------|
| Document ID | AFIP-DOC-018 |
| Version | 1.0.0 |
| Status | Draft |

---

## Next Document

**→ Continue to**: [19_Coding_Standards.md](./19_Coding_Standards.md)  
**← Back to**: [17_Frontend_Workflow.md](./17_Frontend_Workflow.md)
