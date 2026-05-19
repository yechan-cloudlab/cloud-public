# Ollama Series Examples

Ollama 4부작 시리즈의 실습 예제를 모아둔 저장소입니다.

> 이 저장소는 학습용 샘플입니다. 운영 환경에 그대로 적용하기보다는, 블로그 글을 읽으면서 로컬에서 Ollama 호출 흐름을 이해하는 용도로 사용하세요.

---

## 📎 관련 아티클

| 편 | 아티클 | 예제 폴더 |
|---|---|---|
| 1편 | [Ollama란 무엇인가: 내 PC에서 LLM을 실행하는 가장 쉬운 방법](https://tistory-cloud.tistory.com/entry/Ollama%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-%EB%82%B4-PC%EC%97%90%EC%84%9C-LLM%EC%9D%84-%EC%8B%A4%ED%96%89%ED%95%98%EB%8A%94-%EA%B0%80%EC%9E%A5-%EC%89%AC%EC%9A%B4-%EB%B0%A9%EB%B2%95) | 글 중심, 별도 예제 없음 |
| 2편 | [Ollama 기본 사용법: 설치부터 모델 실행, API 호출까지](https://tistory-cloud.tistory.com/entry/Ollama-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%84%A4%EC%B9%98%EB%B6%80%ED%84%B0-%EB%AA%A8%EB%8D%B8-%EC%8B%A4%ED%96%89-API-%ED%98%B8%EC%B6%9C%EA%B9%8C%EC%A7%80) | [`basic-usage/`](basic-usage/) |
| 3편 | [Ollama를 개발에 붙이는 방법: Python, JavaScript, Modelfile까지](https://tistory-cloud.tistory.com/entry/Ollama%EB%A5%BC-%EA%B0%9C%EB%B0%9C%EC%97%90-%EB%B6%99%EC%9D%B4%EB%8A%94-%EB%B0%A9%EB%B2%95-Python-JavaScript-Modelfile%EA%B9%8C%EC%A7%80) | [`app-integration-guide/`](app-integration-guide/) |
| 4편 | [Ollama Structured Outputs 사용법: 로컬 LLM 응답을 JSON으로 고정하는 방법](https://tistory-cloud.tistory.com/entry/Ollama-Structured-Outputs-%EC%82%AC%EC%9A%A9%EB%B2%95-%EB%A1%9C%EC%BB%AC-LLM-%EC%9D%91%EB%8B%B5%EC%9D%84-JSON%EC%9C%BC%EB%A1%9C-%EA%B3%A0%EC%A0%95%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95) | [`structured-outputs-guide/`](structured-outputs-guide/) |

---

## ✅ 이 예제가 보여주는 것

- Ollama를 로컬에서 실행하고 API로 호출하는 기본 흐름
- `generate` API와 `chat` API를 curl로 호출하는 방법
- Python과 JavaScript 코드에서 Ollama를 호출하는 방법
- `Modelfile`로 시스템 프롬프트와 temperature를 재사용하는 방법
- Structured Outputs로 로컬 LLM 응답을 JSON 형태로 고정하는 방법

---

## ❌ 이 예제가 하지 않는 것

- 운영 환경용 LLM 서빙 아키텍처를 제공하지 않습니다.
- 인증, 권한, 방화벽, 외부 공개 설정을 다루지 않습니다.
- 모델 품질 평가나 벤치마크를 다루지 않습니다.
- 모든 PC에서 같은 속도와 결과가 나온다고 가정하지 않습니다.

---

## 📁 폴더 구조

```text
basic-usage/               2편 예제 - CLI 명령어와 curl API 호출
app-integration-guide/     3편 예제 - Python, JavaScript, Modelfile 연동
structured-outputs-guide/  4편 예제 - JSON Schema 기반 structured output
```

---

## 🚀 빠른 시작

### 1. 저장소를 내려받습니다

```bash
git clone https://github.com/yechan-cloudlab/cloud-public.git
cd cloud-public/ollama/series-examples
```

### 2. Ollama 설치 상태를 확인합니다

```bash
ollama --version
```

Ollama가 실행 중인지도 확인합니다.

```bash
curl http://localhost:11434
```

정상이라면 Ollama가 실행 중이라는 응답을 확인할 수 있습니다.

### 3. 예제에서 사용할 모델을 내려받습니다

```bash
ollama pull gemma3
```

### 4. 읽고 있는 글에 맞는 폴더로 이동합니다

```text
처음 실행해 보기        → basic-usage/
애플리케이션에 붙이기  → app-integration-guide/
JSON 응답 고정하기     → structured-outputs-guide/
```

각 폴더의 README에 실행 명령이 따로 정리되어 있습니다.

---

## 🧭 어떤 순서로 보면 좋은가

처음이라면 아래 순서를 추천합니다.

1. 1편 글을 읽고 Ollama와 로컬 LLM의 개념을 이해합니다.
2. `basic-usage/`에서 CLI와 curl API 호출을 실행합니다.
3. `app-integration-guide/`에서 Python과 JavaScript 호출 예제를 실행합니다.
4. `structured-outputs-guide/`에서 JSON 응답 고정 예제를 실행합니다.

---

## ⚠️ 사용 전 확인

- Ollama가 로컬에 설치되어 실행 중이어야 합니다.
- 로컬 API 기본 URL은 `http://localhost:11434/api`입니다.
- 샘플 모델명은 `gemma3`를 기준으로 작성했습니다.
- 다른 모델을 사용할 경우 README와 코드의 `model` 값을 함께 변경하세요.
- 실제 프로젝트에 적용하기 전에는 오류 처리, timeout, 재시도, 로깅, 입력 길이 제한을 추가하세요.
- 외부 네트워크에 Ollama를 공개하는 구성은 이 예제의 범위가 아닙니다.

---

## 🧯 자주 막히는 지점

| 증상 | 확인할 것 |
|---|---|
| `ollama` 명령어가 인식되지 않음 | Ollama 설치 여부와 PATH 설정 확인 |
| API 호출이 실패함 | `curl http://localhost:11434`로 Ollama 실행 여부 확인 |
| 모델을 찾을 수 없음 | `ollama pull gemma3` 실행 여부 확인 |
| 응답이 너무 느림 | 더 작은 모델 사용 또는 PC 자원 확인 |
| JSON 파싱 실패 | structured output 예제에서 스키마와 응답 검증 로직 확인 |

---

## 📚 참고 문서

- [Ollama API introduction](https://docs.ollama.com/api)
- [Ollama quickstart](https://docs.ollama.com/quickstart)
- [Structured outputs](https://docs.ollama.com/capabilities/structured-outputs)
- [Modelfile reference](https://docs.ollama.com/modelfile)
