# Terraform sample

This folder contains a minimal CloudWatch Dashboard and estimated billing alarm example.

## Commands

```bash
terraform init
terraform plan
```

Do not run `terraform apply` against a production AWS account without reviewing every resource.

## Notes

- Billing metrics are generally viewed from `us-east-1`.
- The dashboard uses a custom namespace example: `Custom/BedrockRouter`.
- You need to publish your own metrics for input tokens, output tokens, selected model, and request category.
