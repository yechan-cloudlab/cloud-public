# S3 Cost Allocation by Department

> **Sample example repository** for readers following the related blog article.  
> 이 저장소는 바로 복사해 참고할 수 있는 학습용 샘플이며, 조직의 실제 계정 구조·보안 정책·과금 체계에 맞게 수정해서 사용해야 합니다.

부서별 S3 비용을 더 명확하게 귀속하기 위한 Terraform 샘플입니다.

> S3 비용 최적화의 시작은 삭제가 아니라 비용 귀속입니다.  
> Access Point는 접근 제어를 나누는 도구이고, 비용 귀속의 기본 단위는 버킷과 Cost Allocation Tag입니다.

## 이 샘플이 보여주는 것

- 부서별 버킷 분리 예제
- `Department`, `Environment`, `CostCenter` 태그 설계
- Terraform으로 반복 가능한 S3 버킷 생성
- Access Point와 비용 추적을 혼동하지 않기 위한 보조 설명

## 이 샘플이 하지 않는 것

- 실제 조직의 완성형 FinOps 표준을 대신하지 않습니다.
- 공유 버킷 안의 객체별 비용을 자동으로 회계 분리하지 않습니다.
- Access Point 태그만으로 부서별 S3 비용을 분리한다고 가정하지 않습니다.

## 구조

```text
terraform/      공통 Terraform 샘플 코드
examples/       부서별 tfvars 샘플
access-point/   Access Point를 어디에 써야 하는지 설명
```

## 왜 버킷을 나누는가

S3 Cost Allocation Tag는 버킷 태그를 기준으로 비용을 분류합니다. 여러 부서가 하나의 버킷을 함께 쓰면 Cost Explorer에서 부서별 비용을 깔끔하게 나누기 어렵습니다. 반대로 부서별 버킷을 만들고 태그를 일관되게 붙이면, 비용 귀속과 책임 구분이 훨씬 선명해집니다.

## 빠른 시작

```bash
cd terraform
terraform init
terraform plan -var-file=../examples/marketing.tfvars
```

샘플을 실제로 배포하려면 `plan` 결과를 검토한 뒤 아래 명령을 사용합니다.

```bash
terraform apply -var-file=../examples/marketing.tfvars
```

같은 코드에 다른 변수 파일을 넣으면 `dev`, `data` 버킷도 같은 방식으로 만들 수 있습니다.

## 기본 태그 설계

| Tag | Example | Purpose |
|---|---|---|
| `Department` | `marketing` | 부서별 비용 귀속 |
| `Environment` | `prod` | 환경 구분 |
| `CostCenter` | `mkt-001` | 회계/예산 연결 |
| `ManagedBy` | `terraform` | 운영 방식 식별 |

## 중요한 구분

| 목적 | 권장 도구 |
|---|---|
| 부서별 비용 귀속 | 버킷 분리 + Cost Allocation Tag |
| 같은 버킷 안의 접근 제어 분리 | S3 Access Point |

Access Point에 태그를 붙이는 것은 유용할 수 있지만, S3 비용 귀속을 그 태그만으로 해결한다고 보면 안 됩니다. Access Point 예시는 [`access-point/README.md`](access-point/README.md)에 따로 정리했습니다.

## 사용 전 확인할 것

- AWS Billing에서 사용자 정의 Cost Allocation Tag를 활성화해야 Cost Explorer에서 사용할 수 있습니다.
- 태그는 활성화 후의 비용 분류에 활용되므로, 과거 비용을 완전히 소급해 정리하는 도구로 보면 안 됩니다.
- 요청 비용, 데이터 전송, 스토리지 클래스 비용은 모두 함께 봐야 실제 S3 비용 구조를 이해할 수 있습니다.
- 샘플 버킷 이름은 전역 고유해야 하므로, 그대로 쓰지 말고 조직 규칙에 맞게 바꾸세요.

## 참고 문서

- [Using cost allocation S3 bucket tags](https://docs.aws.amazon.com/console/s3/cost-allocation-tagging)
- [Tagging for cost allocation or ABAC](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html)
- [Managing access to shared datasets with access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html)

## 다음 확장 아이디어

- 공통 모듈화
- Lifecycle rule 샘플 추가
- Cost and Usage Report 기반 심화 분석 예제
- 여러 계정에서 같은 태그 체계를 적용하는 예제
