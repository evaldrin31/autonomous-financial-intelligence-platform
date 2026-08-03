# TypeScript Coding Standards: AFIP

**Version**: 1.0

## Style

- Prettier formatter
- ESLint with TypeScript
- Strict mode enabled
- No `any`

## Naming

| Type | Convention |
|------|-----------|
| Interfaces | PascalCase |
| Types | PascalCase |
| Functions | camelCase |
| Variables | camelCase |
| Constants | UPPER_SNAKE |
| Components | PascalCase |
| Hooks | camelCase, `use` prefix |

## Types

```typescript
// Prefer interface for objects
interface User {
  id: string;
  name: string;
}

// Use type for unions
type Status = 'active' | 'inactive';

// Explicit return types
function getUser(id: string): User {
  ...
}

// Generic constraints
function sort<T extends { id: string }>(items: T[]): T[] {
  ...
}
```

## Components

```typescript
// Props interface
interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
}

// Component
export function Button({ label, onClick, disabled }: ButtonProps) {
  return (
    <button onClick={onClick} disabled={disabled}>
      {label}
    </button>
  );
}
```

## Async

```typescript
// Proper error handling
async function fetchData(): Promise<Data> {
  try {
    const response = await api.get('/data');
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.message);
    }
    throw error;
  }
}
```

## React

```typescript
// Hooks
const [value, setValue] = useState<string>('');
const data = useQuery({ queryKey: ['key'], queryFn: fetchData });

// Effects
useEffect(() => {
  // effect
  return () => {
    // cleanup
  };
}, [dependency]);
```

## Anti-patterns

- ❌ `as any`
- ❌ `@ts-ignore`
- ❌ Implicit returns
- ❌ `var`
- ❌ Non-null assertion `!`
