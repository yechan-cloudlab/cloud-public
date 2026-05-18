# Where S3 Access Points Fit

> **Sample note** for the companion blog article.  
> 이 문서는 Access Point를 비용 분리 도구로 오해하지 않기 위한 보조 설명입니다.

S3 Access Point는 같은 버킷을 여러 애플리케이션이나 팀이 함께 사용할 때, 접근 경로와 정책을 분리하기 위한 기능입니다.

## Access Point가 잘하는 일

- 팀별 또는 애플리케이션별 정책 분리
- VPC 전용 접근 경로 구성
- 하나의 버킷을 여러 사용 사례에 더 안전하게 노출

## Access Point가 해결하지 않는 일

- Cost Explorer에서 부서별 S3 비용을 자동으로 쪼개 보여 주는 일
- 하나의 공유 버킷 비용을 Access Point 태그만으로 회계적으로 분리하는 일

## 실무 기준

```text
비용을 나누고 싶다  -> 버킷 구조와 Cost Allocation Tag를 먼저 설계
접근을 나누고 싶다  -> Access Point를 사용
```

같은 조직 안에서도 이 두 문제는 자주 섞입니다. 하지만 비용 귀속과 접근 제어는 서로 다른 축입니다. 먼저 무엇을 나누고 싶은지부터 분명히 해야 설계가 단단해집니다.
