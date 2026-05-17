# cloud-public

Public examples and reference files for the [tistory-cloud blog](https://tistory-cloud.tistory.com/).

This repository collects practical deployment examples that accompany blog posts.
Each topic lives in its own folder so readers can inspect the files, clone the repository, and reproduce the guide from the same source.

## Topics

- `keycloak/helm-practical-guide/` - deployable wrapper chart for installing Keycloak with Helm, RDS, TLS, and realm configuration examples

## Repository policy

- Example files use `{{PLACEHOLDER}}` values where environment-specific data is required.
- Secrets, passwords, private keys, and real production endpoints are never committed.
- Files ending with `.example.yaml` are templates for readers to copy and adapt before deployment.
- When an upstream Helm chart is used, this repository pins the dependency and documents the chart and image versions used in the article.
