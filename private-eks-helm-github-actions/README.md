# Private EKS Helm deployment with GitHub Actions

This example accompanies the [tistory-cloud blog](https://tistory-cloud.tistory.com/) and shows how to deploy a small Helm chart to a private Amazon EKS cluster by running the workflow on a self-hosted runner inside the VPC.

## What this repository demonstrates

- Private EKS requires the deployment command to run from a network path that can reach the private API endpoint.
- A self-hosted runner can execute GitHub Actions jobs from inside the VPC.
- OIDC can be used so the workflow assumes an AWS role without storing long-lived AWS access keys.
- Helm validation should run before deployment.

## Folder structure

- `.github/workflows/deploy-private-eks.yaml` - deployment workflow
- `chart/` - minimal sample Helm chart
- `values/` - dev and prod values examples
- `runner/` - self-hosted runner notes
- `docs/` - architecture, prerequisites, credentials, troubleshooting, checklist

## Quick start

1. Prepare a private EKS cluster.
2. Place a self-hosted runner in a network that can reach the cluster private endpoint.
3. Configure GitHub OIDC and an IAM role for the workflow.
4. Add the required GitHub secrets:
   - `AWS_ROLE_TO_ASSUME`
   - `EKS_CLUSTER_NAME`
5. Run the workflow manually and choose `dev` or `prod`.

## Related blog post

- [tistory-cloud blog](https://tistory-cloud.tistory.com/)
- Related article: `GitHub Actions로 Private EKS에 Helm 배포 자동화하는 방법: self-hosted runner 구성부터 배포까지`
- Add the direct article URL here after the post is published so readers can move from the example code to the full guide in one click.
