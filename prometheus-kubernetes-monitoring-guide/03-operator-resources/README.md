# 03 Operator Resources

Prometheus Operator custom resource examples.

## Files

- `servicemonitor-example.yaml`: Scrape metrics through a Kubernetes Service.
- `podmonitor-example.yaml`: Scrape metrics directly from matching Pods.
- `prometheusrule-example.yaml`: Example alerting rules.

## Apply

```bash
kubectl apply -f servicemonitor-example.yaml
kubectl apply -f podmonitor-example.yaml
kubectl apply -f prometheusrule-example.yaml
```
