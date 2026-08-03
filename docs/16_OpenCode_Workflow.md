# OpenCode Workflow: Autonomous Financial Intelligence Platform

## Executive Summary

This document defines the standardized workflow for using OpenCode (this AI assistant) in the AFIP development process.

---

## 1. OpenCode Capabilities

### 1.1 Supported Tasks

| Task Type | Capability | Best Practices |
|-----------|------------|----------------|
| **Code Generation** | Write new features | Provide clear specifications |
| **Refactoring** | Restructure code | Define scope clearly |
| **Debugging** | Find and fix bugs | Provide error logs |
| **Documentation** | Generate docs | Specify audience |
| **Architecture** | Design systems | Give constraints |
| **Testing** | Write tests | Define coverage |

### 1.2 Context Management

```
Context Levels:

Level 1: Project Scaffold
├── Use /freeze to restrict scope
├── Reference docs/ files
└── Verify file paths

Level 2: Feature Development
├── Read existing code first
├── Understand patterns
└── Follow conventions

Level 3: Debugging
├── Provide stack traces
├── Show relevant code
└── Describe expected behavior
```

---

## 2. Effective Prompting

### 2.1 Prompt Structure

```
[CONTEXT]
- What you're working on
- Current state
- Constraints

[REQUIREMENT]
- What you need
- Expected outcome
- Success criteria

[ADDITIONAL INFO]
- Relevant files
- Error messages
- Examples
```

### 2.2 Example Prompts

**Feature Request**:
```
I need to implement a portfolio rebalancing endpoint.

Context:
- FastAPI backend at backend/api/portfolios.py
- Portfolio model has assets[] and target_weights

Requirements:
- POST /portfolios/{id}/rebalance
- Calculate required trades
- Return trade list
- Requires authentication

Please implement the endpoint following existing patterns.
```

**Debug Request**:
```
I'm getting an error in the portfolio service.

Error: sqlalchemy.exc.InvalidRequestError: Object not bound to session

File: backend/services/portfolio.py:45

Context: Using async SQLAlchemy 2.0

Please help identify and fix the issue.
```

---

## 3. Workflow Integration

### 3.1 Development Loop

```
1. Plan
   └── Ask OpenCode for architecture/design

2. Implement
   └── Request code generation
   └── Review generated code
   └── Iterate if needed

3. Test
   └── Request test generation
   └── Run tests
   └── Debug if failing

4. Document
   └── Generate/update docs
   └── Add inline comments
   └── Update README

5. Review
   └── Ask for code review
   └── Address feedback
   └── Finalize
```

### 3.2 Best Practices

- **Be Specific**: Clear requirements yield better results
- **Provide Context**: Reference files, show code, explain constraints
- **Iterate**: Review and refine rather than expecting perfection
- **Verify**: Always test generated code
- **Learn**: Understand patterns for future work

---

## 4. Document Information

| Field | Value |
|-------|-------|
| Document ID | AFIP-DOC-016 |
| Version | 1.0.0 |
| Status | Draft |

---

## Next Document

**→ Continue to**: [17_Frontend_Workflow.md](./17_Frontend_Workflow.md)  
**← Back to**: [15_Git_Workflow.md](./15_Git_Workflow.md)
