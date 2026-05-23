# Grafana dashboard notes

Recommended Istio dashboard signals:

- request volume
- success rate
- p50 / p90 / p99 latency
- 4xx / 5xx error rate
- source workload
- destination workload
- response flags from Envoy access logs

Use this together with service-level dashboards, not as the only production dashboard.
