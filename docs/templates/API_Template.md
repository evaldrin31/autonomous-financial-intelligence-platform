# API Endpoint Template

## Overview

Brief description of the endpoint.

## Request

### Method

`GET | POST | PUT | DELETE`

### URL

`/api/v1/resource`

### Headers

```
Authorization: Bearer {token}
Content-Type: application/json
```

### Body (if applicable)

```json
{
  "field": "value"
}
```

## Response

### Success (200)

```json
{
  "success": true,
  "data": {}
}
```

### Error (4XX/5XX)

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Description"
  }
}
```

## Examples

### Example 1

Request:
```bash
curl /api/v1/resource
```

Response:
```json
{}
```

## Errors

| Code | Meaning |
|------|---------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
