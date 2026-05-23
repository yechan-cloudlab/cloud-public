# Model selection guide

This guide explains how to choose a Claude model tier for each request category.

## Recommended default

Do not start with Opus as the default model for every request. A practical default is to start with Sonnet, downgrade simple tasks to Haiku, and escalate only complex or high-value tasks to Opus.

## Suggested routing

| Request type | Suggested model tier | Reason |
| --- | --- | --- |
| Summarization | Haiku | Fast and cost-sensitive |
| Classification | Haiku | Usually repetitive and simple |
| Translation | Haiku | Can often start with a cheaper model |
| Code generation | Sonnet | Needs stronger instruction following |
| Code review | Sonnet | Balanced reasoning and cost |
| Security audit | Sonnet or Opus | Depends on risk and complexity |
| Deep reasoning | Opus | Use only for high-value complex tasks |

## Escalation policy

Routing should not be based on cost alone. Escalate to a stronger model when:

- the task involves security, permissions, or personal data;
- generated code may affect production systems;
- the answer must combine multiple long documents;
- the cheaper model produces low-confidence or repeated retry results.

## Evaluation before production

- Build a small golden dataset.
- Compare answer quality by task category.
- Track latency, cost, failure rate, and retry rate.
- Do not evaluate only by subjective answer quality.
- Keep human review for high-risk tasks.
