# Sidecar injection not working

Check:

- namespace has `istio-injection=enabled`;
- pods were restarted after labeling the namespace;
- mutating webhook exists and is healthy;
- pod labels do not disable injection;
- namespace is not excluded from injection policy.
