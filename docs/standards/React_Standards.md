# React Standards: AFIP

**Version**: 1.0

## Components

### Server Components (Default)

```typescript
// app/page.tsx
export default async function Page() {
  const data = await fetchData();
  return <Component data={data} />;
}
```

### Client Components

```typescript
'use client';

export function InteractiveComponent() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}
```

## Hooks

```typescript
// Data fetching
const { data, isLoading } = useQuery({
  queryKey: ['portfolios'],
  queryFn: fetchPortfolios,
});

// Mutations
const mutation = useMutation({
  mutationFn: createPortfolio,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['portfolios'] });
  },
});

// State
const [state, setState] = useState<State>(initialState);
```

## Styling

```typescript
// Tailwind
className="flex flex-col gap-4 p-6 bg-white rounded-lg"

// Conditional
className={cn(
  "base-classes",
  isActive && "active-classes",
  isDisabled && "disabled-classes"
)}
```

## Props

```typescript
interface CardProps {
  title: string;
  children: React.ReactNode;
  className?: string;
}

export function Card({ title, children, className }: CardProps) {
  return (
    <div className={cn("card", className)}>
      <h2>{title}</h2>
      {children}
    </div>
  );
}
```

## Error Boundaries

```typescript
// app/error.tsx
'use client';

export default function Error({ error, reset }: { error: Error; reset: () => void }) {
  return (
    <div>
      <h2>Something went wrong</h2>
      <button onClick={reset}>Try again</button>
    </div>
  );
}
```

## Performance

- Use `React.memo` for expensive renders
- Use `useMemo` for expensive calculations
- Use `useCallback` for event handlers passed to children

## Anti-patterns

- ❌ Inline function definitions in render
- ❌ `useEffect` without dependency array
- ❌ State updates in render
- ❌ Prop drilling
