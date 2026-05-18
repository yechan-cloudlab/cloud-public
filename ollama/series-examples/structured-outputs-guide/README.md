# Ollama Structured Outputs Guide

Companion sample folder for the article:

- [Ollama Structured Outputs 사용법: 로컬 LLM 응답을 JSON으로 고정하는 방법](https://tistory-cloud.tistory.com/entry/Ollama-Structured-Outputs-%EC%82%AC%EC%9A%A9%EB%B2%95-%EB%A1%9C%EC%BB%AC-LLM-%EC%9D%91%EB%8B%B5%EC%9D%84-JSON%EC%9C%BC%EB%A1%9C-%EA%B3%A0%EC%A0%95%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95)

## What this sample covers

- Pydantic 기반 Python structured output
- Zod 기반 JavaScript structured output
- 정보 추출과 문의 분류 예제
- 재사용 가능한 JSON Schema 예시

## Files

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

## Install dependencies

```bash
# Python
pip install -r requirements.txt

# JavaScript
npm install
```

## Run the examples

```bash
python python/extract_pet_info.py
python python/classify_support_ticket.py
npm run extract:pet
npm run classify:ticket
```

## Notes

- structured outputs는 자동화 친화적인 응답을 만들기 위한 기능입니다.
- 공식 문서는 더 안정적인 응답을 위해 낮은 temperature 사용을 권장합니다.
- 실제 서비스에서는 응답 검증 실패와 재시도 전략도 함께 설계하세요.
