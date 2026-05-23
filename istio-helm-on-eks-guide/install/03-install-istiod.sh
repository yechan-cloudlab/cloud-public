#!/usr/bin/env bash
set -euo pipefail

helm upgrade --install istiod istio/istiod \
  --namespace istio-system \
  --values charts-values/istiod-values.yaml \
  --wait
