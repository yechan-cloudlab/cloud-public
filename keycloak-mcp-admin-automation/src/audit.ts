import type { AuditResult } from "./types.js";

export interface AuditEvent {
  requestId: string;
  tool: string;
  realm: string;
  result: AuditResult;
  dryRun: boolean;
  subjectCount?: number;
  message?: string;
}

export function audit(event: AuditEvent): void {
  console.error(JSON.stringify({ timestamp: new Date().toISOString(), ...event }));
}
