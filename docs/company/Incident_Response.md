# Incident Response: AFIP

**Version**: 1.0

## Severity Levels

| Level | Impact | Response Time | Examples |
|-------|--------|-------------|----------|
| P0 | Critical | 15 min | Data loss, security breach |
| P1 | High | 1 hour | Major feature down |
| P2 | Medium | 4 hours | Degraded performance |
| P3 | Low | 24 hours | Minor bug |

## Response Process

### Detection

- Monitoring alerts
- User reports
- Automated checks

### Response

1. **Triage** (5 min)
   - Assess severity
   - Assign owner
   - Create incident channel

2. **Mitigate** (15 min)
   - Stop the bleeding
   - Implement workaround
   - Preserve evidence

3. **Fix** (varies)
   - Root cause analysis
   - Implement fix
   - Test fix
   - Deploy

4. **Post-mortem** (24-48 hours)
   - What happened
   - Why it happened
   - How we fixed it
   - How we prevent it

## Communication

| Audience | Channel | Frequency |
|----------|---------|-----------|
| Responders | #incident-{id} | Real-time |
| Stakeholders | #incidents | Every 30 min |
| Users | Status page | When known |

## Runbook

Common incidents:
- Database down → Failover to replica
- API slow → Scale workers
- Memory leak → Restart, investigate
- Security → Isolate, patch

## On-call

- Primary: Engineer on rotation
- Secondary: Backup engineer
- Escalation: Lead Architect
