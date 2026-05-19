# Ollama Structured Outputs Guide

Ollama 4편 글에서 사용하는 Structured Outputs 예제입니다.

> 이 폴더는 로컬 LLM 응답을 자유 텍스트가 아니라, 프로그램이 검증하고 처리할 수 있는 JSON 구조로 받는 방법을 보여주는 학습용 샘플입니다.

---

## 📎 관련 아티클

- [Ollama Structured Outputs 사용법: 로컬 LLM 응답을 JSON으로 고정하는 방법](https://tistory-cloud.tistory.com/entry/Ollama-Structured-Outputs-%EC%82%AC%EC%9A%A9%EB%B2%95-%EB%A1%9C%EC%BB%AC-LLM-%EC%9D%91%EB%8B%B5%EC%9D%84-JSON%EC%9C%BC%EB%A1%9C-%EA%B3%A0%EC%A0%95%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95)

---

## ✅ 이 예제가 보여주는 것

- Ollama Structured Outputs 기본 사용법
- Python Pydantic 모델을 JSON Schema로 변환하는 방법
- JavaScript Zod 스키마를 JSON Schema로 변환하는 방법
- 자연어 문장에서 구조화된 정보를 추출하는 방법
- 고객 문의를 카테고리와 우선순위로 분류하는 방법
- LLM 응답을 다시 검증하는 기본 패턴

---

## 📁 폴더 구조

```text
python/
  extract_pet_info.py
  classify_support_ticket.py
javascript/
  extract_pet_info.js
  classify_support_ticket.js
schemas/
  pet.schema.json
  ticket.schema.json
requirements.txt
package.json
```

---

## 🚀 빠른 시작

### 1. 이 폴더로 이동합니다

```bash
cd cloud-public/ollama/series-examples/structured-outputs-guide
```

### 2. Ollama와 모델을 확인합니다

```bash
curl http://localhost:11434
ollama pull gemma3
```

### 3. Python 의존성을 설치합니다

```bash
pip install -r requirements.txt
```

### 4. Python 예제를 실행합니다

```bash
python python/extract_pet_info.py
python python/classify_support_ticket.py
```

### 5. JavaScript 의존성을 설치합니다

```bash
npm install
```

### 6. JavaScript 예제를 실행합니다

```bash
npm run extract:pet
npm run classify:ticket
```

---

## 🧪 예제 파일 설명

| 파일 | 설명 |
|---|---|
| `python/extract_pet_info.py` | 문장에서 반려동물 정보를 추출하는 Pydantic 예제 |
| `python/classify_support_ticket.py` | 고객 문의를 카테고리와 우선순위로 분류하는 Pydantic 예제 |
| `javascript/extract_pet_info.js` | 문장에서 반려동물 정보를 추출하는 Zod 예제 |
| `javascript/classify_support_ticket.js` | 고객 문의를 분류하는 Zod 예제 |
| `schemas/pet.schema.json` | 반려동물 정보 추출용 JSON Schema 참고 파일 |
| `schemas/ticket.schema.json` | 고객 문의 분류용 JSON Schema 참고 파일 |

---

## 🧭 실행 결과를 어떻게 보면 되나

예제의 목표는 예쁜 문장을 출력하는 것이 아닙니다. 아래처럼 프로그램이 바로 사용할 수 있는 구조화된 값을 얻는 것입니다.

```json
{
  "pets": [
    {"name": "Bori", "animal": "dog", "age": 3},
    {"name": "Nabi", "animal": "cat", "age": 2}
  ]
}
```

또는 고객 문의를 아래처럼 분류합니다.

```json
{
  "category": "billing",
  "priority": "high",
  "summary": "Customer was charged twice and requests a refund."
}
```

실제 출력은 모델 상태와 환경에 따라 조금 달라질 수 있습니다. 그래서 예제는 출력값을 그대로 믿지 않고 Pydantic 또는 Zod로 다시 검증합니다.

---

## ⚠️ 사용 전 확인

- Ollama가 로컬에서 실행 중이어야 합니다.
- 예제 모델은 `gemma3`를 기준으로 작성했습니다.
- Structured Outputs 예제는 낮은 temperature를 사용합니다.
- 모델 응답은 반드시 검증한 뒤 다음 로직으로 넘기는 것이 좋습니다.
- 실제 서비스에서는 파싱 실패, 검증 실패, 의미상 오분류를 모두 처리해야 합니다.

---

## 🧯 자주 막히는 지점

| 증상 | 확인할 것 |
|---|---|
| Python에서 `pydantic` 모듈을 찾지 못함 | `pip install -r requirements.txt` 실행 여부 확인 |
| JavaScript에서 `zod` 모듈을 찾지 못함 | `npm install` 실행 여부 확인 |
| JSON 파싱 실패 | 모델 응답에 설명 문장이 섞였는지 확인 |
| 스키마 검증 실패 | 필수 필드, 타입, enum 값 확인 |
| 결과가 매번 흔들림 | temperature를 낮게 유지하고 입력 문장을 더 명확히 작성 |

---

## 🧩 실무 적용 아이디어

이 패턴은 아래 작업에 응용할 수 있습니다.

- 고객 문의 분류
- 장애 로그 요약과 심각도 분류
- 이메일에서 주문 정보 추출
- 보안 이벤트에서 위험도와 권장 조치 추출
- 문서에서 날짜, 담당자, 상태 값 추출

---

## 다음 단계

이 예제는 Ollama 4부작의 마지막 실습입니다. 여기까지 따라왔다면 아래 흐름을 모두 경험한 것입니다.

```text
Ollama 이해 → CLI/API 호출 → Python/JavaScript 연동 → JSON 응답 고정
```

이제 이 패턴을 실제 업무 자동화나 내부 도구에 맞게 작게 변형해보면 좋습니다.
