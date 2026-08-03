# Database Documentation

## Autonomous Financial Intelligence Platform Database Schema

### Overview

This document describes the database architecture, schema design, and conventions for the Autonomous Financial Intelligence Platform.

**Database**: PostgreSQL 15+
**ORM**: SQLAlchemy 2.0+
**Migration Tool**: Alembic

---

## Schema Design Principles

1. **Normalization**: Tables are normalized to 3NF (Third Normal Form)
2. **Naming Conventions**: Snake_case for table and column names
3. **Primary Keys**: UUID v4 for all primary keys
4. **Timestamps**: All tables include `created_at` and `updated_at` columns
5. **Soft Deletes**: Use `deleted_at` column for soft deletes (optional)
6. **Indexes**: Strategic indexes on foreign keys and frequently queried columns

---

## Entity Relationship Diagram

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│     users       │     │   portfolios    │     │    assets     │
├─────────────────┤     ├─────────────────┤     ├─────────────────┤
│ id (PK)         │────<│ id (PK)         │────<│ id (PK)         │
│ email           │     │ user_id (FK)    │     │ portfolio_id(FK)│
│ password_hash   │     │ name            │     │ symbol          │
│ full_name       │     │ description     │     │ name            │
│ is_active       │     │ currency        │     │ quantity        │
│ is_superuser    │     │ total_value     │     │ avg_price       │
│ created_at      │     │ created_at      │     │ current_price   │
│ updated_at      │     │ updated_at      │     │ created_at      │
└─────────────────┘     └─────────────────┘     │ updated_at      │
        │                     │                 └─────────────────┘
        │                     │                           │
        │              ┌──────┴──────┐                   │
        │              │             │                   │
┌───────▼────────┐     │    ┌────────▼────────┐     ┌────▼────────────┐
│ refresh_tokens │     │    │  transactions   │     │  price_history  │
├────────────────┤     │    ├─────────────────┤     ├─────────────────┤
│ id (PK)        │     │    │ id (PK)         │     │ id (PK)         │
│ user_id (FK)   │     │    │ portfolio_id(FK)│    │ asset_id (FK)   │
│ token          │     │    │ asset_id (FK)   │     │ price           │
│ expires_at     │     │    │ type            │     │ timestamp       │
│ created_at     │     │    │ quantity        │     │ source          │
└────────────────┘     │    │ price           │     │ created_at      │
                       │    │ fees            │     └─────────────────┘
                       │    │ timestamp       │
                       │    │ created_at      │
                       │    └─────────────────┘
                       │
                       │    ┌─────────────────┐
                       └───>│  analytics      │
                            ├─────────────────┤
                            │ id (PK)         │
                            │ portfolio_id(FK)│
                            │ metric_type     │
                            │ value           │
                            │ period_start    │
                            │ period_end      │
                            │ created_at      │
                            └─────────────────┘
```

---

## Table Definitions

### users

Stores user account information.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier |
| email | VARCHAR(255) | UNIQUE, NOT NULL | User email address |
| password_hash | VARCHAR(255) | NOT NULL | Hashed password (bcrypt) |
| full_name | VARCHAR(255) | | User's full name |
| is_active | BOOLEAN | DEFAULT true | Account status |
| is_superuser | BOOLEAN | DEFAULT false | Admin flag |
| last_login | TIMESTAMP | | Last login timestamp |
| created_at | TIMESTAMP | NOT NULL | Creation timestamp |
| updated_at | TIMESTAMP | NOT NULL | Last update timestamp |

**Indexes**:
- `idx_users_email` on `email`
- `idx_users_created_at` on `created_at`

---

### portfolios

Stores portfolio information.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier |
| user_id | UUID | FOREIGN KEY (users.id) | Portfolio owner |
| name | VARCHAR(255) | NOT NULL | Portfolio name |
| description | TEXT | | Portfolio description |
| currency | VARCHAR(3) | DEFAULT 'USD' | Base currency (ISO 4217) |
| total_value | DECIMAL(19,4) | DEFAULT 0 | Current total value |
| is_active | BOOLEAN | DEFAULT true | Portfolio status |
| created_at | TIMESTAMP | NOT NULL | Creation timestamp |
| updated_at | TIMESTAMP | NOT NULL | Last update timestamp |

**Indexes**:
- `idx_portfolios_user_id` on `user_id`
- `idx_portfolios_created_at` on `created_at`

---

### assets

Stores individual assets within portfolios.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier |
| portfolio_id | UUID | FOREIGN KEY (portfolios.id) | Parent portfolio |
| symbol | VARCHAR(20) | NOT NULL | Asset ticker symbol |
| name | VARCHAR(255) | | Asset name |
| asset_type | VARCHAR(50) | NOT NULL | stock, bond, crypto, etc. |
| quantity | DECIMAL(19,8) | NOT NULL | Holdings quantity |
| avg_buy_price | DECIMAL(19,8) | | Average purchase price |
| current_price | DECIMAL(19,8) | | Current market price |
| current_value | DECIMAL(19,4) | GENERATED | Computed value |
| created_at | TIMESTAMP | NOT NULL | Creation timestamp |
| updated_at | TIMESTAMP | NOT NULL | Last update timestamp |

**Indexes**:
- `idx_assets_portfolio_id` on `portfolio_id`
- `idx_assets_symbol` on `symbol`

---

### transactions

Stores all buy/sell transactions.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier |
| portfolio_id | UUID | FOREIGN KEY (portfolios.id) | Related portfolio |
| asset_id | UUID | FOREIGN KEY (assets.id) | Related asset |
| type | VARCHAR(10) | NOT NULL | BUY or SELL |
| quantity | DECIMAL(19,8) | NOT NULL | Transaction quantity |
| price | DECIMAL(19,8) | NOT NULL | Price per unit |
| fees | DECIMAL(19,4) | DEFAULT 0 | Transaction fees |
| total_amount | DECIMAL(19,4) | NOT NULL | Total amount |
| timestamp | TIMESTAMP | NOT NULL | Transaction time |
| notes | TEXT | | Optional notes |
| created_at | TIMESTAMP | NOT NULL | Creation timestamp |

**Indexes**:
- `idx_transactions_portfolio_id` on `portfolio_id`
- `idx_transactions_asset_id` on `asset_id`
- `idx_transactions_timestamp` on `timestamp`

---

### price_history

Stores historical price data for assets.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier |
| symbol | VARCHAR(20) | NOT NULL | Asset symbol |
| price | DECIMAL(19,8) | NOT NULL | Price at timestamp |
| timestamp | TIMESTAMP | NOT NULL | Price timestamp |
| source | VARCHAR(50) | | Data source |
| volume | BIGINT | | Trading volume |
| created_at | TIMESTAMP | NOT NULL | Creation timestamp |

**Indexes**:
- `idx_price_history_symbol_timestamp` on `(symbol, timestamp)`

---

### analytics

Stores pre-computed analytics metrics.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier |
| portfolio_id | UUID | FOREIGN KEY (portfolios.id) | Related portfolio |
| metric_type | VARCHAR(50) | NOT NULL | Type of metric |
| value | JSONB | NOT NULL | Metric value (flexible) |
| period_start | DATE | | Metric period start |
| period_end | DATE | | Metric period end |
| created_at | TIMESTAMP | NOT NULL | Creation timestamp |

**Indexes**:
- `idx_analytics_portfolio_id` on `portfolio_id`
- `idx_analytics_metric_type` on `metric_type`
- `idx_analytics_period` on `(period_start, period_end)`

---

## Migration Management

### Creating a Migration

```bash
cd backend
alembic revision --autogenerate -m "Description of changes"
```

### Applying Migrations

```bash
# Apply all pending migrations
alembic upgrade head

# Apply specific migration
alembic upgrade <revision_id>

# Rollback one migration
alembic downgrade -1
```

### Migration Best Practices

1. Always test migrations locally before deploying
2. Never modify existing migration files after commit
3. Include both `upgrade()` and `downgrade()` functions
4. Use transactions for data migrations
5. Add indexes in separate migrations for large tables

---

## Connection Pooling

Recommended settings for PostgreSQL connection pooling:

```python
engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=30,
    pool_pre_ping=True,
    pool_recycle=3600,
)
```

---

## Backup Strategy

### Automated Backups

- **Frequency**: Daily full backups
- **Retention**: 30 days
- **Storage**: Encrypted S3-compatible storage
- **Testing**: Weekly restore testing

### Manual Backup

```bash
# Full database backup
pg_dump -h localhost -U postgres -d financial_intelligence > backup.sql

# Restore from backup
psql -h localhost -U postgres -d financial_intelligence < backup.sql
```

---

## Performance Optimization

### Query Optimization

1. Use EXPLAIN ANALYZE for slow queries
2. Avoid SELECT * in production queries
3. Use appropriate indexes for filtering
4. Consider partitioning for time-series data
5. Use materialized views for complex aggregations

### Monitoring

Key metrics to monitor:
- Query execution time (p95, p99)
- Connection pool utilization
- Cache hit ratio
- Table bloat
- Lock contention

---

## Security Considerations

1. **Encryption**: Data encrypted at rest (TDE) and in transit (TLS)
2. **Access Control**: Role-based database access
3. **Audit Logging**: All DDL changes logged
4. **Data Masking**: PII masked in non-production environments
5. **Connection Security**: SSL/TLS required for all connections
