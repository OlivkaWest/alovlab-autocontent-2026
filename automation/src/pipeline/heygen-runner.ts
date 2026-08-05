import path from "node:path";
import { projectDir, saveProject, loadProject, addHistory, nowIso } from "../store/projects";
import { createLogger } from "../logger";
import { resolveNeuromonk, NEUROMONK } from "../reels/neuromonk";
import { createVideo } from "../heygen/create-video";
import { getVideoStatus } from "../heygen/get-video-status";
import { downloadVideo } from "../heygen/download-video";
import { HeygenError } from "../heygen/errors";
import { HeygenJob, type Project, type Scene } from "../store/types";

const log = createLogger("heygen-runner");

const sleep = (ms: number) => new Promise<void>((r) => setTimeout(r, ms));

/** Текст, который произносит аватар: для всего ролика — вся речь по сценам. */
function narrationFor(project: Project, scene: Scene | null): string {
  if (scene) return scene.spokenText || scene.subtitle || "";
  const active = project.script?.scenes.filter((s) => !s.disabled) || [];
  return active.map((s) => s.spokenText).filter(Boolean).join(" ");
}

function upsertJob(project: Project, job: HeygenJob): void {
  const i = project.heygenJobs.findIndex((j) => j.sceneId === job.sceneId);
  if (i === -1) project.heygenJobs.push(job);
  else project.heygenJobs[i] = job;
}

/**
 * Полный прогон HeyGen для проекта (или одной сцены при sceneId).
 * Создаёт задачу, сохраняет video_id, поллит статус, скачивает MP4.
 * Состояние пишется в проект на каждом шаге — переживает перезапуск.
 */
export async function runHeygen(projectId: string, sceneId: string | null, options: { background?: string } = {}): Promise<void> {
  let project = loadProject(projectId);
  if (!project || !project.script) return;

  const neuromonk = resolveNeuromonk();
  if (!neuromonk.ready) {
    project.status = "failed";
    addHistory(project, "heygen_blocked", neuromonk.message || "нет avatar_id/voice_id");
    saveProject(project);
    return;
  }

  const scene = sceneId ? project.script.scenes.find((s) => s.id === sceneId) || null : null;
  const text = narrationFor(project, scene);

  project.status = "sending_to_heygen";
  saveProject(project);

  let videoId: string;
  let mock: boolean;
  try {
    const created = await createVideo({
      script: text,
      avatarId: neuromonk.avatarId,
      voiceId: neuromonk.voiceId,
      language: neuromonk.language,
      engine: neuromonk.engine || undefined,
      width: NEUROMONK.width,
      height: NEUROMONK.height,
      background: options.background,
      title: project.script.title,
    });
    videoId = created.videoId;
    mock = created.mock;
  } catch (err) {
    project = loadProject(projectId) || project;
    project.status = "failed";
    const msg = err instanceof HeygenError ? err.human : String(err);
    addHistory(project, "heygen_create_failed", msg);
    saveProject(project);
    log.error("Создание видео упало", msg);
    return;
  }

  const now = nowIso();
  const job: HeygenJob = HeygenJob.parse({
    videoId,
    sceneId,
    status: "processing",
    mock,
    videoUrl: null,
    localPath: null,
    creditsUsed: null,
    error: null,
    createdAt: now,
    updatedAt: now,
  });
  project = loadProject(projectId) || project;
  upsertJob(project, job);
  project.status = "processing_avatar";
  addHistory(project, "heygen_created", `${videoId}${sceneId ? ` (сцена ${sceneId})` : ""}`);
  saveProject(project);

  // Поллинг с бэкоффом. Не бесконечный.
  const maxPolls = 40;
  let delay = 3000;
  for (let i = 0; i < maxPolls; i++) {
    await sleep(delay);
    delay = Math.min(delay * 1.3, 15000);
    let state;
    try {
      state = await getVideoStatus(videoId);
    } catch (err) {
      log.warn(`Опрос статуса ${videoId} не удался, продолжаем`, String(err));
      continue;
    }
    project = loadProject(projectId) || project;
    const j = project.heygenJobs.find((x) => x.videoId === videoId);
    if (j) {
      j.status = state.status;
      j.videoUrl = state.videoUrl;
      j.creditsUsed = state.creditsUsed;
      j.updatedAt = nowIso();
    }
    saveProject(project);

    if (state.status === "failed") {
      project.status = "failed";
      if (j) j.error = state.error || "video_failed";
      addHistory(project, "heygen_failed", state.error || "");
      saveProject(project);
      return;
    }
    if (state.status === "completed" && state.videoUrl) {
      project.status = "avatar_ready";
      saveProject(project);
      // Скачивание
      const dest = path.join(projectDir(projectId), "video", `${sceneId ? `scene_${sceneId}` : "avatar"}.mp4`);
      try {
        await downloadVideo(state.videoUrl, dest, videoId);
      } catch (err) {
        project = loadProject(projectId) || project;
        project.status = "failed";
        addHistory(project, "download_failed", err instanceof HeygenError ? err.human : String(err));
        saveProject(project);
        return;
      }
      project = loadProject(projectId) || project;
      const jj = project.heygenJobs.find((x) => x.videoId === videoId);
      if (jj) {
        jj.localPath = dest;
        jj.status = "completed";
        jj.updatedAt = nowIso();
      }
      addHistory(project, "avatar_downloaded", dest);
      saveProject(project);
      return;
    }
  }

  // Таймаут поллинга
  project = loadProject(projectId) || project;
  project.status = "failed";
  addHistory(project, "heygen_timeout", `видео ${videoId} не собралось за отведённое время`);
  saveProject(project);
}
