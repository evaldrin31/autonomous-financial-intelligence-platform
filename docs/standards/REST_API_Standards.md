# REST API Standards: AFIP

**Version**: 1.0

## URL Structure

```
/api/v1/resources
/api/v1/resources/{id}
/api/v1/resources/{id}/subresources
```

## Methods

| Method | Action | Response |
|--------|--------|----------|
| GET | Read | 200, 404 |
| POST | Create | 201, 400 |
| PUT | Update | 200, 404 |
| DELETE | Delete | 204, 404 |

## Response Format

```json
{
  "success": true,
  "data": { },
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z"
  }
}
```

## Error Format

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input"
  }
}
```

## Status Codes

| Code | Use |
|------|-----|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 422 | Validation Error |
| 500 | Server Error |

## Pagination

```
GET /portfolios?limit=20&cursor=xxx
```

```json
{
  "data": [],
  "pagination": {
    "next_cursor": "xxx",
    "has_more": true
  }
}
```

## Versioning

- URL-based: `/api/v1/`
- Breaking changes → new version
- Deprecation period: 6 months
