# How To: Add New AI Agent

**Version**: 1.0

## Overview

Add a new AI agent to the multi-agent system.

## Prerequisites

- [ ] Read AI Agent Architecture
- [ ] Understand agent patterns
- [ ] Define agent purpose

## Steps

### 1. Create Agent Class

```python
# backend/agents/market_researcher.py
from agents.base import Agent

class MarketResearchAgent(Agent):
    """Agent for market research and analysis."""
    
    name = "market_researcher"
    capabilities = ["research", "analysis"]
    
    async def analyze(
        self,
        symbols: List[str],
        timeframe: str
    ) -> ResearchResult:
        # Gather data
        data = await self._gather_data(symbols)
        
        # Build prompt
        prompt = self._build_prompt(data, timeframe)
        
        # Call LLM
        response = await self.llm.generate(prompt)
        
        # Parse and return
        return self._parse_response(response)
```

### 2. Write Prompt Template

```python
# backend/prompts/market_research.txt
"""
[SYSTEM]
You are a market research analyst...

[CONTEXT]
Symbols: {symbols}
Timeframe: {timeframe}

[INSTRUCTIONS]
1. Analyze market trends
2. Identify opportunities
3. Assess risks

[OUTPUT FORMAT]
JSON with analysis.
"""
```

### 3. Register with Orchestrator

```python
# backend/agents/orchestrator.py
from agents.market_researcher import MarketResearchAgent

orchestrator.register_agent(MarketResearchAgent)
```

### 4. Write Tests

```python
async def test_market_research_agent():
    agent = MarketResearchAgent(llm=mock_llm)
    result = await agent.analyze(["AAPL"], "1Y")
    assert result.analysis is not None
```

## Verification

- [ ] Agent runs successfully
- [ ] Output format correct
- [ ] Tests pass
- [ ] Prompt effective

## References

- [AI Agent Architecture](../../architecture/05_AI_Agent_Architecture.md)
- [AI Agent Protocol](../../prompts/AI_AGENT_PROTOCOL.md)
