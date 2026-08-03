# Project Decisions: Autonomous Financial Intelligence Platform

## Architecture Decision Records (ADRs)

---

## ADR-001: FastAPI for Backend Framework

**Status**: Accepted ✅  
**Date**: 2024-01-01  
**Decision Maker**: Lead Architect

### Context

Need to select a Python web framework for the AFIP backend API.

### Decision

Use **FastAPI** as the backend framework.

### Rationale

- Native async/await support
- Automatic OpenAPI documentation
- Type safety with Pydantic
- High performance (Starlette + Uvicorn)
- Modern Python 3.11+ features
- Excellent DX with auto-reload

### Alternatives Considered

| Alternative | Reason Not Chosen |
|-------------|-------------------|
| Django | Too heavy, not async-native |
| Flask | No native async, requires more boilerplate |
| FastAPI | ✅ Selected |

### Consequences

**Positive**:
- Faster development
- Auto-generated docs
- Type safety
- High performance

**Negative**:
- Learning curve for team new to async
- Smaller ecosystem than Django

---

## ADR-002: Next.js for Frontend

**Status**: Accepted ✅  
**Date**: 2024-01-01  
**Decision Maker**: Lead Architect

### Context

Need to select a frontend framework for the AFIP web application.

### Decision

Use **Next.js 14** with App Router.

### Rationale

- Server Components for performance
- App Router for modern routing
- React 18 concurrent features
- Built-in optimizations
- Excellent TypeScript support

### Alternatives Considered

| Alternative | Reason Not Chosen |
|-------------|-------------------|
| Vue 3 | Smaller ecosystem |
| Remix | Newer, less mature |
| Next.js | ✅ Selected |

### Consequences

**Positive**:
- SEO-friendly with SSR
- Excellent developer experience
- Large ecosystem
- Vercel integration

**Negative**:
- Learning curve for App Router
- Can be complex for simple apps

---

## ADR-003: PostgreSQL for Primary Database

**Status**: Accepted ✅  
**Date**: 2024-01-01  
**Decision Maker**: Lead Architect

### Context

Need to select a primary database for storing application data.

### Decision

Use **PostgreSQL 15+** as the primary database.

### Rationale

- ACID compliance
- Excellent relational capabilities
- pgvector for embeddings
- JSON support for flexibility
- Proven at scale

### Alternatives Considered

| Alternative | Reason Not Chosen |
|-------------|-------------------|
| MySQL | Less feature-rich |
| MongoDB | No ACID transactions |
| PostgreSQL | ✅ Selected |

---

## ADR-004: SQLAlchemy 2.0 for ORM

**Status**: Accepted ✅  
**Date**: 2024-01-01  
**Decision Maker**: Lead Architect

### Context

Need an ORM for database operations.

### Decision

Use **SQLAlchemy 2.0** with async support.

### Rationale

- Full async support
- Type-safe with mypy
- Modern declarative syntax
- Excellent migration support (Alembic)

---

## ADR-005: Modular Architecture

**Status**: Accepted ✅  
**Date**: 2024-01-01  
**Decision Maker**: Lead Architect

### Context

Need to organize codebase for maintainability.

### Decision

Use **layered modular architecture**:
- API layer (routes)
- Service layer (business logic)
- Repository layer (data access)
- Model layer (database)

### Rationale

- Clear separation of concerns
- Testable layers
- Reusable components
- Easy to understand

---

## Document Information

| Field | Value |
|-------|-------|
| Document ID | AFIP-DOC-023 |
| Version | 1.0.0 |
| Status | Active |

---

## Next Document

**→ Continue to**: [24_Future_Scope.md](./24_Future_Scope.md)  
**← Back to**: [22_Project_State.md](./22_Project_State.md)
