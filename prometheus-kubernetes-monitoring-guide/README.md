# Prometheus Kubernetes Monitoring Guide

Prometheus Kubernetes monitoring examples for the blog series.

This directory contains practical examples for installing and operating Prometheus on Kubernetes.
The examples are designed for learning and review. They are not production-ready defaults.

## Blog Series Mapping

| Part | Blog Topic | Directory | Example Files | Blog |
|---:|---|---|---|---|
| 1 | Prometheus monitoring architecture and metrics flow | Concept article | No example files | [Part 1](https://tistory-cloud.tistory.com/entry/Prometheus%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-Kubernetes-%EB%AA%A8%EB%8B%88%ED%84%B0%EB%A7%81-%EA%B5%AC%EC%A1%B0%EC%99%80-%EB%A9%94%ED%8A%B8%EB%A6%AD-%EC%88%98%EC%A7%91-%ED%9D%90%EB%A6%84-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0) |
| 2 | Prometheus Helm install with kube-prometheus-stack | `02-helm-install/` and legacy `helm/` | `install-commands.md`, `values-minimal.yaml`, `values-prod-example.yaml` | [Part 2](https://tistory-cloud.tistory.com/entry/Prometheus-Helm-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95-kube-prometheus-stack%EC%9C%BC%EB%A1%9C-Grafana%EC%99%80-Alertmanager%EA%B9%8C%EC%A7%80-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0) |
| 3 | Prometheus Operator resources | `03-operator-resources/` | `servicemonitor-example.yaml`, `podmonitor-example.yaml`, `prometheusrule-example.yaml` | [Part 3](https://tistory-cloud.tistory.com/entry/Prometheus%EC%99%80-Prometheus-Operator-%EC%B0%A8%EC%9D%B4-ServiceMonitor-PodMonitor-PrometheusRule-%EC%97%AD%ED%95%A0-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0) |
| 4 | Basic exporters | `04-basic-exporters/` | node-exporter, cAdvisor, kube-state-metrics PromQL examples | [Part 4](https://tistory-cloud.tistory.com/entry/Prometheus-%EA%B8%B0%EB%B3%B8-%EC%88%98%EC%A7%91%EA%B8%B0-%EC%A0%95%EB%A6%AC-node-exporter-cAdvisor-kube-state-metrics%EB%8A%94-%EB%AC%B4%EC%97%87%EC%9D%84-%EC%88%98%EC%A7%91%ED%95%A0%EA%B9%8C) |
| 5 | Application custom metrics | `05-application-metrics/` | ServiceMonitor, PodMonitor, application PromQL examples | [Part 5](https://tistory-cloud.tistory.com/entry/Prometheus-%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EB%A9%94%ED%8A%B8%EB%A6%AD-%EC%88%98%EC%A7%91-%EB%B0%A9%EB%B2%95-ServiceMonitor%EC%99%80-PodMonitor%EB%A1%9C-custom-metrics-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0) |
| 6 | Special exporters | `06-special-exporters/` | Blackbox, NGINX, NVIDIA DCGM examples | [Part 6](https://tistory-cloud.tistory.com/entry/Prometheus-%ED%8A%B9%EC%88%98-Exporter-%EC%A0%95%EB%A6%AC-NGINX-NVIDIA-DCGM-Blackbox-Exporter%EB%A1%9C-%ED%99%95%EC%9E%A5-%EB%AA%A8%EB%8B%88%ED%84%B0%EB%A7%81%ED%95%98%EA%B8%B0) |
| 7 | PromQL examples | `07-promql-basics/` | Kubernetes resource, Pod status, HTTP service, exporter queries | [Part 7](https://tistory-cloud.tistory.com/entry/PromQL-%EC%82%AC%EC%9A%A9%EB%B2%95-%EA%B8%B0%EC%B4%88-Prometheus-%EB%A9%94%ED%8A%B8%EB%A6%AD%EC%9D%84-%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B3%A0-CPU%C2%B7%EB%A9%94%EB%AA%A8%EB%A6%AC%C2%B7Pod-%EC%83%81%ED%83%9C%EB%A5%BC-%EB%B6%84%EC%84%9D%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95) |
| 8 | Grafana dashboards | `08-grafana-dashboard/` | dashboard JSON and provisioning example | [Part 8](https://tistory-cloud.tistory.com/entry/Grafana-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C-%EB%A7%8C%EB%93%9C%EB%8A%94-%EB%B0%A9%EB%B2%95-Prometheus-%EB%A9%94%ED%8A%B8%EB%A6%AD%EC%9C%BC%EB%A1%9C-Kubernetes-%EC%9A%B4%EC%98%81-%ED%99%94%EB%A9%B4-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0) |
| 9 | Alertmanager rules and routing | `09-alertmanager/` | PrometheusRule, AlertmanagerConfig, inhibition, labeling guide | [Part 9](https://tistory-cloud.tistory.com/entry/Prometheus-Alertmanager-%EC%82%AC%EC%9A%A9%EB%B2%95-PrometheusRule%EB%A1%9C-%EC%95%8C%EB%A6%BC-%EC%A1%B0%EA%B1%B4%EA%B3%BC-%EC%9E%A5%EC%95%A0-%EB%8C%80%EC%9D%91-%ED%9D%90%EB%A6%84-%EB%A7%8C%EB%93%A4%EA%B8%B0) |
| 10 | Long-term storage and remote write | `10-long-term-storage/` | retention values, remote write, relabeling, Thanos sidecar examples | [Part 10](https://tistory-cloud.tistory.com/entry/Prometheus-%EC%9E%A5%EA%B8%B0-%EC%A0%80%EC%9E%A5-%EB%B0%A9%EB%B2%95-Thanos-Remote-Write-%EC%99%B8%EB%B6%80-%EC%A0%80%EC%9E%A5%EC%86%8C%EB%A1%9C-%EB%A9%94%ED%8A%B8%EB%A6%AD-%EB%B3%B4%EA%B4%80%ED%95%98%EA%B8%B0) |

## Current Scope

The current files support **Part 2 through Part 10** of the Prometheus blog series. Part 1 is a concept article without a dedicated example directory.

```text
prometheus-kubernetes-monitoring-guide/
├─ README.md
├─ helm/                         # legacy path kept for existing blog links
├─ 02-helm-install/
├─ 03-operator-resources/
├─ 04-basic-exporters/
├─ 05-application-metrics/
├─ 06-special-exporters/
├─ 07-promql-basics/
└─ 08-grafana-dashboard/
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
