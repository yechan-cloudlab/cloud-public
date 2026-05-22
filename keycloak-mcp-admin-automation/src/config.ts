export interface AppConfig {
  keycloakBaseUrl: string;
  adminRealm: string;
  targetRealm: string;
  clientId: string;
  clientSecret: string;
  allowedRealms: string[];
  allowWriteTools: boolean;
  defaultDryRun: boolean;
  rollbackMode: "disable" | "delete";
}

function required(name: string): string {
  const value = process.env[name];
  if (!value) throw new Error("Missing required environment variable: " + name);
  return value;
}

export function loadConfig(): AppConfig {
  const allowedRealms = (process.env.KEYCLOAK_ALLOWED_REALMS ?? "demo").split(",").map((v) => v.trim()).filter(Boolean);
  return {
    keycloakBaseUrl: required("KEYCLOAK_BASE_URL").replace(/\/$/, ""),
    adminRealm: process.env.KEYCLOAK_ADMIN_REALM ?? "master",
    targetRealm: process.env.KEYCLOAK_TARGET_REALM ?? "demo",
    clientId: required("KEYCLOAK_CLIENT_ID"),
    clientSecret: required("KEYCLOAK_CLIENT_SECRET"),
    allowedRealms,
    allowWriteTools: process.env.KEYCLOAK_ALLOW_WRITE_TOOLS === "true",
    defaultDryRun: process.env.KEYCLOAK_DEFAULT_DRY_RUN !== "false",
    rollbackMode: process.env.KEYCLOAK_ROLLBACK_MODE === "delete" ? "delete" : "disable"
  };
}
