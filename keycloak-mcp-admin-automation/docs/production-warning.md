# Production Warning

Do not connect this sample directly to production.

Before production use, add:

- Change approval workflow
- Strong authentication around the MCP host
- Network isolation
- Rate limits
- Audit log retention
- Dedicated service account
- Secret manager integration
- Break-glass rollback process
- Legal and privacy review for user data

## Recommended production posture

For production, keep write tools behind an approval workflow.

A safer production pattern is:

1. MCP generates a change plan.
2. Human operator reviews the plan.
3. Existing IAM change process approves the request.
4. Automation executes with a short-lived credential.
5. Audit log is stored in a central log system.
