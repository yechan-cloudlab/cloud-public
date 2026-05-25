# Roadmap

`eks-manifest-auditor` v0.1 intentionally performs local manifest static analysis only. It does not call AWS APIs, connect to EKS, or read kubeconfig.

## Planned Capabilities

- Live Kubernetes Cluster Scan
- EKS API Integration
- IRSA Visualization
- AI-based Troubleshooting
- Prometheus Alert Analysis
- HTML Dashboard

## Design Direction

- Keep local static analysis as the default safe mode.
- Add scanners as separate modules instead of mixing AWS calls into current checks.
- Add plugin registration for custom checks.
- Keep reporters independent from scanners so the same findings can power CLI, JSON, Markdown, and future HTML output.
