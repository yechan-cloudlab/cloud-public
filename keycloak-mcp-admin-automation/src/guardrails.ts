import type { AppConfig } from "./config.js";

export function assertAllowedRealm(config: AppConfig, realm: string): void {
  if (!config.allowedRealms.includes(realm)) throw new Error("Blocked realm: " + realm);
}

export function assertWriteAllowed(config: AppConfig, dryRun: boolean): void {
  if (!dryRun && !config.allowWriteTools) throw new Error("Write tools are disabled. Set KEYCLOAK_ALLOW_WRITE_TOOLS=true only after review.");
}

export function assertSafeTemporaryPassword(password: string): void {
  if (password.length < 10) throw new Error("Temporary password must be at least 10 characters.");
  if (!/[A-Z]/.test(password) || !/[a-z]/.test(password) || !/[0-9]/.test(password)) throw new Error("Temporary password must include upper, lower, and number characters.");
}

export function assertReasonableBatchSize(count: number): void {
  if (count < 1) throw new Error("User batch must contain at least one user.");
  if (count > 100) throw new Error("This sample blocks batches larger than 100 users.");
}
