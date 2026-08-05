import path from "node:path";
import fs from "node:fs";
import dotenv from "dotenv";

// Грузим .env из папки automation, если он есть. Секреты только локально.
dotenv.config({ path: path.resolve(__dirname, "..", ".env") });

function bool(v: string | undefined, def = false): boolean {
  if (v === undefined || v === "") return def;
  return ["1", "true", "yes", "on"].includes(v.trim().toLowerCase());
}
function num(v: string | undefined): number | null {
  if (v === undefined || v === "") return null;
  const n = Number(v);
  return Number.isFinite(n) ? n : null;
}

// Корень репозитория (…/automation/src → repo root).
export const repoRoot = path.resolve(__dirname, "..", "..");

// Куда пишутся дни производства. По умолчанию — content/ в корне репозитория.
const contentRoot = path.isAbsolute(process.env.CONTENT_ROOT || "")
  ? (process.env.CONTENT_ROOT as string)
  : path.resolve(repoRoot, process.env.CONTENT_ROOT || "content");

const dataDir = path.resolve(__dirname, "..", process.env.DATA_DIR || "./data");

export const config = {
  repoRoot,
  contentRoot,
  dataDir,

  heygen: {
    apiKey: process.env.HEYGEN_API_KEY || "",
    apiBase: (process.env.HEYGEN_API_BASE || "https://api.heygen.com").replace(/\/+$/, ""),
    avatarId: process.env.HEYGEN_AVATAR_ID || "",
    voiceId: process.env.HEYGEN_VOICE_ID || "",
    language: process.env.HEYGEN_DEFAULT_LANGUAGE || "ru",
    engine: process.env.HEYGEN_DEFAULT_ENGINE || "",
    webhookSecret: process.env.HEYGEN_WEBHOOK_SECRET || "",
    mock: bool(process.env.HEYGEN_MOCK_MODE, true),
  },

  grok: {
    apiKey: process.env.XAI_API_KEY || "",
    apiBase: (process.env.XAI_API_BASE || "https://api.x.ai").replace(/\/+$/, ""),
    model: process.env.XAI_VIDEO_MODEL || "grok-imagine-video-1.5",
    resolution: process.env.XAI_VIDEO_RESOLUTION || "1080p",
    aspectRatio: process.env.XAI_VIDEO_ASPECT_RATIO || "9:16",
    mock: bool(process.env.XAI_VIDEO_MOCK_MODE, true),
  },

  higgsfield: {
    // Higgsfield подключается через MCP в самом Claude Code (не через ключ в .env).
    // Флаг только для оффлайн-прогонов пайплайна.
    mock: bool(process.env.HIGGSFIELD_MOCK_MODE, true),
  },

  video: {
    maxCostUsd: num(process.env.MAX_VIDEO_GENERATION_COST_USD),
    maxRetries: Number(process.env.VIDEO_GENERATION_MAX_RETRIES || 2),
    allowAutoGenerate: bool(process.env.ALLOW_AUTO_GENERATE, true),
  },

  ffmpeg: {
    ffmpegPath: process.env.FFMPEG_PATH || "",
    ffprobePath: process.env.FFPROBE_PATH || "",
  },

  llm: {
    provider: (process.env.LLM_PROVIDER || "template") as "template" | "anthropic",
    anthropicKey: process.env.ANTHROPIC_API_KEY || "",
    anthropicModel: process.env.ANTHROPIC_MODEL || "claude-opus-4-8",
  },
} as const;

export function ensureDataDir(): string {
  fs.mkdirSync(config.dataDir, { recursive: true });
  return config.dataDir;
}

/** Маскирует секрет для логов и сообщений: keep первые/последние символы. */
export function maskSecret(secret: string | undefined | null): string {
  if (!secret) return "(не задан)";
  const s = String(secret);
  if (s.length <= 8) return "****";
  return `${s.slice(0, 4)}…${s.slice(-2)}`;
}

/** Готов ли аватар Нейромонах к запуску (есть avatar_id и voice_id). */
export function neuromonkReady(): { ready: boolean; message?: string } {
  // В mock-режиме ключи не нужны — пайплайн проходит целиком без трат.
  if (config.heygen.mock) return { ready: true };
  if (!config.heygen.avatarId || !config.heygen.voiceId) {
    return {
      ready: false,
      message: "Добавь HEYGEN_AVATAR_ID и HEYGEN_VOICE_ID в настройки проекта",
    };
  }
  return { ready: true };
}
