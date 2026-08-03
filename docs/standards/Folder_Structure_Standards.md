# Folder Structure Standards: AFIP

**Version**: 1.0

## Root

```
afip/
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── docker-compose.yml
├── backend/
├── frontend/
├── docs/
├── docker/
└── scripts/
```

## Backend

```
backend/
├── api/           # Routes
│   ├── v1/
│   └── deps.py
├── core/          # Config
├── database/      # DB setup
├── models/        # SQLAlchemy
├── schemas/       # Pydantic
├── services/      # Business logic
├── repositories/  # Data access
├── agents/        # AI agents
├── rag/           # RAG
├── utils/         # Helpers
└── tests/         # Tests
```

## Frontend

```
frontend/
├── app/              # Next.js routes
│   ├── (dashboard)/
│   └── (auth)/
├── components/       # React components
│   └── ui/          # shadcn
├── hooks/            # Custom hooks
├── lib/              # Utils
├── store/            # Zustand
├── types/            # TypeScript
└── styles/           # Global CSS
```

## Docs

```
docs/
├── company/      # Governance
├── prompts/      # OpenCode prompts
├── roles/        # Role definitions
├── standards/    # Coding standards
├── playbooks/    # How-to guides
├── templates/    # Templates
└── architecture/ # Architecture docs
```

## Principles

1. Group by feature, not type
2. Co-locate related files
3. Flat structure preferred
4. No deeply nested folders
