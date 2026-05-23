# Troubleshooting flow

Recommended order:

1. `istioctl analyze`
2. `istioctl proxy-status`
3. check sidecar injection
4. check Gateway / VirtualService / DestinationRule
5. check PeerAuthentication / AuthorizationPolicy
6. inspect Envoy access logs
7. use Kiali and Prometheus to narrow the failing edge
