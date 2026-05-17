# cloud-public

Public examples and reference files for the [tistory-cloud blog](https://tistory-cloud.tistory.com/).

This repository collects practical deployment examples that accompany blog posts.
Each topic lives in its own folder so readers can inspect the files, clone the repository, and reproduce the guide from the same source.

## Topics

- `keycloak/helm-practical-guide/` - deployable wrapper chart for installing Keycloak with Helm, RDS, TLS, and realm configuration examples
  - [Blog 1: Keycloak Helm 설치 방법](https://tistory-cloud.tistory.com/entry/Keycloak-Helm-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95-valuesyaml%EB%A1%9C-RDS-%EC%9D%B8%EC%A6%9D%EC%84%9C-Realm%EA%B9%8C%EC%A7%80-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0)
  - [Blog 2: Keycloak 운영 방법](https://tistory-cloud.tistory.com/entry/Keycloak-%EC%9A%B4%EC%98%81-%EB%B0%A9%EB%B2%95-%EC%9D%B8%EC%A6%9D%EC%84%9C-%EA%B0%B1%EC%8B%A0-%EB%B0%B1%EC%97%85-%EC%97%85%EA%B7%B8%EB%A0%88%EC%9D%B4%EB%93%9C-%EC%9E%A5%EC%95%A0-%EB%8C%80%EC%9D%91-%EC%B2%B4%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%8A%B8)
- `private-eks-helm-github-actions/` - GitHub Actions example for deploying a Helm chart to a private EKS cluster through a self-hosted runner
  - [Blog: GitHub Actions로 Private EKS에 Helm 배포 자동화하는 방법](https://tistory-cloud.tistory.com/entry/GitHub-Actions%EB%A1%9C-Private-EKS%EC%97%90-Helm-%EB%B0%B0%ED%8F%AC-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-self-hosted-runner-%EA%B5%AC%EC%84%B1%EB%B6%80%ED%84%B0-%EB%B0%B0%ED%8F%AC%EA%B9%8C%EC%A7%80)

## Repository policy

- Example files use `{{PLACEHOLDER}}` values where environment-specific data is required.
- Secrets, passwords, private keys, and real production endpoints are never committed.
- Files ending with `.example.yaml` are templates for readers to copy and adapt before deployment.
- When an upstream Helm chart is used, this repository pins the dependency and documents the chart and image versions used in the article.

## Linking convention

Every topic folder should make the relationship with the blog explicit:

1. Link back to the `tistory-cloud` blog from the folder README.
2. Add direct post URLs when the related article has been published.
3. Keep the repository examples and the article instructions aligned so readers can move between both without guessing.
