# Testing Strategy: Autonomous Financial Intelligence Platform

## Executive Summary

This document defines the comprehensive testing strategy for AFIP, covering unit tests, integration tests, end-to-end tests, and performance testing.

---

## 1. Testing Pyramid

```
                    ┌─────────┐
                    │   E2E   │  <- 10%
                    │  Tests  │
                   ┌┴─────────┴┐
                   │ Integration │  <- 30%
                   │   Tests     │
                  ┌┴─────────────┴┐
                  │    Unit Tests    │  <- 60%
                  │                  │
                  └──────────────────┘
```

---

## 2. Unit Testing

### 2.1 Python Unit Tests

```python
# backend/tests/test_portfolio_service.py
import pytest
from decimal import Decimal
from services.portfolio import PortfolioService

@pytest.fixture
async def portfolio_service(db_session):
    return PortfolioService(db_session)

class TestPortfolioService:
    """Test suite for PortfolioService."""
    
    async def test_create_portfolio(
        self,
        portfolio_service
    ):
        """Test creating a new portfolio."""
        # Arrange
        user_id = uuid4()
        data = PortfolioCreate(
            name="Test Portfolio",
            currency="USD"
        )
        
        # Act
        portfolio = await portfolio_service.create(user_id, data)
        
        # Assert
        assert portfolio.name == "Test Portfolio"
        assert portfolio.currency == "USD"
        assert portfolio.total_value == 0
    
    async def test_calculate_portfolio_value(
        self,
        portfolio_service
    ):
        """Test value calculation with multiple assets."""
        # Arrange
        assets = [
            Asset(symbol="AAPL", quantity=10, current_price=150),
            Asset(symbol="GOOGL", quantity=5, current_price=100),
        ]
        
        # Act
        value = await portfolio_service.calculate_value(assets)
        
        # Assert
        expected = Decimal('2000')
        assert value == expected
```

### 2.2 Frontend Unit Tests

```typescript
// frontend/__tests__/components/PortfolioCard.test.tsx
import { render, screen } from '@testing-library/react';
import { PortfolioCard } from '@/components/dashboard/PortfolioCard';

describe('PortfolioCard', () => {
  const mockPortfolio = {
    id: '1',
    name: 'Test Portfolio',
    totalValue: 10000,
  };
  
  it('renders portfolio name', () => {
    render(<PortfolioCard portfolio={mockPortfolio} onSelect={() => {}} />);
    expect(screen.getByText('Test Portfolio')).toBeInTheDocument();
  });
  
  it('displays formatted value', () => {
    render(<PortfolioCard portfolio={mockPortfolio} onSelect={() => {}} />);
    expect(screen.getByText('$10,000')).toBeInTheDocument();
  });
  
  it('calls onSelect when clicked', () => {
    const handleSelect = jest.fn();
    render(<PortfolioCard portfolio={mockPortfolio} onSelect={handleSelect} />);
    
    screen.getByRole('button').click();
    expect(handleSelect).toHaveBeenCalledWith('1');
  });
});
```

---

## 3. Integration Testing

### 3.1 API Integration Tests

```python
# backend/tests/integration/test_portfolio_api.py
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestPortfolioAPI:
    """Integration tests for portfolio endpoints."""
    
    def test_create_portfolio_unauthorized(self):
        """Test that auth is required."""
        response = client.post(
            "/api/v1/portfolios",
            json={"name": "Test", "currency": "USD"}
        )
        assert response.status_code == 401
    
    def test_create_portfolio_success(self, auth_headers):
        """Test successful portfolio creation."""
        response = client.post(
            "/api/v1/portfolios",
            json={"name": "Test", "currency": "USD"},
            headers=auth_headers
        )
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Test"
```

---

## 4. Test Coverage

### 4.1 Coverage Requirements

| Component | Minimum Coverage |
|-----------|------------------|
| Backend API | 80% |
| Backend Services | 85% |
| Frontend Components | 70% |
| Frontend Hooks | 75% |
| Critical Paths | 90% |

---

## 5. Document Information

| Field | Value |
|-------|-------|
| Document ID | AFIP-DOC-020 |
| Version | 1.0.0 |
| Status | Draft |

---

## Next Document

**→ Continue to**: [21_Roadmap.md](./21_Roadmap.md)  
**← Back to**: [19_Coding_Standards.md](./19_Coding_Standards.md)
