# Engineering Principles: AFIP

**Version**: 1.0

## Core Principles

### 1. Simplicity Over Complexity

Choose the simpler solution. Complex systems fail in complex ways.

### 2. Explicit Over Implicit

Code should be self-documenting. Magic is forbidden.

### 3. Fail Fast, Fail Loud

Errors should surface immediately, not hide in logs.

### 4. Test What You Ship

Every feature needs tests. No exceptions.

### 5. Automate Everything

Manual processes become bottlenecks. Automate or eliminate.

### 6. Own Your Code

Authors maintain what they build. Full lifecycle ownership.

### 7. Review Everything

All code requires peer review. Two sets of eyes minimum.

### 8. Document Once, Update Often

Docs should live with code. Stale docs are lies.

### 9. Optimize for Readers

Code is read 10x more than written. Make it readable.

### 10. Security by Default

Secure by design. Never bolt on later.

## Decision Framework

When in doubt:
1. What is simplest?
2. What is most maintainable?
3. What has fewer dependencies?
4. What is easier to test?
5. What is easier to debug?

## Anti-Patterns

- ❌ Premature optimization
- ❌ Over-engineering
- ❌ Copy-paste without refactoring
- ❌ Untested code
- ❌ Undocumented assumptions
