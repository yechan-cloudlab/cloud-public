export type AppConfig = {
  keycloakBaseUrl: string;
  adminRealm: string;
  targetRealm: string;
  clientId: string;
  clientSecret: string;
};

export function loadConfig(): AppConfig {
  const required = [
    "KEYCLOAK_BASE_URL",
    "KEYCLOAK_ADMIN_REALM",
    "KEYCLOAK_TARGET_REALM",
    "KEYCLOAK_CLIENT_ID",
    "KEYCLOAK_CLIENT_SECRET",
  ];

  for (const key of required) {
    if (!process.env[key]) {
      throw new Error(`Missing required environment variable: ${key}`);
    }
  }

  if (process.env.KEYCLOAK_ALLOW_WRITE_TOOLS === "true") {
    throw new Error("This sample server is readonly. KEYCLOAK_ALLOW_WRITE_TOOLS must not be true.");
  }

  return {
    keycloakBaseUrl: process.env.KEYCLOAK_BASE_URL!.replace(/\/$/, ""),
    adminRealm: process.env.KEYCLOAK_ADMIN_REALM!,
    targetRealm: process.env.KEYCLOAK_TARGET_REALM!,
    clientId: process.env.KEYCLOAK_CLIENT_ID!,
    clientSecret: process.env.KEYCLOAK_CLIENT_SECRET!,
  };
}
