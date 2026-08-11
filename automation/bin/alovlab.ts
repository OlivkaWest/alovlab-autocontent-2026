#!/usr/bin/env node
/**
 * AlovLab CLI — точка входа для команд Claude Code.
 * Пример: npm run alovlab -- reel 2026-08-05
 *         npm run alovlab -- content "5 августа"
 *
 * Команды понимают дату в ISO (2026-08-05) и по-русски («5 августа»).
 */
import path from "node:path";
import fs from "node:fs";
import { config, maskSecret, neuromonkReady } from "../src/config";
import { resolveDate, todayIso } from "../src/dates";
import { getContentByDate, buildIndex } from "../src/content/adapter";
import { loadStatus, DAY_STATUS_LABELS, reelsDir, dayDir } from "../src/project/day-store";
import { makeReel, stepScript, stepPlan } from "../src/pipeline/make-reel";
import { regenerateScene } from "../src/pipeline/regen-scene";
import { hasFfmpeg, resolveFfmpeg } from "../src/video/ffmpeg";
import { resolveFfprobe } from "../src/video/verify";
import { listAvatars } from "../src/heygen/avatars";
import { listVoices } from "../src/heygen/voices";
import { makeVoiceover } from "../src/pipeline/make-voiceover";
import { makePodcast, type PodcastFormat } from "../src/podcast/generate";
import { makePodcastFromFile } from "../src/podcast/from-file";
import { publish } from "../src/publishing/telegram/client";
import { buildCaption } from "../src/publishing/telegram/caption";
import { subDir } from "../src/project/day-store";

function print(...a: unknown[]) {
  // eslint-disable-next-line no-console
  console.log(...a);
}

function needDate(args: string[]): string | null {
  const phrase = args.join(" ").trim();
  if (!phrase) {
    print("Укажи дату, например: reel 2026-08-05  или  reel «5 августа»");
    return null;
  }
  const date = resolveDate(phrase);
  if (!date) {
    print(`Не понял дату из «${phrase}». Формат: 2026-08-05 или «5 августа».`);
    return null;
  }
  return date;
}

async function cmdContent(date: string) {
  const c = getContentByDate(date);
  if (!c.found) {
    print(`На ${date} материал в контент-плане не найден.`);
    return;
  }
  print(`\n${date}`);
  print(`Тема: ${c.topic}`);
  print(`Формат: ${c.content_type}`);
  print(`Цель: ${c.goal}`);
  print(`Аудитория: ${c.audience || "—"}`);
  print(`Карточек: ${c.cards.length}  ·  Визуалов: ${c.visuals.length}  ·  PNG: ${c.carousel_png.length}`);
  if (c.missing.length) print(`Не хватает: ${c.missing.join(", ")}`);
}

async function cmdStatus(date: string) {
  const s = loadStatus(date);
  if (!s) {
    print(`По ${date} задача ещё не создавалась.`);
    return;
  }
  print(`\n${date} — ${DAY_STATUS_LABELS[s.status]} (${s.status})`);
  print(`Тема: ${s.topic}`);
  if (s.heygen_jobs.length) {
    print("HeyGen:");
    for (const j of s.heygen_jobs) print(`  ${j.scene_id}: ${j.status} ${j.local_path ? "→ " + path.basename(j.local_path) : ""}`);
  }
  if (s.approved_final) print(`Финал: ${s.approved_final}`);
}

function reportReel(r: Awaited<ReturnType<typeof makeReel>>) {
  if (!r.ok && r.reason) {
    print(r.reason);
    return;
  }
  const ready = Boolean(r.finalPath && r.verify?.passed);
  print("");
  print(ready ? `Ролик на ${r.date} готов.` : `Ролик на ${r.date}: собран черновик, есть незавершённые шаги.`);
  print("");
  print(`Тема: ${r.topic}`);
  print(`Длительность: ${r.durationSeconds} секунд`);
  print(`Сцен: ${r.scenes}`);
  print(`HeyGen-сцен: ${r.heygenScenes}`);
  print(`B-roll-сцен: ${r.brollScenes}`);
  if (r.routing) print(`Маршрутизация: ${Object.entries(r.routing).map(([k, v]) => `${k}=${v}`).join("  ")}`);
  print("");
  if (r.finalPath) print(`Финальный файл:\n${path.relative(config.repoRoot, r.finalPath)}`);
  print("");
  print("Дополнительно:");
  for (const [label, p] of [
    ["сценарий", r.scriptPath],
    ["сцен-план", r.storyboardPath],
    ["план генерации", r.planPath],
    ["монтажный план", r.editPlanPath],
    ["субтитры", r.srtPath],
  ] as const) {
    if (p) print(`— ${label}: ${path.relative(config.repoRoot, p)}`);
  }
  if (r.verify) {
    print("\nПроверка финала:");
    for (const c of r.verify.checks) print(`  ${c.ok ? "✓" : "✗"} ${c.name}${c.detail ? ` — ${c.detail}` : ""}`);
  }
  if (r.incomplete && r.incomplete.length) {
    print("\nНе удалось / не хватило:");
    for (const i of r.incomplete) print(`— ${i}`);
  }
}

function cmdDoctor() {
  print("\nAlovLab Automation — статус подключений\n");
  const nm = neuromonkReady();
  print("HeyGen (аватар Нейромонах):");
  print(`  режим: ${config.heygen.mock ? "MOCK (кредиты не тратятся)" : "РЕАЛЬНЫЙ"}`);
  print(`  API-ключ: ${maskSecret(config.heygen.apiKey)}`);
  print(`  avatar_id: ${config.heygen.avatarId || "(не задан)"}  voice_id: ${config.heygen.voiceId || "(не задан)"}`);
  print(`  готовность: ${nm.ready ? "готов" : nm.message}`);
  print("\nGrok (xAI, B-roll):");
  print(`  режим: ${config.grok.mock ? "MOCK" : "РЕАЛЬНЫЙ"}`);
  print(`  API-ключ: ${maskSecret(config.grok.apiKey)}  модель: ${config.grok.model}`);
  print(`  endpoint видео: ${process.env.XAI_VIDEO_ENDPOINT || "/v1/videos/generations (дефолт по докам xAI)"}`);
  print("\nHiggsfield (B-roll, image-to-video):");
  print(`  подключение: через MCP внутри Claude Code (не через .env)`);
  print(`  оффлайн-режим пайплайна: ${config.higgsfield.mock ? "MOCK" : "ожидает MCP"}`);
  try {
    const id = JSON.parse(fs.readFileSync(path.join(config.repoRoot, "assets", "characters", "neuromonk", "identity.json"), "utf8"));
    const s = id.higgsfield_soul_id || {};
    print(`  Soul ID нейромонаха: ${s.reference_id || "(не задан)"} [${s.status || "?"}]${s.name ? " — " + s.name : ""}`);
  } catch { /* нет файла */ }
  print("\nElevenLabs (мой голос, озвучка/подкасты):");
  print(`  режим: ${config.elevenlabs.mock ? "MOCK" : "РЕАЛЬНЫЙ"}`);
  print(`  API-ключ: ${maskSecret(config.elevenlabs.apiKey)}  voice_id: ${config.elevenlabs.voiceId || "(не задан)"}  модель: ${config.elevenlabs.modelId}`);

  print("\nTelegram (публикация):");
  print(`  режим: ${config.telegram.publishMode.toUpperCase()}${config.telegram.publishMode === "draft" ? " (реальная отправка выключена)" : ""}`);
  print(`  bot token: ${maskSecret(config.telegram.botToken)}  channel: ${config.telegram.channelId || "(не задан)"}`);

  print("\nFFmpeg (монтаж):");
  print(`  ffmpeg: ${hasFfmpeg() ? resolveFfmpeg() : "НЕ НАЙДЕН — задай FFMPEG_PATH"}`);
  print(`  ffprobe: ${resolveFfprobe() || "нет (используем ffmpeg)"}`);
  print(`\nContent root: ${config.contentRoot}`);
  print(`Сегодня: ${todayIso()}`);
}

async function main() {
  const [cmd, ...rest] = process.argv.slice(2);
  switch (cmd) {
    case "doctor":
      return cmdDoctor();
    case "avatars": {
      const list = await listAvatars().catch((e) => {
        print(`Не удалось получить аватары: ${e?.message || e}`);
        return [];
      });
      print(`Аватары (${config.heygen.mock ? "MOCK" : "HeyGen"}): ${list.length}`);
      for (const a of list.slice(0, 50)) print(`  ${a.avatarId}  —  ${a.name}`);
      print("\nВыбери нужный и впиши в .env: HEYGEN_AVATAR_ID=<avatar_id>");
      return;
    }
    case "voices": {
      const list = await listVoices().catch((e) => {
        print(`Не удалось получить голоса: ${e?.message || e}`);
        return [];
      });
      const ru = list.filter((v) => /ru/i.test(v.language || ""));
      print(`Голоса (${config.heygen.mock ? "MOCK" : "HeyGen"}): всего ${list.length}, русских ${ru.length}`);
      for (const v of (ru.length ? ru : list).slice(0, 50)) print(`  ${v.voiceId}  —  ${v.name} [${v.language || "?"}]`);
      print("\nВыбери русский голос и впиши в .env: HEYGEN_VOICE_ID=<voice_id>");
      return;
    }
    case "soul": {
      const idPath = path.join(config.repoRoot, "assets", "characters", "neuromonk", "identity.json");
      const id = JSON.parse(fs.readFileSync(idPath, "utf8"));
      const s = id.higgsfield_soul_id || {};
      print("Идентичность нейромонаха:");
      print(`  Higgsfield Soul ID: ${s.reference_id || "(не задан)"} [${s.status || "?"}] ${s.name ? "— " + s.name : ""}`);
      print(`  HeyGen avatar_id: ${config.heygen.avatarId || "(не задан)"}  voice_id: ${config.heygen.voiceId || "(не задан)"}`);
      return;
    }
    case "index": {
      const idx = buildIndex();
      print(`Индекс собран: ${Object.keys(idx).length} дней → ${path.join(config.contentRoot, "index.json")}`);
      return;
    }
    case "content": {
      const d = needDate(rest);
      if (d) await cmdContent(d);
      return;
    }
    case "status": {
      const d = needDate(rest);
      if (d) await cmdStatus(d);
      return;
    }
    case "script": {
      const d = needDate(rest);
      if (!d) return;
      const res = await stepScript(d, {});
      if ("error" in res) return print(res.error);
      stepPlan(d, res.script, res.content, {});
      print(`Сценарий на ${d} готов: ${path.relative(config.repoRoot, res.scriptPath)}`);
      print(`Сцен-план: ${path.relative(config.repoRoot, res.storyboardPath)}`);
      return;
    }
    case "scenes": {
      const d = needDate(rest);
      if (!d) return;
      const dir = reelsDir(d);
      const files = fs.existsSync(dir) ? fs.readdirSync(dir).filter((f) => /storyboard_v\d+\.json/.test(f)).sort() : [];
      if (!files.length) return print(`Сцен-плана на ${d} нет. Сначала: script ${d}`);
      const latest = path.join(dir, files[files.length - 1]);
      const sb = JSON.parse(fs.readFileSync(latest, "utf8"));
      print(`Сцен-план ${d} (${path.basename(latest)}):`);
      for (const [i, sc] of sb.scenes.entries()) {
        print(`  ${i + 1}. [${sc.type}] ${sc.durationSeconds}с — ${sc.spokenText}`);
      }
      return;
    }
    case "route": {
      const d = needDate(rest);
      if (!d) return;
      const res = await stepScript(d, {});
      if ("error" in res) return print(res.error);
      const { plan } = stepPlan(d, res.script, res.content, {});
      print(`Маршрутизация сцен ${d}:`);
      for (const r of plan.scenes) print(`  ${r.scene_id}: ${r.generator}${r.fallback_generator ? ` (fallback: ${r.fallback_generator})` : ""} — ${r.reason}`);
      return;
    }
    case "reel": {
      const d = needDate(rest);
      if (!d) return;
      reportReel(await makeReel(d));
      return;
    }
    case "script-only":
    case "prepare": {
      const d = needDate(rest);
      if (!d) return;
      reportReel(await makeReel(d, { runHeygen: false, assemble: false }));
      return;
    }
    case "heygen": {
      const d = needDate(rest);
      if (!d) return;
      reportReel(await makeReel(d, { runHeygen: true, assemble: true }));
      return;
    }
    case "assemble": {
      const d = needDate(rest);
      if (!d) return;
      reportReel(await makeReel(d, { runHeygen: false, assemble: true }));
      return;
    }
    case "voiceover": {
      const d = needDate(rest);
      if (!d) return;
      const res = await stepScript(d, {});
      if ("error" in res) return print(res.error);
      const narration = res.script.scenes.filter((s) => !s.disabled).map((s) => s.spokenText).filter(Boolean).join("\n\n");
      const vo = await makeVoiceover(d, narration, { label: "reels" });
      if (!vo.ok) return print(`Озвучка не сделана: ${vo.message}`);
      print(`Озвучка (${config.elevenlabs.mock ? "MOCK" : "ElevenLabs"}): ${vo.segments} сегм. → ${path.relative(config.repoRoot, vo.fullPath!)}`);
      return;
    }
    case "podcast": {
      // Готовый markdown-скрипт в озвучку verbatim: podcast <path.md>
      const fileArg = rest.find((r) => /\.md$/i.test(r));
      if (fileArg) {
        const rf = await makePodcastFromFile(fileArg, {
          cta: "Рабочая тетрадь дня — в закрепе Telegram AlovLab.",
          link: "https://t.me/AlovLab",
        });
        if (!rf.ok && rf.reason) return print(rf.reason);
        print(`\nПодкаст из файла: ${rf.title}`);
        if (rf.audioPath) print(`  аудио: ${path.relative(config.repoRoot, rf.audioPath)}${rf.durationSeconds ? ` (${rf.durationSeconds.toFixed(0)}с, ${rf.segments} сегм.)` : ""}`);
        if (rf.voiceScriptPath) print(`  голосовой сценарий: ${path.relative(config.repoRoot, rf.voiceScriptPath)}`);
        if (rf.captionPath) print(`  подпись: ${path.relative(config.repoRoot, rf.captionPath)}`);
        if (rf.telegramDraft) print(`  telegram-черновик: ${path.relative(config.repoRoot, rf.telegramDraft)}`);
        for (const i of rf.incomplete || []) print(`  — ${i}`);
        return;
      }
      const fmt = (["audiopost", "short", "full"] as PodcastFormat[]).find((f) => rest.includes(f));
      const d = needDate(rest.filter((r) => !["audiopost", "short", "full"].includes(r)));
      if (!d) return;
      const r = await makePodcast(d, { format: fmt });
      if (!r.ok && r.reason) return print(r.reason);
      print(`\nПодкаст на ${r.date} (${r.format}):`);
      if (r.audioPath) print(`  аудио: ${path.relative(config.repoRoot, r.audioPath)}${r.durationSeconds ? ` (${r.durationSeconds.toFixed(0)}с)` : ""}`);
      if (r.scriptPath) print(`  сценарий: ${path.relative(config.repoRoot, r.scriptPath)}`);
      if (r.telegramDraft) print(`  telegram-черновик: ${path.relative(config.repoRoot, r.telegramDraft)}`);
      for (const i of r.incomplete || []) print(`  — ${i}`);
      return;
    }
    case "telegram": {
      const d = needDate(rest);
      if (!d) return;
      const content = getContentByDate(d);
      const renderDir = path.join(reelsDir(d), "render");
      const finals = fs.existsSync(renderDir) ? fs.readdirSync(renderDir).filter((f) => /^final_reels_v\d+\.mp4$/.test(f)).sort() : [];
      if (!finals.length) return print(`Финального ролика на ${d} нет. Сначала: reel ${d}`);
      const finalPath = path.join(renderDir, finals[finals.length - 1]);
      const caption = buildCaption({ kind: "reel", title: content.topic, hook: content.topic, cta: content.cta, link: content.links[0] });
      const pub = await publish({ method: "sendVideo", filePath: finalPath, caption }, subDir(d, "publishing"));
      print(`Telegram (${pub.mode}): ${pub.ok ? "ок" : "ошибка: " + pub.error}`);
      print(pub.mode === "draft" ? "Режим draft — реальная отправка выключена (TELEGRAM_PUBLISH_MODE=live чтобы публиковать)." : `message_id: ${pub.messageId}`);
      if (pub.payloadPath) print(`payload: ${path.relative(config.repoRoot, pub.payloadPath)}`);
      return;
    }
    case "regen-scene": {
      const d = resolveDate(rest.slice(0, -1).join(" ") || rest[0] || "");
      const sceneRef = rest[rest.length - 1];
      if (!d || !sceneRef) return print("Использование: regen-scene <дата> <sceneId|номер>");
      const out = await regenerateScene(d, sceneRef);
      print(out.message);
      return;
    }
    default:
      print("Команды: doctor | avatars | voices | soul | index | content <дата> | status <дата> | script <дата> | scenes <дата> | route <дата> | reel <дата> | prepare <дата> | assemble <дата> | regen-scene <дата> <сцена> | voiceover <дата> | podcast <дата> [audiopost|short|full] | podcast <path.md> | telegram <дата>");
  }
}

main().catch((err) => {
  // eslint-disable-next-line no-console
  console.error("Ошибка:", err?.message || err);
  process.exit(1);
});
