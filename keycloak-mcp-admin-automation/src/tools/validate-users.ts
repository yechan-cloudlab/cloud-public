import { z } from "zod";
import { audit } from "../audit.js";
import type { AppConfig } from "../config.js";
import { assertAllowedRealm } from "../guardrails.js";
import type { KeycloakClient } from "../keycloak-client.js";

export const ValidateUsersArgs = z.object({
  realm: z.string().min(1),
  usernames: z.array(z.string().min(1)).min(1).max(100),
  expectedRoles: z.array(z.string().min(1)).max(10).optional(),
});

export async function validateUsers(
  config: AppConfig,
  client: KeycloakClient,
  input: z.infer<typeof ValidateUsersArgs>,
) {
  const requestId = crypto.randomUUID();
  assertAllowedRealm(config, input.realm);

  const results: Array<{
    username: string;
    exists: boolean;
    roles?: string[];
    missingRoles?: string[];
  }> = [];

  for (const username of input.usernames) {
    const userId = await client.findUserId(input.realm, username);

    if (!userId) {
      results.push({ username, exists: false });
      continue;
    }

    if (input.expectedRoles && input.expectedRoles.length > 0) {
      const roles = await client.listUserRealmRoles(input.realm, userId);
      const roleNames = roles.map((role) => role.name);
      const missingRoles = input.expectedRoles.filter((role) => !roleNames.includes(role));
      results.push({ username, exists: true, roles: roleNames, missingRoles });
      continue;
    }

    results.push({ username, exists: true });
  }

  audit({
    requestId,
    tool: "validate_users",
    realm: input.realm,
    dryRun: false,
    result: "success",
    subjectCount: input.usernames.length,
  });

  return { requestId, results };
}
