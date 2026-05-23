# 503 NR: no route

Typical checks:

- VirtualService host matches the request host.
- Gateway is referenced by the VirtualService.
- Gateway selector matches the ingress gateway labels.
- DestinationRule subset names match VirtualService routes.
- Service port names follow Istio protocol naming such as `http`.
