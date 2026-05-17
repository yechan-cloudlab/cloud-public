# values files

## Placeholder map

| Placeholder | Meaning |
| --- | --- |
| `{{KEYCLOAK_ADMIN_USER}}` | Keycloak admin username |
| `{{KEYCLOAK_ADMIN_SECRET_NAME}}` | Secret containing the admin password |
| `{{RDS_HOST}}` | External PostgreSQL or RDS endpoint |
| `{{KEYCLOAK_DB_USER}}` | Database username |
| `{{KEYCLOAK_DB_NAME}}` | Database name |
| `{{KEYCLOAK_DB_SECRET_NAME}}` | Secret containing database credentials |
| `{{INGRESS_CLASS_NAME}}` | Ingress class name |
| `{{KEYCLOAK_DOMAIN}}` | Public Keycloak hostname |
| `{{TLS_SECRET_NAME}}` | TLS Secret referenced by the Ingress |
| `{{REALM_CONFIGMAP_NAME}}` | ConfigMap containing declarative realm configuration |

## Notes

- `values-prod.example.yaml` assumes TLS terminates at Ingress.
- `values-dev.example.yaml` is only for local or short-lived environments.
- Replace placeholders before running Helm. They are not automatically rendered by Helm.
