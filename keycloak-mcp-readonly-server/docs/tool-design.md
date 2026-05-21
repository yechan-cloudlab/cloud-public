# Tool design

## Readonly tools

### list_realms

Lists realms visible to the service account.

Output is intentionally small:

- realm
- enabled

### list_clients

Lists client metadata without secrets.

Output includes:

- clientId
- enabled
- publicClient
- protocol
- redirectUriCount
- webOriginCount

### check_redirect_uris

Finds redirect URIs that require review:

- wildcard redirect URIs
- localhost redirect URIs
- 127.0.0.1 redirect URIs

This is a heuristic check. A finding means "review this", not "this is automatically exploitable".

### list_users

Lists limited user metadata. Email values are masked.

Output includes:

- id
- username
- enabled
- emailVerified
- maskedEmail

Use search filters when possible. Do not dump all production users through an AI client.

### check_admin_roles

Lists realm roles whose names appear admin-like.

This sample does not fully resolve all user, group, and composite role assignments. Treat the output as a starting point for manual review.

## Not allowed

Do not implement these as MCP tools in this sample:

- delete_user
- reset_password
- assign_role
- update_role
- get_client_secret
- rotate_client_secret
- update_realm_settings
- delete_client
