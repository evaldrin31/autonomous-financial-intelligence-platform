# PROJECT_MASTER: Autonomous Financial Intelligence Platform

## Executive Summary

This document serves as the **master index and entry point** for the Autonomous Financial Intelligence Platform (AFIP). All future developers should start here.

---

## Vision

Build the world's most transparent, explainable, and autonomous financial intelligence platform that empowers users to make data-driven investment decisions with confidence.

---

## Problem Statement

See [02_Problem_Statement.md](./02_Problem_Statement.md)

**Key Challenges**:
- Information overload in financial markets
- Emotional bias in investment decisions
- Slow decision-making processes
- Lack of explainability in AI systems
- Risk management complexity

---

## Solution

See [03_Solution_Overview.md](./03_Solution_Overview.md)

**Core Components**:
- Multi-agent AI system
- RAG-powered knowledge base
- Explainable decision engine
- Comprehensive risk management
- Paper trading validation

---

## System Overview

```
AFIP System:
┌─────────────────────────────────────────────────────────────┐
│                      CLIENT LAYER                          │
│  Web App (Next.js) | Mobile (Future) | API Clients          │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────┐
│                       API GATEWAY                            │
│              FastAPI + Authentication + Rate Limiting        │
└─────────────────────────────────────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
┌────────▼────────┐  ┌────────▼────────┐  ┌───────▼────────┐
│ SERVICE LAYER   │  │ INTELLIGENCE    │  │ RAG LAYER      │
│ • Portfolio     │  │ • Agents        │  │ • Vector DB    │
│ • Analytics     │  │ • Decision      │  │ • Documents    │
│ • Market Data   │  │ • Explainability│  │ • Retrieval    │
└─────────────────┘  └─────────────────┘  └────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────┐
│                        DATA LAYER                           │
│            PostgreSQL | Redis | MinIO | Vector Store        │
└─────────────────────────────────────────────────────────────┘
```

---

## Folder Structure

```
autonomous-financial-intelligence-platform/
├── backend/              # FastAPI application
│   ├── api/             # API routes
│   ├── core/            # Configuration
│   ├── database/        # DB setup
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # Pydantic schemas
│   ├── services/        # Business logic
│   ├── agents/          # AI agents
│   ├── rag/             # RAG system
│   └── tests/           # Test suite
├── frontend/             # Next.js application
│   ├── app/             # App Router
│   ├── components/      # React components
│   ├── hooks/           # Custom hooks
│   ├── store/           # Zustand stores
│   └── types/           # TypeScript types
├── docs/                 # Documentation
│   ├── 01_Project_Overview.md
│   ├── 02_Problem_Statement.md
│   └── ... (26 total)
├── docker/               # Docker configs
└── docker-compose.yml    # Local orchestration
```

---

## Engineering Operating System (EOS)

The EOS governs all development:

| Section | Purpose |
|---------|---------|
| [company/](./company/) | Engineering governance |
| [prompts/](./prompts/) | OpenCode instructions |
| [roles/](./roles/) | Team definitions |
| [standards/](./standards/) | Coding standards |
| [playbooks/](./playbooks/) | How-to guides |
| [templates/](./templates/) | Reusable formats |

**Start Here**: [company/Engineering_Handbook.md](./company/Engineering_Handbook.md)

---

## Documentation Index

### Getting Started
1. [01_Project_Overview.md](./01_Project_Overview.md) - Project introduction
2. [02_Problem_Statement.md](./02_Problem_Statement.md) - Problems we solve
3. [03_Solution_Overview.md](./03_Solution_Overview.md) - How we solve them

### Architecture
4. [04_System_Architecture.md](./04_System_Architecture.md) - System design
5. [05_AI_Agent_Architecture.md](./05_AI_Agent_Architecture.md) - AI agents
6. [06_RAG_Architecture.md](./06_RAG_Architecture.md) - RAG system
7. [07_Backend_Architecture.md](./07_Backend_Architecture.md) - Backend
8. [08_Frontend_Architecture.md](./08_Frontend_Architecture.md) - Frontend
9. [09_Database_Architecture.md](./09_Database_Architecture.md) - Database
10. [10_API_Architecture.md](./10_API_Architecture.md) - API design

### Features
11. [11_Paper_Trading_Engine.md](./11_Paper_Trading_Engine.md) - Simulation
12. [12_Risk_Management.md](./12_Risk_Management.md) - Risk system
13. [13_Explainability_Engine.md](./13_Explainability_Engine.md) - Transparency

### Development
14. [14_Project_Workflow.md](./14_Project_Workflow.md) - Project process
15. [15_Git_Workflow.md](./15_Git_Workflow.md) - Git process
16. [16_OpenCode_Workflow.md](./16_OpenCode_Workflow.md) - AI assistant
17. [17_Frontend_Workflow.md](./17_Frontend_Workflow.md) - Frontend dev

### Operations
18. [18_Deployment_Guide.md](./18_Deployment_Guide.md) - Deployment
19. [19_Coding_Standards.md](./19_Coding_Standards.md) - Standards
20. [20_Testing_Strategy.md](./20_Testing_Strategy.md) - Testing

### Planning
21. [21_Roadmap.md](./21_Roadmap.md) - Development roadmap
22. [22_Project_State.md](./22_Project_State.md) - Current status
23. [23_Project_Decisions.md](./23_Project_Decisions.md) - ADRs
24. [24_Future_Scope.md](./24_Future_Scope.md) - Future plans

### Project Management
25. [PROJECT_MASTER.md](./PROJECT_MASTER.md) - This file
26. [CHANGELOG.md](./CHANGELOG.md) - Change history

---

## Development Workflow

### Standard Workflow

```
1. Read relevant architecture docs
2. Review PROJECT_STATE.md
3. Pick task from current milestone
4. Follow Git workflow (company/Git_Workflow.md)
5. Follow Coding standards (standards/)
6. Write tests (standards/Testing_Standards.md)
7. Update CHANGELOG.md
8. Create PR
9. Merge after review
```

### Using OpenCode

1. Read [MASTER_INSTRUCTIONS](./prompts/MASTER_INSTRUCTIONS.md)
2. Select protocol from [prompts/](./prompts/)
3. Follow protocol steps
4. Verify with [standards/](./standards/)
5. Complete [Definition of Done](./company/Definition_of_Done.md)

---

## Technology Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Next.js 14, React 18, TypeScript, Tailwind CSS |
| **Backend** | Python 3.11, FastAPI, SQLAlchemy 2.0 |
| **Database** | PostgreSQL 15, pgvector, Redis 7 |
| **AI/ML** | OpenAI, HuggingFace, LangChain |
| **Infrastructure** | Docker, Docker Compose |
| **Testing** | Pytest, Jest, React Testing Library |

---

## Milestones

| Milestone | Status | Description |
|-----------|--------|-------------|
| 1. Scaffold | ✅ Complete | Project setup |
| 2. Backend | 🟡 In Progress | Core API |
| 3. Frontend | 🔴 Planned | Dashboard |
| 4. Database | 🔴 Planned | Models & Migrations |
| 5. Auth | 🔴 Planned | Authentication |
| 6. Market Data | 🔴 Planned | Data pipeline |
| 7. RAG | 🔴 Planned | Knowledge system |
| 8. AI Agents | 🔴 Planned | Intelligence layer |
| 9. Decision Engine | 🔴 Planned | Autonomy |
| 10. Paper Trading | 🔴 Planned | Simulation |

---

## Team Responsibilities

| Role | Responsibilities |
|------|-------------------|
| **Lead Architect** | System design, ADRs, reviews |
| **Backend Engineers** | API, services, database |
| **Frontend Engineers** | UI, components, state |
| **AI Engineers** | Agents, RAG, ML models |
| **DevOps** | Deployment, monitoring, CI/CD |

---

## Quick Start

### For Engineers

1. Read [Engineering Handbook](./company/Engineering_Handbook.md)
2. Review your [role definition](./roles/)
3. Check [Definition of Done](./company/Definition_of_Done.md)
4. Follow [Sprint Workflow](./company/Sprint_Workflow.md)

### Setup

```bash
# Clone
git clone [repo-url]
cd afip

# Setup
cp .env.example .env
# Edit .env

# Run
docker-compose up -d

# Access
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
# Docs: http://localhost:8000/docs
```

---

## Current Status

See [22_Project_State.md](./22_Project_State.md)

**Milestone 1 Complete**: Project scaffold ready for development.

---

## Future Expansion

See [24_Future_Scope.md](./24_Future_Scope.md)

**Phase 2**: Enhanced AI, live trading, mobile apps

---

## Document Information

| Field | Value |
|-------|-------|
| Document ID | AFIP-MASTER |
| Version | 1.0.0 |
| Status | Active |
| Last Updated | 2024-01-01 |
| Owner | Lead Architect |

---

**Welcome to AFIP. Start with 01_Project_Overview.md.**
