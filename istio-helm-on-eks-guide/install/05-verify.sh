#!/usr/bin/env bash
set -euo pipefail

kubectl get ns istio-system istio-ingress
kubectl get pods -n istio-system
kubectl get pods -n istio-ingress
kubectl get svc -n istio-ingress
kubectl get crd | grep 'istio.io' || true

echo
echo "If istioctl is installed, run:"
echo "  istioctl analyze"
echo "  istioctl proxy-status"
