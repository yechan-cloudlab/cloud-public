import { z } from "zod";
import { audit } from "../audit.js";
import type { AppConfig } from "../config.js";
import { assertAllowedRealm, assertWriteAllowed } from "../guardrails.js";
import type { KeycloakClient } from "../keycloak-client.js";

export const RollbackUsersArgs = z.object({
  realm: z.string().min(1),
  usernames: z.array(z.string().min(1)).min(1).max(100),
  mode: z.enum(["disable", "delete"]).optional(),
  dryRun: z.boolean().optional(),
});

export async function rollbackUsers(
  config: AppConfig,
  client: KeycloakClient,
  input: z.infer<typeof RollbackUsersArgs>,
) {
  const dryRun = input.dryRun ?? config.defaultDryRun;
  const mode = input.mode ?? config.rollbackMode;
  const requestId = crypto.randomUUID();

  assertAllowedRealm(config, input.realm);
  assertWriteAllowed(config, dryRun);

  if (dryRun) {
    audit({
      requestId,
      tool: "rollback_users",
      realm: input.realm,
      dryRun,
      result: "dry_run",
      subjectCount: input.usernames.length,
    });

    return { requestId, dryRun, planned: { usernames: input.usernames, mode } };
  }

  const results: Array<{
    username: string;
    status: "disabled" | "deleted" | "not_found" | "failed";
    error?: string;
  }> = [];

  for (const username of input.usernames) {
    try {
      const userId = await client.findUserId(input.realm, username);
      if (!userId) {
        results.push({ username, status: "not_found" });
        continue;
      }

      if (mode === "delete") {
        await client.deleteUser(input.realm, userId);
        results.push({ username, status: "deleted" });
      } else {
        await client.setUserEnabled(input.realm, userId, false);
        results.push({ username, status: "disabled" });
      }
    } catch (error) {
      results.push({
        username,
        status: "failed",
        error: error instanceof Error ? error.message : String(error),
      });
    }
  }

  audit({
    requestId,
    tool: "rollback_users",
    realm: input.realm,
    dryRun,
    result: "success",
    subjectCount: input.usernames.length,
  });

  return { requestId, dryRun, mode, results };
}
