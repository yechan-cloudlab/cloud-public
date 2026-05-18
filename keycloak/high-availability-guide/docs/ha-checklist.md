# Keycloak HA Checklist

## Before deployment

- [ ] At least 2 replicas are configured.
- [ ] Keycloak Pods can be scheduled across more than one node.
- [ ] Topology spread or anti-affinity is defined.
- [ ] External database is not a single-AZ deployment.
- [ ] Readiness, liveness, and startup probes are reviewed.
- [ ] PodDisruptionBudget is configured.
- [ ] Ingress or load balancer health checks match the application behavior.
- [ ] Cache transport ports and network policy assumptions are reviewed.

## During deployment

- [ ] Rolling update keeps at least one healthy Pod available.
- [ ] New Pods become Ready before old Pods terminate.
- [ ] Login and token issuance are tested during rollout.

## After deployment

- [ ] Delete one Pod and confirm login remains available.
- [ ] Drain one node and confirm traffic continues.
- [ ] Review database failover behavior separately.
- [ ] Confirm monitoring and alerting cover authentication availability.
