# Architecture

```text
GitHub workflow
      ↓
self-hosted runner inside VPC
      ↓
AWS OIDC role assumption
      ↓
aws eks update-kubeconfig
      ↓
Private EKS API endpoint
      ↓
Helm deployment
```

The runner is the bridge between GitHub Actions and the private cluster network.
