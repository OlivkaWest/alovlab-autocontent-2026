// Типы запросов/ответов HeyGen (изолированы в модуле).

export interface HeygenAvatar {
  avatarId: string;
  name: string;
  previewUrl?: string;
}

export interface HeygenVoice {
  voiceId: string;
  name: string;
  language?: string;
  gender?: string;
}

// Единый статус видео, к которому приводим ответ HeyGen.
export type HeygenVideoStatus = "pending" | "processing" | "completed" | "failed";

export interface HeygenVideoState {
  videoId: string;
  status: HeygenVideoStatus;
  videoUrl: string | null;
  progress: number; // 0..100
  creditsUsed: number | null;
  error: string | null;
}

// Вход для создания видео (нейтральный контракт — не привязан к формату HeyGen).
export interface CreateVideoInput {
  script: string; // текст, который произносит аватар
  avatarId: string;
  voiceId: string;
  language: string;
  engine?: string;
  width: number;
  height: number;
  background?: string; // цвет фона (#RRGGBB) или пусто
  title?: string;
}
