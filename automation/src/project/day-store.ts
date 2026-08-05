import fs from "node:fs";
import path from "node:path";
import { z } from "zod";
import { config } from "../config";
import { monthDir } from "../dates";

// Статусы дня (из брифа: planned … ready/failed).
export const DAY_STATUSES = [
  "planned",
  "content_ready",
  "script_ready",
  "approved",
  "heygen_pending",
  "heygen_processing",
  "avatar_ready",
  "assembling",
  "ready",
  "failed",
] as const;
export const DayStatusEnum = z.enum(DAY_STATUSES);
export type DayStatusName = z.infer<typeof DayStatusEnum>;

export const DAY_STATUS_LABELS: Record<DayStatusName, string> = {
  planned: "Запланировано",
  content_ready: "Контент готов",
  script_ready: "Сценарий готов",
  approved: "Сценарий утверждён",
  heygen_pending: "Отправляем в HeyGen",
  heygen_processing: "Аватар создаётся",
  avatar_ready: "Аватар готов",
  assembling: "Собираем ролик",
  ready: "Ролик готов",
  failed: "Одна сцена сломалась",
};

export const HeygenJobRef = z.object({
  scene_id: z.string(),
  video_id: z.string(),
  status: z.string(),
  local_path: z.string().nullable().default(null),
});

export const DayStatus = z.object({
  date: z.string(),
  status: DayStatusEnum.default("planned"),
  topic: z.string().default(""),
  content_type: z.string().default(""),
  approved_script: z.string().nullable().default(null), // путь к утверждённой версии
  approved_final: z.string().nullable().default(null), // путь к утверждённому MP4
  heygen_jobs: z.array(HeygenJobRef).default([]),
  history: z.array(z.object({ at: z.string(), action: z.string(), detail: z.string().default("") })).default([]),
  updated_at: z.string(),
});
export type DayStatus = z.infer<typeof DayStatus>;

// ─── Пути ───
export function dayDir(date: string): string {
  return path.join(config.contentRoot, monthDir(date), date);
}
export function subDir(date: string, ...parts: string[]): string {
  const dir = path.join(dayDir(date), ...parts);
  fs.mkdirSync(dir, { recursive: true });
  return dir;
}
export function reelsDir(date: string): string {
  return subDir(date, "reels");
}

function statusFile(date: string): string {
  return path.join(dayDir(date), "status.json");
}

function nowIso(): string {
  return new Date().toISOString();
}

export function loadStatus(date: string): DayStatus | null {
  const f = statusFile(date);
  if (!fs.existsSync(f)) return null;
  try {
    return DayStatus.parse(JSON.parse(fs.readFileSync(f, "utf8")));
  } catch {
    return null;
  }
}

export function saveStatus(status: DayStatus): DayStatus {
  const parsed = DayStatus.parse({ ...status, updated_at: nowIso() });
  fs.mkdirSync(dayDir(parsed.date), { recursive: true });
  const f = statusFile(parsed.date);
  const tmp = `${f}.tmp`;
  fs.writeFileSync(tmp, JSON.stringify(parsed, null, 2), "utf8");
  fs.renameSync(tmp, f);
  return parsed;
}

export function ensureStatus(date: string, seed: Partial<DayStatus> = {}): DayStatus {
  const existing = loadStatus(date);
  if (existing) return existing;
  return saveStatus(DayStatus.parse({ date, updated_at: nowIso(), ...seed }));
}

export function setStatus(date: string, status: DayStatusName, action: string, detail = ""): DayStatus {
  const s = ensureStatus(date);
  s.status = status;
  s.history.push({ at: nowIso(), action, detail });
  return saveStatus(s);
}

// ─── Версионирование: reels_script_v1.json, final_reels_v2.mp4 … ───
export function latestVersion(dir: string, base: string, ext: string): number {
  if (!fs.existsSync(dir)) return 0;
  const re = new RegExp(`^${base}_v(\\d+)\\.${ext}$`);
  let max = 0;
  for (const f of fs.readdirSync(dir)) {
    const m = f.match(re);
    if (m) max = Math.max(max, Number(m[1]));
  }
  return max;
}

export function nextVersionPath(dir: string, base: string, ext: string): { path: string; version: number } {
  fs.mkdirSync(dir, { recursive: true });
  const version = latestVersion(dir, base, ext) + 1;
  return { path: path.join(dir, `${base}_v${version}.${ext}`), version };
}

export function writeVersioned(dir: string, base: string, ext: string, content: string): { path: string; version: number } {
  const { path: p, version } = nextVersionPath(dir, base, ext);
  fs.writeFileSync(p, content, "utf8");
  return { path: p, version };
}

export function appendLog(date: string, line: string): void {
  const f = path.join(reelsDir(date), "generation.log");
  fs.appendFileSync(f, `[${nowIso()}] ${line}\n`, "utf8");
}
