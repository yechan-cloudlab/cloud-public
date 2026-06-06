# 02 Helm Install

Examples for installing `kube-prometheus-stack` with Helm.

## Files

- `install-commands.md`: Helm repository and install commands.
- `values-minimal.yaml`: Small local/dev-oriented values example.
- `values-prod-example.yaml`: More production-like values example.

## Validate

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm template monitoring prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  -f values-minimal.yaml
```
