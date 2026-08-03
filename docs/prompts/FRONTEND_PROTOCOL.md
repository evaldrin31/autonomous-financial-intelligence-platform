# FRONTEND PROTOCOL: OpenCode

**Version**: 1.0

## Scope

Frontend development with Next.js 14, React, TypeScript, Tailwind.

## Prerequisites

Read:
- [ ] ../standards/TypeScript_Coding_Standards.md
- [ ] ../standards/React_Standards.md

## Project Structure

```
frontend/
├── app/              # Next.js App Router
├── components/       # React components
├── hooks/            # Custom hooks
├── lib/              # Utilities
├── store/            # Zustand stores
├── types/            # TypeScript types
└── styles/           # Global styles
```

## Development Workflow

### New Page

1. Create route in `app/`
2. Build components in `components/`
3. Add data fetching in `hooks/`
4. Style with Tailwind

### Pattern

```typescript
// hooks/usePortfolio.ts
export function usePortfolio(id: string) {
  return useQuery({
    queryKey: ['portfolio', id],
    queryFn: () => api.portfolios.get(id),
  });
}

// components/PortfolioCard.tsx
export function PortfolioCard({ portfolio }: Props) {
  return (
    <Card>
      <h3>{portfolio.name}</h3>
      <p>${portfolio.totalValue}</p>
    </Card>
  );
}

// app/portfolios/page.tsx
export default function PortfoliosPage() {
  const { data } = usePortfolios();
  return <PortfolioList portfolios={data} />;
}
```

## Standards

### TypeScript

- Strict mode
- No `any`
- Explicit return types
- Interface over type

### React

- Server Components by default
- 'use client' only when needed
- Hooks for state
- Props destructuring

### Styling

- Tailwind classes
- cn() for conditionals
- Responsive design
- Dark mode support

## Testing

```typescript
// Component test
render(<PortfolioCard portfolio={mock} />);
expect(screen.getByText('Test')).toBeInTheDocument();
```

## Common Tasks

| Task | Command |
|------|---------|
| Dev server | `npm run dev` |
| Build | `npm run build` |
| Test | `npm test` |
| Lint | `npm run lint` |
| Format | `npm run format` |
