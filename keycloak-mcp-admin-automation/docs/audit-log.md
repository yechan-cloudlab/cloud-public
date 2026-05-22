# Audit Log

Audit events are written to stderr as JSON lines so stdout stays available for MCP stdio transport.

```json
{
  "timestamp": "2026-05-21T12:00:00.000Z",
  "requestId": "uuid",
  "tool": "bulk_user_create",
  "realm": "demo",
  "dryRun": true,
  "result": "dry_run",
  "subjectCount": 50
}
```

Do not log tokens, client secrets, passwords, or full user payloads.
