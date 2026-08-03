# Technical Debt Policy: AFIP

**Version**: 1.0

## Definition

Technical debt = shortcuts that will cost more later.

## Types

| Type | Acceptable? | When? |
|------|-------------|-------|
| Intentional | Yes | Speed to market |
| Unintentional | No | Always fix |
| Outdated | Yes | Deprecate gradually |
| Documentation | No | Update immediately |

## Managing Debt

### Track

- Label issues as `tech-debt`
- Estimate effort to fix
- Prioritize quarterly

### Allow

- Sprint deadlines
- Prototypes
- MVPs
- Learning projects

### Prevent

- Code reviews
- Linting
- Testing
- Documentation

## Debt Payment

- Reserve 20% of sprint capacity
- Pay debt before new features
- One debt item per sprint minimum

## When to Take Debt

- [ ] Market pressure
- [ ] Learning opportunity
- [ ] Known scope
- [ ] Can pay back soon

## When NOT to Take Debt

- [ ] Core infrastructure
- [ ] Security
- [ ] Performance critical
- [ ] Unknown consequences

## Process

1. Identify debt
2. Create issue with `tech-debt` label
3. Estimate effort
4. Prioritize in backlog
5. Pay in sprint
6. Verify fixed
