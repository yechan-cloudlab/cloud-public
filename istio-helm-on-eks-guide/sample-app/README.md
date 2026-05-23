# Sample app

This folder contains:

- `httpbin-v1`
- `httpbin-v2`
- shared `httpbin` Service
- `frontend` test client with a dedicated ServiceAccount

The `frontend` ServiceAccount is used by the AuthorizationPolicy sample.

## Deploy

```bash
kubectl apply -f sample-app/
```

## Test from inside the mesh

```bash
kubectl exec -n istio-sample deploy/frontend -c curl -- curl -s http://httpbin:8000/get
```
