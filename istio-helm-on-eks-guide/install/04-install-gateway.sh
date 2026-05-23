#!/usr/bin/env bash
set -euo pipefail

kubectl create namespace istio-ingress --dry-run=client -o yaml | kubectl apply -f -

helm upgrade --install istio-ingress istio/gateway \
  --namespace istio-ingress \
  --values charts-values/istio-gateway-values.yaml \
  --wait
