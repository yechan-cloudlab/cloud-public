# Operations checklist

## Before production

- [ ] Current AWS Bedrock pricing has been checked.
- [ ] Model IDs are available in the target region.
- [ ] `max_tokens` is set for every request.
- [ ] Request category is logged.
- [ ] Model ID is logged.
- [ ] Input and output token counts are stored.
- [ ] Cost alarms are configured.
- [ ] Sensitive prompts are masked or excluded from logs.
- [ ] Routing rules have dry-run mode.
- [ ] Rollback path to a single default model exists.

## Cost controls

- [ ] Daily budget alarm
- [ ] Monthly budget alarm
- [ ] Per-model usage dashboard
- [ ] Per-category usage dashboard
- [ ] High-output-token request alert
- [ ] Retry count alert

## Quality controls

- [ ] Golden test set
- [ ] Model fallback policy
- [ ] Human review for high-risk tasks
- [ ] Prompt injection review for external content
- [ ] Regression test after prompt or rule changes

## Logging guidance

Log metadata by default:

- request id
- request category
- selected model
- input token count
- output token count
- latency
- estimated cost

Avoid logging raw prompts unless you have a clear privacy and retention policy.
