import { z } from "zod";
import type { KeycloakClientApi } from "../keycloak-client.js";
import { maskEmail } from "../guardrails.js";

export const ListUsersArgs = z.object({
  realm: z.string().optional(),
  search: z.string().optional(),
});

export async function listUsers(api: KeycloakClientApi, args: z.infer<typeof ListUsersArgs>) {
  const users = await api.listUsers(args.realm, args.search);
  return users.map((user) => ({
    id: user.id,
    username: user.username,
    enabled: user.enabled,
    emailVerified: user.emailVerified,
    maskedEmail: maskEmail(user.email),
  }));
}
