# Secrets and OIDC

## Required GitHub secrets

- `AWS_ROLE_TO_ASSUME`
- `EKS_CLUSTER_NAME`

## OIDC guidance

Prefer GitHub OIDC role assumption over long-lived AWS access keys.
Restrict trust conditions by repository, branch, and environment.
