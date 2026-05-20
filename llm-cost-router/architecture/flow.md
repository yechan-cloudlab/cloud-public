# LLM Router Flow

```text
Client
  ↓
API Gateway or ALB
  ↓
Router
  ├─ simple summary / simple classification → Ollama
  └─ code generation / complex reasoning    → Bedrock Claude
```

## Design Notes

- 라우터는 요청 내용을 보고 모델을 고릅니다.
- 처음에는 규칙 기반 라우팅으로 시작하는 것이 좋습니다.
- 운영 데이터가 쌓이면 LLM 기반 classifier나 embedding 기반 classifier로 확장할 수 있습니다.
- 긴 프롬프트와 스트리밍 응답은 별도 설계가 필요합니다.

## Why not Lambda@Edge?

LLM 요청은 본문이 길어질 수 있습니다. Lambda@Edge는 요청 본문 처리에 제한이 있으므로, 이 예제에서는 API Gateway 또는 ALB 뒤의 Lambda/ECS Router를 기본 구조로 봅니다.

## Sample Runtime Choices

| Router 위치 | 장점 | 주의점 |
|---|---|---|
| Lambda | 가볍고 시작하기 쉬움 | 긴 처리 시간, 스트리밍, cold start 고려 |
| ECS | 장기 실행과 커넥션 관리에 유리 | 서비스 운영 부담 증가 |
| Local script | 학습과 검증에 쉬움 | 운영용 API로는 부적합 |
