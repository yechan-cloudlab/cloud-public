# Perplexity Sonar API Examples

인용 출처가 포함된 웹 기반 AI 답변을 만드는 Perplexity Sonar API 예제입니다.

> 이 저장소는 블로그 글을 위한 **학습용 샘플**입니다. 공식 Perplexity 저장소가 아니며, 프로덕션용이 아닙니다. API 구조, 인용 처리, 스트리밍, 검색 옵션을 이해하는 용도로 사용하세요.

---

## 📎 관련 아티클

- [Perplexity Sonar API 사용법: 실시간 웹 검색이 가능한 AI 답변 API 만들기](https://tistory-cloud.tistory.com/entry/Perplexity-Sonar-API-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%8B%A4%EC%8B%9C%EA%B0%84-%EC%9B%B9-%EA%B2%80%EC%83%89%EC%9D%B4-%EA%B0%80%EB%8A%A5%ED%95%9C-AI-%EB%8B%B5%EB%B3%80-API-%EB%A7%8C%EB%93%A4%EA%B8%B0)

---

## ✅ 이 예제가 보여주는 것

- OpenAI 호환 Python SDK로 Perplexity Sonar API 호출하는 방법
- Sonar 모델로 웹 기반 답변 생성하는 방법
- 응답에서 `citations`와 `search_results` 읽는 방법
- 스트리밍 응답 처리 방법
- `extra_body`로 Perplexity 전용 검색 옵션 전달하는 방법
- API 키를 소스 코드에서 분리하는 방법

## ❌ 이 예제가 하지 않는 것

- 실제 API 키를 포함하지 않습니다.
- 답변 정확도를 보장하지 않습니다.
- 출처 검토, 법적 검토, 보안 검토를 대신하지 않습니다.
- 프로덕션 수준의 인증, retry, rate limit, cache, 관찰 가능성을 포함하지 않습니다.

---

## 📁 폴더 구조

```text
python/             Sonar API 예제
examples/           샘플 질문 및 예상 응답 노트
docs/               API 개요, 프롬프트 패턴, 운영 체크리스트
.env.example        환경 변수 템플릿
requirements.txt    Python 의존성
```

---

## 🚀 빠른 시작

**1. 의존성 설치**

```bash
pip install -r requirements.txt
```

**2. 환경 변수 복사**

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

**3. API 키 설정**

`.env` 파일 편집:

```env
PERPLEXITY_API_KEY=pplx-your-api-key
PERPLEXITY_MODEL=sonar-pro
PERPLEXITY_BASE_URL=https://api.perplexity.ai
```

**4. 기본 답변 예제 실행**

```bash
python python/basic_search_answer.py
```

**5. 인용 및 검색 결과 확인**

```bash
python python/cited_answer.py
```

**6. 스트리밍 예제 실행**

```bash
python python/streaming_answer.py
```

---

## ⚠️ 사용 전 확인

- Perplexity의 표준 Sonar 엔드포인트는 `POST /v1/sonar`입니다.
- OpenAI SDK 사용 시 `client.chat.completions.create()`는 `/chat/completions`로 라우팅되며, Perplexity가 호환성을 위해 이를 허용합니다.
- OpenAI SDK에서 `base_url="https://api.perplexity.ai"`를 사용하세요.
- `search_domain_filter`, `search_recency_filter`, `search_mode` 등 Perplexity 전용 옵션은 Python OpenAI SDK의 `extra_body`로 전달할 수 있습니다.
- 응답 필드는 모델과 API 버전에 따라 다를 수 있으므로, 프로덕션 파싱 로직 작성 전에 원시 응답을 먼저 확인하세요.

---

## 📚 참고 문서

- [Perplexity Sonar API Quickstart](https://docs.perplexity.ai/docs/sonar/quickstart)
- [Perplexity OpenAI SDK Compatibility](https://docs.perplexity.ai/docs/sonar/openai-compatibility)
- [Perplexity Sonar API Reference](https://docs.perplexity.ai/api-reference/sonar-post)
- [Perplexity Search Filters](https://docs.perplexity.ai/docs/sonar/filters)
