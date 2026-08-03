# Prompt Engineering Standards: AFIP

**Version**: 1.0

## Structure

```
[SYSTEM]
Role definition

[CONTEXT]
Background information

[INSTRUCTIONS]
What to do

[CONSTRAINTS]
Rules and limitations

[OUTPUT FORMAT]
Expected format

[EXAMPLES]
Examples if needed
```

## Principles

1. **Clear Role**: Define who the AI is
2. **Specific Instructions**: Be precise
3. **Constraints**: Set boundaries
4. **Examples**: Show, don't just tell
5. **Output Format**: Specify structure

## Template

```
[SYSTEM]
You are a {role} with expertise in {domain}.

[CONTEXT]
{relevant context}

[INSTRUCTIONS]
1. {instruction 1}
2. {instruction 2}
3. {instruction 3}

[CONSTRAINTS]
- Constraint 1
- Constraint 2

[OUTPUT FORMAT]
{format specification}

[EXAMPLES]
Input: {example input}
Output: {example output}
```

## Best Practices

- Use clear, unambiguous language
- Provide context
- Set constraints
- Request structured output
- Include examples

## Versioning

- Store prompts in version control
- Track changes
- A/B test variants
- Document performance
