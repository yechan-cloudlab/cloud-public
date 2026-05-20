# Blog Outline Mapping

이 저장소는 아래 블로그 글을 보조하기 위한 예제입니다.

## 확정 제목

```text
Ollama + Bedrock 비용 최적화:
쉬운 요청은 로컬 LLM, 어려운 요청은 Claude로 보내기
```

## 섹션 구성

```text
SECTION 01. 왜 모든 LLM 요청을 Claude로 보내면 비용이 커지는가
SECTION 02. Ollama와 Bedrock Claude의 역할을 나누는 기준
SECTION 03. LLM 라우터 아키텍처란 무엇인가
SECTION 04. 쉬운 요청과 어려운 요청을 어떻게 구분할까
SECTION 05. 규칙 기반 라우팅부터 시작하기
SECTION 06. LangChain Router로 요청 난이도 분류하기
SECTION 07. “요약”은 Ollama, “코드/추론”은 Claude로 보내기
SECTION 08. API Gateway + Lambda Router + Bedrock 구조
SECTION 09. Ollama 서버는 어디에 둘 것인가: 로컬, EC2, ECS
SECTION 10. 스트리밍 응답과 긴 프롬프트 처리 시 주의사항
SECTION 11. 샘플 비용 계산: 모든 요청 Claude vs 하이브리드 라우팅
SECTION 12. LLM 비용 최적화 운영 체크리스트
SUMMARY. 핵심 요약
CONCLUSION. 마무리
```

## 핵심 메시지

모든 요청에 최고 성능 모델을 쓰는 것은 비효율적입니다. 쉬운 요청은 Ollama 같은 로컬 LLM으로 처리하고, 어려운 요청만 Bedrock Claude로 보내면 비용과 품질의 균형을 잡을 수 있습니다.
