"""Check registry for manifest audit rules."""

from collections.abc import Callable

from eks_manifest_auditor.checks.ingress import check_ingress_annotations
from eks_manifest_auditor.checks.security import (
    check_allow_privilege_escalation,
    check_default_namespace,
    check_host_path_volumes,
    check_privileged_containers,
    check_run_as_non_root,
)
from eks_manifest_auditor.checks.service import check_load_balancer_service, check_node_port_service
from eks_manifest_auditor.checks.serviceaccount import check_irsa_annotation
from eks_manifest_auditor.checks.workload import (
    check_image_latest_tag,
    check_replicas,
    check_resource_limits,
    check_resource_requests,
)
from eks_manifest_auditor.models import Finding, ManifestResource

Check = Callable[[ManifestResource], list[Finding]]

CHECKS: list[Check] = [
    check_resource_requests,
    check_resource_limits,
    check_image_latest_tag,
    check_replicas,
    check_privileged_containers,
    check_host_path_volumes,
    check_default_namespace,
    check_allow_privilege_escalation,
    check_run_as_non_root,
    check_load_balancer_service,
    check_node_port_service,
    check_ingress_annotations,
    check_irsa_annotation,
]
