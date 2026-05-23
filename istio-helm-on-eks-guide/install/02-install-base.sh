#!/usr/bin/env bash
set -euo pipefail

kubectl create namespace istio-system --dry-run=client -o yaml | kubectl apply -f -

helm upgrade --install istio-base istio/base \
  --namespace istio-system \
  --values charts-values/istio-base-values.yaml \
  --wait
