import fs from "node:fs";
import path from "node:path";
import { execFile } from "node:child_process";
import { config } from "../config";
import { resolveFfmpeg } from "./ffmpeg";

// Ищем ffprobe: env → рядом с ffmpeg → PATH. null = отдельного ffprobe нет,
// тогда используем разбор вывода ffmpeg (fallback).
export function resolveFfprobe(): string | null {
  if (config.ffmpeg.ffprobePath && fs.existsSync(config.ffmpeg.ffprobePath)) return config.ffmpeg.ffprobePath;
  const ff = resolveFfmpeg();
  if (ff && ff.includes("/")) {
    const cand = path.join(path.dirname(ff), "ffprobe");
    if (fs.existsSync(cand)) return cand;
  }
  // Проверяем PATH.
  for (const dir of (process.env.PATH || "").split(":")) {
    if (dir && fs.existsSync(path.join(dir, "ffprobe"))) return path.join(dir, "ffprobe");
  }
  return null;
}

export interface ProbeResult {
  ok: boolean;
  width: number | null;
  height: number | null;
  durationSeconds: number | null;
  hasVideo: boolean;
  hasAudio: boolean;
  raw?: string;
}

function run(bin: string, args: string[]): Promise<string> {
  return new Promise((resolve, reject) => {
    execFile(bin, args, { timeout: 30000, maxBuffer: 1024 * 1024 * 8 }, (err, stdout) => {
      if (err) return reject(err);
      resolve(stdout);
    });
  });
}

/** Готовый файл: разрешение, длительность, дорожки. ffprobe → иначе разбор ffmpeg. */
export async function probe(file: string): Promise<ProbeResult> {
  const bin = resolveFfprobe();
  if (bin) {
    try {
      const out = await run(bin, ["-v", "error", "-print_format", "json", "-show_format", "-show_streams", file]);
      const data = JSON.parse(out);
      const v = (data.streams || []).find((s: any) => s.codec_type === "video");
      const a = (data.streams || []).find((s: any) => s.codec_type === "audio");
      return {
        ok: true,
        width: v ? Number(v.width) : null,
        height: v ? Number(v.height) : null,
        durationSeconds: data.format?.duration ? Number(data.format.duration) : null,
        hasVideo: Boolean(v),
        hasAudio: Boolean(a),
        raw: out,
      };
    } catch (err) {
      return { ok: false, width: null, height: null, durationSeconds: null, hasVideo: false, hasAudio: false, raw: String(err) };
    }
  }
  return probeWithFfmpeg(file);
}

// Fallback: ffprobe нет — читаем stderr `ffmpeg -i file`.
async function probeWithFfmpeg(file: string): Promise<ProbeResult> {
  const ff = resolveFfmpeg();
  if (!ff) return { ok: false, width: null, height: null, durationSeconds: null, hasVideo: false, hasAudio: false };
  const stderr = await new Promise<string>((resolve) => {
    execFile(ff, ["-i", file], { timeout: 30000, maxBuffer: 1024 * 1024 * 8 }, (_e, _o, se) => resolve(String(se)));
  });
  const res = stderr.match(/Stream #\d+:\d+.*Video:.* (\d{2,5})x(\d{2,5})/);
  const dur = stderr.match(/Duration:\s*(\d+):(\d+):(\d+\.\d+)/);
  const hasVideo = /Video:/.test(stderr);
  const hasAudio = /Audio:/.test(stderr);
  const durationSeconds = dur ? Number(dur[1]) * 3600 + Number(dur[2]) * 60 + Number(dur[3]) : null;
  return {
    ok: hasVideo || hasAudio,
    width: res ? Number(res[1]) : null,
    height: res ? Number(res[2]) : null,
    durationSeconds,
    hasVideo,
    hasAudio,
    raw: stderr.slice(-600),
  };
}

export interface FinalCheck {
  passed: boolean;
  checks: Array<{ name: string; ok: boolean; detail?: string }>;
}

/**
 * Проверка финального файла из брифа: существует, не пустой, открывается,
 * 1080×1920, есть видео и аудио, длительность в разумных пределах.
 */
export async function verifyFinal(file: string, expectedSeconds: number): Promise<FinalCheck> {
  const checks: FinalCheck["checks"] = [];
  const add = (name: string, ok: boolean, detail?: string) => checks.push({ name, ok, detail });

  const exists = fs.existsSync(file);
  add("Файл существует", exists);
  if (!exists) return { passed: false, checks };

  const size = fs.statSync(file).size;
  add("Размер больше нуля", size > 0, `${size} байт`);

  const p = await probe(file);
  add("Открывается через ffprobe", p.ok, p.ok ? "" : "ffprobe не смог прочитать файл");
  add("Есть видеодорожка", p.hasVideo);
  add("Есть аудиодорожка", p.hasAudio);
  add("Разрешение 1080×1920", p.width === 1080 && p.height === 1920, `${p.width}×${p.height}`);
  if (p.durationSeconds != null) {
    const within = Math.abs(p.durationSeconds - expectedSeconds) <= Math.max(3, expectedSeconds * 0.4);
    add("Длительность близка к сценарию", within, `${p.durationSeconds?.toFixed(1)}с (ожидалось ~${expectedSeconds}с)`);
  }

  return { passed: checks.every((c) => c.ok), checks };
}
