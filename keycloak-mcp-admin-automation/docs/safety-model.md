# Safety Model

This sample assumes Keycloak write automation is dangerous by default.

## Controls

- Realm allowlist
- dry-run default
- write tools disabled by default
- batch size limit
- temporary password policy
- audit logging
- rollback workflow

## Non-goals

This repository is not a production-ready IAM automation platform.
It is a sample that demonstrates safe patterns for test realms.
