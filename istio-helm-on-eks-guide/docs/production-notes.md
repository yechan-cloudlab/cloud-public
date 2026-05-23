# Production notes

Review before production use:

- chart version pinning
- Helm release ownership
- multi-AZ gateway replicas
- HPA and PodDisruptionBudget
- ingress gateway annotations for EKS load balancers
- TLS certificate management
- mTLS rollout strategy
- AuthorizationPolicy review
- dashboard and alert ownership
- rollback plan

This repository is a learning sample. Treat it as a starting point, not an approved production baseline.
