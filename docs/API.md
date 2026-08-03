# API Documentation

## Autonomous Financial Intelligence Platform API

### Overview

This document describes the REST API for the Autonomous Financial Intelligence Platform.

**Base URL**: `http://localhost:8000/api/v1`

**Content-Type**: `application/json`

### Authentication

All API requests (except login/register) require authentication via JWT token.

**Header Format**:
```
Authorization: Bearer <token>
```

### Response Format

All responses follow this structure:

```json
{
  "success": true,
  "data": { },
  "message": "Optional message",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

Error responses:

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": { }
  },
  "timestamp": "2024-01-01T00:00:00Z"
}
```

### HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Request succeeded |
| 201 | Created - Resource created successfully |
| 400 | Bad Request - Invalid input data |
| 401 | Unauthorized - Authentication required |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found - Resource not found |
| 422 | Unprocessable Entity - Validation error |
| 500 | Internal Server Error - Server error |

---

## Endpoints

### Health Check

**GET** `/health`

Check API health status.

**Response**:
```json
{
  "success": true,
  "data": {
    "status": "healthy",
    "version": "1.0.0",
    "timestamp": "2024-01-01T00:00:00Z"
  }
}
```

### Authentication

#### Register

**POST** `/auth/register`

Register a new user.

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securepassword123",
  "full_name": "John Doe"
}
```

**Response**:
```json
{
  "success": true,
  "data": {
    "user_id": "uuid",
    "email": "user@example.com",
    "access_token": "jwt_token",
    "refresh_token": "refresh_token"
  }
}
```

#### Login

**POST** `/auth/login`

Authenticate user and receive tokens.

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

#### Refresh Token

**POST** `/auth/refresh`

Refresh access token using refresh token.

**Request Body**:
```json
{
  "refresh_token": "refresh_token"
}
```

#### Logout

**POST** `/auth/logout`

Invalidate tokens.

**Headers**:
```
Authorization: Bearer <token>
```

---

### Users

#### Get Current User

**GET** `/users/me`

Get current authenticated user details.

**Response**:
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "email": "user@example.com",
    "full_name": "John Doe",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  }
}
```

#### Update User

**PUT** `/users/me`

Update current user details.

---

### Portfolios

#### List Portfolios

**GET** `/portfolios`

List all portfolios for the current user.

**Query Parameters**:
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20, max: 100)

**Response**:
```json
{
  "success": true,
  "data": {
    "items": [...],
    "total": 100,
    "page": 1,
    "limit": 20
  }
}
```

#### Create Portfolio

**POST** `/portfolios`

Create a new portfolio.

**Request Body**:
```json
{
  "name": "My Portfolio",
  "description": "Long-term investment portfolio",
  "currency": "USD"
}
```

#### Get Portfolio

**GET** `/portfolios/{portfolio_id}`

Get portfolio details by ID.

#### Update Portfolio

**PUT** `/portfolios/{portfolio_id}`

Update portfolio details.

#### Delete Portfolio

**DELETE** `/portfolios/{portfolio_id}`

Delete a portfolio.

---

### Analytics

#### Portfolio Analytics

**GET** `/analytics/portfolios/{portfolio_id}`

Get comprehensive analytics for a portfolio.

**Query Parameters**:
- `start_date`: Start date (ISO 8601)
- `end_date`: End date (ISO 8601)

**Response**:
```json
{
  "success": true,
  "data": {
    "returns": {
      "total": 15.5,
      "annualized": 12.3,
      "daily": [...]
    },
    "risk": {
      "volatility": 18.2,
      "sharpe_ratio": 0.85,
      "max_drawdown": -12.5
    },
    "allocation": [...]
  }
}
```

---

## WebSocket API

Real-time updates are available via WebSocket.

**URL**: `ws://localhost:8000/ws`

### Connection

Connect with authentication token as query parameter:

```
ws://localhost:8000/ws?token=<jwt_token>
```

### Message Format

**Client to Server**:
```json
{
  "type": "subscribe",
  "channel": "portfolio_updates",
  "data": {
    "portfolio_id": "uuid"
  }
}
```

**Server to Client**:
```json
{
  "type": "portfolio_update",
  "timestamp": "2024-01-01T00:00:00Z",
  "data": {
    "portfolio_id": "uuid",
    "total_value": 100000,
    "change": 500
  }
}
```

### Channels

| Channel | Description |
|---------|-------------|
| `portfolio_updates` | Real-time portfolio value updates |
| `market_data` | Market price updates |
| `alerts` | System alerts and notifications |

---

## Rate Limits

| Endpoint | Limit |
|----------|-------|
| General API | 1000 requests/hour |
| Authentication | 10 requests/minute |
| Portfolio Operations | 100 requests/minute |
| Analytics | 60 requests/minute |

---

## SDKs and Clients

Official SDKs (coming soon):
- Python: `pip install afip-sdk`
- JavaScript: `npm install @afip/sdk`
- TypeScript: `npm install @afip/sdk`

---

## Changelog

### v1.0.0 (Current)
- Initial API release
- Authentication endpoints
- Portfolio CRUD operations
- Basic analytics endpoints

### v1.1.0 (Planned)
- WebSocket support
- Advanced analytics
- Report generation
