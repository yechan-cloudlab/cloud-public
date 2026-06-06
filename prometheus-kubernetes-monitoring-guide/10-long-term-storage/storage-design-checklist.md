# Prometheus Long-term Storage Design Checklist

## Retention

- Define required retention period.
- Confirm PVC capacity and retention size.
- Monitor Prometheus disk usage.
- Keep local retention short when Thanos object storage is used.

## Remote Write

- Use placeholder endpoints in public examples.
- Store real credentials in Kubernetes Secrets.
- Monitor queue capacity, failed samples, and endpoint latency.
- Use write relabeling to drop noisy or unnecessary series.

## Thanos

- Use object storage for long-term blocks.
- Confirm Sidecar can upload blocks.
- Run Compactor for compaction, downsampling, and retention.
- Restrict object storage permissions.
- Monitor Store Gateway and Query availability.

## Cardinality

- Avoid user ID, request ID, order ID, and raw URL labels.
- Review high-cardinality metrics before long-term storage.
- Drop unnecessary runtime metrics before Remote Write when possible.
