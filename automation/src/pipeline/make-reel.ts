import fs from "node:fs";
import path from "node:path";
import { createLogger } from "../logger";
import { config, neuromonkReady } from "../config";
import { getContentByDate, type DayContent } from "../content/adapter";
import {
  dayDir,
  reelsDir,
  subDir,
  setStatus,
  ensureStatus,
  saveStatus,
  writeVersioned,
  nextVersionPath,
  latestVersion,
  appendLog,
} from "../project/day-store";
import { Brief, Carousel, Card, type ReelsScript, type Scene } from "../store/types";
import { generateScript } from "../reels/script-generator";
import { auditScriptStyle, validateScript } from "../reels/scenes";
import { buildSubtitles, toSrt } from "../reels/subtitles";
import { toAss } from "../reels/ass";
import { buildGenerationPlan, type GenerationPlan, type SceneRoute } from "../generators/router";
import { estimateCost } from "../video/cost";
import { renderCards } from "../carousel/render";
import {
  hasFfmpeg,
  runFfmpeg,
  synthTestClip,
  buildCardClipArgs,
  buildColorClipArgs,
  buildConcatArgs,
  buildAssembleArgs,
  assertSafeArg,
  OUT_WIDTH,
  OUT_HEIGHT,
} from "../video/ffmpeg";
import { buildAvatarSegmentArgs } from "../video/assemble";
import { verifyFinal, probe } from "../video/verify";
import { resolveNeuromonk, NEUROMONK } from "../reels/neuromonk";
import { makeVoiceover } from "./make-voiceover";
import { voiceReady } from "../config";
import { createVideo } from "../heygen/create-video";
import { getVideoStatus } from "../heygen/get-video-status";
import { downloadVideo } from "../heygen/download-video";
import { buildCreateVideoPayload } from "../heygen/payload";
import { grokCreateVideo, grokGetStatus, grokDownload } from "../grok/client";
import { higgsfieldMockGenerate, writeHiggsfieldSpec } from "../higgsfield";

const log = createLogger("make-reel");
const sleep = (ms: number) => new Promise<void>((r) => setTimeout(r, ms));

export interface MakeReelOptions {
  runHeygen?: boolean; // запускать генерацию аватара
  assemble?: boolean; // собирать финал
  allowGrok?: boolean;
  burnSubtitles?: boolean;
  provocative?: boolean; // более провокационная подача
}

export interface MakeReelResult {
  ok: boolean;
  date: string;
  reason?: string;
  topic?: string;
  contentType?: string;
  scriptPath?: string;
  storyboardPath?: string;
  planPath?: string;
  editPlanPath?: string;
  finalPath?: string | null;
  srtPath?: string;
  scenes?: number;
  heygenScenes?: number;
  brollScenes?: number;
  durationSeconds?: number;
  routing?: Record<string, number>;
  verify?: { passed: boolean; checks: Array<{ name: string; ok: boolean; detail?: string }> };
  incomplete?: string[];
}

// Подгоняет длительности активных сцен под реальную длину озвучки (audio-first).
function rescaleScenes(script: ReelsScript, targetSeconds: number): void {
  const active = script.scenes.filter((s) => !s.disabled);
  const sum = active.reduce((a, s) => a + s.durationSeconds, 0) || 1;
  const factor = targetSeconds / sum;
  for (const s of active) s.durationSeconds = Math.max(1, Math.round(s.durationSeconds * factor * 10) / 10);
  script.durationSeconds = Math.round(active.reduce((a, s) => a + s.durationSeconds, 0));
}

function contentToBrief(c: DayContent, provocative: boolean): Brief {
  return Brief.parse({
    theme: c.topic || "Без темы",
    audience: c.audience,
    goal: (["reach", "subscribe", "save", "comment", "telegram", "course_sale", "studio_lead", "warmup"].includes(c.goal)
      ? c.goal
      : "reach") as Brief["goal"],
    platform: c.platform,
    desiredAction: c.desired_action + (provocative ? " (провокационная подача)" : ""),
    cardCount: c.card_count,
    reelsDurationSeconds: c.reels_duration_seconds,
  });
}

function contentToCarousel(c: DayContent): Carousel | null {
  if (!c.cards.length) return null;
  const roles = ["cover", "problem", "insight", "solution", "example", "action", "cta"];
  const cards: Card[] = c.cards.map((dc, i) =>
    Card.parse({
      id: `card_${i}`,
      index: i,
      role: (dc.role && roles.includes(dc.role) ? dc.role : roles[Math.min(i, roles.length - 1)]) as Card["role"],
      title: dc.title,
      body: dc.body,
      accent: "",
    })
  );
  return Carousel.parse({ title: c.topic, cards, cta: c.cta, caption: c.post.slice(0, 300) });
}

/** Человеческий markdown сценария для быстрого чтения. */
function scriptToMd(date: string, s: ReelsScript): string {
  const scenes = s.scenes
    .map(
      (sc, i) =>
        `### Сцена ${i + 1} — ${sc.type === "avatar" ? "Аватар" : "B-roll"} · ${sc.durationSeconds}с\n` +
        `- Речь: ${sc.spokenText}\n- На экране: ${sc.onScreenText}\n- Визуал: ${sc.visualSource}\n- Камера: ${sc.cameraMotion}\n- Переход: ${sc.transition}\n- Субтитр: ${sc.subtitle}`
    )
    .join("\n\n");
  return `# Reels — ${date}\n\n**Тема:** ${s.title}\n**Длительность:** ${s.durationSeconds}с · **Цель:** ${s.goal} · **Режим:** ${s.mode}\n\n**Хук:** ${s.hook}\n\n**Речь аватара:** ${s.avatarScript}\n\n**Закадровый текст:** ${s.voiceoverScript}\n\n**CTA:** ${s.cta}\n\n## Сцены\n\n${scenes}\n`;
}

// ─── Шаг: сценарий ───────────────────────────────────────────
export async function stepScript(date: string, opts: MakeReelOptions = {}): Promise<{ script: ReelsScript; content: DayContent; scriptPath: string; storyboardPath: string } | { error: string }> {
  const content = getContentByDate(date);
  if (!content.found) {
    return { error: `На ${date} материал в контент-плане не найден.` };
  }
  ensureStatus(date, { topic: content.topic, content_type: content.content_type });
  setStatus(date, "content_ready", "content_loaded", content.topic);

  const brief = contentToBrief(content, Boolean(opts.provocative));
  const carousel = contentToCarousel(content);
  const script = await generateScript(brief, carousel, {
    mode: content.visuals.length || carousel ? "avatar_broll" : "avatar_only",
    product: content.links[0] || "",
    style: opts.provocative ? "провокационная" : "спокойная уверенность",
  });

  // Проверки сценария
  const validation = validateScript(script);
  const style = auditScriptStyle(script);
  if (style.length) log.warn(`Стиль: найдено ${style.length} замечаний`, style.map((s) => s.match));

  const rDir = reelsDir(date);
  const { path: scriptPath, version } = writeVersioned(rDir, "reels_script", "json", JSON.stringify(script, null, 2));
  fs.writeFileSync(path.join(rDir, "reels_script.md"), scriptToMd(date, script), "utf8");
  const { path: storyboardPath } = writeVersioned(rDir, "storyboard", "json", JSON.stringify({ date, version, scenes: script.scenes }, null, 2));

  setStatus(date, "script_ready", "script_generated", `v${version}, замечаний по стилю: ${style.length}, валиден: ${validation.ok}`);
  appendLog(date, `Сценарий v${version} готов. Сцен: ${script.scenes.length}. Стиль-замечаний: ${style.length}.`);
  return { script, content, scriptPath, storyboardPath };
}

// ─── Шаг: план генерации ─────────────────────────────────────
export function stepPlan(date: string, script: ReelsScript, content: DayContent, opts: MakeReelOptions): { plan: GenerationPlan; planPath: string } {
  const rDir = reelsDir(date);
  const version = latestVersion(rDir, "generation_plan", "json") + 1;
  const plan = buildGenerationPlan(date, script, content, version, { allowGrok: opts.allowGrok });
  const { path: planPath } = writeVersioned(rDir, "generation_plan", "json", JSON.stringify(plan, null, 2));
  const cost = estimateCost(plan, config.video.maxCostUsd);
  appendLog(date, `План генерации v${version}: heygen=${cost.heygenScenes} higgsfield=${cost.higgsfieldScenes} grok=${cost.grokScenes} ffmpeg=${cost.ffmpegScenes}. ${cost.note}`);
  return { plan, planPath };
}

// ─── Шаг: карточки карусели в PNG (b-roll источники) ─────────
async function ensureCarouselPng(date: string, content: DayContent): Promise<string[]> {
  if (content.carousel_png.length) return content.carousel_png;
  const carousel = contentToCarousel(content);
  if (!carousel) return [];
  try {
    const dir = subDir(date, "carousel");
    const rendered = await renderCards(carousel.cards, dir);
    appendLog(date, `Отрендерено PNG-карточек: ${rendered.length}`);
    return rendered.map((r) => r.file);
  } catch (err) {
    appendLog(date, `Не удалось отрендерить карточки (${String(err).slice(0, 120)}) — B-roll соберём из аватара`);
    return [];
  }
}

// ─── Шаг: генерация аватара HeyGen (мастер-нарратив) ─────────
async function generateAvatarMaster(date: string, script: ReelsScript, background?: string): Promise<string | null> {
  const nm = resolveNeuromonk();
  if (!nm.ready) {
    appendLog(date, `HeyGen заблокирован: ${nm.message}`);
    return null;
  }
  const hgDir = subDir(date, "reels", "heygen");
  const narration = script.scenes.filter((s) => !s.disabled).map((s) => s.spokenText).filter(Boolean).join(" ");
  const input = {
    script: narration,
    avatarId: nm.avatarId,
    voiceId: nm.voiceId,
    language: nm.language,
    engine: nm.engine || undefined,
    width: NEUROMONK.width,
    height: NEUROMONK.height,
    background,
    title: script.title,
  };
  // Сохраняем payload (для аудита; ключи в него не входят).
  fs.writeFileSync(path.join(hgDir, "avatar_master_payload.json"), JSON.stringify(buildCreateVideoPayload(input), null, 2), "utf8");

  setStatus(date, "heygen_pending", "heygen_create", "avatar master");
  const created = await createVideo(input);
  fs.writeFileSync(path.join(hgDir, "avatar_master_response.json"), JSON.stringify({ video_id: created.videoId, mock: created.mock }, null, 2), "utf8");

  const st = ensureStatus(date);
  st.heygen_jobs = [{ scene_id: "avatar_master", video_id: created.videoId, status: "processing", local_path: null }];
  saveStatus(st);
  setStatus(date, "heygen_processing", "heygen_poll", created.videoId);

  let delay = 2500;
  for (let i = 0; i < 40; i++) {
    await sleep(delay);
    delay = Math.min(delay * 1.3, 12000);
    const state = await getVideoStatus(created.videoId).catch(() => null);
    if (!state) continue;
    if (state.status === "failed") {
      setStatus(date, "failed", "heygen_failed", state.error || "");
      return null;
    }
    if (state.status === "completed" && state.videoUrl) {
      const dest = path.join(hgDir, "avatar_master.mp4");
      await downloadVideo(state.videoUrl, dest, created.videoId);
      // В mock-режиме HeyGen отдаёт короткую заглушку — растягиваем мастер-клип
      // на всю длительность нарратива, чтобы монтаж не обрезался по -shortest.
      if (created.mock) {
        const total = script.scenes.filter((s) => !s.disabled).reduce((a, s) => a + s.durationSeconds, 0);
        await synthTestClip(dest, Math.max(total, 5)).catch(() => {});
      }
      const s2 = ensureStatus(date);
      s2.heygen_jobs = [{ scene_id: "avatar_master", video_id: created.videoId, status: "completed", local_path: dest }];
      saveStatus(s2);
      setStatus(date, "avatar_ready", "avatar_downloaded", dest);
      appendLog(date, `Аватар готов: ${dest}`);
      return dest;
    }
  }
  setStatus(date, "failed", "heygen_timeout", created.videoId);
  return null;
}

// ─── Шаг: генерация B-roll по маршруту (mock: локальные клипы) ─
async function generateBroll(date: string, route: SceneRoute, seconds: number): Promise<string | null> {
  const brollDir = subDir(date, "reels", "broll");
  const dest = path.join(brollDir, `${route.scene_id}.mp4`);
  try {
    if (route.generator === "grok") {
      const { requestId } = await grokCreateVideo({
        mode: route.source_assets.length ? "image_to_video" : "text_to_video",
        prompt: route.prompt,
        imagePath: route.source_assets[0],
        durationSeconds: Math.min(seconds, 10),
        aspectRatio: config.grok.aspectRatio,
        resolution: config.grok.resolution,
      });
      const gDir = subDir(date, "reels", "grok");
      fs.writeFileSync(path.join(gDir, `${route.scene_id}_prompt.md`), route.prompt, "utf8");
      let url: string | null = null;
      for (let i = 0; i < 20; i++) {
        await sleep(1500);
        const st = await grokGetStatus(requestId);
        if (st.status === "failed") return null;
        if (st.status === "completed" && st.videoUrl) {
          url = st.videoUrl;
          break;
        }
      }
      if (!url) return null;
      await grokDownload(url, dest, requestId);
      appendLog(date, `Grok B-roll: ${route.scene_id} → ${dest}`);
      return dest;
    }
    if (route.generator === "higgsfield") {
      writeHiggsfieldSpec(subDir(date, "reels", "higgsfield"), {
        sceneId: route.scene_id,
        mode: route.source_assets.length ? "image_to_video" : "text_to_video",
        sourceImage: route.source_assets[0],
        prompt: route.prompt,
        motion: "slow controlled push-in",
        aspectRatio: "9:16",
        durationSeconds: seconds,
        preserve: "Original layout, composition, brand colors",
        avoid: "Text deformation, flicker, sudden camera movement",
        model: route.model,
      });
      // Реальная генерация Higgsfield выполняется Claude через MCP.
      // В оффлайн/mock-прогоне собираем тестовый клип локально.
      if (config.higgsfield.mock) {
        await higgsfieldMockGenerate(dest, seconds);
        appendLog(date, `Higgsfield B-roll (mock): ${route.scene_id} → ${dest}`);
        return dest;
      }
      return null; // ждём MCP-генерацию
    }
  } catch (err) {
    appendLog(date, `Генерация B-roll ${route.scene_id} упала: ${String(err).slice(0, 140)}`);
    return null;
  }
  return null; // ffmpeg / existing_asset обрабатываются в монтаже
}

// ─── Шаг: монтаж финала ──────────────────────────────────────
function cardPngForRoute(route: SceneRoute, pngs: string[]): string | null {
  if (route.source_assets[0] && fs.existsSync(route.source_assets[0])) return route.source_assets[0];
  const m = route.scene_id;
  void m;
  return pngs[0] || null;
}

export async function stepAssemble(
  date: string,
  script: ReelsScript,
  plan: GenerationPlan,
  content: DayContent,
  avatarMaster: string | null,
  brollClips: Record<string, string>,
  pngs: string[],
  opts: MakeReelOptions,
  masterAudio: string | null = null
): Promise<{ finalPath: string | null; srtPath: string; editPlanPath: string; verify: Awaited<ReturnType<typeof verifyFinal>> | null; incomplete: string[] }> {
  const rDir = reelsDir(date);
  const renderDir = subDir(date, "reels", "render");
  const incomplete: string[] = [];

  // Субтитры
  const cues = buildSubtitles(script);
  const srtPath = path.join(rDir, "subtitles.srt");
  fs.writeFileSync(srtPath, toSrt(cues), "utf8");
  fs.writeFileSync(path.join(rDir, "subtitles.ass"), toAss(cues), "utf8");

  // Монтажный план (версионируется)
  const editVersion = latestVersion(renderDir, "final_reels", "mp4") + 1;
  const editPlan = {
    date,
    version: editVersion,
    resolution: `${OUT_WIDTH}x${OUT_HEIGHT}`,
    duration_seconds: script.durationSeconds,
    scenes: plan.scenes.map((r) => ({
      id: r.scene_id,
      generator: r.generator,
      type: r.type,
      duration: r.duration_seconds,
      source: brollClips[r.scene_id] || (r.generator === "heygen" ? avatarMaster : cardPngForRoute(r, pngs)),
    })),
    logo: findLogo(),
    subtitles: opts.burnSubtitles ? "subtitles.srt (burned)" : "subtitles.srt (separate)",
  };
  const { path: editPlanPath } = writeVersioned(rDir, "edit_plan", "json", JSON.stringify(editPlan, null, 2));

  if (!hasFfmpeg()) {
    incomplete.push("Монтаж: FFmpeg не найден — укажи FFMPEG_PATH.");
    setStatus(date, "failed", "assemble_blocked", "no ffmpeg");
    return { finalPath: null, srtPath, editPlanPath, verify: null, incomplete };
  }

  const hasAvatar = Boolean(avatarMaster && fs.existsSync(avatarMaster));
  // Голос: приоритет — озвучка ElevenLabs; иначе аудио аватара HeyGen.
  const voice = masterAudio && fs.existsSync(masterAudio) ? masterAudio : hasAvatar ? avatarMaster : null;
  if (!voice) {
    incomplete.push("Монтаж: нет ни озвучки ElevenLabs, ни клипа аватара — нет аудиодорожки.");
    return { finalPath: null, srtPath, editPlanPath, verify: null, incomplete };
  }
  if (!hasAvatar) {
    incomplete.push("Ролик собран без аватара HeyGen (B-roll + мой голос): аватар недоступен.");
  }

  // Визуал для сцены, когда клипа аватара нет: карточка карусели, иначе брендовый фон.
  const visualFallback = async (seg: string, seconds: number, png: string | null) => {
    if (hasAvatar) return runFfmpeg(buildAvatarSegmentArgs(avatarMaster!, seg, seconds));
    if (png && fs.existsSync(png)) return runFfmpeg(buildCardClipArgs(png, seg, seconds));
    return runFfmpeg(buildColorClipArgs(seg, seconds));
  };

  setStatus(date, "assembling", "assemble_start", `v${editVersion}`);

  // Клип на каждую активную сцену (video-only, единый формат)
  const active = script.scenes.filter((s) => !s.disabled);
  const segDir = subDir(date, "reels", "render", "segments");
  const segments: string[] = [];
  for (let i = 0; i < active.length; i++) {
    const scene = active[i];
    const route = plan.scenes.find((r) => r.scene_id === scene.id);
    const seg = path.join(segDir, `scene_${String(i + 1).padStart(2, "0")}.mp4`);
    const broll = brollClips[scene.id];
    const cardPng = route ? cardPngForRoute(route, pngs) : pngs[0] || null;
    try {
      if (broll && fs.existsSync(broll) && isRealVideo(broll)) {
        await runFfmpeg(buildAvatarSegmentArgs(broll, seg, scene.durationSeconds)); // нормализуем к 9:16
      } else if (scene.type === "avatar" && hasAvatar) {
        await runFfmpeg(buildAvatarSegmentArgs(avatarMaster!, seg, scene.durationSeconds));
      } else {
        // B-roll / нет аватара → карточка карусели, иначе аватар/фон (visualFallback)
        await visualFallback(seg, scene.durationSeconds, cardPng);
      }
      segments.push(seg);
    } catch (err) {
      appendLog(date, `Сцена ${scene.id} не собралась: ${String(err).slice(0, 140)} — пропускаем`);
      incomplete.push(`Сцена ${scene.id} пропущена в монтаже.`);
    }
  }
  if (!segments.length) {
    setStatus(date, "failed", "assemble_no_segments", "");
    return { finalPath: null, srtPath, editPlanPath, verify: null, incomplete };
  }

  // Логотип в финале (1.5с), если PNG найден
  const logo = findLogo();
  if (logo) {
    const logoSeg = path.join(segDir, "scene_zz_logo.mp4");
    try {
      await runFfmpeg(buildLogoOutroArgs(logo, logoSeg, 1.5));
      segments.push(logoSeg);
    } catch (err) {
      appendLog(date, `Логотип-аутро пропущен: ${String(err).slice(0, 120)}`);
    }
  }

  // Конкатенация видео
  const listFile = path.join(renderDir, "concat.txt");
  fs.writeFileSync(listFile, segments.map((s) => `file '${assertSafeArg(s)}'`).join("\n"), "utf8");
  const concatOut = path.join(renderDir, "concat.mp4");
  await runFfmpeg(buildConcatArgs(listFile, concatOut));

  // Финальный мукс: видео + голос (уже выбран выше: ElevenLabs → иначе аватар) + субтитры.
  const { path: finalPath } = nextVersionPath(renderDir, "final_reels", "mp4");
  const args = buildAssembleArgs({
    videoInput: concatOut,
    voiceInput: voice,
    subtitleFile: opts.burnSubtitles ? srtPath : undefined,
    output: finalPath,
    burnSubtitles: Boolean(opts.burnSubtitles),
  });
  await runFfmpeg(args, { timeoutMs: 240000 });

  const verify = await verifyFinal(finalPath, script.durationSeconds);
  const st = ensureStatus(date);
  if (verify.passed) {
    st.approved_final = finalPath;
    saveStatus(st);
    setStatus(date, "ready", "final_ready", finalPath);
    appendLog(date, `Финал готов и проверен: ${finalPath}`);
  } else {
    setStatus(date, "failed", "final_check_failed", verify.checks.filter((c) => !c.ok).map((c) => c.name).join("; "));
    incomplete.push("Финал собран, но не прошёл автоматическую проверку — см. verify.");
  }
  return { finalPath, srtPath, editPlanPath, verify, incomplete };
}

function isRealVideo(file: string): boolean {
  try {
    return fs.statSync(file).size > 2048;
  } catch {
    return false;
  }
}

function findLogo(): string | null {
  const candidates = [
    path.join(config.repoRoot, "assets", "img", "logo-mark.png"),
    path.join(config.repoRoot, "assets", "characters", "neuromonk", "logo.png"),
  ];
  return candidates.find((c) => fs.existsSync(c)) || null;
}

function buildLogoOutroArgs(logo: string, output: string, seconds: number): string[] {
  return [
    "-y",
    "-f", "lavfi",
    "-i", `color=c=#0b0a09:s=${OUT_WIDTH}x${OUT_HEIGHT}:d=${seconds}:r=30`,
    "-i", logo,
    "-filter_complex",
    `[1:v]scale=360:-1[logo];[0:v][logo]overlay=(W-w)/2:(H-h)/2:enable='gte(t,0.2)',format=yuv420p[v]`,
    "-map", "[v]",
    "-t", String(seconds),
    "-c:v", "libx264",
    output,
  ];
}

/**
 * Полный цикл «Сделай ролик на <дата>».
 */
export async function makeReel(date: string, opts: MakeReelOptions = {}): Promise<MakeReelResult> {
  const o: MakeReelOptions = { runHeygen: true, assemble: true, allowGrok: true, burnSubtitles: true, ...opts };

  const scriptStep = await stepScript(date, o);
  if ("error" in scriptStep) return { ok: false, date, reason: scriptStep.error };
  const { script, scriptPath, storyboardPath } = scriptStep;

  // Сначала карточки в PNG, затем маршрутизация — чтобы сцены с готовым кадром
  // ушли в higgsfield (оживление), а не в grok (генерация с нуля).
  const pngs = await ensureCarouselPng(date, scriptStep.content);
  const content = getContentByDate(date); // перечитываем — теперь carousel_png заполнен
  const { plan, planPath } = stepPlan(date, script, content, o);

  const routing: Record<string, number> = {};
  for (const r of plan.scenes) routing[r.generator] = (routing[r.generator] || 0) + 1;

  const incomplete: string[] = [];
  let avatarMaster: string | null = null;
  let voiceoverPath: string | null = null;
  const brollClips: Record<string, string> = {};

  // Озвучка моим голосом (ElevenLabs) — станет мастер-дорожкой монтажа.
  if (voiceReady().ready) {
    const narration = script.scenes.filter((s) => !s.disabled).map((s) => s.spokenText).filter(Boolean).join("\n\n");
    const vo = await makeVoiceover(date, narration, { label: "reels", delivery: o.provocative ? "sharp" : "confident" });
    if (vo.ok && vo.fullPath) {
      voiceoverPath = vo.fullPath;
      // Audio-first: подстраиваем длительность сцен под реальную речь (не наоборот).
      const pr = await probe(voiceoverPath).catch(() => null);
      if (pr?.durationSeconds && pr.durationSeconds > 3) rescaleScenes(script, pr.durationSeconds);
    } else if (vo.message) incomplete.push(`Озвучка ElevenLabs: ${vo.message}`);
  }

  if (o.runHeygen) {
    if (!neuromonkReady().ready) {
      incomplete.push(`HeyGen не запущен: ${neuromonkReady().message}.`);
    } else {
      avatarMaster = await generateAvatarMaster(date, script);
      if (!avatarMaster) incomplete.push("HeyGen не вернул готовый клип аватара.");
    }
    // B-roll для сцен, требующих генерации
    for (const r of plan.scenes) {
      if (r.requires_generation && (r.generator === "grok" || r.generator === "higgsfield")) {
        const clip = await generateBroll(date, r, r.duration_seconds);
        if (clip) brollClips[r.scene_id] = clip;
        else incomplete.push(`B-roll сцены ${r.scene_id} (${r.generator}) не сгенерирован.`);
      }
    }
  }

  let finalPath: string | null = null;
  let srtPath = path.join(reelsDir(date), "subtitles.srt");
  let editPlanPath = "";
  let verify: MakeReelResult["verify"] = undefined;

  if (o.assemble) {
    const asm = await stepAssemble(date, script, plan, content, avatarMaster, brollClips, pngs, o, voiceoverPath);
    finalPath = asm.finalPath;
    srtPath = asm.srtPath;
    editPlanPath = asm.editPlanPath;
    verify = asm.verify ?? undefined;
    incomplete.push(...asm.incomplete);
  }

  const heygenScenes = plan.scenes.filter((s) => s.generator === "heygen").length;
  const brollScenes = plan.scenes.length - heygenScenes;

  return {
    ok: Boolean(finalPath && verify?.passed) || (!o.assemble && !("error" in scriptStep)),
    date,
    topic: content.topic,
    contentType: content.content_type,
    scriptPath,
    storyboardPath,
    planPath,
    editPlanPath,
    finalPath,
    srtPath,
    scenes: plan.scenes.length,
    heygenScenes,
    brollScenes,
    durationSeconds: script.durationSeconds,
    routing,
    verify,
    incomplete: [...incomplete, ...content.missing.map((m) => `Не было в контенте: ${m}`)],
  };
}
