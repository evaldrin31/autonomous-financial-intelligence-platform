# Frontend Architecture: Autonomous Financial Intelligence Platform

## Executive Summary

This document defines the frontend architecture for AFIP, built on Next.js 14 with a modern React stack optimized for financial data visualization, real-time updates, and AI-driven user experiences.

---

## 1. Frontend Overview

### 1.1 Technology Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| Framework | Next.js | 14+ | React framework with App Router |
| Language | TypeScript | 5.3+ | Type safety |
| Styling | Tailwind CSS | 3.4+ | Utility-first CSS |
| UI Components | shadcn/ui | - | Accessible components |
| State Management | Zustand | 4.5+ | Global state |
| Data Fetching | TanStack Query | 5.17+ | Server state |
| HTTP Client | Axios | 1.6+ | API requests |
| Charts | Recharts | 2.10+ | Data visualization |
| Icons | Lucide React | - | Icon library |

### 1.2 Architecture Principles

1. **Server Components First**: Use Next.js App Router
2. **Type Safety**: Strict TypeScript throughout
3. **Composition**: Small, reusable components
4. **Performance**: Code splitting, lazy loading
5. **Accessibility**: WCAG 2.1 AA compliance

---

## 2. Project Structure

```
frontend/
├── app/                        # Next.js App Router
│   ├── layout.tsx             # Root layout
│   ├── page.tsx               # Home page
│   ├── loading.tsx            # Loading UI
│   ├── error.tsx              # Error handling
│   ├── globals.css            # Global styles
│   │
│   ├── (dashboard)/           # Dashboard group
│   │   ├── layout.tsx         # Dashboard layout
│   │   ├── page.tsx           # Dashboard home
│   │   ├── portfolios/        # Portfolios section
│   │   │   ├── page.tsx
│   │   │   └── [id]/
│   │   ├── analytics/         # Analytics section
│   │   └── settings/          # Settings section
│   │
│   └── (auth)/                # Auth group (no layout)
│       ├── login/
│       └── register/
│
├── components/                 # React components
│   ├── ui/                    # shadcn/ui components
│   ├── layout/                # Layout components
│   │   ├── Header.tsx
│   │   ├── Sidebar.tsx
│   │   └── Footer.tsx
│   ├── dashboard/             # Dashboard components
│   │   ├── PortfolioCard.tsx
│   │   ├── AssetTable.tsx
│   │   └── PerformanceChart.tsx
│   ├── charts/                # Chart components
│   │   ├── LineChart.tsx
│   │   ├── PieChart.tsx
│   │   └── CandlestickChart.tsx
│   └── forms/                 # Form components
│       └── PortfolioForm.tsx
│
├── hooks/                      # Custom hooks
│   ├── usePortfolio.ts
│   ├── useMarketData.ts
│   ├── useAuth.ts
│   └── useWebSocket.ts
│
├── lib/                        # Utilities
│   ├── api.ts                 # API client
│   ├── utils.ts               # Helper functions
│   └── constants.ts           # Constants
│
├── store/                      # Zustand stores
│   ├── authStore.ts
│   ├── portfolioStore.ts
│   └── uiStore.ts
│
├── types/                      # TypeScript types
│   ├── api.ts
│   ├── portfolio.ts
│   └── user.ts
│
├── public/                     # Static assets
│   ├── images/
│   └── fonts/
│
├── styles/                     # Additional styles
│   └── charts.css
│
├── next.config.js             # Next.js config
├── tailwind.config.js         # Tailwind config
├── tsconfig.json              # TypeScript config
└── package.json               # Dependencies
```

---

## 3. App Router Architecture

### 3.1 Route Groups

```
app/
├── layout.tsx              # Root layout (applies to all)
├── (marketing)/            # Marketing pages
│   ├── layout.tsx
│   ├── page.tsx            # Landing
│   └── about/
├── (dashboard)/            # Dashboard (requires auth)
│   ├── layout.tsx          # Dashboard shell
│   ├── page.tsx            # Overview
│   ├── portfolios/
│   ├── analytics/
│   └── settings/
└── (auth)/                 # Auth pages (no layout)
    ├── login/
    └── register/
```

### 3.2 Route Structure

| Route | Group | Access | Description |
|-------|-------|--------|-------------|
| `/` | Marketing | Public | Landing page |
| `/login` | Auth | Public | Authentication |
| `/dashboard` | Dashboard | Protected | Portfolio overview |
| `/dashboard/portfolios` | Dashboard | Protected | Portfolio list |
| `/dashboard/portfolios/[id]` | Dashboard | Protected | Portfolio detail |
| `/dashboard/analytics` | Dashboard | Protected | Analytics dashboard |

---

## 4. Component Architecture

### 4.1 Component Hierarchy

```
Layout (Server Component)
├── Header (Client Component)
│   ├── Navigation
│   └── UserMenu
├── Sidebar (Client Component)
│   └── PortfolioList
└── Main Content
    └── Page (Server Component)
        └── Data Fetching
            └── Components
                ├── Chart (Client)
                └── Table (Client)
```

### 4.2 Component Patterns

**Server Component Pattern**:
```typescript
// Server component for data fetching
import { PortfolioList } from '@/components/dashboard/PortfolioList';

export default async function PortfoliosPage() {
  // Fetch on server
  const portfolios = await api.portfolios.list();
  
  return (
    <div>
      <h1>Portfolios</h1>
      {/* Pass data to client component */}
      <PortfolioList portfolios={portfolios} />
    </div>
  );
}
```

**Client Component Pattern**:
```typescript
'use client';

import { useState } from 'react';

export function PortfolioList({ portfolios }: Props) {
  const [selected, setSelected] = useState<string | null>(null);
  
  return (
    <ul>
      {portfolios.map(p => (
        <li 
          key={p.id}
          onClick={() => setSelected(p.id)}
          className={selected === p.id ? 'selected' : ''}
        >
          {p.name}
        </li>
      ))}
    </ul>
  );
}
```

---

## 5. State Management

### 5.1 Zustand Stores

**Auth Store**:
```typescript
// store/authStore.ts
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  setUser: (user: User) => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set, get) => ({
      user: null,
      token: null,
      isAuthenticated: false,
      
      login: async (email, password) => {
        const { user, token } = await api.auth.login(email, password);
        set({ user, token, isAuthenticated: true });
      },
      
      logout: () => {
        set({ user: null, token: null, isAuthenticated: false });
      },
      
      setUser: (user) => set({ user }),
    }),
    {
      name: 'auth-storage',
      partialize: (state) => ({ token: state.token }),
    }
  )
);
```

**Portfolio Store**:
```typescript
// store/portfolioStore.ts
interface PortfolioState {
  portfolios: Portfolio[];
  selectedPortfolio: Portfolio | null;
  
  setPortfolios: (portfolios: Portfolio[]) => void;
  selectPortfolio: (id: string) => void;
  updatePortfolio: (id: string, data: Partial<Portfolio>) => void;
}

export const usePortfolioStore = create<PortfolioState>((set, get) => ({
  portfolios: [],
  selectedPortfolio: null,
  
  setPortfolios: (portfolios) => set({ portfolios }),
  
  selectPortfolio: (id) => {
    const portfolio = get().portfolios.find(p => p.id === id);
    set({ selectedPortfolio: portfolio });
  },
  
  updatePortfolio: (id, data) => {
    const portfolios = get().portfolios.map(p =>
      p.id === id ? { ...p, ...data } : p
    );
    set({ portfolios });
  },
}));
```

---

## 6. Data Fetching

### 6.1 TanStack Query Pattern

```typescript
// hooks/usePortfolio.ts
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/lib/api';

export function usePortfolios() {
  return useQuery({
    queryKey: ['portfolios'],
    queryFn: () => api.portfolios.list(),
    staleTime: 60000, // 1 minute
  });
}

export function usePortfolio(id: string) {
  return useQuery({
    queryKey: ['portfolios', id],
    queryFn: () => api.portfolios.get(id),
    enabled: !!id,
  });
}

export function useCreatePortfolio() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: (data: CreatePortfolioData) =>
      api.portfolios.create(data),
    onSuccess: () => {
      // Invalidate and refetch
      queryClient.invalidateQueries({
        queryKey: ['portfolios']
      });
    },
  });
}
```

### 6.2 API Client

```typescript
// lib/api.ts
import axios from 'axios';
import { useAuthStore } from '@/store/authStore';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
  timeout: 10000,
});

// Request interceptor
api.interceptors.request.use((config) => {
  const token = useAuthStore.getState().token;
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Response interceptor
api.interceptors.response.use(
  (response) => response.data,
  (error) => {
    if (error.response?.status === 401) {
      useAuthStore.getState().logout();
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export const apiClient = {
  portfolios: {
    list: () => api.get('/portfolios'),
    get: (id: string) => api.get(`/portfolios/${id}`),
    create: (data: CreatePortfolioData) => api.post('/portfolios', data),
    update: (id: string, data: UpdatePortfolioData) =>
      api.put(`/portfolios/${id}`, data),
    delete: (id: string) => api.delete(`/portfolios/${id}`),
  },
  // ... other endpoints
};
```

---

## 7. Document Information

| Field | Value |
|-------|-------|
| Document ID | AFIP-DOC-008 |
| Version | 1.0.0 |
| Status | Draft |

---

## Next Document

**→ Continue to**: [09_Database_Architecture.md](./09_Database_Architecture.md)  
**← Back to**: [07_Backend_Architecture.md](./07_Backend_Architecture.md)
