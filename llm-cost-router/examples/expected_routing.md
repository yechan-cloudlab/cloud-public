# Expected Routing

| Request ID | Expected Route | Reason |
|---|---|---|
| simple-summary | Ollama | 짧은 요약 요청은 로컬 LLM으로 처리 |
| simple-classification | Ollama | 단순 분류는 로컬 LLM으로 처리 |
| code-generation | Bedrock Claude | 코드 생성은 품질이 중요함 |
| architecture-review | Bedrock Claude | 긴 아키텍처 분석은 복잡한 추론에 가까움 |

이 결과는 `router/routing_rules.json` 기준입니다. 실제 운영에서는 요청 로그를 보고 규칙을 계속 조정해야 합니다.
