import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import type { CreateVideoInput, HeygenVideoState, HeygenAvatar, HeygenVoice } from "./types";

// Mock-режим: реальные запросы не уходят, кредиты не тратятся.
// Каждый video_id проходит тот же путь статусов: pending → processing → completed.

interface MockRecord {
  polls: number;
  input: CreateVideoInput;
}

const store = new Map<string, MockRecord>();

// Через сколько опросов считаем видео готовым.
const POLLS_TO_READY = 2;

export function mockCreateVideo(input: CreateVideoInput): { videoId: string } {
  const videoId = `mock_${crypto.randomBytes(6).toString("hex")}`;
  store.set(videoId, { polls: 0, input });
  return { videoId };
}

export function mockGetStatus(videoId: string): HeygenVideoState {
  const rec = store.get(videoId);
  if (!rec) {
    // После перезапуска процесса память пуста — считаем готовым, чтобы не зависнуть.
    return { videoId, status: "completed", videoUrl: `mock://${videoId}.mp4`, progress: 100, creditsUsed: 0, error: null };
  }
  rec.polls += 1;
  if (rec.polls >= POLLS_TO_READY) {
    return { videoId, status: "completed", videoUrl: `mock://${videoId}.mp4`, progress: 100, creditsUsed: 0, error: null };
  }
  return {
    videoId,
    status: rec.polls === 1 ? "pending" : "processing",
    videoUrl: null,
    progress: rec.polls * 40,
    creditsUsed: null,
    error: null,
  };
}

/**
 * «Скачивание» в mock-режиме: кладём локальный тестовый MP4.
 * Пытаемся собрать короткий чёрный клип 9:16 через ffmpeg; если ffmpeg нет —
 * пишем минимальный валидный по контейнеру заглушечный файл.
 */
export async function mockDownload(videoId: string, destPath: string): Promise<string> {
  fs.mkdirSync(path.dirname(destPath), { recursive: true });
  const { synthTestClip } = await import("../video/ffmpeg");
  const ok = await synthTestClip(destPath).catch(() => false);
  if (!ok) {
    // Заглушка: помечаем, что это mock-файл. Достаточно для проверки пайплайна.
    fs.writeFileSync(destPath, Buffer.from(`ALOVLAB-MOCK-MP4:${videoId}`));
  }
  return destPath;
}

export const MOCK_AVATARS: HeygenAvatar[] = [
  { avatarId: "mock_neuromonk", name: "Нейромонах (mock)", previewUrl: "" },
  { avatarId: "mock_avatar_2", name: "Аватар 2 (mock)", previewUrl: "" },
];

export const MOCK_VOICES: HeygenVoice[] = [
  { voiceId: "mock_voice_ru", name: "Русский мужской (mock)", language: "ru", gender: "male" },
  { voiceId: "mock_voice_ru_f", name: "Русский женский (mock)", language: "ru", gender: "female" },
];
