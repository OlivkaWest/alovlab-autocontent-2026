import fs from "node:fs";
import path from "node:path";
import { projectDir } from "../store/projects";
import { createLogger } from "../logger";
import { toSrt } from "../reels/subtitles";
import { buildSubtitles } from "../reels/subtitles";
import {
  OUT_WIDTH,
  OUT_HEIGHT,
  hasFfmpeg,
  runFfmpeg,
  buildCardClipArgs,
  buildConcatArgs,
  buildAssembleArgs,
  assertSafeArg,
} from "./ffmpeg";
import type { Project, Scene } from "../store/types";

const log = createLogger("assemble");

/** Video-only нормализация клипа аватара к 9:16 с обрезкой по длительности сцены. */
export function buildAvatarSegmentArgs(input: string, output: string, seconds: number): string[] {
  return [
    "-y",
    "-i", input,
    "-t", String(seconds),
    "-an",
    "-vf",
    `scale=${OUT_WIDTH}:${OUT_HEIGHT}:force_original_aspect_ratio=decrease,pad=${OUT_WIDTH}:${OUT_HEIGHT}:(ow-iw)/2:(oh-ih)/2:color=#0b0a09,setsar=1`,
    "-r", "30",
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    output,
  ];
}

function cardPngForScene(project: Project, scene: Scene): string | null {
  const files = project.carouselExport?.pngFiles || [];
  if (!files.length) return null;
  const m = scene.visualSource.match(/card:(\d+)/);
  const idx = m ? Number(m[1]) : 1;
  const byName = files.find((f) => path.basename(f).startsWith(String(idx + 1).padStart(2, "0")));
  return byName || files[Math.min(idx, files.length - 1)] || files[0];
}

export interface AssembleResult {
  finalPath: string;
  srtPath: string;
  usedFfmpeg: boolean;
}

/**
 * Собирает финальный вертикальный ролик из сцен.
 * Голос берётся из клипа аватара и продолжается поверх B-roll.
 * Субтитры вшиваются из SRT-файла (безопасно, без инъекций).
 */
export async function assembleFinalVideo(
  project: Project,
  opts: { burnSubtitles?: boolean } = {}
): Promise<AssembleResult> {
  if (!project.script) throw new Error("Нет сценария — сначала сгенерируй его");

  const dir = path.join(projectDir(project.id), "video");
  fs.mkdirSync(dir, { recursive: true });

  // 1. Субтитры
  const cues = project.subtitles.length ? project.subtitles : buildSubtitles(project.script);
  const srtPath = path.join(dir, "subtitles.srt");
  fs.writeFileSync(srtPath, toSrt(cues), "utf8");

  const finalPath = path.join(dir, "final.mp4");

  if (!hasFfmpeg()) {
    throw new Error(
      "FFmpeg не найден. Укажи путь в FFMPEG_PATH или установи ffmpeg (см. README, раздел «Монтаж»)."
    );
  }

  // Мастер-аудио: клип основного аватара (sceneId=null) или первый доступный.
  const primary =
    project.heygenJobs.find((j) => j.sceneId === null && j.localPath) ||
    project.heygenJobs.find((j) => j.localPath);
  if (!primary?.localPath || !fs.existsSync(primary.localPath)) {
    throw new Error("Нет готового клипа аватара — сначала сгенерируй видео в HeyGen");
  }

  // 2. Клип на каждую активную сцену (video-only, единый кодек/формат)
  const activeScenes = project.script.scenes.filter((s) => !s.disabled);
  const segments: string[] = [];
  for (let i = 0; i < activeScenes.length; i++) {
    const scene = activeScenes[i];
    const seg = path.join(dir, `scene_${String(i + 1).padStart(2, "0")}.mp4`);
    const perSceneJob = project.heygenJobs.find((j) => j.sceneId === scene.id && j.localPath);
    const useBroll = scene.type === "broll" && project.script.mode === "avatar_broll";

    if (useBroll) {
      const png = cardPngForScene(project, scene);
      if (png && fs.existsSync(png)) {
        await runFfmpeg(buildCardClipArgs(png, seg, scene.durationSeconds));
        segments.push(seg);
        continue;
      }
    }
    const avatarClip = perSceneJob?.localPath || primary.localPath;
    await runFfmpeg(buildAvatarSegmentArgs(avatarClip, seg, scene.durationSeconds));
    segments.push(seg);
  }

  // 3. Конкатенация видео-дорожек
  const listFile = path.join(dir, "concat.txt");
  fs.writeFileSync(listFile, segments.map((s) => `file '${assertSafeArg(s)}'`).join("\n"), "utf8");
  const concatOut = path.join(dir, "concat.mp4");
  await runFfmpeg(buildConcatArgs(listFile, concatOut));

  // 4. Финальный мукс: видео + голос аватара + (опц.) вшитые субтитры
  const args = buildAssembleArgs({
    videoInput: concatOut,
    voiceInput: primary.localPath,
    subtitleFile: opts.burnSubtitles ? srtPath : undefined,
    output: finalPath,
    burnSubtitles: Boolean(opts.burnSubtitles),
  });
  await runFfmpeg(args, { timeoutMs: 240000 });

  log.info(`Финальный ролик собран: ${finalPath}`);
  return { finalPath, srtPath, usedFfmpeg: true };
}
