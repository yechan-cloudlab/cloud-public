# Keycloak permissions

This sample uses OAuth2 Client Credentials to call Keycloak Admin API.

## Recommended setup

1. Create a dedicated confidential client, for example `mcp-readonly`.
2. Enable service accounts for the client.
3. Assign only the realm-management roles needed for inspection.
4. Test against a development realm before connecting production.

## Minimum role direction

Exact roles depend on your Keycloak version and inspection scope. Start narrow and add only what a tool needs.

Common readonly needs:

- view-realm
- view-clients
- view-users

Avoid broad roles unless you understand the impact:

- realm-admin
- manage-users
- manage-clients
- manage-realm

## Do not expose

The MCP server should not expose:

- client secrets
- raw access tokens
- password reset actions
- user deletion
- role assignment changes
- realm setting updates

## Production note

Readonly does not mean harmless. Realm names, client IDs, redirect URIs, usernames, group structure, and role names can reveal internal security architecture.
