# Istio troubleshooting commands

```bash
istioctl analyze
istioctl proxy-status
istioctl proxy-config routes <pod> -n <namespace>
istioctl proxy-config clusters <pod> -n <namespace>
istioctl proxy-config endpoints <pod> -n <namespace>
kubectl logs <pod> -n <namespace> -c istio-proxy
kubectl describe virtualservice <name> -n <namespace>
kubectl describe destinationrule <name> -n <namespace>
kubectl describe authorizationpolicy <name> -n <namespace>
```
