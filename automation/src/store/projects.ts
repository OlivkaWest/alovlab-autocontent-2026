import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { config, ensureDataDir } from "../config";
import { createLogger } from "../logger";
import { Project, type HistoryEntry } from "./types";

const log = createLogger("store");

function projectsDir(): string {
  const dir = path.join(ensureDataDir(), "projects");
  fs.mkdirSync(dir, { recursive: true });
  return dir;
}

export function projectDir(id: string): string {
  const dir = path.join(projectsDir(), id);
  fs.mkdirSync(dir, { recursive: true });
  return dir;
}

function projectFile(id: string): string {
  return path.join(projectDir(id), "project.json");
}

export function newId(prefix = "prj"): string {
  return `${prefix}_${crypto.randomBytes(6).toString("hex")}`;
}

export function nowIso(): string {
  return new Date().toISOString();
}

/** Атомарная запись: пишем во временный файл, затем rename. Переживает перезапуск. */
function writeJsonAtomic(file: string, data: unknown): void {
  const tmp = `${file}.${crypto.randomBytes(4).toString("hex")}.tmp`;
  fs.writeFileSync(tmp, JSON.stringify(data, null, 2), "utf8");
  fs.renameSync(tmp, file);
}

export function saveProject(project: Project): Project {
  const parsed = Project.parse(project);
  parsed.updatedAt = nowIso();
  writeJsonAtomic(projectFile(parsed.id), parsed);
  return parsed;
}

export function loadProject(id: string): Project | null {
  const file = projectFile(id);
  if (!fs.existsSync(file)) return null;
  try {
    const raw = JSON.parse(fs.readFileSync(file, "utf8"));
    return Project.parse(raw);
  } catch (err) {
    log.error(`Не удалось прочитать проект ${id}`, String(err));
    return null;
  }
}

export function listProjects(): Project[] {
  const dir = projectsDir();
  if (!fs.existsSync(dir)) return [];
  const out: Project[] = [];
  for (const entry of fs.readdirSync(dir)) {
    const p = loadProject(entry);
    if (p) out.push(p);
  }
  return out.sort((a, b) => (a.createdAt < b.createdAt ? 1 : -1));
}

export function deleteProject(id: string): boolean {
  const dir = projectDir(id);
  if (!fs.existsSync(dir)) return false;
  fs.rmSync(dir, { recursive: true, force: true });
  return true;
}

export function addHistory(project: Project, action: string, detail = ""): Project {
  const entry: HistoryEntry = { at: nowIso(), action, detail };
  project.history.push(entry);
  return project;
}

export { config };
