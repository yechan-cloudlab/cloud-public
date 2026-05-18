# yechan-cloudlab / cloud-public

Practical cloud examples that accompany the [tistory-cloud blog](https://tistory-cloud.tistory.com/).

This repository is built around one idea:

> **The blog explains the why. This repository gives you the files to try the how.**

Each topic lives in its own folder with deployable examples, notes, and direct links back to the related article.

## Topics

| Topic | What you can learn | Blog |
| --- | --- | --- |
| `keycloak/helm-practical-guide/` | Deploy Keycloak with Helm, RDS, TLS, and realm configuration | [Install guide](https://tistory-cloud.tistory.com/entry/Keycloak-Helm-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95-valuesyaml%EB%A1%9C-RDS-%EC%9D%B8%EC%A6%9D%EC%84%9C-Realm%EA%B9%8C%EC%A7%80-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0) · [Operations guide](https://tistory-cloud.tistory.com/entry/Keycloak-%EC%9A%B4%EC%98%81-%EB%B0%A9%EB%B2%95-%EC%9D%B8%EC%A6%9D%EC%84%9C-%EA%B0%B1%EC%8B%A0-%EB%B0%B1%EC%97%85-%EC%97%85%EA%B7%B8%EB%A0%88%EC%9D%B4%EB%93%9C-%EC%9E%A5%EC%95%A0-%EB%8C%80%EC%9D%91-%EC%B2%B4%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%8A%B8) |
| `private-eks-helm-github-actions/` | Deploy Helm charts to a private EKS cluster with a self-hosted runner | [Private EKS deployment guide](https://tistory-cloud.tistory.com/entry/GitHub-Actions%EB%A1%9C-Private-EKS%EC%97%90-Helm-%EB%B0%B0%ED%8F%AC-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-self-hosted-runner-%EA%B5%AC%EC%84%B1%EB%B6%80%ED%84%B0-%EB%B0%B0%ED%8F%AC%EA%B9%8C%EC%A7%80) |
| `cloudwatch-application-signals-eks/` | Observe EKS application latency, errors, and dependencies with Application Signals | [Application Signals guide](https://tistory-cloud.tistory.com/entry/CloudWatch-Application-Signals-%EC%82%AC%EC%9A%A9%EB%B2%95-EKS-%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EC%A7%80%EC%97%B0%EA%B3%BC-%EC%98%A4%EB%A5%98%EB%A5%BC-%EC%9E%90%EB%8F%99%EC%9C%BC%EB%A1%9C-%ED%99%95%EC%9D%B8%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95) |
| `route53-resolver-query-log-analyzer/` | Analyze Resolver query logs with Athena and generate suspicious-domain reports | [Route 53 Resolver DNS](https://tistory-cloud.tistory.com/entry/%EC%9A%B0%EB%A6%AC-%EC%84%9C%EB%B2%84%EA%B0%80-%EC%88%98%EC%83%81%ED%95%9C-%EB%8F%84%EB%A9%94%EC%9D%B8%EC%9D%84-%EC%A1%B0%ED%9A%8C%ED%96%88%EB%84%A4-Route-53-Resolver-DNS-%EB%A1%9C%EA%B7%B8-%EB%B6%84%EC%84%9D%EA%B8%B0-%EB%A7%8C%EB%93%A4%EA%B8%B0) |
| `s3-cost-allocation-by-department/` | Explore a sample Terraform design for bucket-level S3 cost allocation by department | [S3 버킷 태그와 Cost Allocation Tag로 부서별 비용 추적하기](https://tistory-cloud.tistory.com/entry/S3-%EB%B9%84%EC%9A%A9%EC%9D%B4-%EC%96%B4%EB%94%94%EC%84%9C-%EB%82%98%EC%98%A4%EB%8A%94%EC%A7%80-%EB%AA%A8%EB%A5%BC-%EB%95%8C-%EB%B2%84%ED%82%B7-%ED%83%9C%EA%B7%B8%EC%99%80-Cost-Allocation-Tag%EB%A1%9C-%EB%B6%80%EC%84%9C%EB%B3%84-%EB%B9%84%EC%9A%A9-%EC%B6%94%EC%A0%81%ED%95%98%EA%B8%B0) |

## How to use this repository

1. Pick a topic folder.
2. Open its README first.
3. Follow the related blog article for the full explanation.
4. Copy the example files, replace placeholders, and adapt them to your own environment.

## Repository policy

- Environment-specific values use `{{PLACEHOLDER}}` notation.
- Secrets, passwords, private keys, and real production endpoints are never committed.
- Files ending with `.example.yaml` are templates for readers to copy and adapt.
- When an upstream Helm chart is used, this repository pins and documents the chart and image versions used in the article.

## Linking convention

Every topic folder should:

1. Link to the related `tistory-cloud` article.
2. Explain what the folder demonstrates.
3. Tell readers what to review before deploying.
4. Keep the examples aligned with the article so the blog and code stay useful together.
