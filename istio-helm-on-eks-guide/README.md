# istio-helm-on-eks-guide

> Sample repository for installing and operating Istio on EKS with official Helm charts.

This is a **sample repository** for a blog series about Istio on EKS. It focuses on a Helm-based installation workflow and practical operations: traffic routing, mTLS security, observability, and troubleshooting.

## Scope

This repository is intentionally practical and small. It does not try to become a complete production platform.

Included:

- Istio installation with official Helm charts
- `base`, `istiod`, and `gateway` chart separation
- Sample application with sidecar injection
- Gateway, VirtualService, and DestinationRule examples
- Canary and header-based routing examples
- mTLS and AuthorizationPolicy examples
- Observability notes for Prometheus, Grafana, and Kiali
- Troubleshooting notes for common Istio failures

Not included:

- Full EKS cluster provisioning
- Production-grade GitOps pipeline
- Organization-specific security policy
- Complete monitoring stack installation
- Certificate automation for production TLS

## Related blog articles

1. [Istio란 무엇인가: Kubernetes 서비스 메시 구성요소와 트래픽 흐름 이해하기](https://tistory-cloud.tistory.com/entry/Istio%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-Kubernetes-%EC%84%9C%EB%B9%84%EC%8A%A4-%EB%A9%94%EC%8B%9C-%EA%B5%AC%EC%84%B1%EC%9A%94%EC%86%8C%EC%99%80-%ED%8A%B8%EB%9E%98%ED%94%BD-%ED%9D%90%EB%A6%84-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0)
2. [Istio Helm Chart 설치 방법: EKS에서 base, istiod, gateway 구성하기](https://tistory-cloud.tistory.com/entry/Istio-Helm-Chart-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95-EKS%EC%97%90%EC%84%9C-base-istiod-gateway-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0)
3. [Istio Canary 배포 방법: VirtualService와 DestinationRule로 트래픽 나누기](https://tistory-cloud.tistory.com/entry/Istio-Canary-%EB%B0%B0%ED%8F%AC-%EB%B0%A9%EB%B2%95-VirtualService%EC%99%80-DestinationRule%EB%A1%9C-%ED%8A%B8%EB%9E%98%ED%94%BD-%EB%82%98%EB%88%84%EA%B8%B0)
4. [Istio mTLS 설정 방법: PeerAuthentication과 AuthorizationPolicy로 서비스 간 통신 보호하기](https://tistory-cloud.tistory.com/entry/Istio-mTLS-%EC%84%A4%EC%A0%95-%EB%B0%A9%EB%B2%95-PeerAuthentication%EA%B3%BC-AuthorizationPolicy%EB%A1%9C-%EC%84%9C%EB%B9%84%EC%8A%A4-%EA%B0%84-%ED%86%B5%EC%8B%A0-%EB%B3%B4%ED%98%B8%ED%95%98%EA%B8%B0)
5. [Istio 관측성 운영 방법: Prometheus, Grafana, Kiali로 서비스 메시 확인하기](https://tistory-cloud.tistory.com/entry/Istio-%EA%B4%80%EC%B8%A1%EC%84%B1-%EC%9A%B4%EC%98%81-%EB%B0%A9%EB%B2%95-Prometheus-Grafana-Kiali%EB%A1%9C-%EC%84%9C%EB%B9%84%EC%8A%A4-%EB%A9%94%EC%8B%9C-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0)
6. [Istio 트러블슈팅 가이드: 503 오류, mTLS, VirtualService, Sidecar 문제 해결하기](https://tistory-cloud.tistory.com/entry/Istio-%ED%8A%B8%EB%9F%AC%EB%B8%94%EC%8A%88%ED%8C%85-%EA%B0%80%EC%9D%B4%EB%93%9C-503-%EC%98%A4%EB%A5%98-mTLS-VirtualService-Sidecar-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0%ED%95%98%EA%B8%B0)

## Repository structure

```text
istio-helm-on-eks-guide/
  charts-values/       # Helm values examples for base, istiod, gateway
  install/             # Helm installation and verification scripts
  sample-app/          # Sample app with v1, v2, service, frontend client
  traffic-routing/     # Gateway, VirtualService, DestinationRule
  mtls-security/       # PeerAuthentication, AuthorizationPolicy, mTLS policy
  observability/       # Prometheus, Grafana, Kiali notes
  troubleshooting/     # Common failure cases and commands
  docs/                # Architecture and operation notes
  scripts/             # Repository validation scripts
```

## Prerequisites

- Kubernetes cluster or EKS cluster
- `kubectl` configured for the target cluster
- `helm` installed
- Optional: `istioctl` for `analyze`, `proxy-status`, and proxy config inspection
- AWS Load Balancer support if you expose the ingress gateway as `LoadBalancer`

## Install Istio with Helm

Run from the repository root:

```bash
chmod +x install/*.sh

./install/01-add-helm-repo.sh
./install/02-install-base.sh
./install/03-install-istiod.sh
./install/04-install-gateway.sh
./install/05-verify.sh
```

Equivalent Helm flow:

```bash
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update

helm upgrade --install istio-base istio/base \
  -n istio-system \
  --create-namespace \
  -f charts-values/istio-base-values.yaml \
  --wait

helm upgrade --install istiod istio/istiod \
  -n istio-system \
  -f charts-values/istiod-values.yaml \
  --wait

helm upgrade --install istio-ingress istio/gateway \
  -n istio-ingress \
  --create-namespace \
  -f charts-values/istio-gateway-values.yaml \
  --wait
```

## Deploy the sample app

```bash
kubectl apply -f sample-app/namespace.yaml
kubectl apply -f sample-app/serviceaccount-frontend.yaml
kubectl apply -f sample-app/app-v1.yaml
kubectl apply -f sample-app/app-v2.yaml
kubectl apply -f sample-app/service.yaml
kubectl apply -f sample-app/frontend.yaml
```

Verify sidecar injection:

```bash
kubectl get pods -n istio-sample
kubectl get pod -n istio-sample -l app=httpbin -o jsonpath='{.items[0].spec.containers[*].name}'
```

You should see an `istio-proxy` container in injected workloads.

## Apply traffic routing

```bash
kubectl apply -f traffic-routing/gateway.yaml
kubectl apply -f traffic-routing/destinationrule.yaml
kubectl apply -f traffic-routing/virtualservice-canary.yaml
```

Header-based routing:

```bash
kubectl apply -f traffic-routing/virtualservice-header.yaml
```

## Apply mTLS and authorization examples

Apply gradually in a test namespace first:

```bash
kubectl apply -f mtls-security/peerauthentication-strict.yaml
kubectl apply -f mtls-security/destinationrule-mtls.yaml
kubectl apply -f mtls-security/authorizationpolicy-allow-only-frontend.yaml
```

## Troubleshooting first commands

```bash
istioctl analyze
istioctl proxy-status
kubectl get pods -n istio-system
kubectl get pods -n istio-ingress
kubectl logs -n istio-ingress deploy/istio-ingress -c istio-proxy
```

More troubleshooting notes are in `troubleshooting/`.

## Validate this repository

```bash
node scripts/validate-repo.mjs
```

The validation script checks required files, expected blog links, and basic YAML markers. It does not replace `kubectl --dry-run=server` or `istioctl analyze`.

## Important notes

- The official Istio Helm installation uses separate charts for `base`, `istiod`, and `gateway`.
- The gateway chart is managed separately from the control plane.
- The labels on the gateway deployment pods must match the selector in the Istio `Gateway` resource.
- Do not mix `istioctl` ownership and Helm ownership without reviewing migration steps.
- Use `helm upgrade` and `helm rollback` for chart-managed resources.
- Apply mTLS policies gradually. Start with namespace-level testing before mesh-wide STRICT mode.

## Official references

- Istio install with Helm: https://istio.io/latest/docs/setup/install/helm/
- Istio gateway installation: https://istio.io/latest/docs/setup/additional-setup/gateway/
- Istio traffic management: https://istio.io/latest/docs/concepts/traffic-management/
- Istio security: https://istio.io/latest/docs/concepts/security/
- Istio observability: https://istio.io/latest/docs/concepts/observability/

## License

MIT
