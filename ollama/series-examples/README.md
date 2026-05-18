# Ollama Series Examples

> **Sample example repository** for readers following the Ollama blog series.  
> 이 저장소는 Ollama 4부작 중 2편부터 4편까지의 실습 예제를 모아둔 학습용 샘플입니다.

## Series map

| Part | Article | Example folder |
|---|---|---|
| 1 | [Ollama란 무엇인가: 내 PC에서 LLM을 실행하는 가장 쉬운 방법](https://tistory-cloud.tistory.com/entry/Ollama%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-%EB%82%B4-PC%EC%97%90%EC%84%9C-LLM%EC%9D%84-%EC%8B%A4%ED%96%89%ED%95%98%EB%8A%94-%EA%B0%80%EC%9E%A5-%EC%89%AC%EC%9A%B4-%EB%B0%A9%EB%B2%95) | 글 중심, 별도 예제 없음 |
| 2 | [Ollama 기본 사용법: 설치부터 모델 실행, API 호출까지](https://tistory-cloud.tistory.com/entry/Ollama-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%84%A4%EC%B9%98%EB%B6%80%ED%84%B0-%EB%AA%A8%EB%8D%B8-%EC%8B%A4%ED%96%89-API-%ED%98%B8%EC%B6%9C%EA%B9%8C%EC%A7%80) | [`basic-usage/`](basic-usage/) |
| 3 | [Ollama를 개발에 붙이는 방법: Python, JavaScript, Modelfile까지](https://tistory-cloud.tistory.com/entry/Ollama%EB%A5%BC-%EA%B0%9C%EB%B0%9C%EC%97%90-%EB%B6%99%EC%9D%B4%EB%8A%94-%EB%B0%A9%EB%B2%95-Python-JavaScript-Modelfile%EA%B9%8C%EC%A7%80) | [`app-integration-guide/`](app-integration-guide/) |
| 4 | [Ollama Structured Outputs 사용법: 로컬 LLM 응답을 JSON으로 고정하는 방법](https://tistory-cloud.tistory.com/entry/Ollama-Structured-Outputs-%EC%82%AC%EC%9A%A9%EB%B2%95-%EB%A1%9C%EC%BB%AC-LLM-%EC%9D%91%EB%8B%B5%EC%9D%84-JSON%EC%9C%BC%EB%A1%9C-%EA%B3%A0%EC%A0%95%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95) | [`structured-outputs-guide/`](structured-outputs-guide/) |

## Folder structure

```text
basic-usage/
app-integration-guide/
structured-outputs-guide/
```

## Shared assumptions

- Ollama is installed and running locally.
- Local API base URL: `http://localhost:11434/api`
- The sample model name is `gemma3`.
- Every folder is a **sample companion**, not production-ready application code.

## Quick start

```bash
ollama pull gemma3
```

Then open the folder that matches the article you are reading:

```text
처음 실행해 보기        → basic-usage/
애플리케이션에 붙이기  → app-integration-guide/
JSON 응답 고정하기     → structured-outputs-guide/
```

## Notes

- 실제 프로젝트에 넣기 전에는 모델 이름, 오류 처리, 타임아웃, 재시도, 배포 정책을 직접 조정해야 합니다.
- Python 예제는 공식 `ollama` 패키지를, JavaScript 예제는 공식 `ollama` 패키지를 사용합니다.
- Structured Outputs 예제는 Python에서 `pydantic`, JavaScript에서 `zod`와 `zod-to-json-schema`를 추가로 사용합니다.
- 각 하위 폴더의 README를 먼저 읽고 실행하면 필요한 의존성과 명령을 바로 확인할 수 있습니다.

## Official references

- [Ollama API introduction](https://docs.ollama.com/api)
- [Ollama quickstart](https://docs.ollama.com/quickstart)
- [Structured outputs](https://docs.ollama.com/capabilities/structured-outputs)
- [Modelfile reference](https://docs.ollama.com/modelfile)
