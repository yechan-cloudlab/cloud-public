import { z } from "zod";
import type { KeycloakClientApi } from "../keycloak-client.js";

export const ListRealmsArgs = z.object({});

export async function listRealms(api: KeycloakClientApi) {
  const realms = await api.listRealms();
  return realms.map((realm) => ({
    realm: realm.realm,
    enabled: realm.enabled ?? true,
  }));
}
