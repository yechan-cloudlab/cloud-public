# Expected response shape

Perplexity Sonar responses follow the OpenAI Chat Completions shape and can include Perplexity-specific fields.

Common fields to inspect:

```json
{
  "id": "...",
  "model": "sonar-pro",
  "object": "chat.completion",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "answer text"
      }
    }
  ],
  "usage": {
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0
  },
  "citations": [
    "https://example.com/source"
  ],
  "search_results": [
    {
      "title": "source title",
      "url": "https://example.com/source",
      "date": "2026-01-01"
    }
  ]
}
```

## Production parsing checklist

- Do not assume every optional field exists.
- Check `choices[0].message.content` before rendering the answer.
- Store citations separately if the UI needs source cards.
- Track `usage` for cost analysis.
- Log status code, request ID, and error message for failed calls.
