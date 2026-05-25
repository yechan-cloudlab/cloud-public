# ☁️ yechan-cloudlab / cloud-public

> **The blog explains the why. This repository gives you the files to try the how.**

Practical cloud examples that accompany the [tistory-cloud blog](https://tistory-cloud.tistory.com/).  
Each folder maps 1:1 to a blog article and provides deployable example files you can reference or adapt.

[tistory-cloud 블로그](https://tistory-cloud.tistory.com/)와 함께하는 실전 클라우드 예제 모음입니다.  
각 폴더는 블로그 아티클과 1:1로 연결되며, 바로 배포하거나 참고할 수 있는 예제 파일을 제공합니다.

![GitHub last commit](https://img.shields.io/github/last-commit/yechan-cloudlab/cloud-public)
![GitHub repo size](https://img.shields.io/github/repo-size/yechan-cloudlab/cloud-public)
![GitHub stars](https://img.shields.io/github/stars/yechan-cloudlab/cloud-public?style=social)
[![Blog](https://img.shields.io/badge/Blog-tistory--cloud-orange)](https://tistory-cloud.tistory.com/)

---

## 📚 Topics

| Folder | Description | 설명 | Blog |
| --- | --- | --- | --- |
| `keycloak/helm-practical-guide/` | Deploy Keycloak with Helm, RDS, TLS, Realm | Helm, RDS, TLS, Realm 설정으로 Keycloak 배포 | [설치 가이드](https://tistory-cloud.tistory.com/entry/Keycloak-Helm-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95-valuesyaml%EB%A1%9C-RDS-%EC%9D%B8%EC%A6%9D%EC%84%9C-Realm%EA%B9%8C%EC%A7%80-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0) · [운영 가이드](https://tistory-cloud.tistory.com/entry/Keycloak-%EC%9A%B4%EC%98%81-%EB%B0%A9%EB%B2%95-%EC%9D%B8%EC%A6%9D%EC%84%9C-%EA%B0%B1%EC%8B%A0-%EB%B0%B1%EC%97%85-%EC%97%85%EA%B7%B8%EB%A0%88%EC%9D%B4%EB%93%9C-%EC%9E%A5%EC%95%A0-%EB%8C%80%EC%9D%91-%EC%B2%B4%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%8A%B8) |
| `keycloak/high-availability-guide/` | Single-cluster HA design for Keycloak on EKS | EKS에서 Keycloak single-cluster HA 설계 샘플 | [이중화 가이드](https://tistory-cloud.tistory.com/entry/Keycloak-%EC%9D%B4%EC%A4%91%ED%99%94-%EA%B5%AC%EC%84%B1-%EB%B0%A9%EB%B2%95-EKS%EC%97%90%EC%84%9C-Pod-AZ-RDS%EA%B9%8C%EC%A7%80-%EC%96%B4%EB%94%94%EB%A5%BC-%EC%9D%B4%EC%A4%91%ED%99%94%ED%95%B4%EC%95%BC-%ED%95%98%EB%8A%94%EA%B0%80) |
| `keycloak-mcp-readonly-server/` | Readonly MCP server wrapping Keycloak Admin API | Keycloak Admin API를 읽기 전용 MCP Tool로 감싼 TypeScript 샘플 | [1편](https://tistory-cloud.tistory.com/entry/Keycloak-MCP%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-AI-Agent%EB%A1%9C-%EC%9D%B8%EC%A6%9D-%EC%84%A4%EC%A0%95%EC%9D%84-%EC%A0%90%EA%B2%80%ED%95%98%EB%8A%94-%EC%9D%BD%EA%B8%B0-%EC%A0%84%EC%9A%A9-%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0) · [2편](https://tistory-cloud.tistory.com/entry/Keycloak-MCP-%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0-Realm-Client-User-%EC%A1%B0%ED%9A%8C-Tool%EC%9D%84-TypeScript%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0) · [3편](https://tistory-cloud.tistory.com/entry/Keycloak-MCP-%EB%B3%B4%EC%95%88-%EC%9A%B4%EC%98%81-%EA%B0%80%EC%9D%B4%EB%93%9C-AI-Agent%EC%97%90%EA%B2%8C-%EC%9D%B8%EC%A6%9D-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%84-%EC%96%B4%EB%94%94%EA%B9%8C%EC%A7%80-%EB%B3%B4%EC%97%AC%EC%A4%84-%EA%B2%83%EC%9D%B8%EA%B0%80) |
| `keycloak-mcp-admin-automation/` | MCP automation for Keycloak user/role management | Claude/Cursor에서 Keycloak 사용자 생성, Role 부여, 검증, 롤백을 실습하는 MCP 자동화 샘플 | [자동화 실전](https://tistory-cloud.tistory.com/entry/Claude%ED%95%9C%ED%85%8C-%E2%80%9C%ED%82%A4%ED%81%B4%EB%9D%BD-%EC%9C%A0%EC%A0%80-100%EB%AA%85-%EC%83%9D%EC%84%B1%ED%95%B4%EC%A4%98%E2%80%9D-%ED%96%88%EB%8D%94%EB%8B%88-10%EC%B4%88-%EB%A7%8C%EC%97%90-%EB%81%9D%EB%82%AC%EB%8B%A4-Keycloak-MCP-%EC%9E%90%EB%8F%99%ED%99%94-%EC%8B%A4%EC%A0%84) |
| `private-eks-helm-github-actions/` | Automate Helm deployments to private EKS | Self-hosted runner로 Private EKS에 Helm 배포 자동화 | [배포 가이드](https://tistory-cloud.tistory.com/entry/GitHub-Actions%EB%A1%9C-Private-EKS%EC%97%90-Helm-%EB%B0%B0%ED%8F%AC-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-self-hosted-runner-%EA%B5%AC%EC%84%B1%EB%B6%80%ED%84%B0-%EB%B0%B0%ED%8F%AC%EA%B9%8C%EC%A7%80) |
| `cloudwatch-application-signals-eks/` | Observe EKS app latency, errors, and dependencies | Application Signals로 EKS 애플리케이션 지연·오류·의존성 관찰 | [사용 가이드](https://tistory-cloud.tistory.com/entry/CloudWatch-Application-Signals-%EC%82%AC%EC%9A%A9%EB%B2%95-EKS-%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EC%A7%80%EC%97%B0%EA%B3%BC-%EC%98%A4%EB%A5%98%EB%A5%BC-%EC%9E%90%EB%8F%99%EC%9C%BC%EB%A1%9C-%ED%99%95%EC%9D%B8%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95) |
| `route53-resolver-query-log-analyzer/` | Analyze Resolver query logs and generate suspicious-domain reports | Athena로 Resolver 쿼리 로그 분석 및 의심 도메인 리포트 생성 | [분석기 만들기](https://tistory-cloud.tistory.com/entry/%EC%9A%B0%EB%A6%AC-%EC%84%9C%EB%B2%84%EA%B0%80-%EC%88%98%EC%83%81%ED%95%9C-%EB%8F%84%EB%A9%94%EC%9D%B8%EC%9D%84-%EC%A1%B0%ED%9A%8C%ED%96%88%EB%84%A4-Route-53-Resolver-DNS-%EB%A1%9C%EA%B7%B8-%EB%B6%84%EC%84%9D%EA%B8%B0-%EB%A7%8C%EB%93%A4%EA%B8%B0) |
| `s3-cost-allocation-by-department/` | Terraform sample for S3 cost allocation by department | 부서별 S3 비용 귀속을 위한 Terraform 샘플 | [비용 추적 가이드](https://tistory-cloud.tistory.com/entry/S3-%EB%B9%84%EC%9A%A9%EC%9D%B4-%EC%96%B4%EB%94%94%EC%84%9C-%EB%82%98%EC%98%A4%EB%8A%94%EC%A7%80-%EB%AA%A8%EB%A5%BC-%EB%95%8C-%EB%B2%84%ED%82%B7-%ED%83%9C%EA%B7%B8%EC%99%80-Cost-Allocation-Tag%EB%A1%9C-%EB%B6%80%EC%84%9C%EB%B3%84-%EB%B9%84%EC%9A%A9-%EC%B6%94%EC%A0%81%ED%95%98%EA%B8%B0) |
| `ollama/series-examples/` | Ollama 4-part series practical examples | Ollama 4부작 실습 예제 모음 | [1편](https://tistory-cloud.tistory.com/entry/Ollama%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-%EB%82%B4-PC%EC%97%90%EC%84%9C-LLM%EC%9D%84-%EC%8B%A4%ED%96%89%ED%95%98%EB%8A%94-%EA%B0%80%EC%9E%A5-%EC%89%AC%EC%9A%B4-%EB%B0%A9%EB%B2%95) · [2편](https://tistory-cloud.tistory.com/entry/Ollama-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%84%A4%EC%B9%98%EB%B6%80%ED%84%B0-%EB%AA%A8%EB%8D%B8-%EC%8B%A4%ED%96%89-API-%ED%98%B8%EC%B6%9C%EA%B9%8C%EC%A7%80) · [3편](https://tistory-cloud.tistory.com/entry/Ollama%EB%A5%BC-%EA%B0%9C%EB%B0%9C%EC%97%90-%EB%B6%99%EC%9D%B4%EB%8A%94-%EB%B0%A9%EB%B2%95-Python-JavaScript-Modelfile%EA%B9%8C%EC%A7%80) · [4편](https://tistory-cloud.tistory.com/entry/Ollama-Structured-Outputs-%EC%82%AC%EC%9A%A9%EB%B2%95-%EB%A1%9C%EC%BB%AC-LLM-%EC%9D%91%EB%8B%B5%EC%9D%84-JSON%EC%9C%BC%EB%A1%9C-%EA%B3%A0%EC%A0%95%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95) |
| `llm-cost-router/` | LLM request router using Ollama and Bedrock Claude | Ollama와 Bedrock Claude를 함께 쓰는 LLM 비용 라우터 샘플 | [비용 최적화 가이드](https://tistory-cloud.tistory.com/entry/Ollama-Bedrock-%EB%B9%84%EC%9A%A9-%EC%B5%9C%EC%A0%81%ED%99%94-%EC%89%AC%EC%9A%B4-%EC%9A%94%EC%B2%AD%EC%9D%80-%EB%A1%9C%EC%BB%AC-LLM-%EC%96%B4%EB%A0%A4%EC%9A%B4-%EC%9A%94%EC%B2%AD%EC%9D%80-Claude%EB%A1%9C-%EB%B3%B4%EB%82%B4%EA%B8%B0#s1) |
| `bedrock-cost-compare/` | Amazon Bedrock Claude model cost comparison and routing strategy | Amazon Bedrock Claude 모델 비용 비교 및 라우팅 전략 샘플 | [비용 라우팅 가이드](https://tistory-cloud.tistory.com/entry/Claude-Opus%EB%A7%8C-%EC%93%B0%EB%A9%B4-Bedrock-%EB%B9%84%EC%9A%A9%EC%9D%B4-%ED%84%B0%EC%A7%91%EB%8B%88%EB%8B%A4-Haiku%C2%B7Sonnet%C2%B7Opus-%EB%9D%BC%EC%9A%B0%ED%8C%85-%EC%A0%84%EB%9E%B5) |
| `vllm-on-ecs/` | Deploy a vLLM OpenAI-compatible API server on ECS GPU EC2 | vLLM OpenAI 호환 API 서버를 ECS GPU EC2 클러스터에 배포하는 샘플 | [운영 가이드](https://tistory-cloud.tistory.com/entry/vLLM%EC%9C%BC%EB%A1%9C-OpenAI-%ED%98%B8%ED%99%98-API-%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0-ECS-GPU-EC2-%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0-%EC%9A%B4%EC%98%81-%EB%B0%A9%EB%B2%95) |
| `perplexity-sonar-api-examples/` | Build source-aware AI answers with the Perplexity Sonar API | 인용 출처가 포함된 웹 기반 AI 답변을 만드는 Perplexity Sonar API 예제 | [Sonar API 가이드](https://tistory-cloud.tistory.com/entry/Perplexity-Sonar-API-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%8B%A4%EC%8B%9C%EA%B0%84-%EC%9B%B9-%EA%B2%80%EC%83%89%EC%9D%B4-%EA%B0%80%EB%8A%A5%ED%95%9C-AI-%EB%8B%B5%EB%B3%80-API-%EB%A7%8C%EB%93%A4%EA%B8%B0) |
| `eks-manifest-auditor/` | Local Kubernetes/EKS manifest static analysis CLI | AWS 접속 없이 Kubernetes/EKS YAML의 보안, 리소스, Service, Ingress, IRSA 문제를 검사하는 Python CLI | [글 보기](https://tistory-cloud.tistory.com/entry/EKS-Manifest-%EA%B2%80%EC%82%AC-%EC%9E%90%EB%8F%99%ED%99%94-Kubernetes-YAML-%EB%B3%B4%EC%95%88%C2%B7%EB%A6%AC%EC%86%8C%EC%8A%A4-%EB%AC%B8%EC%A0%9C%EB%A5%BC-%EB%A1%9C%EC%BB%AC%EC%97%90%EC%84%9C-%EC%B0%BE%EB%8A%94-Python-CLI-%EB%A7%8C%EB%93%A4%EA%B8%B0) |
| `istio-helm-on-eks-guide/` | Install and operate Istio on EKS with Helm, traffic routing, mTLS, observability, and troubleshooting | Helm Chart로 Istio base, istiod, gateway를 설치하고 라우팅, mTLS, 관측성, 트러블슈팅을 실습하는 샘플 | [1편](https://tistory-cloud.tistory.com/entry/Istio%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-Kubernetes-%EC%84%9C%EB%B9%84%EC%8A%A4-%EB%A9%94%EC%8B%9C-%EA%B5%AC%EC%84%B1%EC%9A%94%EC%86%8C%EC%99%80-%ED%8A%B8%EB%9E%98%ED%94%BD-%ED%9D%90%EB%A6%84-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0) · [2편](https://tistory-cloud.tistory.com/entry/Istio-Helm-Chart-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95-EKS%EC%97%90%EC%84%9C-base-istiod-gateway-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0) · [3편](https://tistory-cloud.tistory.com/entry/Istio-Canary-%EB%B0%B0%ED%8F%AC-%EB%B0%A9%EB%B2%95-VirtualService%EC%99%80-DestinationRule%EB%A1%9C-%ED%8A%B8%EB%9E%98%ED%94%BD-%EB%82%98%EB%88%84%EA%B8%B0) · [4편](https://tistory-cloud.tistory.com/entry/Istio-mTLS-%EC%84%A4%EC%A0%95-%EB%B0%A9%EB%B2%95-PeerAuthentication%EA%B3%BC-AuthorizationPolicy%EB%A1%9C-%EC%84%9C%EB%B9%84%EC%8A%A4-%EA%B0%84-%ED%86%B5%EC%8B%A0-%EB%B3%B4%ED%98%B8%ED%95%98%EA%B8%B0) · [5편](https://tistory-cloud.tistory.com/entry/Istio-%EA%B4%80%EC%B8%A1%EC%84%B1-%EC%9A%B4%EC%98%81-%EB%B0%A9%EB%B2%95-Prometheus-Grafana-Kiali%EB%A1%9C-%EC%84%9C%EB%B9%84%EC%8A%A4-%EB%A9%94%EC%8B%9C-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0) · [6편](https://tistory-cloud.tistory.com/entry/Istio-%ED%8A%B8%EB%9F%AC%EB%B8%94%EC%8A%88%ED%8C%85-%EA%B0%80%EC%9D%B4%EB%93%9C-503-%EC%98%A4%EB%A5%98-mTLS-VirtualService-Sidecar-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0%ED%95%98%EA%B8%B0) |

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
