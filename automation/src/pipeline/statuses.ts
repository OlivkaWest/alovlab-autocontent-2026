import type { JobStatus } from "../store/types";

// Человеческие формулировки. Внутренние коды пользователю без объяснения не показываем.
export const STATUS_LABELS: Record<JobStatus, string> = {
  draft: "Черновик",
  script_ready: "Сценарий готов",
  waiting_for_approval: "Ждём подтверждения сцен",
  sending_to_heygen: "Отправляем в HeyGen",
  processing_avatar: "Аватар создаётся",
  avatar_ready: "Аватар готов",
  rendering_broll: "Собираем B-roll",
  assembling_video: "Собираем сцены",
  adding_subtitles: "Добавляем субтитры",
  ready: "Ролик готов",
  failed: "Одна сцена сломалась",
};

export function humanStatus(status: JobStatus): string {
  return STATUS_LABELS[status] ?? status;
}

// Порядок этапов для отрисовки прогресса.
export const STATUS_ORDER: JobStatus[] = [
  "draft",
  "script_ready",
  "waiting_for_approval",
  "sending_to_heygen",
  "processing_avatar",
  "avatar_ready",
  "rendering_broll",
  "assembling_video",
  "adding_subtitles",
  "ready",
];
