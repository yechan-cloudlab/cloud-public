import { readFileSync, readdirSync, statSync } from "node:fs";
import { join, relative } from "node:path";

const root = process.cwd();
const requiredFiles = [
  "README.md",
  "LICENSE",
  ".env.example",
  "package.json",
  "tsconfig.json",
  "src/index.ts",
  "src/keycloak-client.ts",
  "src/guardrails.ts",
  "docs/security-model.md",
  "docs/operation-checklist.md",
];

for (const file of requiredFiles) {
  statSync(join(root, file));
}

for (const file of ["package.json", "tsconfig.json", "examples/claude-desktop-config.json"]) {
  JSON.parse(readFileSync(join(root, file), "utf8"));
}

const files = [];
function walk(dir) {
  for (const name of readdirSync(dir)) {
    if (["node_modules", "dist", ".git"].includes(name)) continue;
    const path = join(dir, name);
    const stat = statSync(path);
    if (stat.isDirectory()) walk(path);
    else files.push(path);
  }
}
walk(root);

const secretPatterns = [
  /-----BEGIN [A-Z ]*PRIVATE KEY-----/,
  /AKIA[0-9A-Z]{16}/,
  /aws_secret_access_key\s*=/i,
  /^KEYCLOAK_CLIENT_SECRET=(?!replace-me)/m,
];

for (const file of files) {
  const text = readFileSync(file, "utf8");
  if (text.includes("\uFFFD")) {
    throw new Error(`Invalid replacement character found in ${relative(root, file)}`);
  }
  for (const pattern of secretPatterns) {
    if (pattern.test(text)) {
      throw new Error(`Possible secret found in ${relative(root, file)} using ${pattern}`);
    }
  }
}

const index = readFileSync(join(root, "src/index.ts"), "utf8");
const forbiddenToolNames = [
  "delete_user",
  "reset_password",
  "assign_role",
  "update_role",
  "get_client_secret",
  "update_realm_settings",
  "delete_client",
];
for (const tool of forbiddenToolNames) {
  if (index.includes(`server.tool("${tool}"`) || index.includes(`registerTool("${tool}"`)) {
    throw new Error(`Forbidden write-capable tool registered: ${tool}`);
  }
}

console.log("Repository validation passed.");
