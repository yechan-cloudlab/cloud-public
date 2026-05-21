# Security model

Keycloak MCP should be treated as a security boundary.

## Minimum recommendations

- Use a dedicated Keycloak service account.
- Use readonly realm-management roles where possible.
- Do not grant broad admin roles to the MCP client.
- Do not return client secrets.
- Do not return full user profiles by default.
- Run the MCP server on a trusted machine or private network.
- Do not expose the MCP server directly to the public internet.

## Data sensitivity

Even readonly access can reveal:

- realm names
- client IDs
- redirect URIs
- role names
- usernames
- group structure
- authentication policy design

Treat these as internal operational data.

## Tool boundary

Allowed tools should answer inspection questions only. Any tool that changes Keycloak state must be excluded from this sample.

Blocked examples:

- create user
- delete user
- reset password
- assign role
- update client
- read or rotate client secret
- update realm settings

## Logging

The sample writes simple audit events to stderr. A production system should send structured audit events to a central log system with retention and access controls.
