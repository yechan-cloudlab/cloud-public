import { z } from "zod";
import { audit } from "../audit.js";
import type { AppConfig } from "../config.js";
import { assertAllowedRealm, assertWriteAllowed } from "../guardrails.js";
import type { KeycloakClient } from "../keycloak-client.js";

export const AssignRolesArgs = z.object({
  realm: z.string().min(1),
  usernames: z.array(z.string().min(1)).min(1).max(100),
  roles: z.array(z.string().min(1)).min(1).max(10),
  dryRun: z.boolean().optional(),
});

export async function assignRoles(
  config: AppConfig,
  client: KeycloakClient,
  input: z.infer<typeof AssignRolesArgs>,
) {
  const dryRun = input.dryRun ?? config.defaultDryRun;
  const requestId = crypto.randomUUID();

  assertAllowedRealm(config, input.realm);
  assertWriteAllowed(config, dryRun);

  if (dryRun) {
    audit({
      requestId,
      tool: "assign_roles",
      realm: input.realm,
      dryRun,
      result: "dry_run",
      subjectCount: input.usernames.length,
    });

    return { requestId, dryRun, planned: { usernames: input.usernames, roles: input.roles } };
  }

  const realmRoles = await client.listRealmRoles(input.realm);
  const selectedRoles = realmRoles.filter((role) => input.roles.includes(role.name));
  const missingRoles = input.roles.filter((roleName) => !selectedRoles.some((role) => role.name === roleName));

  if (missingRoles.length > 0) {
    throw new Error(`Role not found in realm ${input.realm}: ${missingRoles.join(", ")}`);
  }

  const results: Array<{ username: string; status: "assigned" | "failed"; error?: string }> = [];

  for (const username of input.usernames) {
    try {
      const userId = await client.findUserId(input.realm, username);
      if (!userId) throw new Error("User not found");

      await client.assignRealmRoles(input.realm, userId, selectedRoles);
      results.push({ username, status: "assigned" });
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
    tool: "assign_roles",
    realm: input.realm,
    dryRun,
    result: "success",
    subjectCount: input.usernames.length,
  });

  return { requestId, dryRun, results };
}
