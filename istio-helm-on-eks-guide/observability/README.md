# Observability notes

Istio observability should be used to answer:

- Which service is calling which service?
- Which edge has high latency?
- Which workload is returning 5xx?
- Did a routing rule change traffic distribution?
- Did mTLS or AuthorizationPolicy introduce failures?

Use:

- Prometheus for metrics
- Grafana for dashboards
- Kiali for service graph
- Envoy access logs for request-level debugging
