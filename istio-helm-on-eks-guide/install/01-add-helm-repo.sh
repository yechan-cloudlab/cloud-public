#!/usr/bin/env bash
set -euo pipefail

helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update
helm search repo istio
