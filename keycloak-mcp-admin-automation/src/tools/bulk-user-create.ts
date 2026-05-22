import { z } from "zod";
import { audit } from "../audit.js";
import type { AppConfig } from "../config.js";
import {
  assertAllowedRealm,
  assertReasonableBatchSize,
  assertSafeTemporaryPassword,
  assertWriteAllowed,
} from "../guardrails.js";
import type { KeycloakClient } from "../keycloak-client.js";

export const BulkUserCreateArgs = z.object({
  realm: z.string().min(1),
  department: z.string().min(1).optional(),
  users: z.array(
    z.object({
      username: z.string().min(1),
      email: z.string().email().optional(),
      firstName: z.string().optional(),
      lastName: z.string().optional(),
      enabled: z.boolean().optional(),
    }),
  ),
  temporaryPassword: z.string().min(10),
  dryRun: z.boolean().optional(),
});

export async function bulkUserCreate(
  config: AppConfig,
  client: KeycloakClient,
  input: z.infer<typeof BulkUserCreateArgs>,
) {
  const dryRun = input.dryRun ?? config.defaultDryRun;
  const requestId = crypto.randomUUID();

  assertAllowedRealm(config, input.realm);
  assertWriteAllowed(config, dryRun);
  assertReasonableBatchSize(input.users.length);
  assertSafeTemporaryPassword(input.temporaryPassword);

  const duplicated = input.users
    .map((user) => user.username)
    .filter((username, index, usernames) => usernames.indexOf(username) !== index);

  if (duplicated.length > 0) {
    throw new Error(`Duplicated usernames in request: ${[...new Set(duplicated)].join(", ")}`);
  }

  if (dryRun) {
    audit({
      requestId,
      tool: "bulk_user_create",
      realm: input.realm,
      dryRun,
      result: "dry_run",
      subjectCount: input.users.length,
    });

    return {
      requestId,
      dryRun,
      planned: input.users.map((user) => ({ username: user.username, email: user.email })),
    };
  }

  const results: Array<{ username: string; status: "created" | "failed"; error?: string }> = [];

  for (const user of input.users) {
    try {
      await client.createUser(input.realm, user, input.temporaryPassword);
      results.push({ username: user.username, status: "created" });
    } catch (error) {
      results.push({
        username: user.username,
        status: "failed",
        error: error instanceof Error ? error.message : String(error),
      });
    }
  }

  audit({
    requestId,
    tool: "bulk_user_create",
    realm: input.realm,
    dryRun,
    result: "success",
    subjectCount: input.users.length,
  });

  return { requestId, dryRun, results };
}
