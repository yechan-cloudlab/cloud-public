# bedrock-cost-compare

> Example repository for comparing Amazon Bedrock Claude model costs and designing a simple request routing strategy.

This is a **sample repository**. It is not a production-ready Bedrock cost platform. The goal is to show how Claude Haiku, Sonnet, and Opus-style model tiers can be selected by request type so teams can understand and control token cost.

## Why this example exists

A common Bedrock cost problem is sending every request to the strongest model. Simple summarization, classification, and translation requests usually do not need the same model tier as complex reasoning or high-risk code review.

This example shows a small workflow:

1. Classify each request into a category such as `summarize`, `classify`, `code_generate`, or `deep_reasoning`.
2. Select a model tier from routing rules.
3. Estimate cost by separating input tokens and output tokens.
4. Compare a fixed-model strategy with a routed strategy.

## What is included

- Cost calculator for Bedrock Claude-style model tiers
- Request routing rules by task category
- Fixed-model vs routed-model comparison script
- CloudWatch Dashboard sample
- Terraform sample for a dashboard and billing alarm
- Model selection guide
- Operations checklist
- Unit tests using Python standard library `unittest`

## Pricing policy

AWS Bedrock pricing can change by model, version, region, and billing mode. This repository does not hard-code real production prices.

- `config/pricing.template.json`: template for real pricing. Fill it with current AWS pricing before using it.
- `config/pricing.demo.json`: fictional demo pricing for local execution only. Do not use it for billing decisions.

Always verify current pricing and model availability from official AWS documentation:

- AWS Bedrock pricing: https://aws.amazon.com/bedrock/pricing/
- Amazon Bedrock User Guide: https://docs.aws.amazon.com/bedrock/
- Anthropic models in Amazon Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html

## Repository structure

```text
bedrock-cost-compare/
  config/
    pricing.demo.json
    pricing.template.json
    routing-rules.example.json
  dashboards/
    cloudwatch-dashboard.sample.json
  docs/
    model-selection.md
    operations-checklist.md
  examples/
    requests.jsonl
  src/
    bedrock_client.py
    compare_strategies.py
    cost_calculator.py
    router.py
  terraform/
    main.tf
    outputs.tf
    variables.tf
  tests/
    test_cost_calculator.py
  README.md
```

## Quick start

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Run the demo cost calculator

```bash
python src/cost_calculator.py --pricing config/pricing.demo.json --requests examples/requests.jsonl
```

### 3. Run the router demo

```bash
python src/router.py --rules config/routing-rules.example.json --requests examples/requests.jsonl
```

### 4. Compare fixed model vs routing strategy

```bash
python src/compare_strategies.py --pricing config/pricing.demo.json --rules config/routing-rules.example.json --requests examples/requests.jsonl --baseline claude-opus
```

## Example routing policy

| Request category | Suggested model tier | Reason |
| --- | --- | --- |
| `summarize` | Claude Haiku | Short summarization is usually cost and latency sensitive. |
| `classify` | Claude Haiku | Classification is often repetitive and simple. |
| `translate` | Claude Haiku | Translation can often start with a lower-cost model. |
| `code_generate` | Claude Sonnet | Code generation needs stronger instruction following. |
| `code_review` | Claude Sonnet | Code review needs balanced reasoning and cost. |
| `security_audit` | Claude Sonnet or Opus | Security tasks need stronger review and sometimes escalation. |
| `deep_reasoning` | Claude Opus | Use the strongest model only for high-value complex reasoning. |

## Run tests

```bash
python -m unittest discover -s tests
```

## Terraform sample

Terraform files in `terraform/` create a sample CloudWatch Dashboard and a simple estimated billing alarm.

```bash
cd terraform
terraform init
terraform plan
```

Review the Terraform files before applying them to any AWS account.

## Production checklist

Before using this idea in production:

- Check current AWS Bedrock pricing.
- Confirm model availability in your target region.
- Set `max_tokens` for every request.
- Log request category, selected model, input tokens, and output tokens.
- Mask sensitive prompts and customer data.
- Add budget alarms before rollout.
- Start with dry-run routing.
- Keep a rollback path to a single default model.

## Related blog article

Coming soon.

## License

MIT License. See `LICENSE`.
