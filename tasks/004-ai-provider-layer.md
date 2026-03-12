# 004 — AI Provider Layer

## Intent

Provide a **single abstraction layer for all LLM interactions** via **OpenRouter**. No service, view, or model may call an AI provider SDK directly. All inference must flow through the client defined in [`ai/client.py`](ai/client.py).

OpenRouter allows us to access Claude, GPT, Llama, and other models through a unified API.

---

## Architecture

```
services → AIClient → OpenRouter Implementation → OpenRouter API → Provider
```

Modules:

```
ai/
  __init__.py
  client.py
  providers.py
  types.py
```

---

## Provider Interface

Defined in [`ai/providers.py`](ai/providers.py).

Required method:

```
generate(
  prompt: str,
  system: str | None,
  model: str,
  temperature: float,
  response_format: dict | None
) -> dict
```

Return value must always be a **parsed JSON dictionary**.

---

## Environment Variables

Required:

```
OPENROUTER_API_KEY
DEFAULT_AI_MODEL (e.g., "anthropic/claude-3-opus")
```

---

## Prompt Loading

Prompts are primarily stored in the **database** (within `Author` and `Editor` models) to allow for real-time UI-based editing. A fallback mechanism for file-based prompts in `/prompts` may be maintained for system-level tasks.

---

## JSON Output Enforcement

All AI prompts must require **strict JSON responses**.

AIClient responsibilities:

- parse JSON
- validate schema
- retry if JSON invalid

---

## Retry Strategy

Retries triggered by:

- network errors
- rate limits
- invalid JSON output

Maximum attempts: 3.

---

## Logging

Each request must log:

- model
- latency
- retry count
- prompt source (DB vs File)

---

## Implementation Steps

1. Create `ai` module
2. Implement `OpenRouterProvider`
3. Implement `AIClient`
4. Add database prompt loading logic
5. Add JSON validation
6. Add retry logic

---

## Verification

Run Django shell:

```
python manage.py shell
```

```
from ai.client import AIClient

client = AIClient()
client.generate(
  prompt="Return JSON {\"ok\": true}",
  system="Respond only with JSON",
  model="gpt-4o",
  temperature=0
)
```

Expected output:

```
{"ok": true}
```

---

## Dot Execution Plan

```
004.ai.providers.BaseProvider.generate
004.ai.providers.OpenAIProvider.generate
004.ai.providers.AnthropicProvider.generate

004.ai.client.AIClient.__init__
004.ai.client.AIClient.load_prompt
004.ai.client.AIClient.render_prompt
004.ai.client.AIClient.execute
004.ai.client.AIClient.parse_json
004.ai.client.AIClient.generate
```

---

End of specification.
