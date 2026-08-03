# How To: Add New Database Table

**Version**: 1.0

## Overview

Add a new PostgreSQL table with SQLAlchemy and Alembic.

## Prerequisites

- [ ] Read Database Standards
- [ ] Schema designed
- [ ] Reviewed existing tables

## Steps

### 1. Create Model

```python
# backend/models/transaction.py
from database.base import Base

class Transaction(Base):
    __tablename__ = "transactions"
    
    id: Mapped[UUID] = mapped_column(primary_key=True)
    portfolio_id: Mapped[UUID] = mapped_column(
        ForeignKey("portfolios.id")
    )
    type: Mapped[str] = mapped_column(String(10))
    quantity: Mapped[Decimal] = mapped_column(Numeric(19,8))
    price: Mapped[Decimal] = mapped_column(Numeric(19,8))
    timestamp: Mapped[datetime]
    created_at: Mapped[datetime] = mapped_column(default=now)
```

### 2. Generate Migration

```bash
cd backend
alembic revision --autogenerate -m "create transactions table"
```

### 3. Review Migration

Check the generated file in `alembic/versions/`:
- Upgrade function correct
- Downgrade function correct
- Types appropriate
- Indexes added

### 4. Apply Migration

```bash
alembic upgrade head
```

### 5. Create Repository

```python
# backend/repositories/transaction.py
class TransactionRepository:
    async def create(self, data: TransactionCreate) -> Transaction:
        transaction = Transaction(**data.dict())
        await self.db.add(transaction)
        await self.db.commit()
        return transaction
```

### 6. Write Tests

```python
async def test_create_transaction(db):
    repo = TransactionRepository(db)
    transaction = await repo.create(mock_data)
    assert transaction.id is not None
```

## Verification

- [ ] Migration applies cleanly
- [ ] Table exists
- [ ] Queries work
- [ ] Tests pass

## Common Issues

| Issue | Solution |
|-------|----------|
| Migration fails | Check dependencies |
| Table not created | Check model import |
| Column wrong type | Edit migration |

## References

- [Database Standards](../standards/Database_Standards.md)
- [Database Protocol](../../prompts/DATABASE_PROTOCOL.md)
