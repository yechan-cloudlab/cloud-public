# eks-manifest-auditor

`eks-manifest-auditor` is a Python CLI that scans local Kubernetes/EKS YAML manifests and reports operational, security, and resource risks before anything is deployed.

It does not connect to AWS, EKS, kubeconfig, or a live Kubernetes cluster. The v0.1 scope is intentionally limited to local static analysis so the tool can be developed, tested, and reviewed without cloud access.

Related Article: [EKS Manifest 검사 자동화: Kubernetes YAML 보안·리소스 문제를 로컬에서 찾는 Python CLI 만들기](https://tistory-cloud.tistory.com/entry/EKS-Manifest-%EA%B2%80%EC%82%AC-%EC%9E%90%EB%8F%99%ED%99%94-Kubernetes-YAML-%EB%B3%B4%EC%95%88%C2%B7%EB%A6%AC%EC%86%8C%EC%8A%A4-%EB%AC%B8%EC%A0%9C%EB%A5%BC-%EB%A1%9C%EC%BB%AC%EC%97%90%EC%84%9C-%EC%B0%BE%EB%8A%94-Python-CLI-%EB%A7%8C%EB%93%A4%EA%B8%B0)

## Why This Is Needed

Many EKS incidents start in manifest files:

- containers without CPU or memory requests
- mutable image tags such as `latest`
- privileged containers
- `hostPath` volumes
- public `LoadBalancer` or `NodePort` Services
- missing or unclear IRSA annotations

Finding these problems before CI/CD or production rollout gives platform teams a lightweight guardrail that works on a laptop, in pull requests, and in future automation pipelines.

## Features

- Recursively scans `.yaml` and `.yml` files
- Parses multi-document Kubernetes YAML files
- Handles invalid YAML without stopping the whole scan
- Detects workload, security, service, ingress, and IRSA issues
- Prints Rich console tables with severity colors
- Writes JSON reports
- Writes Markdown reports
- Keeps scanner, parser, checks, and reporters separated for future extension

## Checks

### Workload Checks

- Missing `resources.requests` in `Deployment`, `StatefulSet`, and `DaemonSet` containers
- Missing `resources.limits`
- Images using the `latest` tag or no explicit tag
- `replicas` value of `1` or lower

### Security Checks

- `privileged: true`
- `hostPath` volume usage
- `default` namespace usage
- `allowPrivilegeEscalation: true`
- Missing `runAsNonRoot`

### Service Checks

- `Service` type `LoadBalancer`
- `NodePort` usage

### Ingress Checks

- Lists Ingress annotations
- Checks whether an ingress class annotation or `spec.ingressClassName` is set

### IRSA Checks

- Checks whether a `ServiceAccount` has the `eks.amazonaws.com/role-arn` annotation

## Installation

Use Python 3.12.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

On PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

## Usage

Put Kubernetes YAML files under a local directory such as `manifests/`.

```text
manifests/
  deployment.yaml
  service.yaml
  ingress.yaml
  serviceaccount.yaml
```

Nested directories are supported.

```text
manifests/
  app1/
    deployment.yaml
  app2/
    service.yaml
  ingress.yaml
```

Scan a manifest directory and print a console table:

```bash
eks-manifest-auditor scan ./manifests
```

The directory name does not have to be `manifests`. Any local path containing Kubernetes YAML files can be scanned.

```bash
eks-manifest-auditor scan ./k8s
eks-manifest-auditor scan ./deploy
eks-manifest-auditor scan ./helm-rendered
```

If you use Helm, render the chart first and scan the rendered YAML output.

```bash
helm template my-app ./chart > ./helm-rendered/my-app.yaml
eks-manifest-auditor scan ./helm-rendered
```

Scan the included example manifests:

```bash
eks-manifest-auditor scan ./examples
```

Write a JSON report:

```bash
eks-manifest-auditor scan ./examples --output json --file report.json
```

Write a Markdown report:

```bash
eks-manifest-auditor scan ./examples --output markdown --file report.md
```

## Console Output Example

```text
EKS Manifest Auditor Findings

Severity  Check ID                         Resource              Namespace   Message
HIGH      WORKLOAD_IMAGE_LATEST_TAG        Deployment/risky-api  default     Container 'app' uses a mutable image tag: nginx:latest.
HIGH      SECURITY_PRIVILEGED_CONTAINER    Deployment/risky-api  default     Container 'app' sets privileged: true.
HIGH      SECURITY_HOST_PATH_VOLUME        Deployment/risky-api  default     Volume 'host-data' uses hostPath.
MEDIUM    SERVICE_LOAD_BALANCER            Service/risky-api     default     Service exposes a cloud LoadBalancer.

Summary
HIGH 4
MEDIUM 9
LOW 3
```

## JSON Example

```json
{
  "summary": {
    "LOW": 3,
    "MEDIUM": 9,
    "HIGH": 4
  },
  "findings": [
    {
      "severity": "HIGH",
      "check_id": "WORKLOAD_IMAGE_LATEST_TAG",
      "resource_kind": "Deployment",
      "resource_name": "risky-api",
      "namespace": "default",
      "message": "Container 'app' uses a mutable image tag: nginx:latest.",
      "recommendation": "Pin images to immutable version tags or digests.",
      "file_path": "examples/bad-deployment.yaml"
    }
  ]
}
```

## Markdown Report Example

```markdown
# EKS Manifest Auditor Report

## Summary

- Total findings: 16
- HIGH: 4
- MEDIUM: 9
- LOW: 3

## Findings Table

| Severity | Check ID | Resource | Namespace | Message | File |
|---|---|---|---|---|---|
| HIGH | WORKLOAD_IMAGE_LATEST_TAG | Deployment/risky-api | default | Container 'app' uses a mutable image tag: nginx:latest. | examples/bad-deployment.yaml |

## Severity Summary

| Severity | Count |
|---|---:|
| HIGH | 4 |
| MEDIUM | 9 |
| LOW | 3 |

## Recommendations

1. **WORKLOAD_IMAGE_LATEST_TAG** (Deployment/risky-api): Pin images to immutable version tags or digests.
```

## Development

Run tests:

```bash
pytest
```

Run lint:

```bash
ruff check .
```

## Project Structure

```text
eks-manifest-auditor/
  README.md
  pyproject.toml
  .gitignore
  examples/
    good-deployment.yaml
    bad-deployment.yaml
    ingress-example.yaml
  eks_manifest_auditor/
    main.py
    scanner.py
    parser.py
    models.py
    utils.py
    checks/
    reporters/
  tests/
  docs/
    roadmap.md
```

## Safety Boundary

The v0.1 implementation intentionally does not:

- call AWS APIs
- connect to EKS
- read kubeconfig
- query a live Kubernetes cluster
- send manifests to an AI service

All analysis is local static analysis of YAML files.

## Roadmap

- Live Kubernetes Cluster Scan
- EKS API Integration
- IRSA Visualization
- AI-based Troubleshooting
- Prometheus Alert Analysis
- HTML Dashboard
