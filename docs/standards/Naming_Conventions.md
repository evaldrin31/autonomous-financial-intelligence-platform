# Naming Conventions: AFIP

**Version**: 1.0

## General

| Type | Convention | Example |
|------|------------|---------|
| Files | snake_case | `portfolio_service.py` |
| Classes | PascalCase | `PortfolioService` |
| Functions | snake_case | `calculate_returns` |
| Variables | snake_case | `total_value` |
| Constants | UPPER_SNAKE | `MAX_RETRY` |
| Private | _prefix | `_internal_method` |

## Backend

| Type | Convention | Example |
|------|------------|---------|
| Routes | plural, lowercase | `/portfolios` |
| Models | singular, PascalCase | `class Portfolio` |
| Services | PascalCase + Service | `PortfolioService` |
| Schemas | PascalCase | `PortfolioCreate` |

## Frontend

| Type | Convention | Example |
|------|------------|---------|
| Components | PascalCase | `PortfolioCard` |
| Hooks | camelCase + use | `usePortfolio` |
| Props | camelCase | `portfolioId` |
| Files | PascalCase (components) | `PortfolioCard.tsx` |
| Files | camelCase (utils) | `apiClient.ts` |

## Database

| Type | Convention | Example |
|------|------------|---------|
| Tables | snake_case, plural | `portfolios` |
| Columns | snake_case | `created_at` |
| Indexes | idx_table_column | `idx_portfolios_user_id` |

## API

| Type | Convention | Example |
|------|------------|---------|
| Endpoints | lowercase, hyphen | `/portfolio-analytics` |
| Parameters | camelCase | `portfolioId` |
| Response fields | camelCase | `totalValue` |

## Git

| Type | Convention | Example |
|------|------------|---------|
| Branches | type/description | `feature/auth-login` |
| Tags | vX.X.X | `v1.0.0` |
