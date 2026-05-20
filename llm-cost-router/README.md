# LLM Cost Router

Ollama와 Amazon Bedrock Claude를 함께 사용하는 LLM 요청 라우터 예제입니다.

> 이 저장소는 블로그 글을 보조하기 위한 **학습용 샘플**입니다. 운영 환경에 그대로 적용하기보다는, 쉬운 요청은 로컬 LLM으로 보내고 어려운 요청은 Claude 같은 고성능 모델로 보내는 구조를 이해하는 용도로 사용하세요.

---

## 📎 관련 아티클

- Ollama + Bedrock 비용 최적화: 쉬운 요청은 로컬 LLM, 어려운 요청은 Claude로 보내기

---

## ✅ 이 예제가 보여주는 것

- LLM 요청을 난이도와 작업 유형에 따라 분기하는 기본 구조
- 쉬운 요약, 단순 분류, 짧은 변환 요청을 Ollama로 보내는 방식
- 코드 생성, 복잡한 추론, 긴 문서 분석 요청을 Bedrock Claude로 보내는 방식
- 규칙 기반 라우팅 JSON 설계
- Python으로 Ollama API와 Bedrock Runtime을 호출하는 최소 예제
- 모든 요청을 Claude로 보냈을 때와 하이브리드 라우팅을 했을 때의 비용 시뮬레이션 관점

---

## ❌ 이 예제가 하지 않는 것

- 운영용 인증, 권한, 속도 제한, API Key 관리를 포함하지 않습니다.
- Terraform 배포 코드를 포함하지 않습니다.
- Lambda@Edge 기반 라우팅은 다루지 않습니다.
- 스트리밍 응답 전체 구현은 다루지 않습니다.
- 실제 비용 절감률을 보장하지 않습니다.

---

## 📁 폴더 구조

```text
architecture/       라우터 흐름 설명
router/             요청 분류와 라우팅 로직
ollama/             Ollama API 호출 클라이언트
bedrock/            Bedrock Claude 호출 클라이언트
examples/           샘플 요청과 예상 라우팅 결과
docs/               블로그 구조, 비용 시뮬레이션, 운영 체크리스트
```

---

## 🧭 블로그 섹션과 예제 파일 매핑

| 블로그 섹션 | 관련 파일 |
|---|---|
| LLM 라우터 아키텍처란 무엇인가 | `architecture/flow.md` |
| 규칙 기반 라우팅부터 시작하기 | `router/routing_rules.json`, `router/classify_request.py` |
| “요약”은 Ollama, “코드/추론”은 Claude | `examples/sample_requests.json`, `examples/expected_routing.md` |
| API Gateway + Lambda Router + Bedrock 구조 | `router/router.py`, `bedrock/claude_client.py` |
| Ollama 서버는 어디에 둘 것인가 | `ollama/ollama_client.py`, `architecture/flow.md` |
| 샘플 비용 계산 | `docs/cost-simulation.md` |
| 운영 체크리스트 | `docs/operation-checklist.md` |

---

## 🚀 빠른 시작

### 1. 의존성을 설치합니다

```bash
pip install -r requirements.txt
```

### 2. 환경 변수 예제를 복사합니다

```bash
cp .env.example .env
```

Windows PowerShell에서는 아래처럼 복사할 수 있습니다.

```powershell
Copy-Item .env.example .env
```

### 3. Ollama를 실행하고 모델을 내려받습니다

```bash
ollama pull gemma3
curl http://localhost:11434
```

### 4. 라우팅 결과만 먼저 확인합니다

이 명령은 Ollama나 Bedrock을 실제 호출하지 않습니다.

```bash
python router/classify_request.py examples/sample_requests.json
```

### 5. dry-run으로 라우터를 실행합니다

```bash
python router/router.py "요약해줘: 쉬운 요청은 Ollama로 보내고 어려운 요청은 Claude로 보낸다." --dry-run
```

### 6. Ollama 실제 호출을 테스트합니다

```bash
python router/router.py "요약해줘: LLM 라우터는 쉬운 요청을 로컬 모델로 보내고 어려운 요청을 Claude로 보낸다."
```

Bedrock Claude 호출을 실제로 사용하려면 AWS 자격 증명, 리전, Bedrock 모델 접근 권한이 필요합니다.

---

## ⚠️ 사용 전 확인

- Ollama가 로컬에서 실행 중이어야 합니다.
- 기본 Ollama URL은 `http://localhost:11434`입니다.
- 샘플 모델명은 `gemma3`입니다.
- Bedrock Claude 호출은 AWS 계정, 리전, 모델 접근 권한이 필요합니다.
- `BEDROCK_MODEL_ID`는 계정과 리전에서 활성화된 모델 ID로 바꿔야 합니다.
- 실제 운영에서는 인증, 로깅, retry, timeout, fallback, rate limit을 반드시 추가하세요.

---

## 🧯 자주 막히는 지점

| 증상 | 확인할 것 |
|---|---|
| Ollama 연결 실패 | `curl http://localhost:11434` 확인 |
| 모델을 찾을 수 없음 | `ollama pull gemma3` 실행 여부 확인 |
| Bedrock 권한 오류 | AWS 자격 증명, 리전, 모델 접근 권한 확인 |
| 비용이 예상보다 큼 | fallback 비율과 Claude 라우팅 비율 확인 |
| 품질이 낮음 | Ollama로 보낸 요청 유형과 라우팅 규칙 재검토 |

---

## 📚 참고 문서

- [Ollama API](https://docs.ollama.com/api)
- [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- [Amazon Bedrock Runtime API](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)
