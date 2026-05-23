# mTLS security examples

This folder contains namespace-level examples:

- `peerauthentication-strict.yaml`
- `destinationrule-mtls.yaml`
- `authorizationpolicy-allow-only-frontend.yaml`

Apply these only after confirming sidecar injection is working.

## Recommended order

1. Verify workloads have `istio-proxy`.
2. Test traffic without mTLS STRICT.
3. Apply `PeerAuthentication` in a test namespace.
4. Apply `AuthorizationPolicy`.
5. Watch for 403, 503, and mTLS handshake failures.
