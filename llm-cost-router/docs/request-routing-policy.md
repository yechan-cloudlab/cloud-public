# Request Routing Policy

이 샘플은 처음부터 복잡한 LLM classifier를 사용하지 않고, 규칙 기반 라우팅으로 시작합니다.

## 기본 정책

| 요청 유형 | 기본 라우트 | 이유 |
|---|---|---|
| 짧은 요약 | Ollama | 품질 요구가 비교적 낮고 반복 호출이 많음 |
| 단순 분류 | Ollama | 정해진 카테고리 분류는 로컬 모델로도 실험 가능 |
| 코드 생성 | Bedrock Claude | 정확성과 추론 품질이 중요함 |
| 복잡한 아키텍처 분석 | Bedrock Claude | 긴 문맥과 복합 추론이 필요함 |
| 애매한 요청 | Bedrock Claude | fallback은 품질 우선 |

## 운영에서 조정할 것

- 실제 요청 로그를 보고 `routing_rules.json`을 계속 조정합니다.
- Ollama 품질이 낮은 작업은 Claude로 승격합니다.
- Claude 비용이 큰 작업은 프롬프트 길이와 fallback 비율을 줄입니다.
- 실패한 요청은 별도 로그로 남겨 라우팅 정책을 개선합니다.
