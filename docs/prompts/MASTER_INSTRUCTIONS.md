# MASTER INSTRUCTIONS: OpenCode

**Version**: 1.0

## Purpose

This document governs how OpenCode interacts with this repository.

## Mode Selection

Before starting, determine mode:

| Mode | Use When |
|------|----------|
| **Implement** | Building features, fixing bugs |
| **Review** | Code review, architecture review |
| **Document** | Creating documentation |
| **Investigate** | Debugging, root cause analysis |
| **Plan** | Architecture decisions, design |

## Universal Rules

1. **Read First**: Always read relevant docs before writing
2. **Follow Standards**: Apply standards from docs/standards/
3. **Check Context**: Review PROJECT_STATE.md for current status
4. **Be Minimal**: Make smallest effective change
5. **Test Everything**: Verify changes work
6. **Document Changes**: Update docs with code

## Safety Protocols

### Before Any Edit

- [ ] Understand current state
- [ ] Review related files
- [ ] Check for dependencies
- [ ] Verify permissions

### Before Destructive Action

- [ ] Confirm with user
- [ ] Create backup
- [ ] Document reasoning

### Before Git Operations

- [ ] Check current branch
- [ ] Review changes
- [ ] Verify commit message

## Workflow

```
1. UNDERSTAND
   └── Read relevant architecture docs
   └── Check PROJECT_STATE.md
   └── Review existing code

2. PLAN
   └── Identify files to modify
   └── Consider side effects
   └── Choose approach

3. IMPLEMENT
   └── Follow standards
   └── Write tests
   └── Update docs

4. VERIFY
   └── Check for errors
   └── Run tests
   └── Review output

5. COMMIT
   └── Stage changes
   └── Write message
   └── Push
```

## Forbidden Actions

- ❌ Delete files without confirmation
- ❌ Modify .env files
- ❌ Hard code secrets
- ❌ Skip tests
- ❌ Break backward compatibility without versioning

## Required Actions

- ✅ Type all code
- ✅ Handle errors
- ✅ Write docstrings
- ✅ Update CHANGELOG

## Documentation

When modifying:
| Area | Update |
|------|--------|
| Code | Inline comments |
| APIs | OpenAPI docs |
| Architecture | Relevant arch doc |
| Process | Playbook if changed |
| Decisions | ADR if new |

## Communication

- Ask when uncertain
- Explain decisions
- Show examples
- Provide alternatives

## Self-Correction

If you realize an error:
1. Stop immediately
2. Assess impact
3. Notify user
4. Propose fix
5. Wait for confirmation
