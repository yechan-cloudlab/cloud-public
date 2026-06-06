# kube-prometheus-stack Install Commands

## Add Helm Repository

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

## Create Namespace

```bash
kubectl create namespace monitoring
```

If the namespace already exists, this command can be skipped.

## Minimal Install

```bash
helm upgrade --install kube-prometheus-stack \
  prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  -f helm/values-minimal.yaml
```

## Production Example Install

```bash
helm upgrade --install kube-prometheus-stack \
  prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  -f helm/values-prod-example.yaml
```

## Verify Installation

```bash
kubectl get pods -n monitoring
kubectl get svc -n monitoring
kubectl get prometheus -n monitoring
kubectl get alertmanager -n monitoring
helm list -n monitoring
```

## Port Forward

Service names can vary depending on the Helm release name. Check actual service names first.

```bash
kubectl get svc -n monitoring
```

Example:

```bash
kubectl port-forward -n monitoring svc/kube-prometheus-stack-prometheus 9090:9090
kubectl port-forward -n monitoring svc/kube-prometheus-stack-grafana 3000:80
kubectl port-forward -n monitoring svc/kube-prometheus-stack-alertmanager 9093:9093
```

## Uninstall

```bash
helm uninstall kube-prometheus-stack -n monitoring
kubectl get pvc -n monitoring
kubectl get crd | findstr monitoring.coreos.com
```
