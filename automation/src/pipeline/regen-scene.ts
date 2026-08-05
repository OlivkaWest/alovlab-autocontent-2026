import fs from "node:fs";
import path from "node:path";
import { reelsDir, subDir, latestVersion, appendLog } from "../project/day-store";
import { getContentByDate } from "../content/adapter";
import { ReelsScript, type Scene } from "../store/types";
import { routeScene } from "../generators/router";
import { higgsfieldMockGenerate } from "../higgsfield";
import { config } from "../config";
import { grokCreateVideo, grokGetStatus, grokDownload } from "../grok/client";
import { createLogger } from "../logger";

const log = createLogger("regen-scene");
const sleep = (ms: number) => new Promise<void>((r) => setTimeout(r, ms));

function loadLatestScript(date: string): ReelsScript | null {
  const dir = reelsDir(date);
  if (!fs.existsSync(dir)) return null;
  const files = fs.readdirSync(dir).filter((f) => /^reels_script(_v\d+)?\.json$/.test(f)).sort();
  if (!files.length) return null;
  try {
    return ReelsScript.parse(JSON.parse(fs.readFileSync(path.join(dir, files[files.length - 1]), "utf8")));
  } catch {
    return null;
  }
}

function findScene(script: ReelsScript, ref: string): Scene | null {
  const byId = script.scenes.find((s) => s.id === ref);
  if (byId) return byId;
  const n = Number(ref);
  if (Number.isInteger(n) && n >= 1 && n <= script.scenes.length) return script.scenes[n - 1];
  return null;
}

/**
 * Перегенерирует ОДНУ сцену, не трогая остальные. Новая версия клипа сохраняется
 * отдельно (scene_id_vN.mp4). Финал пересобирается отдельной командой assemble.
 */
export async function regenerateScene(date: string, ref: string): Promise<{ ok: boolean; message: string }> {
  const script = loadLatestScript(date);
  if (!script) return { ok: false, message: `Сценария на ${date} нет. Сначала: script ${date}` };
  const scene = findScene(script, ref);
  if (!scene) return { ok: false, message: `Сцена «${ref}» не найдена в сценарии ${date}.` };

  const content = getContentByDate(date);
  const route = routeScene(scene, content, { allowGrok: config.video.allowAutoGenerate });

  if (route.generator === "heygen") {
    return {
      ok: false,
      message:
        `Сцена ${scene.id} — аватарная (HeyGen). Перегенерация аватарной сцены запускает HeyGen: ` +
        `выполни «reel ${date}» или отдельный HeyGen-прогон. Остальные сцены не трогаются.`,
    };
  }

  const brollDir = subDir(date, "reels", "broll");
  const version = latestVersion(brollDir, scene.id, "mp4") + 1;
  const dest = path.join(brollDir, `${scene.id}_v${version}.mp4`);

  try {
    if (route.generator === "grok") {
      const { requestId } = await grokCreateVideo({
        mode: route.source_assets.length ? "image_to_video" : "text_to_video",
        prompt: route.prompt,
        imagePath: route.source_assets[0],
        durationSeconds: Math.min(scene.durationSeconds, 10),
        aspectRatio: config.grok.aspectRatio,
        resolution: config.grok.resolution,
      });
      let url: string | null = null;
      for (let i = 0; i < 20; i++) {
        await sleep(1200);
        const st = await grokGetStatus(requestId);
        if (st.status === "completed" && st.videoUrl) { url = st.videoUrl; break; }
        if (st.status === "failed") break;
      }
      if (!url) return { ok: false, message: `Grok не собрал сцену ${scene.id}.` };
      await grokDownload(url, dest, requestId);
    } else {
      await higgsfieldMockGenerate(dest, scene.durationSeconds);
    }
  } catch (err) {
    return { ok: false, message: `Перегенерация сцены ${scene.id} упала: ${String(err).slice(0, 160)}` };
  }

  appendLog(date, `Перегенерирована сцена ${scene.id} → ${path.basename(dest)}`);
  log.info(`Сцена ${scene.id} → ${dest}`);
  return {
    ok: true,
    message: `Сцена ${scene.id} перегенерирована (v${version}): ${path.relative(config.repoRoot, dest)}. Собери финал: assemble ${date}`,
  };
}
