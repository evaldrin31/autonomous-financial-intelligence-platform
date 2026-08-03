# API Architecture: Autonomous Financial Intelligence Platform

## Executive Summary

This document defines the REST API architecture for AFIP, specifying endpoint design, authentication, rate limiting, versioning strategy, and data formats. The API follows RESTful principles with comprehensive OpenAPI documentation.

---

## 1. API Overview

### 1.1 Base URLs

| Environment | URL |
|-------------|-----|
| Development | `http://localhost:8000/api/v1` |
| Staging | `https://api-staging.afip.com/api/v1` |
| Production | `https://api.afip.com/api/v1` |

### 1.2 Protocol

- **Primary**: HTTPS (TLS 1.3)
- **WebSocket**: WSS for real-time updates
- **CORS**: Configured for authorized origins

---

## 2. Authentication

### 2.1 JWT Authentication

**Header Format**:
```
Authorization: Bearer <jwt_token>
```

**Token Structure**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

**Token Claims**:
```json
{
  "sub": "user-uuid",
  "exp": 1704067200,
  "iat": 1704063600,
  "type": "access"
}
```

### 2.2 Authentication Endpoints

| Endpoint | Method | Auth Required | Description |
|----------|--------|---------------|-------------|
| `/auth/register` | POST | No | Create account |
| `/auth/login` | POST | No | Authenticate |
| `/auth/refresh` | POST | No | Refresh token |
| `/auth/logout` | POST | Yes | Invalidate tokens |
| `/auth/me` | GET | Yes | Current user |

---

## 3. API Standards

### 3.1 Response Format

**Success Response**:
```json
{
  "success": true,
  "data": { },
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z",
    "request_id": "uuid"
  }
}
```

**Error Response**:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {
      "field": ["error description"]
    }
  },
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z",
    "request_id": "uuid"
  }
}
```

### 3.2 HTTP Status Codes

| Code | Meaning | Usage |
|------|---------|-------|
| 200 | OK | GET, PUT success |
| 201 | Created | POST success |
| 204 | No Content | DELETE success |
| 400 | Bad Request | Validation error |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | Permission denied |
| 404 | Not Found | Resource not found |
| 422 | Validation Error | Schema validation failed |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Server Error | Unexpected error |

---

## 4. Endpoints

### 4.1 Portfolio Endpoints

```
GET    /portfolios              - List portfolios
POST   /portfolios              - Create portfolio
GET    /portfolios/{id}         - Get portfolio
PUT    /portfolios/{id}         - Update portfolio
DELETE /portfolios/{id}         - Delete portfolio
GET    /portfolios/{id}/assets  - List assets
POST   /portfolios/{id}/analyze - Analyze portfolio
```

**Portfolio Schema**:
```json
{
  "id": "uuid",
  "name": "My Portfolio",
  "description": "Investment portfolio",
  "currency": "USD",
  "total_value": 100000.00,
  "assets": [
    {
      "id": "uuid",
      "symbol": "AAPL",
      "name": "Apple Inc.",
      "quantity": 100,
      "current_price": 150.00,
      "current_value": 15000.00
    }
  ],
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

### 4.2 Asset Endpoints

```
GET    /assets              - List assets
POST   /assets              - Add asset
GET    /assets/{id}         - Get asset
PUT    /assets/{id}         - Update asset
DELETE /assets/{id}         - Remove asset
```

### 4.3 Transaction Endpoints

```
GET    /transactions              - List transactions
POST   /transactions              - Create transaction
GET    /transactions/{id}       - Get transaction
DELETE /transactions/{id}       - Cancel transaction (if pending)
```

### 4.4 Analytics Endpoints

```
GET /analytics/portfolios/{id}   - Portfolio analytics
GET /analytics/assets/{id}       - Asset analytics
GET /analytics/market            - Market analytics
```

**Analytics Response**:
```json
{
  "portfolio_id": "uuid",
  "time_range": "1Y",
  "returns": {
    "total": 15.5,
    "annualized": 12.3,
    "daily": [...]
  },
  "risk": {
    "volatility": 18.2,
    "sharpe_ratio": 0.85,
    "max_drawdown": -12.5,
    "var_95": -2.1
  },
  "allocation": [
    { "sector": "Technology", "percentage": 40.0 },
    { "sector": "Healthcare", "percentage": 30.0 }
  ]
}
```

### 4.5 AI Agent Endpoints

```
POST   /agents/analyze/portfolio/{id}  - Analyze portfolio
POST   /agents/research/market         - Market research
POST   /agents/ask                      - Natural language query
GET    /agents/decisions                - List decisions
GET    /agents/decisions/{id}           - Get decision details
```

### 4.6 RAG Endpoints

```
POST   /rag/query      - Query knowledge base
POST   /rag/ingest     - Ingest documents (admin)
GET    /rag/documents  - List documents (admin)
DELETE /rag/documents/{id} - Remove document (admin)
```

---

## 5. Pagination

### 5.1 Cursor-Based Pagination

**Request**:
```
GET /portfolios?limit=20&cursor=eyJpZCI6MTAwfQ==
```

**Response**:
```json
{
  "success": true,
  "data": [...],
  "pagination": {
    "limit": 20,
    "next_cursor": "eyJpZCI6MTIwfQ==",
    "has_more": true
  }
}
```

---

## 6. Rate Limiting

### 6.1 Rate Limit Headers

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1704067200
```

### 6.2 Rate Limits by Tier

| Tier | Requests/Min | Requests/Hour |
|------|--------------|-----------------|
| Free | 60 | 1000 |
| Pro | 300 | 10000 |
| Enterprise | 1000 | 50000 |

---

## 7. WebSocket API

### 7.1 Connection

```
WSS: wss://api.afip.com/ws?token=<jwt_token>
```

### 7.2 Message Types

**Subscribe**:
```json
{
  "type": "subscribe",
  "channel": "portfolio_updates",
  "data": { "portfolio_id": "uuid" }
}
```

**Update**:
```json
{
  "type": "portfolio_update",
  "timestamp": "2024-01-01T00:00:00Z",
  "data": {
    "portfolio_id": "uuid",
    "total_value": 105000.00,
    "change": 5000.00
  }
}
```

---

## 8. Document Information

| Field | Value |
|-------|-------|
| Document ID | AFIP-DOC-010 |
| Version | 1.0.0 |
| Status | Draft |

---

## Next Document

**→ Continue to**: [11_Paper_Trading_Engine.md](./11_Paper_Trading_Engine.md)  
**← Back to**: [09_Database_Architecture.md](./09_Database_Architecture.md)
