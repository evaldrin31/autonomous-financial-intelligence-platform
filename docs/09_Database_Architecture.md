# Database Architecture: Autonomous Financial Intelligence Platform

## Executive Summary

This document defines the database architecture for AFIP, using PostgreSQL as the primary datastore with specialized extensions for vector operations (pgvector) and full-text search. The architecture supports relational data, document embeddings, and time-series market data.

---

## 1. Database Overview

### 1.1 Technology Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| Primary DB | PostgreSQL | 15+ | OLTP and analytics |
| Extensions | pgvector | 0.5+ | Vector embeddings |
| Extensions | pg_trgm | Built-in | Text search |
| Migrations | Alembic | 1.12+ | Schema versioning |
| ORM | SQLAlchemy | 2.0+ | Python interface |
| Cache Layer | Redis | 7+ | Session and query cache |

### 1.2 Design Principles

1. **Normalization**: 3NF for core data, denormalized for analytics
2. **Auditability**: All changes tracked with timestamps
3. **Scalability**: Partitioning for time-series data
4. **Type Safety**: Strong typing with constraints
5. **Soft Deletes**: Never lose data

---

## 2. Entity Relationship Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    ENTITY RELATIONSHIPS                         │
└─────────────────────────────────────────────────────────────────┘

┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│    users     │         │  portfolios  │         │    assets    │
├──────────────┤         ├──────────────┤         ├──────────────┤
│ id (PK)      │──────<──│ id (PK)      │──────<──│ id (PK)      │
│ email        │    1:M  │ user_id (FK) │    1:M  │ portfolio_id │
│ password_hash│         │ name         │         │ symbol       │
│ full_name    │         │ total_value  │         │ quantity     │
│ is_active    │         │ currency     │         │ avg_price    │
└──────────────┘         └──────────────┘         └──────────────┘
        │                        │                        │
        │                        │                        │
        ▼                        ▼                        ▼
┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│refresh_tokens│         │transactions  │         │price_history │
├──────────────┤         ├──────────────┤         ├──────────────┤
│ id (PK)      │         │ id (PK)      │         │ id (PK)      │
│ user_id (FK) │         │ asset_id (FK)│         │ asset_id (FK)│
│ token        │         │ type         │         │ price        │
│ expires_at   │         │ quantity     │         │ timestamp    │
└──────────────┘         │ price        │         └──────────────┘
                         └──────────────┘
```

---

## 3. Core Tables

### 3.1 Users Table

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    is_superuser BOOLEAN DEFAULT FALSE,
    last_login TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at);
```

### 3.2 Portfolios Table

```sql
CREATE TABLE portfolios (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    currency VARCHAR(3) DEFAULT 'USD',
    total_value NUMERIC(19,4) DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_portfolios_user_id ON portfolios(user_id);
CREATE INDEX idx_portfolios_created_at ON portfolios(created_at);
```

### 3.3 Assets Table

```sql
CREATE TABLE assets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    portfolio_id UUID NOT NULL REFERENCES portfolios(id) ON DELETE CASCADE,
    symbol VARCHAR(20) NOT NULL,
    name VARCHAR(255),
    asset_type VARCHAR(50) NOT NULL, -- stock, bond, crypto, etc.
    quantity NUMERIC(19,8) NOT NULL DEFAULT 0,
    avg_buy_price NUMERIC(19,8),
    current_price NUMERIC(19,8),
    current_value NUMERIC(19,4) GENERATED ALWAYS AS (
        COALESCE(quantity * current_price, 0)
    ) STORED,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_assets_portfolio_id ON assets(portfolio_id);
CREATE INDEX idx_assets_symbol ON assets(symbol);
```

### 3.4 Transactions Table

```sql
CREATE TABLE transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    portfolio_id UUID NOT NULL REFERENCES portfolios(id) ON DELETE CASCADE,
    asset_id UUID REFERENCES assets(id) ON DELETE SET NULL,
    type VARCHAR(10) NOT NULL CHECK (type IN ('BUY', 'SELL', 'DIVIDEND')),
    quantity NUMERIC(19,8) NOT NULL,
    price NUMERIC(19,8) NOT NULL,
    fees NUMERIC(19,4) DEFAULT 0,
    total_amount NUMERIC(19,4) NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_transactions_portfolio_id ON transactions(portfolio_id);
CREATE INDEX idx_transactions_asset_id ON transactions(asset_id);
CREATE INDEX idx_transactions_timestamp ON transactions(timestamp);
```

---

## 4. Vector Tables (RAG)

### 4.1 Documents Table

```sql
-- Enable pgvector
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source VARCHAR(255) NOT NULL,
    source_type VARCHAR(50) NOT NULL,
    title VARCHAR(500),
    content TEXT,
    embedding VECTOR(1536),  -- OpenAI text-embedding-3-small
    metadata JSONB DEFAULT '{}',
    tickers TEXT[] DEFAULT '{}',
    sectors TEXT[] DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- HNSW index for vector similarity
CREATE INDEX idx_documents_embedding ON documents
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- GIN index for metadata filtering
CREATE INDEX idx_documents_metadata ON documents USING GIN (metadata);
CREATE INDEX idx_documents_tickers ON documents USING GIN (tickers);
```

---

## 5. Partitioning Strategy

### 5.1 Time-Series Partitioning

```sql
-- Price history partitioned by month
CREATE TABLE price_history (
    id UUID,
    asset_id UUID NOT NULL,
    price NUMERIC(19,8) NOT NULL,
    volume BIGINT,
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    PRIMARY KEY (id, timestamp)
) PARTITION BY RANGE (timestamp);

-- Create monthly partitions
CREATE TABLE price_history_2024_01 PARTITION OF price_history
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE price_history_2024_02 PARTITION OF price_history
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');
```

---

## 6. Migration Management

### 6.1 Alembic Structure

```
backend/alembic/
├── env.py                    # Migration environment
├── script.py.mako           # Migration template
├── alembic.ini              # Configuration
└── versions/                # Migration files
    ├── 001_create_users.py
    ├── 002_create_portfolios.py
    └── 003_create_assets.py
```

### 6.2 Migration Commands

```bash
# Create migration
alembic revision --autogenerate -m "create users table"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1

# Show current
alembic current
```

---

## 7. Document Information

| Field | Value |
|-------|-------|
| Document ID | AFIP-DOC-009 |
| Version | 1.0.0 |
| Status | Draft |

---

## Next Document

**→ Continue to**: [10_API_Architecture.md](./10_API_Architecture.md)  
**← Back to**: [08_Frontend_Architecture.md](./08_Frontend_Architecture.md)
