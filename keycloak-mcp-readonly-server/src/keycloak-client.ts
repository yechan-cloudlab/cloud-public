import type { AppConfig } from "./config.js";

export type KeycloakRealm = {
  id?: string;
  realm: string;
  enabled?: boolean;
};

export type KeycloakClient = {
  id: string;
  clientId: string;
  name?: string;
  enabled?: boolean;
  publicClient?: boolean;
  protocol?: string;
  redirectUris?: string[];
  webOrigins?: string[];
};

export type KeycloakUser = {
  id: string;
  username?: string;
  enabled?: boolean;
  emailVerified?: boolean;
  email?: string;
};

export class KeycloakClientApi {
  private accessToken?: string;
  private tokenExpiresAt = 0;

  constructor(private readonly config: AppConfig) {}

  async listRealms(): Promise<KeycloakRealm[]> {
    return this.request<KeycloakRealm[]>(`/admin/realms`);
  }

  async listClients(realm = this.config.targetRealm): Promise<KeycloakClient[]> {
    return this.request<KeycloakClient[]>(`/admin/realms/${encodeURIComponent(realm)}/clients`);
  }

  async listUsers(realm = this.config.targetRealm, search?: string): Promise<KeycloakUser[]> {
    const params = new URLSearchParams({ max: "50" });
    if (search) params.set("search", search);
    return this.request<KeycloakUser[]>(`/admin/realms/${encodeURIComponent(realm)}/users?${params}`);
  }

  async listRealmRoles(realm = this.config.targetRealm): Promise<Array<{ id: string; name: string; description?: string }>> {
    return this.request(`/admin/realms/${encodeURIComponent(realm)}/roles`);
  }

  private async request<T>(path: string): Promise<T> {
    const token = await this.getAccessToken();
    const response = await fetch(`${this.config.keycloakBaseUrl}${path}`, {
      headers: {
        Authorization: `Bearer ${token}`,
        Accept: "application/json",
      },
    });

    if (!response.ok) {
      const body = await response.text();
      throw new Error(`Keycloak API error ${response.status}: ${body}`);
    }

    return (await response.json()) as T;
  }

  private async getAccessToken(): Promise<string> {
    const now = Date.now();
    if (this.accessToken && now < this.tokenExpiresAt) {
      return this.accessToken;
    }

    const tokenUrl = `${this.config.keycloakBaseUrl}/realms/${encodeURIComponent(this.config.adminRealm)}/protocol/openid-connect/token`;
    const body = new URLSearchParams({
      grant_type: "client_credentials",
      client_id: this.config.clientId,
      client_secret: this.config.clientSecret,
    });

    const response = await fetch(tokenUrl, {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body,
    });

    if (!response.ok) {
      const text = await response.text();
      throw new Error(`Failed to get Keycloak access token ${response.status}: ${text}`);
    }

    const token = (await response.json()) as { access_token: string; expires_in?: number };
    this.accessToken = token.access_token;
    this.tokenExpiresAt = now + Math.max((token.expires_in ?? 60) - 10, 10) * 1000;
    return this.accessToken;
  }
}
