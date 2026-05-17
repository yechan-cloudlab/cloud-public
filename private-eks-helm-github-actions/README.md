# Private EKS Helm deployment with GitHub Actions

A practical example for deploying Helm charts to a **private Amazon EKS cluster** through a **self-hosted GitHub Actions runner** inside the VPC.

- Related article: [GitHub Actions로 Private EKS에 Helm 배포 자동화하는 방법](https://tistory-cloud.tistory.com/entry/GitHub-Actions%EB%A1%9C-Private-EKS%EC%97%90-Helm-%EB%B0%B0%ED%8F%AC-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-self-hosted-runner-%EA%B5%AC%EC%84%B1%EB%B6%80%ED%84%B0-%EB%B0%B0%ED%8F%AC%EA%B9%8C%EC%A7%80)

## What this example shows

- Why private EKS needs deployment traffic to come from a reachable network path
- How a self-hosted runner can execute GitHub Actions jobs inside the VPC
- How OIDC removes the need for long-lived AWS access keys
- Why Helm validation should run before deployment

## Folder map

| Path | Purpose |
| --- | --- |
| `.github/workflows/deploy-private-eks.yaml` | Deployment workflow |
| `chart/` | Minimal sample Helm chart |
| `values/` | Dev and prod values examples |
| `runner/` | Self-hosted runner notes |
| `docs/` | Architecture, prerequisites, credentials, troubleshooting, checklist |

## Quick start

1. Prepare a private EKS cluster.
2. Place a self-hosted runner in a network that can reach the cluster private endpoint.
3. Configure GitHub OIDC and an IAM role for the workflow.
4. Add these GitHub secrets:
   - `AWS_ROLE_TO_ASSUME`
   - `EKS_CLUSTER_NAME`
5. Run the workflow manually and choose `dev` or `prod`.

## Before you use it

- Confirm the runner can reach the private Kubernetes API endpoint.
- Keep the runner isolated and treat it as trusted deployment infrastructure.
- Review IAM permissions before running the workflow in production.
