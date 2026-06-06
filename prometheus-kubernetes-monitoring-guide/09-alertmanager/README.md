# 09 Alertmanager

PrometheusRule and AlertmanagerConfig examples for the Prometheus Alertmanager blog post.

These files are examples only. Do not commit real Slack webhook URLs, email addresses, PagerDuty keys, OpsGenie keys, or internal incident URLs.

## Files

- `prometheusrule-alerts.yaml`: Example alerting rules for service error rate and target availability.
- `alertmanagerconfig-routing.yaml`: Example AlertmanagerConfig routing by team and severity.
- `alertmanager-inhibition-example.yaml`: Example inhibition rule.
- `alert-labeling-guide.md`: Practical label and annotation guide for alert operations.

## Apply

```bash
kubectl apply -f prometheusrule-alerts.yaml
kubectl apply -f alertmanagerconfig-routing.yaml
kubectl apply -f alertmanager-inhibition-example.yaml
```

## Validate

```bash
kubectl get prometheusrule -n monitoring
kubectl get alertmanagerconfig -n monitoring
kubectl describe prometheusrule -n monitoring sample-service-alerts
```

## Safety Notes

- Replace all placeholder receiver values before real use.
- Keep real tokens and webhook URLs in Kubernetes Secrets or private configuration.
- Confirm that your Prometheus instance selects these resources by labels.
- Confirm that your Alertmanager instance is configured to select AlertmanagerConfig resources.
