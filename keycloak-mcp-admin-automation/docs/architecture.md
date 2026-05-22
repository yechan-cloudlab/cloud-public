# Architecture

```text
Claude Desktop / Cursor
        |
        | MCP tool call
        v
Keycloak MCP Admin Automation Server
        |
        | Guardrails + dryRun + audit log
        v
Keycloak Admin REST API
        |
        v
Test Realm
```

The AI client does not directly modify Keycloak. It can only call MCP tools exposed by this server.

## Boundary

The important boundary is the MCP server, not the prompt.

A safe implementation should block dangerous requests in code even if the AI client asks for them.

## Recommended flow

1. Ask for dry-run.
2. Review planned users and roles.
3. Execute only in a test realm.
4. Validate results.
5. Roll back if needed.
