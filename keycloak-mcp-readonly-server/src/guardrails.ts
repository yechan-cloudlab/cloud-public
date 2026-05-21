const blockedToolNames = new Set([
  "create_user",
  "delete_user",
  "reset_password",
  "update_user",
  "update_role",
  "assign_role",
  "remove_role",
  "get_client_secret",
  "rotate_client_secret",
  "update_realm_settings",
  "delete_client",
]);

export function assertReadonlyTool(toolName: string): void {
  if (blockedToolNames.has(toolName)) {
    throw new Error(`Blocked unsafe Keycloak MCP tool: ${toolName}`);
  }
}

export function maskEmail(email?: string): string | undefined {
  if (!email) return undefined;
  const [name, domain] = email.split("@");
  if (!name || !domain) return "***";
  return `${name.slice(0, 2)}***@${domain}`;
}

export function isRiskyRedirectUri(uri: string): boolean {
  const normalized = uri.toLowerCase();
  return (
    normalized.includes("*") ||
    normalized.startsWith("http://localhost") ||
    normalized.startsWith("http://127.0.0.1") ||
    normalized === "*"
  );
}
