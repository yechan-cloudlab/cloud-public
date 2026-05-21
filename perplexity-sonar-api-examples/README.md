# Perplexity Sonar API Examples

Perplexity Sonar API examples for building web-grounded AI answers with citations.

> This repository is a **sample project for a blog post**. It is not an official Perplexity repository and is not production-ready as-is. Use it to understand the API shape, citation handling, streaming, and search options before building your own service.

---

## Related article

- [Perplexity Sonar](https://tistory-cloud.tistory.com/entry/Perplexity-Sonar-API-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%8B%A4%EC%8B%9C%EA%B0%84-%EC%9B%B9-%EA%B2%80%EC%83%89%EC%9D%B4-%EA%B0%80%EB%8A%A5%ED%95%9C-AI-%EB%8B%B5%EB%B3%80-API-%EB%A7%8C%EB%93%A4%EA%B8%B0)

---

## What this example shows

- Calling Perplexity Sonar API with the OpenAI-compatible Python SDK
- Creating web-grounded answers with Sonar models
- Reading `citations` and `search_results` from responses
- Handling streaming responses
- Passing Perplexity-specific search options through `extra_body`
- Keeping API keys out of source code
- Basic operation checklist for cost, latency, and source trust

---

## What this example does not do

- It does not include a real API key.
- It does not guarantee answer accuracy.
- It does not replace source review, legal review, or security review.
- It does not include production-grade auth, retry, rate limit, cache, or observability.

---

## Folder structure

```text
python/             Sonar API examples
examples/           sample questions and expected response notes
docs/               API overview, prompt patterns, operation checklist
.env.example        environment variable template
requirements.txt    Python dependencies
```

---

## Quick start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Copy environment variables

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

### 3. Set your API key

Edit `.env`:

```env
PERPLEXITY_API_KEY=pplx-your-api-key
PERPLEXITY_MODEL=sonar-pro
PERPLEXITY_BASE_URL=https://api.perplexity.ai
```

### 4. Run a basic answer example

```bash
python python/basic_search_answer.py
```

### 5. Inspect citations and search results

```bash
python python/cited_answer.py
```

### 6. Run a streaming example

```bash
python python/streaming_answer.py
```

---

## Blog section mapping

| Blog section | Files |
|---|---|
| What is Sonar API | `docs/sonar-api-overview.md` |
| Calling Sonar API with Python | `python/basic_search_answer.py`, `python/sonar_client.py` |
| Understanding citations | `python/cited_answer.py`, `examples/expected_response.md` |
| Search options and model selection | `python/search_options.py`, `docs/prompt-patterns.md` |
| Streaming responses | `python/streaming_answer.py` |
| Operation checklist | `docs/operation-checklist.md` |

---

## Important notes

- Perplexity's canonical Sonar endpoint is `POST /v1/sonar`.
- When using the OpenAI SDK, `client.chat.completions.create()` routes to `/chat/completions`, which Perplexity accepts for compatibility.
- Use `base_url="https://api.perplexity.ai"` with the OpenAI SDK.
- Perplexity-specific options such as `search_domain_filter`, `search_recency_filter`, and `search_mode` can be passed through `extra_body` in the Python OpenAI SDK.
- Response fields can vary by model and API version. Inspect raw responses before writing production parsing logic.

---

## References

- [Perplexity Sonar API Quickstart](https://docs.perplexity.ai/docs/sonar/quickstart)
- [Perplexity OpenAI SDK Compatibility](https://docs.perplexity.ai/docs/sonar/openai-compatibility)
- [Perplexity Sonar API Reference](https://docs.perplexity.ai/api-reference/sonar-post)
- [Perplexity Search Filters](https://docs.perplexity.ai/docs/sonar/filters)
