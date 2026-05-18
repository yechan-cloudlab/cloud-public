# Keycloak High Availability Guide

EKS에서 Keycloak 단일 클러스터 이중화를 구성하는 예제입니다.

> 이 저장소는 학습용 샘플입니다. 운영 환경에 적용하기 전에 조직의 보안, 네트워크, 데이터베이스, 배포 정책에 맞게 반드시 검토하세요.

---

## 📎 관련 아티클

- [Keycloak 이중화 구성 방법: EKS에서 Pod, AZ, RDS까지 어디를 이중화해야 하는가](https://tistory-cloud.tistory.com/entry/Keycloak-%EC%9D%B4%EC%A4%91%ED%99%94-%EA%B5%AC%EC%84%B1-%EB%B0%A9%EB%B2%95-EKS%EC%97%90%EC%84%9C-Pod-AZ-RDS%EA%B9%8C%EC%A7%80-%EC%96%B4%EB%94%94%EB%A5%BC-%EC%9D%B4%EC%A4%91%ED%99%94%ED%95%B4%EC%95%BC-%ED%95%98%EB%8A%94%EA%B0%80) — 이 저장소의 companion article
- [Keycloak Helm 설치 방법: values.yaml로 RDS, 인증서, Realm까지 설정하기](https://tistory-cloud.tistory.com/entry/Keycloak-Helm-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95-valuesyaml%EB%A1%9C-RDS-%EC%9D%B8%EC%A6%9D%EC%84%9C-Realm%EA%B9%8C%EC%A7%80-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0)
- [Keycloak 인증이 실제로 동작하는 전체 흐름: 세션, 토큰, 쿠키 구조 완전 해부](https://tistory-cloud.tistory.com/entry/Keycloak-%EC%9D%B8%EC%A6%9D%EC%9D%B4-%EC%8B%A4%EC%A0%9C%EB%A1%9C-%EB%8F%99%EC%9E%91%ED%95%98%EB%8A%94-%EC%A0%84%EC%B2%B4-%ED%9D%90%EB%A6%84-%EC%84%B8%EC%85%98-%ED%86%A0%ED%81%B0-%EC%BF%A0%ED%82%A4-%EA%B5%AC%EC%A1%B0-%EC%99%84%EC%A0%84-%ED%95%B4%EB%B6%80)
- [Keycloak 운영 방법: 인증서 갱신, 백업, 업그레이드, 장애 대응 체크리스트](https://tistory-cloud.tistory.com/entry/Keycloak-%EC%9A%B4%EC%98%81-%EB%B0%A9%EB%B2%95-%EC%9D%B8%EC%A6%9D%EC%84%9C-%EA%B0%B1%EC%8B%A0-%EB%B0%B1%EC%97%85-%EC%97%85%EA%B7%B8%EB%A0%88%EC%9D%B4%EB%93%9C-%EC%9E%A5%EC%95%A0-%EB%8C%80%EC%9D%91-%EC%B2%B4%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%8A%B8)

---

## ✅ 이 예제가 보여주는 것

- 2개 이상 Keycloak Pod를 기본으로 두는 단일 클러스터 HA 설계
- 여러 AZ에 Pod가 퍼지도록 하는 배치 전략
- 롤링 업데이트 중 최소 가용 수를 지키는 PodDisruptionBudget
- RDS Multi-AZ와 함께 봐야 하는 장애 지점
- 이중화 구성 점검표와 장애 시나리오 정리

## ❌ 이 예제가 하지 않는 것

- 멀티 클러스터 또는 멀티 리전 Keycloak HA 전체 구성을 다루지 않습니다.
- 조직별 인증 정책, 백업 정책, 운영 절차를 대신하지 않습니다.
- `values-ha.example.yaml`을 그대로 적용하면 완성형 운영 구성이 된다고 가정하지 않습니다.

---

## 📁 폴더 구조

```text
values/      Helm values 샘플
manifests/   PDB와 배치 관련 Kubernetes 매니페스트 샘플
docs/        운영 체크리스트와 장애 시나리오
diagrams/    아키텍처 설명
```

---

## 🚀 빠른 시작

이 저장소는 기존 [`keycloak/helm-practical-guide/`](../helm-practical-guide/)의 wrapper chart와 함께 참고하는 샘플입니다.

```bash
cd keycloak/helm-practical-guide
helm dependency update
helm upgrade --install keycloak . \
  -f ../high-availability-guide/values/values-ha.example.yaml
```

---

## ⚠️ 사용 전 확인

- 실제 배포 전 `{{PLACEHOLDER}}` 값을 모두 교체하세요.
- 클러스터의 스케줄링 정책과 데이터베이스 구성을 반드시 검토하세요.
- Keycloak 이중화는 단순히 replica 수를 늘리는 문제가 아닙니다. 세션, 캐시, 데이터베이스, 로드밸런서, 배포 전략을 함께 봐야 합니다.
- 설치 구조가 익숙하지 않다면 먼저 [`helm-practical-guide`](../helm-practical-guide/) 예제를 확인하세요.

**이 샘플의 범위 (single-cluster HA)**

```text
다루는 것
- Multi-pod
- Multi-AZ node placement
- PodDisruptionBudget
- Readiness / liveness / startup probe 고려
- RDS Multi-AZ와의 결합

다루지 않는 것
- Multi-cluster active/passive
- Multi-region failover
- 외부 Infinispan 기반 멀티 사이트 구성
```

**설계 메모**
- Keycloak 공식 문서는 single-cluster와 multi-cluster HA를 별도 아키텍처로 구분합니다.
- 현재 Keycloak의 분산 캐시는 기본적으로 Infinispan 기반이며, production mode의 기본 cache stack은 `jdbc-ping`입니다.
- 공식 문서는 Pod를 여러 노드에 퍼뜨리기 위해 anti-affinity와 topology spread constraints 사용을 권장합니다.
- 이 샘플은 **chart override 파일**입니다. 독립 실행형 Helm chart가 아닙니다.

---

## 📚 참고 문서

- [High availability overview](https://www.keycloak.org/high-availability/introduction)
- [Configuring distributed caches](https://www.keycloak.org/server/caching)
