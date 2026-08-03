# Decision Making Framework: AFIP

**Version**: 1.0

## Framework

```
Data → Options → Decision → Action → Learn
```

## Decision Types

| Type | Authority | Timeframe |
|------|-----------|-----------|
| Technical | Senior Engineer | 24 hours |
| Architectural | Principal Architect | 1 week |
| Product | Product Manager | 3 days |
| Process | Team consensus | 1 week |
| Hiring | CTO + Hiring Manager | 1 week |

## Technical Decisions

### Low Impact (< 1 day work)

- Decide individually
- Document in code/comments
- No ADR required

### Medium Impact (1-5 days work)

- Consult one peer
- Document briefly
- Optional: Brief ADR

### High Impact (> 5 days work)

- Write ADR
- Review with team
- Get approval from Principal
- Document thoroughly

## Decision Process

1. **Define**: What are we deciding?
2. **Gather**: What data do we need?
3. **Options**: What are the choices?
4. **Evaluate**: Pros/cons of each
5. **Decide**: Pick the best option
6. **Document**: Write it down
7. **Communicate**: Tell the team
8. **Execute**: Implement
9. **Review**: Did it work?

## ADR Template

See [templates/Architecture_Decision_Record_Template.md](../templates/Architecture_Decision_Record_Template.md)

## Reversible vs Irreversible

- **Reversible**: Decide fast, iterate
- **Irreversible**: Analyze more, decide carefully

Most technical decisions are reversible.
