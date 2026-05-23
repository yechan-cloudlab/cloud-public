# Istio architecture

Istio is commonly explained as two planes:

- Control Plane: `istiod`
- Data Plane: Envoy proxies attached to workloads

Traffic flow:

```text
Client
  -> Istio Gateway
  -> Envoy proxy
  -> Kubernetes Service
  -> Envoy proxy
  -> Application container
```
