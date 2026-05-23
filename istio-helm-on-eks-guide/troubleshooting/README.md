# Troubleshooting guide

Start with:

```bash
istioctl analyze
istioctl proxy-status
kubectl get pods -A | grep istio
```

Common cases:

- `503-no-route.md`
- `sidecar-injection.md`
- `virtualservice-not-working.md`
- `destinationrule-subset.md`
- `mtls-strict-fail.md`
- `gateway-not-accessible.md`
- `authorizationpolicy-403.md`
- `commands-cheatsheet.md`
