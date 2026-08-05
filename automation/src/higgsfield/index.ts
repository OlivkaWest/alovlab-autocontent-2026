import fs from "node:fs";
import path from "node:path";

/**
 * Higgsfield подключается через MCP внутри самого Claude Code, а не через ключ в .env.
 * Поэтому node-процесс НЕ вызывает Higgsfield напрямую: он готовит спецификацию задачи
 * (промпт + исходный кадр + параметры движения), а реальную генерацию выполняет
 * Claude через MCP-инструменты (mcp__higgsfield__generate_video / image-to-video).
 * В mock-режиме пайплайн собирает тестовый клип локально, не обращаясь к MCP.
 */
export interface HiggsfieldSpec {
  sceneId: string;
  mode: "image_to_video" | "text_to_video";
  sourceImage?: string;
  prompt: string;
  motion: string;
  aspectRatio: string;
  durationSeconds: number;
  preserve: string;
  avoid: string;
  model: string | null; // выбирается ПОСЛЕ проверки доступных моделей через MCP
}

/** Строит спецификацию Higgsfield-задачи для сцены и сохраняет prompt/request файлы. */
export function writeHiggsfieldSpec(dir: string, spec: HiggsfieldSpec): { promptPath: string; requestPath: string } {
  fs.mkdirSync(dir, { recursive: true });
  const base = `${spec.sceneId}`;
  const promptPath = path.join(dir, `${base}_prompt.md`);
  const requestPath = path.join(dir, `${base}_request.json`);
  const md = [
    spec.sourceImage ? `Source image:\n${spec.sourceImage}\n` : "",
    `Task:\nAnimate into a vertical cinematic B-roll shot.\n`,
    `Motion:\n${spec.motion}\n`,
    `Preserve:\n${spec.preserve}\n`,
    `Avoid:\n${spec.avoid}\n`,
    `Format:\n${spec.aspectRatio}\n`,
    `Duration:\n${spec.durationSeconds} seconds\n`,
    spec.prompt ? `Prompt:\n${spec.prompt}\n` : "",
  ]
    .filter(Boolean)
    .join("\n");
  fs.writeFileSync(promptPath, md, "utf8");
  fs.writeFileSync(requestPath, JSON.stringify(spec, null, 2), "utf8");
  return { promptPath, requestPath };
}

/** Mock-«генерация» Higgsfield для оффлайн-прогона пайплайна. */
export async function higgsfieldMockGenerate(dest: string, seconds = 4): Promise<string> {
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  const { synthTestClip } = await import("../video/ffmpeg");
  const ok = await synthTestClip(dest, seconds).catch(() => false);
  if (!ok) fs.writeFileSync(dest, Buffer.from("ALOVLAB-MOCK-HIGGSFIELD"));
  return dest;
}
