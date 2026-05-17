# Troubleshooting

## No data appears

- Confirm the add-on is active.
- Confirm the workload runtime is supported.
- Confirm the workload was restarted after instrumentation was enabled.
- Review existing OpenTelemetry configuration for conflicts.

## Metrics appear but service map is incomplete

- Check whether the full request path is instrumented.
- Confirm dependencies are generating traces.
