import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { loadConfig } from "./config.js";
import { KeycloakClient } from "./keycloak-client.js";
import { AssignRolesArgs, assignRoles } from "./tools/assign-roles.js";
import { BulkUserCreateArgs, bulkUserCreate } from "./tools/bulk-user-create.js";
import { RollbackUsersArgs, rollbackUsers } from "./tools/rollback-users.js";
import { ValidateUsersArgs, validateUsers } from "./tools/validate-users.js";

const config = loadConfig();
const keycloak = new KeycloakClient(config);

const server = new McpServer({
  name: "keycloak-mcp-admin-automation",
  version: "0.1.0",
});

server.tool(
  "bulk_user_create",
  "Create multiple Keycloak users. Default is dry-run.",
  BulkUserCreateArgs.shape,
  async (input) => {
    const result = await bulkUserCreate(config, keycloak, input);
    return { content: [{ type: "text", text: JSON.stringify(result, null, 2) }] };
  },
);

server.tool(
  "assign_roles",
  "Assign realm roles to Keycloak users. Default is dry-run.",
  AssignRolesArgs.shape,
  async (input) => {
    const result = await assignRoles(config, keycloak, input);
    return { content: [{ type: "text", text: JSON.stringify(result, null, 2) }] };
  },
);

server.tool(
  "validate_users",
  "Validate whether Keycloak users exist.",
  ValidateUsersArgs.shape,
  async (input) => {
    const result = await validateUsers(config, keycloak, input);
    return { content: [{ type: "text", text: JSON.stringify(result, null, 2) }] };
  },
);

server.tool(
  "rollback_users",
  "Disable or delete users created by automation. Default is dry-run and disable mode.",
  RollbackUsersArgs.shape,
  async (input) => {
    const result = await rollbackUsers(config, keycloak, input);
    return { content: [{ type: "text", text: JSON.stringify(result, null, 2) }] };
  },
);

await server.connect(new StdioServerTransport());
