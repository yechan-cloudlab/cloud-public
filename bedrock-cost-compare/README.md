# Bedrock Cost Compare

Amazon Bedrock Claude 모델 비용을 비교하고 간단한 요청 라우팅 전략을 설계하는 예제입니다.

> 이 저장소는 학습용 샘플입니다. 프로덕션용 Bedrock 비용 플랫폼이 아닙니다. Claude Haiku, Sonnet, Opus 스타일의 모델 티어를 요청 유형에 따라 선택해 토큰 비용을 이해하고 제어하는 방법을 보여줍니다.

---

## 📎 관련 아티클

- [Bedrock Cost ](https://tistory-cloud.tistory.com/entry/Claude-Opus%EB%A7%8C-%EC%93%B0%EB%A9%B4-Bedrock-%EB%B9%84%EC%9A%A9%EC%9D%B4-%ED%84%B0%EC%A7%91%EB%8B%88%EB%8B%A4-Haiku%C2%B7Sonnet%C2%B7Opus-%EB%9D%BC%EC%9A%B0%ED%8C%85-%EC%A0%84%EB%9E%B5#s10)

---

## ✅ 이 예제가 보여주는 것

- 요청을 `summarize`, `classify`, `code_generate`, `deep_reasoning` 등 카테고리로 분류하는 방법
- 라우팅 규칙에 따라 모델 티어를 선택하는 방법
- 입력/출력 토큰을 분리해 비용을 추정하는 방법
- 고정 모델 전략과 라우팅 전략의 비용 비교
- CloudWatch Dashboard 샘플 및 Terraform 예제

## ❌ 이 예제가 하지 않는 것

- 실제 AWS Bedrock 프로덕션 가격을 하드코딩하지 않습니다.
- 프로덕션용 인증, 권한, 속도 제한을 포함하지 않습니다.

> **가격 정책**: `config/pricing.template.json`에 실제 AWS 가격을 채워 사용하세요. `config/pricing.demo.json`은 로컬 실행 전용 가상 가격으로, 실제 과금 결정에 사용하지 마세요.  
> 최신 가격은 [AWS Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)에서 확인하세요.

---

## 📁 폴더 구조

```text
config/             가격 템플릿 및 라우팅 규칙
dashboards/         CloudWatch Dashboard 샘플
docs/               모델 선택 가이드, 운영 체크리스트
examples/           샘플 요청 데이터
src/                비용 계산기, 라우터, Bedrock 클라이언트
terraform/          CloudWatch Dashboard 및 빌링 알람 샘플
tests/              단위 테스트
```

**예제 라우팅 정책**

| 요청 카테고리 | 권장 모델 티어 | 이유 |
| --- | --- | --- |
| `summarize` | Claude Haiku | 짧은 요약은 비용·지연 민감도가 높음 |
| `classify` | Claude Haiku | 분류는 반복적이고 단순한 경우가 많음 |
| `translate` | Claude Haiku | 번역은 저비용 모델로 시작 가능 |
| `code_generate` | Claude Sonnet | 코드 생성은 강한 명령 수행 능력 필요 |
| `code_review` | Claude Sonnet | 코드 리뷰는 추론과 비용의 균형 필요 |
| `security_audit` | Claude Sonnet or Opus | 보안 작업은 강한 검토와 에스컬레이션 필요 |
| `deep_reasoning` | Claude Opus | 고가치 복잡 추론에만 최강 모델 사용 |

---

## 🚀 빠른 시작

**1. 가상 환경 생성 및 의존성 설치**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**2. 데모 비용 계산기 실행**

```bash
python src/cost_calculator.py --pricing config/pricing.demo.json --requests examples/requests.jsonl
```

**3. 라우터 데모 실행**

```bash
python src/router.py --rules config/routing-rules.example.json --requests examples/requests.jsonl
```

**4. 고정 모델 vs 라우팅 전략 비교**

```bash
python src/compare_strategies.py --pricing config/pricing.demo.json --rules config/routing-rules.example.json --requests examples/requests.jsonl --baseline claude-opus
```

**5. 테스트 실행**

```bash
python -m unittest discover -s tests
```

**6. Terraform 샘플**

```bash
cd terraform
terraform init
terraform plan
```

---

## ⚠️ 사용 전 확인

- 현재 AWS Bedrock 가격을 반드시 확인하세요.
- 대상 리전에서 모델 사용 가능 여부를 확인하세요.
- 모든 요청에 `max_tokens`를 설정하세요.
- 요청 카테고리, 선택 모델, 입력/출력 토큰을 로깅하세요.
- 민감한 프롬프트와 고객 데이터를 마스킹하세요.
- 롤아웃 전 예산 알람을 설정하세요.
- dry-run 라우팅으로 시작하세요.
- 단일 기본 모델로 롤백할 경로를 유지하세요.

---

## 📚 참고 문서

- [AWS Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)
- [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/)
- [Anthropic models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)

---

## License

MIT License. See `LICENSE`.
