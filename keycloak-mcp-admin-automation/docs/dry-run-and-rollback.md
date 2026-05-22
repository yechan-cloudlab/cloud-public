# Dry-run and Rollback

## Dry-run

All write tools should be called with dry-run first.
Dry-run returns the planned operation but does not call write APIs.

## Rollback

Prefer disabling generated users before deleting them.
Deletion removes evidence and can make troubleshooting harder.

Recommended rollback flow:

1. Validate generated users
2. Disable users
3. Review impact
4. Delete only if approved
