import fs from "node:fs";
import path from "node:path";

const root = process.cwd();

const required = [
  "README.md",
  "LICENSE",
  "SECURITY.md",
  ".env.example",
  ".gitignore",
  "package.json",
  "tsconfig.json",
  "docker-compose.yml",
  "src/index.ts",
  "src/config.ts",
  "src/keycloak-client.ts",
  "src/guardrails.ts",
  "src/audit.ts",
  "src/tools/bulk-user-create.ts",
  "src/tools/assign-roles.ts",
  "src/tools/validate-users.ts",
  "src/tools/rollback-users.ts",
  "examples/claude-desktop-mcp.json",
  "examples/cursor-mcp.json",
  "examples/prompts.md",
  "docs/architecture.md",
  "docs/safety-model.md",
  "docs/keycloak-permissions.md",
  "docs/dry-run-and-rollback.md",
  "docs/audit-log.md",
  "docs/production-warning.md",
];

const missing = required.filter((file) => !fs.existsSync(path.join(root, file)));
if (missing.length) {
  console.error("Missing files:\n" + missing.join("\n"));
  process.exit(1);
}

const readme = fs.readFileSync(path.join(root, "README.md"), "utf8");
for (const phrase of ["test realms", "dryRun", "Rollback", "Audit", "Production", "Claude Desktop", "Cursor"]) {
  if (!readme.toLowerCase().includes(phrase.toLowerCase())) {
    console.error("README is missing phrase: " + phrase);
    process.exit(1);
  }
}

const env = fs.readFileSync(path.join(root, ".env.example"), "utf8");
if (!env.includes("KEYCLOAK_ALLOW_WRITE_TOOLS=false")) {
  console.error(".env.example must keep write tools disabled by default.");
  process.exit(1);
}
if (!env.includes("KEYCLOAK_DEFAULT_DRY_RUN=true")) {
  console.error(".env.example must keep dry-run enabled by default.");
  process.exit(1);
}

const allText = required
  .filter((file) => fs.existsSync(path.join(root, file)))
  .map((file) => fs.readFileSync(path.join(root, file), "utf8"))
  .join("\n");

for (const forbidden of ["KEYCLOAK_CLIENT_SECRET=real", "BEGIN PRIVATE KEY", "password=admin123"]) {
  if (allText.includes(forbidden)) {
    console.error("Potential secret-like text found: " + forbidden);
    process.exit(1);
  }
}

console.log("Repository validation passed.");
