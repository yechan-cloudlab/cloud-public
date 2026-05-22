import type { AppConfig } from "./config.js";
import type { UserInput } from "./types.js";

interface TokenResponse {
  access_token: string;
  expires_in: number;
}

interface KeycloakUserSummary {
  id: string;
  username: string;
}

interface KeycloakUserRepresentation {
  id?: string;
  username?: string;
  email?: string;
  firstName?: string;
  lastName?: string;
  enabled?: boolean;
  [key: string]: unknown;
}

interface KeycloakRole {
  id: string;
  name: string;
}

export class KeycloakClient {
  private token?: { value: string; expiresAt: number };

  constructor(private readonly config: AppConfig) {}

  private async getToken(): Promise<string> {
    if (this.token && Date.now() < this.token.expiresAt) {
      return this.token.value;
    }

    const url = `${this.config.keycloakBaseUrl}/realms/${this.config.adminRealm}/protocol/openid-connect/token`;
    const body = new URLSearchParams({
      grant_type: "client_credentials",
      client_id: this.config.clientId,
      client_secret: this.config.clientSecret,
    });

    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body,
    });

    if (!res.ok) {
      throw new Error(`Failed to get Keycloak token: HTTP ${res.status}`);
    }

    const json = (await res.json()) as TokenResponse;
    this.token = {
      value: json.access_token,
      expiresAt: Date.now() + Math.max(5, json.expires_in - 30) * 1000,
    };

    return json.access_token;
  }

  private async request<T>(realm: string, apiPath: string, init: RequestInit = {}): Promise<T> {
    const token = await this.getToken();
    const res = await fetch(`${this.config.keycloakBaseUrl}/admin/realms/${realm}${apiPath}`, {
      ...init,
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
        ...(init.headers ?? {}),
      },
    });

    if (!res.ok) {
      const body = await res.text();
      throw new Error(`Keycloak API failed: HTTP ${res.status} ${body.slice(0, 300)}`);
    }

    if (res.status === 204) {
      return undefined as T;
    }

    return (await res.json()) as T;
  }

  async createUser(realm: string, user: UserInput, temporaryPassword: string): Promise<void> {
    await this.request<void>(realm, "/users", {
      method: "POST",
      body: JSON.stringify({
        username: user.username,
        email: user.email,
        firstName: user.firstName,
        lastName: user.lastName,
        enabled: user.enabled ?? true,
        credentials: [
          {
            type: "password",
            value: temporaryPassword,
            temporary: true,
          },
        ],
        requiredActions: ["UPDATE_PASSWORD"],
      }),
    });
  }

  async findUserId(realm: string, username: string): Promise<string | undefined> {
    const users = await this.request<KeycloakUserSummary[]>(
      realm,
      `/users?username=${encodeURIComponent(username)}&exact=true`,
    );

    return users.find((user) => user.username === username)?.id;
  }

  async getUser(realm: string, userId: string): Promise<KeycloakUserRepresentation> {
    return this.request<KeycloakUserRepresentation>(realm, `/users/${encodeURIComponent(userId)}`);
  }

  async setUserEnabled(realm: string, userId: string, enabled: boolean): Promise<void> {
    const current = await this.getUser(realm, userId);
    await this.request<void>(realm, `/users/${encodeURIComponent(userId)}`, {
      method: "PUT",
      body: JSON.stringify({ ...current, enabled }),
    });
  }

  async deleteUser(realm: string, userId: string): Promise<void> {
    await this.request<void>(realm, `/users/${encodeURIComponent(userId)}`, {
      method: "DELETE",
    });
  }

  async listRealmRoles(realm: string): Promise<KeycloakRole[]> {
    return this.request<KeycloakRole[]>(realm, "/roles");
  }

  async listUserRealmRoles(realm: string, userId: string): Promise<KeycloakRole[]> {
    return this.request<KeycloakRole[]>(
      realm,
      `/users/${encodeURIComponent(userId)}/role-mappings/realm`,
    );
  }

  async assignRealmRoles(realm: string, userId: string, roles: KeycloakRole[]): Promise<void> {
    await this.request<void>(realm, `/users/${encodeURIComponent(userId)}/role-mappings/realm`, {
      method: "POST",
      body: JSON.stringify(roles),
    });
  }
}
