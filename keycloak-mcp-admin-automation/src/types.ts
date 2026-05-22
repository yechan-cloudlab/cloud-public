export type AuditResult = "dry_run" | "success" | "blocked" | "failed";

export interface UserInput {
  username: string;
  email?: string;
  firstName?: string;
  lastName?: string;
  enabled?: boolean;
}
