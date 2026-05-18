# Route 53 Resolver Query Log Analyzer

Route 53 Resolver Query Log를 Athena로 분석하고, 의심 도메인 조사용 Markdown 리포트를 생성하는 예제 저장소입니다.

> DNS 조회 로그는 실제 네트워크 접속을 확정하지 않습니다.  
> 다만 VPC 내부 워크로드가 어떤 도메인을 조회했는지 보여 주기 때문에, 의심 통신을 좁혀 가는 좋은 출발점이 됩니다.

## 저장소가 해결하는 문제

VPC Flow Logs만 보면 목적지 IP는 보이지만, 사람이 읽기 쉬운 도메인 맥락은 빠집니다. 이 저장소는 Resolver Query Log를 함께 보면서 아래 질문에 답하는 흐름을 제공합니다.

- 어떤 인스턴스가 어떤 도메인을 조회했는가
- `NXDOMAIN`이 비정상적으로 많이 발생했는가
- 긴 도메인이나 `TXT` 쿼리가 과도하게 보이는가
- 알려진 의심 도메인 목록과 일치하는 조회가 있었는가

## 아키텍처

```text
EC2 / Workload
      |
      v
Route 53 Resolver Query Log
      |
      v
Amazon S3
      |
      v
Amazon Athena
      |
      v
CSV export -> Python report generator -> Markdown report
```

## 디렉터리 구조

```text
athena/      Athena 테이블 생성 SQL과 예제 탐지 쿼리
src/         Markdown 리포트 생성 스크립트
rules/       간단한 도메인 룰셋
sample-data/ 샘플 로그와 예제 Athena 결과
reports/     예제 출력 리포트
```

## 빠른 시작

### 1. Athena 테이블 생성

[`athena/create_table.sql`](athena/create_table.sql)의 아래 값을 환경에 맞게 바꿉니다.

- `YOUR_BUCKET`
- `YOUR_ACCOUNT_ID`
- `vpc-xxxxxxxx`
- `projection.date.range`

그 뒤 Athena에서 실행합니다.

### 2. 탐지 쿼리 실행

[`athena/example_queries.sql`](athena/example_queries.sql)에는 아래 예제가 들어 있습니다.

- 최근 조회량 상위 도메인
- 인스턴스별 조회 도메인
- `NXDOMAIN` 급증
- 긴 도메인
- `TXT` 쿼리 과다

필요한 쿼리를 실행한 뒤 결과를 CSV로 내려받습니다. generate_report.py에 바로 넣을 CSV가 필요하면 6번 쿼리를 사용하세요.

### 3. 리포트 생성

```bash
python src/generate_report.py \
  --input sample-data/athena_result_sample.csv \
  --rules rules/suspicious_domains.txt \
  --output reports/example_report.md
```

예제 출력은 [`reports/example_report.md`](reports/example_report.md)에서 볼 수 있습니다.

## 리포트 입력 형식

`generate_report.py`는 아래 컬럼을 가진 CSV를 기대합니다.

| Column | Description |
|---|---|
| `instance_id` | 조회를 발생시킨 인스턴스 ID |
| `query_name` | 조회한 도메인 |
| `query_type` | DNS 레코드 타입 |
| `rcode` | DNS 응답 코드 |
| `query_count` | 동일 패턴의 집계 횟수 |

샘플은 [`sample-data/athena_result_sample.csv`](sample-data/athena_result_sample.csv)를 참고하세요.

## 기본 탐지 로직

| Rule | Score | 설명 |
|---|---:|---|
| 룰셋 도메인과 정확히 일치 | 5 | 알려진 의심 도메인 |
| 도메인 길이 50자 이상 | 2 | 난독화·터널링 징후 탐색용 |
| `TXT` 쿼리 10회 이상 | 2 | 데이터 전달 의심 신호 탐색용 |
| `NXDOMAIN` 20회 이상 | 2 | DGA·오타·잘못된 설정 구분 필요 |

이 점수는 침해 판정기가 아니라 **조사 우선순위 계산기**입니다. 운영 환경에서는 프록시 로그, EDR, VPC Flow Logs, DNS Firewall 이벤트와 함께 보세요.

## 룰 커스터마이징

[`rules/suspicious_domains.txt`](rules/suspicious_domains.txt)에 한 줄에 하나씩 도메인을 추가합니다.

```text
moneropool.example
bad-domain.example
```

현재 버전은 **정확 일치**만 지원합니다. 와일드카드, suffix match, 외부 threat feed 연동은 확장 포인트로 남겨두었습니다.

## 한계와 주의사항

- DNS 조회가 실제 접속을 의미하지는 않습니다.
- Resolver 캐시로 처리된 반복 조회는 로그에 남지 않을 수 있습니다.
- 긴 도메인이나 `TXT` 쿼리는 정상 서비스에서도 나타날 수 있습니다.
- 로그에는 내부 자산 정보가 포함될 수 있으므로 보존 기간과 접근 권한을 함께 설계해야 합니다.

## 다음 확장 아이디어

- suffix match / wildcard rule 지원
- 점수 임계값 CLI 옵션화
- JSON 또는 HTML 리포트 출력
- Athena 결과를 직접 읽는 자동화
- GitHub Actions로 lint/test 자동 실행

## 참고 문서

- [Route 53 Resolver Query Logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs.html)
- [Values that appear in VPC Resolver query logs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs-format.html)
- [Create the table for resolver query logs](https://docs.aws.amazon.com/athena/latest/ug/querying-r53-resolver-logs-creating-the-table.html)
