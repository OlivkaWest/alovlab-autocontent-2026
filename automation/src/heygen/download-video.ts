import fs from "node:fs";
import path from "node:path";
import { config } from "../config";
import { createLogger } from "../logger";
import { HeygenError } from "./errors";
import { mockDownload } from "./mock";

const log = createLogger("heygen-download");

/** Скачивает готовый MP4 по ссылке в локальный файл. Проверяет размер. */
export async function downloadVideo(videoUrl: string, destPath: string, videoId = ""): Promise<string> {
  fs.mkdirSync(path.dirname(destPath), { recursive: true });

  if (config.heygen.mock || videoUrl.startsWith("mock://")) {
    return mockDownload(videoId || "mock", destPath);
  }

  let res: Response;
  try {
    res = await fetch(videoUrl);
  } catch (err) {
    throw new HeygenError("download_failed", String((err as Error)?.message || err));
  }
  if (!res.ok || !res.body) throw new HeygenError("download_failed", `HTTP ${res.status}`);

  const buf = Buffer.from(await res.arrayBuffer());
  if (buf.length < 1024) {
    throw new HeygenError("download_failed", `подозрительно маленький файл (${buf.length} байт) — возможно, повреждён MP4`);
  }
  fs.writeFileSync(destPath, buf);
  log.info(`Скачано видео → ${destPath} (${buf.length} байт)`);
  return destPath;
}
