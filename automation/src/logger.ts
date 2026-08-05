import { maskSecret, config } from "./config";

type Level = "debug" | "info" | "warn" | "error";

// Секреты, которые нельзя выводить в лог целиком.
function scrub(msg: unknown): unknown {
  if (typeof msg !== "string") return msg;
  let out = msg;
  for (const secret of [config.heygen.apiKey, config.heygen.webhookSecret, config.llm.anthropicKey]) {
    if (secret && secret.length > 6) {
      out = out.split(secret).join(maskSecret(secret));
    }
  }
  return out;
}

function line(level: Level, scope: string, msg: unknown, extra?: unknown) {
  const ts = new Date().toISOString();
  const parts: unknown[] = [`[${ts}] ${level.toUpperCase()} (${scope})`, scrub(msg)];
  if (extra !== undefined) parts.push(scrub(extra));
  // eslint-disable-next-line no-console
  const fn = level === "error" ? console.error : level === "warn" ? console.warn : console.log;
  fn(...parts);
}

export function createLogger(scope: string) {
  return {
    debug: (m: unknown, e?: unknown) => line("debug", scope, m, e),
    info: (m: unknown, e?: unknown) => line("info", scope, m, e),
    warn: (m: unknown, e?: unknown) => line("warn", scope, m, e),
    error: (m: unknown, e?: unknown) => line("error", scope, m, e),
  };
}

export type Logger = ReturnType<typeof createLogger>;
