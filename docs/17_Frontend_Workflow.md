# Frontend Workflow: Autonomous Financial Intelligence Platform

## Executive Summary

This document defines the specific workflows, patterns, and standards for frontend development in AFIP.

---

## 1. Development Workflow

### 1.1 Component Development

```
1. Design
   ├── Review Figma/mockups
   ├── Identify reusable components
   └── Plan component API

2. Scaffold
   └── npx shadcn add [component-name]

3. Implement
   ├── Write component
   ├── Add TypeScript types
   └── Add styling with Tailwind

4. Test
   ├── Manual testing
   └── Responsive check

5. Document
   ├── Add JSDoc comments
   └── Update storybook

6. Integrate
   └── Add to page
   └── Test integration
```

### 1.2 Page Development

```
1. Create Route
   └── Add to app/(dashboard)/page.tsx

2. Fetch Data
   └── Use TanStack Query
   └── Add loading states

3. Build UI
   └── Compose components
   └── Add error boundaries

4. Add Interactions
   └── Form handling
   └── State management
   └── Optimistic updates
```

---

## 2. Component Patterns

### 2.1 Component Structure

```typescript
// components/dashboard/PortfolioCard.tsx
'use client';

import { useState } from 'react';
import { Card, CardHeader, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';

interface PortfolioCardProps {
  portfolio: Portfolio;
  onSelect: (id: string) => void;
}

export function PortfolioCard({ portfolio, onSelect }: PortfolioCardProps) {
  const [isHovered, setIsHovered] = useState(false);
  
  return (
    <Card
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      className="cursor-pointer transition-shadow hover:shadow-lg"
    >
      <CardHeader>
        <h3 className="font-semibold">{portfolio.name}</h3>
      </CardHeader>
      <CardContent>
        <p className="text-2xl font-bold">
          ${portfolio.total_value.toLocaleString()}
        </p>
        <Button onClick={() => onSelect(portfolio.id)}>
          View Details
        </Button>
      </CardContent>
    </Card>
  );
}
```

### 2.2 Data Fetching Pattern

```typescript
// hooks/usePortfolios.ts
import { useQuery, useMutation } from '@tanstack/react-query';
import { api } from '@/lib/api';

export function usePortfolios() {
  return useQuery({
    queryKey: ['portfolios'],
    queryFn: () => api.portfolios.list(),
    staleTime: 60000,
  });
}

export function useCreatePortfolio() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: api.portfolios.create,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['portfolios'] });
    },
  });
}
```

---

## 3. Styling Guidelines

### 3.1 Tailwind Patterns

```typescript
// Layout
className="flex flex-col gap-4 p-6"

// Responsive
className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3"

// Conditional
className={cn(
  "base-classes",
  isActive && "active-classes",
  isDisabled && "disabled-classes"
)}

// Theme
className="bg-background text-foreground"
```

### 3.2 Color System

| Semantic | Light | Dark |
|----------|-------|------|
| Background | white | zinc-900 |
| Foreground | zinc-900 | zinc-100 |
| Primary | blue-600 | blue-500 |
| Secondary | zinc-100 | zinc-800 |
| Muted | zinc-500 | zinc-400 |
| Success | green-500 | green-400 |
| Warning | yellow-500 | yellow-400 |
| Error | red-500 | red-400 |

---

## 4. Document Information

| Field | Value |
|-------|-------|
| Document ID | AFIP-DOC-017 |
| Version | 1.0.0 |
| Status | Draft |

---

## Next Document

**→ Continue to**: [18_Deployment_Guide.md](./18_Deployment_Guide.md)  
**← Back to**: [16_OpenCode_Workflow.md](./16_OpenCode_Workflow.md)
