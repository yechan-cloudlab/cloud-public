# Ollama Basic Usage

Companion sample folder for the article:

- [Ollama 기본 사용법: 설치부터 모델 실행, API 호출까지](https://tistory-cloud.tistory.com/entry/Ollama-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%84%A4%EC%B9%98%EB%B6%80%ED%84%B0-%EB%AA%A8%EB%8D%B8-%EC%8B%A4%ED%96%89-API-%ED%98%B8%EC%B6%9C%EA%B9%8C%EC%A7%80)

## What this sample covers

- 자주 쓰는 CLI 명령어
- `generate`와 `chat` API를 호출하는 가장 작은 예제

## Files

```text
commands.md
api-examples/
  curl-generate.sh
  curl-chat.sh
```

## Before you run

1. Ollama가 실행 중이어야 합니다.
2. 사용할 모델을 먼저 내려받아야 합니다.

```bash
ollama pull gemma3
```

## Run the examples

```bash
bash api-examples/curl-generate.sh
bash api-examples/curl-chat.sh
```

## Notes

- 이 폴더는 명령어와 API 호출 흐름을 빠르게 복습하기 위한 샘플입니다.
- 실제 애플리케이션 연동은 다음 편의 `app-integration-guide/`를 참고하세요.
