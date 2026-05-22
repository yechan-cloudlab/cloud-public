# Keycloak MCP Admin Automation

Sample MCP server for **Keycloak admin automation in test realms**.

This repository demonstrates a safe pattern for using Claude Desktop or Cursor to automate repetitive Keycloak administration tasks through controlled MCP tools.

> WARNING: This is a sample project for test realms. Do not connect it directly to a production realm without reviewing permissions, audit logging, approval flow, rate limits, and rollback strategy.

## What this sample does

```text
"Create 30 development team users and assign grafana-reader role. Run dry-run first."
```

The AI client does not directly modify Keycloak. It calls a limited MCP server, and the MCP server applies guardrails before calling Keycloak Admin REST API.

## Features

| Feature | Included |
| --- | --- |
| Bulk user creation | Yes |
| Realm role assignment | Yes |
| User validation | Yes |
| Rollback by disable/delete | Yes |
| dryRun default | Yes |
| Realm allowlist | Yes |
| Batch size limit | Yes |
| Audit log | Yes |
| Production-ready IAM platform | No |

## Safety defaults

| Item | Default |
| --- | --- |
| Write operations | Disabled unless explicitly enabled |
| Tool execution | `dryRun: true` first |
| Realm access | Allowlist required |
| Rollback | `disable` preferred over `delete` |
| Audit log | JSON lines to stderr |
| Production realm | Not recommended |

## Architecture

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

## Tools

| Tool | Purpose | Default behavior |
| --- | --- | --- |
| `bulk_user_create` | Create multiple Keycloak users | `dryRun: true` |
| `assign_roles` | Assign realm roles to users | `dryRun: true` |
| `validate_users` | Validate whether users exist and optionally check expected realm roles | read-only |
| `rollback_users` | Disable or delete generated users | `dryRun: true`, `disable` preferred |

## Repository structure

```text
keycloak-mcp-admin-automation/
|- README.md
|- SECURITY.md
|- .env.example
|- docker-compose.yml
|- src/
|  |- index.ts
|  |- config.ts
|  |- keycloak-client.ts
|  |- audit.ts
|  |- guardrails.ts
|  |- tools/
|     |- bulk-user-create.ts
|     |- assign-roles.ts
|     |- validate-users.ts
|     |- rollback-users.ts
|- examples/
|  |- claude-desktop-mcp.json
|  |- cursor-mcp.json
|  |- users.sample.csv
|  |- users.sample.json
|  |- prompts.md
|- scripts/
|  |- validate-repo.mjs
|  |- smoke-test.mjs
|- docs/
   |- architecture.md
   |- safety-model.md
   |- keycloak-permissions.md
   |- dry-run-and-rollback.md
   |- audit-log.md
   |- production-warning.md
```

## Quick start

### 1. Install dependencies

```bash
npm install
```

### 2. Start local Keycloak for testing

```bash
docker compose up -d
```

Open Keycloak:

```text
http://localhost:8080
```

Default local admin account from `docker-compose.yml`:

```text
username: admin
password: admin
```

### 3. Create a test realm and service account

Create a test realm named `demo` and a confidential client named `mcp-admin-automation`.

Recommended docs:

- `docs/keycloak-permissions.md`
- `docs/production-warning.md`

### 4. Configure environment

```bash
cp .env.example .env
```

Update `.env` with your test Keycloak values.

Important defaults:

```env
KEYCLOAK_ALLOWED_REALMS=demo
KEYCLOAK_ALLOW_WRITE_TOOLS=false
KEYCLOAK_DEFAULT_DRY_RUN=true
```

### 5. Build and validate

```bash
npm run build
npm run validate
```

### 6. Connect from Claude Desktop or Cursor

Use one of these examples:

- `examples/claude-desktop-mcp.json`
- `examples/cursor-mcp.json`

Replace `/absolute/path/to/keycloak-mcp-admin-automation/dist/index.js` with your local path.

## Example prompts

### Dry-run user creation

```text
Create 50 marketing team users in the demo realm.
Use usernames marketing001 to marketing050.
Use emails marketing001@example.com to marketing050@example.com.
Set temporary password Temp123!ChangeMe.
Require password update on first login.
Run dry-run first.
```

### Assign role after review

```text
Assign grafana-reader role to marketing001 through marketing050 in the demo realm.
Run dry-run first.
```

### Rollback

```text
Disable marketing001 through marketing050 in the demo realm.
Run dry-run first.
```

## Production warning

Do not run this against production without:

- Separate service account
- Minimum Keycloak admin roles
- Realm allowlist
- dry-run approval step
- Audit log retention
- Rate limit
- Rollback plan
- Change approval workflow
- Secret manager integration
- Review of user data handling policy

## Related articles

- [Claude한테 “키클락 유저 100명 생성해줘” 했더니 10초 만에 끝났다: Keycloak MCP 자동화 실전](https://tistory-cloud.tistory.com/entry/Claude%ED%95%9C%ED%85%8C-%E2%80%9C%ED%82%A4%ED%81%B4%EB%9D%BD-%EC%9C%A0%EC%A0%80-100%EB%AA%85-%EC%83%9D%EC%84%B1%ED%95%B4%EC%A4%98%E2%80%9D-%ED%96%88%EB%8D%94%EB%8B%88-10%EC%B4%88-%EB%A7%8C%EC%97%90-%EB%81%9D%EB%82%AC%EB%8B%A4-Keycloak-MCP-%EC%9E%90%EB%8F%99%ED%99%94-%EC%8B%A4%EC%A0%84)

This article explains the operational context behind this repository, including dry-run, rollback, service account scope, and test-realm-only guardrails.

## License

MIT
