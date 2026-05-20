# Cost Simulation

이 문서는 비용 계산 방식을 보여주는 샘플입니다. 실제 비용은 모델, 리전, 입력/출력 토큰, Ollama 서버 운영 방식에 따라 달라집니다.

## Scenario

```text
월 요청 수: 100,000건
쉬운 요청: 80%
어려운 요청: 20%
```

## All Claude

모든 요청을 Bedrock Claude로 보내면 전체 요청이 토큰 기반 과금 대상이 됩니다.

```text
100,000 requests → Bedrock Claude
```

## Hybrid Router

```text
80,000 requests → Ollama
20,000 requests → Bedrock Claude
```

Ollama는 외부 API 토큰 과금은 없지만, EC2/GPU/CPU/전력/운영 비용은 존재합니다. 따라서 “무료”가 아니라 “토큰 API 과금이 없는 로컬 처리”로 보는 것이 정확합니다.

## Simple Formula

```text
All Claude Cost = total_requests × avg_tokens × Claude_token_price
Hybrid Cost = Ollama_infra_cost + (claude_requests × avg_tokens × Claude_token_price)
```

## 운영 전 확인할 것

- Ollama 서버 운영 비용
- Bedrock 입력/출력 토큰 비용
- 라우팅 실패 시 fallback 비용
- 품질 저하로 인한 재시도 비용
- 로그와 모니터링 비용
- 쉬운 요청 비율이 실제로 충분히 높은지

## 주의

이 문서는 “비용이 줄어드는 구조”를 설명하기 위한 샘플입니다. 특정 절감률을 보장하지 않습니다.
