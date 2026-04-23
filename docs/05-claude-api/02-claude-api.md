# Claude API

The Claude API lets you integrate Claude into your own applications.

API Usage is pay-as-you-go.

## Quick Start

```python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)
print(message.content[0].text)
```

## Prompt Caching

Cache large system prompts or documents to reduce latency and cost:

```python
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": "You are a helpful assistant...",
            "cache_control": {"type": "ephemeral"}
        }
    ],
    messages=[{"role": "user", "content": "Question here"}]
)
```

## Tool Use

Give Claude the ability to call functions:

```python
tools = [
    {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    }
]
```

## Pricing (approximate)

| Model | Input | Output |
|-------|-------|--------|
| Opus 4.7 | $15 / MTok | $75 / MTok |
| Sonnet 4.6 | $3 / MTok | $15 / MTok |
| Haiku 4.5 | $0.80 / MTok | $4 / MTok |
