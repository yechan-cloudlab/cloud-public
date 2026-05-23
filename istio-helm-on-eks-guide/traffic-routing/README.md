# Traffic routing examples

Main resources:

- `gateway.yaml`
- `destinationrule.yaml`
- `virtualservice-canary.yaml`
- `virtualservice-header.yaml`

## Canary routing

```bash
kubectl apply -f traffic-routing/gateway.yaml
kubectl apply -f traffic-routing/destinationrule.yaml
kubectl apply -f traffic-routing/virtualservice-canary.yaml
```

## Header-based routing

```bash
kubectl apply -f traffic-routing/virtualservice-header.yaml
```

## Gateway selector note

The `Gateway.spec.selector` must match labels on your ingress gateway pods. If you changed Helm values for the gateway labels, update `gateway.yaml`.
