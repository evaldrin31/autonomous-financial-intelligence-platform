# Database Template

## Table: table_name

### Purpose

Brief description.

### Columns

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PK | Primary key |
| created_at | TIMESTAMP | NOT NULL | Creation time |

### Indexes

```sql
CREATE INDEX idx_name ON table_name(column);
```

### Relationships

- Belongs to: table
- Has many: table

### SQL

```sql
CREATE TABLE table_name (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
```

### Model

```python
class Model(Base):
    __tablename__ = "table_name"
    
    id: Mapped[UUID] = mapped_column(primary_key=True)
```

### Migration

```python
def upgrade():
    op.create_table(
        "table_name",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id")
    )
```
