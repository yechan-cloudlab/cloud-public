# Sonar API overview

Perplexity Sonar API provides web-grounded AI responses through an API.

## Why it matters

General LLM APIs are strong at generation, reasoning, summarization, and coding. Sonar is useful when the answer needs live web context, citations, and source-aware research.

## General LLM API vs Sonar API

| Area | General LLM API | Sonar API |
|---|---|---|
| Knowledge source | Model knowledge and prompt context | Web-grounded search context |
| Freshness | Depends on model/tool setup | Designed for current web information |
| Sources | Usually custom implementation | Citations/search results available |
| Best use | Generation, reasoning, coding | Research, source-backed answers, market/news lookup |

## Good use cases

- Latest product or service research
- Source-backed summaries
- Market and industry trend lookup
- Comparison reports
- Research assistant features inside internal tools

## Poor use cases

- Blindly automating legal, medical, or financial decisions
- Sending confidential internal data to an external API without review
- Treating citations as automatically trustworthy
