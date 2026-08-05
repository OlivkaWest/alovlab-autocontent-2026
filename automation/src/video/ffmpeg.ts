import fs from "node:fs";
import path from "node:path";
import { execFile } from "node:child_process";
import { config } from "../config";
import { createLogger } from "../logger";

const log = createLogger("ffmpeg");

// Целевой вертикальный формат.
export const OUT_WIDTH = 1080;
export const OUT_HEIGHT = 1920;

/**
 * Находит ПОЛНОЦЕННЫЙ ffmpeg: env → системный ffmpeg в PATH → бинарь Playwright.
 * Внимание: ffmpeg из Playwright — урезанная сборка без libx264, поэтому он идёт
 * последним, только как крайний fallback.
 */
export function resolveFfmpeg(): string | null {
  if (config.ffmpeg.ffmpegPath && fs.existsSync(config.ffmpeg.ffmpegPath)) return config.ffmpeg.ffmpegPath;
  // Системный ffmpeg (общего назначения) — приоритет.
  for (const p of ["/usr/bin/ffmpeg", "/usr/local/bin/ffmpeg", "/opt/homebrew/bin/ffmpeg"]) {
    if (fs.existsSync(p)) return p;
  }
  for (const dir of (process.env.PATH || "").split(":")) {
    if (dir && fs.existsSync(path.join(dir, "ffmpeg"))) return path.join(dir, "ffmpeg");
  }
  // Крайний fallback — урезанный ffmpeg из Playwright (может не уметь libx264).
  const base = process.env.PLAYWRIGHT_BROWSERS_PATH || "/opt/pw-browsers";
  try {
    const dirs = fs.readdirSync(base).filter((d) => d.startsWith("ffmpeg-"));
    for (const d of dirs) {
      const candidate = path.join(base, d, "ffmpeg-linux");
      if (fs.existsSync(candidate)) return candidate;
    }
  } catch {
    /* нет каталога */
  }
  return null;
}

export function hasFfmpeg(): boolean {
  const bin = resolveFfmpeg();
  if (!bin) return false;
  if (bin.includes("/")) return fs.existsSync(bin);
  return true; // положимся на PATH
}

/**
 * Валидирует, что аргумент безопасен как элемент argv:
 * без null-байтов и переводов строк. Мы НИКОГДА не собираем shell-строку —
 * запуск идёт через execFile с массивом аргументов.
 */
export function assertSafeArg(arg: string): string {
  if (/[\s\u0000-\u001f]/.test(arg)) {
    throw new Error("Небезопасный аргумент ffmpeg (управляющие символы)");
  }
  return arg;
}

/** Запуск ffmpeg через execFile (массив аргументов, без shell). */
export function runFfmpeg(args: string[], opts: { timeoutMs?: number } = {}): Promise<{ code: number; stderr: string }> {
  const bin = resolveFfmpeg();
  if (!bin) return Promise.reject(new Error("ffmpeg не найден"));
  args.forEach(assertSafeArg);
  return new Promise((resolve, reject) => {
    execFile(
      bin,
      args,
      { timeout: opts.timeoutMs ?? 120000, maxBuffer: 1024 * 1024 * 32, shell: false },
      (err, _stdout, stderr) => {
        if (err && (err as any).killed) return reject(new Error("ffmpeg таймаут"));
        if (err && typeof (err as any).code === "number" && (err as any).code !== 0) {
          return reject(new Error(`ffmpeg завершился с кодом ${(err as any).code}: ${String(stderr).slice(-400)}`));
        }
        if (err) return reject(err);
        resolve({ code: 0, stderr: String(stderr) });
      }
    );
  });
}

// ─── Чистые построители команд (тестируются без запуска ffmpeg) ───

/** Привести один клип к 9:16 1080×1920 (pad, без обрезки лиц). */
export function buildScaleArgs(input: string, output: string): string[] {
  return [
    "-y",
    "-i", input,
    "-vf",
    `scale=${OUT_WIDTH}:${OUT_HEIGHT}:force_original_aspect_ratio=decrease,pad=${OUT_WIDTH}:${OUT_HEIGHT}:(ow-iw)/2:(oh-ih)/2:color=#0b0a09,setsar=1`,
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    output,
  ];
}

/** Собрать статичный клип из PNG-карточки с медленным push-in (Ken Burns). */
export function buildCardClipArgs(png: string, output: string, seconds: number): string[] {
  const frames = Math.max(1, Math.round(seconds * 30));
  return [
    "-y",
    "-loop", "1",
    "-i", png,
    "-t", String(seconds),
    "-r", "30",
    "-vf",
    `scale=${OUT_WIDTH * 1.08}:-1,zoompan=z='min(zoom+0.0006,1.08)':d=${frames}:s=${OUT_WIDTH}x${OUT_HEIGHT}:fps=30,setsar=1`,
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    output,
  ];
}

/** Брендовый фоновый видеоклип 9:16 (fallback, когда нет ни аватара, ни карточки). */
export function buildColorClipArgs(output: string, seconds: number): string[] {
  return [
    "-y",
    "-f", "lavfi",
    "-i", `color=c=#0b0a09:s=${OUT_WIDTH}x${OUT_HEIGHT}:d=${seconds}:r=30`,
    "-t", String(seconds),
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    output,
  ];
}

/** Конкатенация клипов через файл-список (concat demuxer). */
export function buildConcatArgs(listFile: string, output: string): string[] {
  return ["-y", "-f", "concat", "-safe", "0", "-i", listFile, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30", output];
}

export interface AssembleOptions {
  videoInput: string; // склеенное видео сцен
  voiceInput?: string; // общий закадровый голос (опц.)
  musicInput?: string; // фоновая музыка (опц.)
  subtitleFile?: string; // .srt/.ass для вшивания (опц.)
  logoInput?: string; // PNG логотипа для финала (опц.)
  output: string;
  burnSubtitles: boolean;
}

/**
 * Финальная сборка: голос + музыка (с приглушением под голосом) + субтитры.
 * Субтитры вшиваются из ФАЙЛА (subtitles=filename) — пользовательский текст
 * не попадает в строку команды.
 */
export function buildAssembleArgs(o: AssembleOptions): string[] {
  const args: string[] = ["-y", "-i", o.videoInput];
  const filters: string[] = [];
  let audioMap = "";

  if (o.voiceInput) args.push("-i", o.voiceInput);
  if (o.musicInput) args.push("-i", o.musicInput);

  // Аудио: музыка приглушается под голосом (sidechaincompress / volume).
  if (o.voiceInput && o.musicInput) {
    filters.push("[2:a]volume=0.18[music]");
    filters.push("[1:a][music]amix=inputs=2:duration=first:dropout_transition=2[aout]");
    audioMap = "[aout]";
  } else if (o.voiceInput) {
    audioMap = "1:a";
  } else if (o.musicInput) {
    filters.push("[1:a]volume=0.3[aout]");
    audioMap = "[aout]";
  }

  // Видео-цепочка: (опц.) субтитры из файла.
  let vlabel = "0:v";
  if (o.burnSubtitles && o.subtitleFile) {
    const safe = o.subtitleFile.replace(/([:\\'])/g, "\\$1");
    filters.push(
      `[0:v]subtitles='${safe}':force_style='Fontsize=16,PrimaryColour=&H00FFFFFF,Alignment=2,MarginV=90,Outline=2'[vout]`
    );
    vlabel = "[vout]";
  }

  if (filters.length) args.push("-filter_complex", filters.join(";"));
  args.push("-map", vlabel);
  if (audioMap) args.push("-map", audioMap);

  args.push("-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", "30");
  if (audioMap) args.push("-c:a", "aac", "-b:a", "192k", "-shortest");
  args.push("-movflags", "+faststart", o.output);
  return args;
}

/** Тихая аудиодорожка mp3 заданной длительности (для mock-озвучки). */
export async function synthSilentMp3(output: string, seconds: number): Promise<boolean> {
  if (!hasFfmpeg()) return false;
  const args = [
    "-y",
    "-f", "lavfi",
    "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
    "-t", String(Math.max(1, seconds)),
    "-c:a", "libmp3lame", "-b:a", "128k",
    output,
  ];
  try {
    await runFfmpeg(args, { timeoutMs: 60000 });
    return fs.existsSync(output);
  } catch (err) {
    log.warn("synthSilentMp3 не удался", String(err));
    return false;
  }
}

/** Склейка mp3-сегментов через concat demuxer (единый формат). */
export function buildAudioConcatArgs(listFile: string, output: string): string[] {
  return ["-y", "-f", "concat", "-safe", "0", "-i", listFile, "-c:a", "libmp3lame", "-b:a", "192k", output];
}

/** Короткий тестовый клип 9:16 (для mock-скачивания). */
export async function synthTestClip(output: string, seconds = 3): Promise<boolean> {
  if (!hasFfmpeg()) return false;
  const args = [
    "-y",
    "-f", "lavfi",
    "-i", `color=c=#0b0a09:s=${OUT_WIDTH}x${OUT_HEIGHT}:d=${seconds}:r=30`,
    "-f", "lavfi",
    "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
    "-t", String(seconds),
    "-c:v", "libx264", "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-shortest", "-movflags", "+faststart",
    output,
  ];
  try {
    await runFfmpeg(args, { timeoutMs: 60000 });
    return fs.existsSync(output);
  } catch (err) {
    log.warn("synthTestClip не удался", String(err));
    return false;
  }
}
