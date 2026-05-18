# CloudWatch Application Signals on EKS

EKS에서 CloudWatch Application Signals를 활성화하여 애플리케이션 지연, 오류, 의존성을 관찰하는 예제입니다.

---

## 📎 관련 아티클

- [CloudWatch Application Signals 사용법: EKS 애플리케이션 지연과 오류를 자동으로 확인하는 방법](https://tistory-cloud.tistory.com/entry/CloudWatch-Application-Signals-%EC%82%AC%EC%9A%A9%EB%B2%95-EKS-%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EC%A7%80%EC%97%B0%EA%B3%BC-%EC%98%A4%EB%A5%98%EB%A5%BC-%EC%9E%90%EB%8F%99%EC%9C%BC%EB%A1%9C-%ED%99%95%EC%9D%B8%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95)

---

## ✅ 이 예제가 보여주는 것

- Application Signals가 인프라 모니터링을 어떻게 보완하는지
- 자동 계측(auto instrumentation) 활성화 전 확인 사항
- 설치, 검증, 설정 검토 방법

---

## 📁 폴더 구조

| 경로 | 설명 |
| --- | --- |
| `manifests/` | 최소 샘플 워크로드 |
| `commands/` | 설치, 검증, 활성화 명령 모음 |
| `docs/` | 아키텍처, 비교, 메트릭, 체크리스트, 트러블슈팅 |
| `images/` | 아키텍처 다이어그램 |

---

## 🚀 빠른 시작

1. CloudWatch Observability EKS 애드온을 설치합니다.
2. `manifests/`의 샘플 워크로드를 배포합니다.
3. 워크로드 또는 네임스페이스에 모니터링을 활성화합니다.
4. CloudWatch에서 Application Signals 데이터를 확인합니다.

---

## ⚠️ 사용 전 확인

- Application Signals 활성화 전 기존 OpenTelemetry 설정을 먼저 검토하세요.
- EKS에서 Application Signals는 Java, Python, Node.js, .NET 워크로드를 지원합니다.
- EKS Windows 노드에서는 Application Signals가 지원되지 않습니다.
