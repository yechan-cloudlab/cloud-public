# ☁️ yechan-cloudlab / cloud-public

> **The blog explains the why. This repository gives you the files to try the how.**

[tistory-cloud 블로그](https://tistory-cloud.tistory.com/)와 함께하는 실전 클라우드 예제 모음입니다.  
각 폴더는 블로그 아티클과 1:1로 연결되며, 바로 배포하거나 참고할 수 있는 예제 파일을 제공합니다.

![GitHub last commit](https://img.shields.io/github/last-commit/yechan-cloudlab/cloud-public)
![GitHub repo size](https://img.shields.io/github/repo-size/yechan-cloudlab/cloud-public)
[![Blog](https://img.shields.io/badge/Blog-tistory--cloud-orange)](https://tistory-cloud.tistory.com/)

---

## 📚 Topics

| 폴더 | 설명 | 블로그 |
| --- | --- | --- |
| `keycloak/helm-practical-guide/` | Helm, RDS, TLS, Realm 설정으로 Keycloak 배포 | [설치 가이드](https://tistory-cloud.tistory.com/entry/Keycloak-Helm-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95-valuesyaml%EB%A1%9C-RDS-%EC%9D%B8%EC%A6%9D%EC%84%9C-Realm%EA%B9%8C%EC%A7%80-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0) · [운영 가이드](https://tistory-cloud.tistory.com/entry/Keycloak-%EC%9A%B4%EC%98%81-%EB%B0%A9%EB%B2%95-%EC%9D%B8%EC%A6%9D%EC%84%9C-%EA%B0%B1%EC%8B%A0-%EB%B0%B1%EC%97%85-%EC%97%85%EA%B7%B8%EB%A0%88%EC%9D%B4%EB%93%9C-%EC%9E%A5%EC%95%A0-%EB%8C%80%EC%9D%91-%EC%B2%B4%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%8A%B8) |
| `private-eks-helm-github-actions/` | Self-hosted runner로 Private EKS에 Helm 배포 자동화 | [배포 가이드](https://tistory-cloud.tistory.com/entry/GitHub-Actions%EB%A1%9C-Private-EKS%EC%97%90-Helm-%EB%B0%B0%ED%8F%AC-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-self-hosted-runner-%EA%B5%AC%EC%84%B1%EB%B6%80%ED%84%B0-%EB%B0%B0%ED%8F%AC%EA%B9%8C%EC%A7%80) |
| `cloudwatch-application-signals-eks/` | Application Signals로 EKS 애플리케이션 지연·오류·의존성 관찰 | [사용 가이드](https://tistory-cloud.tistory.com/entry/CloudWatch-Application-Signals-%EC%82%AC%EC%9A%A9%EB%B2%95-EKS-%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EC%A7%80%EC%97%B0%EA%B3%BC-%EC%98%A4%EB%A5%98%EB%A5%BC-%EC%9E%90%EB%8F%99%EC%9C%BC%EB%A1%9C-%ED%99%95%EC%9D%B8%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95) |
| `route53-resolver-query-log-analyzer/` | Athena로 Resolver 쿼리 로그 분석 및 의심 도메인 리포트 생성 | 🔜 Coming soon |
| `s3-cost-allocation-by-department/` | 부서별 S3 비용 귀속을 위한 Terraform 샘플 | 🔜 Coming soon |

---

## 🚀 사용 방법

1. 원하는 **Topic 폴더**를 선택합니다.
2. 폴더 안의 **README를 먼저** 읽습니다.
3. 연결된 **블로그 아티클**에서 전체 맥락을 확인합니다.
4. 예제 파일을 복사하고, 플레이스홀더를 환경에 맞게 교체합니다.

---

## 📋 저장소 정책

- 환경별 값은 `{{PLACEHOLDER}}` 표기를 사용합니다.
- 시크릿, 비밀번호, 개인 키, 실제 프로덕션 엔드포인트는 커밋하지 않습니다.
- `.example.yaml`로 끝나는 파일은 독자가 복사해 수정하는 템플릿입니다.
- Helm 차트를 사용하는 경우, 아티클에서 사용한 차트 및 이미지 버전을 명시합니다.

---

## 🔗 링크 규칙

각 Topic 폴더는 아래 항목을 포함해야 합니다.

1. 관련 `tistory-cloud` 아티클 링크
2. 폴더가 보여주는 내용 설명
3. 배포 전 검토 사항
4. 블로그와 코드가 함께 유용하도록 예제를 아티클과 일치시킵니다.
