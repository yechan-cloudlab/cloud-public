# Alert Labeling Guide

Use labels for routing and grouping. Use annotations for human-readable context.

## Recommended Labels

| Label | Purpose | Example |
|---|---|---|
| `severity` | Routing and priority | `critical`, `warning` |
| `team` | Ownership | `platform`, `backend` |
| `service` | Affected service | `payment-api` |
| `namespace` | Kubernetes namespace | `production` |
| `cluster` | Cluster identifier | `prod-eks-a` |

## Recommended Annotations

| Annotation | Purpose |
|---|---|
| `summary` | Short alert summary |
| `description` | Current condition and threshold |
| `runbook_url` | Link to runbook or incident guide |
| `dashboard_url` | Link to Grafana dashboard |

## Rule of Thumb

- Labels should be stable and useful for routing.
- Annotations can contain longer text for responders.
- Avoid putting secrets, tokens, or private incident data in rule files.
