# Autonomous Financial Intelligence Platform

<p align="center">
  <strong>AI-Powered Financial Portfolio Management & Analytics</strong>
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#features">Features</a> •
  <a href="#tech-stack">Tech Stack</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#development">Development</a> •
  <a href="#documentation">Documentation</a>
</p>

---

## Overview

The **Autonomous Financial Intelligence Platform (AFIP)** is an enterprise-grade web application that combines traditional portfolio management with cutting-edge AI capabilities. Built with modern technologies and designed for scalability, AFIP empowers users to manage their investments, analyze performance, and receive AI-powered insights for better financial decision-making.

### Key Capabilities

- **Portfolio Management**: Create and manage multiple investment portfolios
- **Asset Tracking**: Monitor assets, transactions, and performance
- **Real-time Analytics**: Comprehensive portfolio analytics and visualization
- **AI-Powered Insights**: Intelligent recommendations and risk assessments
- **WebSocket Updates**: Real-time data streaming and notifications

---

## Features

### Current Features

- ✅ **Project Structure**: Modular, production-ready architecture
- ✅ **Authentication**: JWT-based authentication system
- ✅ **API Documentation**: Auto-generated OpenAPI/Swagger docs
- ✅ **Database**: PostgreSQL with SQLAlchemy ORM
- ✅ **Migrations**: Alembic for database version control
- ✅ **Docker**: Complete containerization for development

### Planned Features

- 🚧 **Portfolio Analytics**: Advanced performance metrics and charts
- 🚧 **AI Agents**: Autonomous analysis and recommendation agents
- 🚧 **RAG System**: Document-based context retrieval
- 🚧 **Backtesting**: Historical strategy simulation
- 🚧 **Real-time Updates**: WebSocket-based live data

---

## Tech Stack

### Backend

| Technology | Purpose |
|------------|---------|
| **Python 3.11+** | Primary language |
| **FastAPI** | Web framework |
| **SQLAlchemy 2.0** | ORM |
| **Pydantic** | Data validation |
| **Alembic** | Database migrations |
| **PostgreSQL** | Primary database |
| **Uvicorn** | ASGI server |
| **Black** | Code formatting |
| **Ruff** | Linting |

### Frontend

| Technology | Purpose |
|------------|---------|
| **Next.js 14** | React framework |
| **TypeScript** | Type-safe development |
| **Tailwind CSS** | Styling |
| **React Query** | Data fetching |
| **Zustand** | State management |
| **Recharts** | Data visualization |
| **Axios** | HTTP client |
| **Prettier** | Code formatting |
| **ESLint** | Linting |

### Infrastructure

| Technology | Purpose |
|------------|---------|
| **Docker** | Containerization |
| **Docker Compose** | Local orchestration |
| **Git** | Version control |

---

## Project Structure

```
autonomous-financial-intelligence-platform/
├── backend/                    # FastAPI application
│   ├── api/                   # API routes and endpoints
│   │   ├── __init__.py
│   │   ├── health.py           # Health check endpoints
│   │   └── routes.py           # API router configuration
│   ├── core/                  # Core configuration
│   │   ├── __init__.py
│   │   └── config.py           # Settings and configuration
│   ├── database/              # Database configuration
│   ├── models/                # SQLAlchemy models
│   ├── schemas/               # Pydantic schemas
│   ├── services/              # Business logic services
│   ├── agents/                # AI agents (placeholder)
│   ├── rag/                   # RAG system (placeholder)
│   ├── prompts/               # AI prompts
│   ├── utils/                 # Utility functions
│   ├── tests/                 # Test suite
│   ├── alembic/               # Database migrations
│   ├── main.py                # Application entry point
│   ├── requirements.txt       # Python dependencies
│   └── pyproject.toml         # Project configuration
├── frontend/                   # Next.js application
│   ├── app/                   # Next.js App Router
│   │   ├── (dashboard)/       # Dashboard route group
│   │   ├── (auth)/            # Auth route group
│   │   ├── layout.tsx         # Root layout
│   │   └── page.tsx           # Home page
│   ├── components/            # React components
│   ├── hooks/                 # Custom React hooks
│   ├── services/              # API services
│   ├── store/                 # Zustand stores
│   ├── types/                 # TypeScript types
│   ├── styles/                # Global styles
│   ├── public/                # Static assets
│   ├── package.json           # Dependencies
│   ├── tsconfig.json          # TypeScript config
│   ├── next.config.js         # Next.js config
│   ├── tailwind.config.js     # Tailwind config
│   ├── postcss.config.js      # PostCSS config
│   ├── .eslintrc.json         # ESLint config
│   └── .prettierrc            # Prettier config
├── docker/                     # Docker configurations
│   ├── Dockerfile.backend     # Backend Dockerfile
│   ├── Dockerfile.backend.prod # Backend production
│   ├── Dockerfile.frontend    # Frontend Dockerfile
│   └── Dockerfile.frontend.prod # Frontend production
├── docs/                       # Documentation
│   ├── Architecture.md        # System architecture
│   ├── API.md                 # API documentation
│   ├── Database.md            # Database schema
│   ├── Roadmap.md             # Development roadmap
│   ├── SRS.md                 # Software requirements
│   └── PromptEngineering.md   # AI prompt guidelines
├── docker-compose.yml          # Docker orchestration
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

---

## Getting Started

### Prerequisites

- **Docker** (recommended) or:
  - Python 3.11+
  - Node.js 20+
  - PostgreSQL 15+

### Quick Start (Docker)

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd autonomous-financial-intelligence-platform
   ```

2. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start all services**:
   ```bash
   docker-compose up -d
   ```

4. **Access the applications**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

5. **Stop services**:
   ```bash
   docker-compose down
   ```

### Manual Setup (Without Docker)

#### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. **Run database migrations** (when available):
   ```bash
   alembic upgrade head
   ```

6. **Start the development server**:
   ```bash
   python main.py
   # Or: uvicorn main:app --reload
   ```

#### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env.local
   # Edit .env.local with your API URL
   ```

4. **Start the development server**:
   ```bash
   npm run dev
   ```

---

## Development

### Backend Development

```bash
# Navigate to backend
cd backend

# Run with auto-reload
python main.py

# Format code
black .
ruff check . --fix

# Run tests
pytest

# Generate new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head
```

### Frontend Development

```bash
# Navigate to frontend
cd frontend

# Run development server
npm run dev

# Format code
npm run format

# Lint code
npm run lint

# Build for production
npm run build
```

### Code Quality

The project enforces code quality through:

- **Backend**: Black (formatting) + Ruff (linting)
- **Frontend**: Prettier (formatting) + ESLint (linting)

Pre-commit hooks recommended for automatic formatting.

---

## API Documentation

The API is documented using OpenAPI/Swagger. Access the interactive documentation at:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API info |
| `/api/v1/health` | GET | Health check |

See [docs/API.md](docs/API.md) for complete API documentation.

---

## Documentation

Comprehensive documentation is available in the `docs/` directory:

- **[Architecture.md](docs/Architecture.md)**: System architecture and design
- **[API.md](docs/API.md)**: API endpoints and usage
- **[Database.md](docs/Database.md)**: Database schema and migrations
- **[Roadmap.md](docs/Roadmap.md)**: Development roadmap
- **[SRS.md](docs/SRS.md)**: Software requirements specification
- **[PromptEngineering.md](docs/PromptEngineering.md)**: AI prompt guidelines

---

## Contributing

This project follows standard Git workflows:

1. Create a feature branch: `git checkout -b feature/name`
2. Make your changes
3. Commit with clear messages: `git commit -m "feat: add feature"`
4. Push to the branch: `git push origin feature/name`
5. Open a Pull Request

### Commit Message Convention

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Adding tests
- `chore:` Maintenance tasks

---

## License

[License information to be added]

---

## Support

For questions or support, please open an issue in the repository.

---

<p align="center">
  Built with ❤️ for the financial intelligence community
</p>
