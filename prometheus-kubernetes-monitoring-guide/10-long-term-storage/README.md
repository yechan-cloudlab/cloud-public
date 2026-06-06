# 10 Long-term Storage

Prometheus long-term storage examples for retention, Remote Write, and Thanos.

These files are examples only. Do not commit real object storage credentials, access keys, secret keys, remote write tokens, or internal endpoints.

## Files

- `prometheus-retention-values.yaml`: kube-prometheus-stack values example for retention and PVC.
- `remote-write-example.yaml`: Prometheus custom resource remoteWrite example.
- `remote-write-relabel-example.yaml`: Remote Write example with write relabeling.
- `thanos-sidecar-values.yaml`: kube-prometheus-stack values example for Thanos sidecar.
- `thanos-object-storage-example.yaml`: Placeholder object storage config example.
- `storage-design-checklist.md`: Design checklist for long-term storage.

## Validate

```bash
helm template kube-prometheus-stack prometheus-community/kube-prometheus-stack \
  -n monitoring \
  -f prometheus-retention-values.yaml
```

## Safety Notes

- Replace every placeholder before real use.
- Keep object storage credentials in Kubernetes Secrets or cloud IAM roles.
- Confirm retention size is smaller than the actual PVC capacity.
- Monitor Remote Write queue and failed samples.
- Review high-cardinality labels before sending metrics to long-term storage.
