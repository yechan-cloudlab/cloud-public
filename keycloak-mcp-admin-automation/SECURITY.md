# Security Policy

This repository is a sample for test realms.

## Do not commit secrets

Never commit Keycloak client secrets, access tokens, refresh tokens, production realm URLs, or real user lists.

## Recommended controls

- Use a dedicated service account
- Keep write tools disabled by default
- Use dry-run before execution
- Keep audit logs
- Prefer disabling users over deleting users during rollback
- Review generated users before role assignment
