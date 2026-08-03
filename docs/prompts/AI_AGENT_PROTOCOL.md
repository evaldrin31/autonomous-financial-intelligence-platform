# AI AGENT PROTOCOL: OpenCode

**Version**: 1.0

## Scope

Developing AI agents for the AFIP platform.

## Prerequisites

Read:
- [ ] ../../docs/architecture/05_AI_Agent_Architecture.md
- [ ] ../../docs/standards/Prompt_Engineering_Standards.md

## Agent Structure

```
backend/agents/
├── base.py           # Base agent class
├── orchestrator.py   # Agent coordination
├── portfolio_analyzer.py
├── market_researcher.py
└── risk_manager.py
```

## Development Workflow

### New Agent

1. Define agent purpose
2. Write prompt template
3. Implement agent class
4. Add to orchestrator
5. Write tests

### Pattern

```python
# agents/portfolio_analyzer.py
class PortfolioAnalysisAgent(Agent):
    """Analyzes portfolio composition."""
    
    async def analyze(
        self,
        portfolio: Portfolio
    ) -> AnalysisResult:
        # Gather data
        data = await self._gather_data(portfolio)
        
        # Build prompt
        prompt = self._build_prompt(data)
        
        # Call LLM
        response = await self.llm.generate(prompt)
        
        # Parse and validate
        result = self._parse_response(response)
        
        return result
```

## Standards

### Prompts

- Clear structure
- Examples provided
- Output format defined
- Constraints listed

### Agents

- Single responsibility
- Async methods
- Typed inputs/outputs
- Error handling

### Orchestration

- State machine
- Clear handoffs
- Timeout handling
- Circuit breakers

## Testing

```python
# Mock LLM response
async def test_analyze():
    agent = PortfolioAnalysisAgent(llm=mock_llm)
    result = await agent.analyze(mock_portfolio)
    assert result.confidence > 0.7
```

## Common Tasks

| Task | Approach |
|------|----------|
| New agent | Extend Agent base |
| Prompt tuning | A/B test variants |
| Add capability | New method |
| Fix hallucination | Add validation |
