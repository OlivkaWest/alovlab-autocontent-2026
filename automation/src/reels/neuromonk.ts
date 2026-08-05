import { config, neuromonkReady } from "../config";

// Аватар Нейромонах — главный и единственный аватар проекта.
// avatar_id и voice_id берутся ТОЛЬКО из окружения и не меняются случайно.
export const NEUROMONK = {
  name: "Нейромонах",
  language: "Russian",
  format: "9:16",
  width: 1080,
  height: 1920,
  delivery: "спокойная, уверенная, живая",
  pace: "средний",
  emotion: "уверенность, лёгкий вызов",
  gestures: "умеренные",
  eyeContact: "взгляд в камеру",
} as const;

export interface NeuromonkResolved {
  ready: boolean;
  message?: string;
  avatarId: string;
  voiceId: string;
  language: string;
  engine: string;
}

/**
 * Возвращает конфигурацию Нейромонаха. Если avatar_id/voice_id не заданы —
 * ready=false и понятное сообщение (без stack trace).
 */
export function resolveNeuromonk(): NeuromonkResolved {
  const r = neuromonkReady();
  // В mock-режиме подставляем тестовые id, чтобы прогнать весь путь без ключей.
  const avatarId = config.heygen.avatarId || (config.heygen.mock ? "mock_neuromonk" : "");
  const voiceId = config.heygen.voiceId || (config.heygen.mock ? "mock_voice_ru" : "");
  return {
    ready: r.ready,
    message: r.message,
    avatarId,
    voiceId,
    language: config.heygen.language,
    engine: config.heygen.engine,
  };
}
