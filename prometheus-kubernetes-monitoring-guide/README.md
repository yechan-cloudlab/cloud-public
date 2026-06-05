# Prometheus Kubernetes Monitoring Guide

Prometheus Kubernetes monitoring examples for the blog series.

This directory contains practical examples for installing and operating Prometheus on Kubernetes.
The examples are designed for learning and review. They are not production-ready defaults.

## Blog Series Mapping

| Part | Blog Topic | Directory | Example Files |
|---:|---|---|---|
| 2 | Prometheus Helm install with kube-prometheus-stack | `helm/` | `install-commands.md`, `values-minimal.yaml`, `values-prod-example.yaml` |
| 3 | Prometheus Operator resources | `operator/` | Planned |
| 4 | Basic exporters | `exporters-basic/` | Planned |
| 5 | Application custom metrics | `app-metrics/` | Planned |
| 6 | Special exporters | `exporters-special/` | Planned |
| 7 | PromQL examples | `promql/` | Planned |
| 8 | Grafana dashboards | `grafana/` | Planned |
| 9 | Alertmanager rules and routing | `alertmanager/` | Planned |
| 10 | Long-term storage and remote write | `storage/` | Planned |

## Current Scope

The current files support **Part 2: Prometheus Helm install**.

```text
prometheus-kubernetes-monitoring-guide/
├─ README.md
└─ helm/
   ├─ install-commands.md
   ├─ values-minimal.yaml
   └─ values-prod-example.yaml
```

## What Each File Is For

### `helm/install-commands.md`

Contains copy-ready commands for:

- adding the `prometheus-community` Helm repository
- creating the `monitoring` namespace
- installing `kube-prometheus-stack`
- checking Pods, Services, Prometheus, Alertmanager, and Helm release status
- using `kubectl port-forward` for Prometheus, Grafana, and Alertmanager
- uninstalling the Helm release

### `helm/values-minimal.yaml`

Minimal values for first installation tests.

This file intentionally keeps the configuration small:

- Grafana enabled
- Alertmanager enabled
- Prometheus retention set to `7d`
- no PVC storage configuration
- no external exposure
- no real passwords or secrets

Use this when you want to confirm that the chart installs and the default stack starts.

### `helm/values-prod-example.yaml`

Production-like review example.

This file adds basic operational settings:

- Grafana enabled
- placeholder Grafana admin password
- Grafana Service kept as `ClusterIP`
- Alertmanager enabled
- Prometheus retention set to `15d`
- Prometheus PVC example with `20Gi`
- commented `storageClassName` example

This file is **not production-ready**. Replace password, storage class, PVC size, ingress, resources, and alert routing before use.

## Prerequisites

You need:

- a running Kubernetes cluster
- `kubectl`
- `helm`
- permission to create resources in the target namespace
- permission to create or manage Prometheus Operator CRDs

Check your local tools:

```bash
kubectl version --client
helm version
kubectl config current-context
kubectl get nodes
```

## Install kube-prometheus-stack

Add the Helm repository:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

Create the namespace:

```bash
kubectl create namespace monitoring
```

If the namespace already exists, skip this step.

Install with the minimal values:

```bash
helm upgrade --install kube-prometheus-stack \
  prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  -f helm/values-minimal.yaml
```

Install with the production-like example values:

```bash
helm upgrade --install kube-prometheus-stack \
  prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  -f helm/values-prod-example.yaml
```

## Verify Installation

Check the Helm release:

```bash
helm list -n monitoring
helm status kube-prometheus-stack -n monitoring
```

Check Pods:

```bash
kubectl get pods -n monitoring
```

Expected components include:

- Prometheus Operator
- Prometheus
- Grafana
- Alertmanager
- node-exporter
- kube-state-metrics

Check Services:

```bash
kubectl get svc -n monitoring
```

Check Prometheus custom resources:

```bash
kubectl get prometheus -n monitoring
kubectl get alertmanager -n monitoring
kubectl get servicemonitor -n monitoring
kubectl get prometheusrule -n monitoring
```

## Access Prometheus, Grafana, and Alertmanager

Service names can vary depending on the Helm release name.
Check actual service names first:

```bash
kubectl get svc -n monitoring
```

Typical port-forward commands:

```bash
kubectl port-forward -n monitoring svc/kube-prometheus-stack-prometheus 9090:9090
kubectl port-forward -n monitoring svc/kube-prometheus-stack-grafana 3000:80
kubectl port-forward -n monitoring svc/kube-prometheus-stack-alertmanager 9093:9093
```

Then open:

| Component | URL |
|---|---|
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |
| Alertmanager | http://localhost:9093 |

## First Things To Check

In Prometheus:

- `Status > Targets`
- whether key targets are `UP`
- query `up`
- query `node_cpu_seconds_total`
- query `kube_pod_info`

In Grafana:

- Prometheus data source is configured
- default dashboards are available
- Kubernetes node and pod metrics are visible

In Alertmanager:

- Alertmanager UI opens
- alert groups are visible when alerts fire
- silence page works

## Common Installation Issues

| Symptom | Check | Fix |
|---|---|---|
| Helm install fails with CRD permission error | `kubectl auth can-i create crd` | Use an account with proper cluster permissions |
| Pods stay Pending | `kubectl describe pod -n monitoring <pod>` | Check node resources, taints, PVC binding, storage class |
| Grafana has no data | Prometheus targets and Grafana data source | Check Prometheus service URL and target status |
| port-forward fails | `kubectl get svc -n monitoring` | Use the actual Service name created by your release |
| Reinstall fails | `helm list -n monitoring`, `kubectl get pvc -n monitoring` | Check old release, PVC, CRD, namespace resources |

## Uninstall

Uninstall Helm release:

```bash
helm uninstall kube-prometheus-stack -n monitoring
```

Check remaining PVCs:

```bash
kubectl get pvc -n monitoring
```

Check remaining CRDs:

```bash
kubectl get crd | grep monitoring.coreos.com
```

On Windows PowerShell:

```powershell
kubectl get crd | findstr monitoring.coreos.com
```

Delete PVCs only when you are sure you no longer need stored metrics or Grafana data.

## Local Validation Status

The files were reviewed structurally, but live installation was not executed in this workspace because `helm` and `kubectl` are not installed in the current environment.

Run the commands below in a machine that has access to a Kubernetes cluster:

```bash
helm lint prometheus-community/kube-prometheus-stack -f helm/values-minimal.yaml
helm template kube-prometheus-stack prometheus-community/kube-prometheus-stack \
  -n monitoring \
  -f helm/values-minimal.yaml > rendered-minimal.yaml
```

For the production-like example:

```bash
helm template kube-prometheus-stack prometheus-community/kube-prometheus-stack \
  -n monitoring \
  -f helm/values-prod-example.yaml > rendered-prod-example.yaml
```

If rendering succeeds, apply to a test cluster before using any values in production.

## Safety Notes

- Do not commit real Grafana admin passwords.
- Do not commit Slack webhook URLs, tokens, or secret values.
- Do not expose Grafana, Prometheus, or Alertmanager publicly without authentication.
- Review storage class, PVC size, retention, and service exposure before production use.
- Treat `values-prod-example.yaml` as a starting point, not a production-ready default.
- Keep production values in a private repository if they contain organization-specific settings.
