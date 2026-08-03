# AI Agent Template

## Agent: agent_name

### Purpose

Brief description of what this agent does.

### Capabilities

- Capability 1
- Capability 2

### Inputs

```python
class AgentInput(BaseModel):
    field: Type
```

### Outputs

```python
class AgentOutput(BaseModel):
    result: Type
```

### Prompt

```
[SYSTEM]
You are...

[CONTEXT]
{context}

[INSTRUCTIONS]
1. Do this
2. Do that

[OUTPUT FORMAT]
JSON format
```

### Implementation

```python
class AgentName(Agent):
    async def execute(self, input: AgentInput) -> AgentOutput:
        # Implementation
        pass
```

### Testing

```python
def test_agent():
    agent = AgentName()
    result = await agent.execute(input)
    assert result.expected
```

### Metrics

| Metric | Target |
|--------|--------|
| Accuracy | > 80% |
| Latency | < 500ms |
