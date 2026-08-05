// Нейтральный контракт задачи Grok (не привязан к финальной схеме xAI).
export interface GrokVideoInput {
  mode: "text_to_video" | "image_to_video";
  prompt: string;
  imagePath?: string; // для image-to-video
  durationSeconds: number;
  aspectRatio: string; // "9:16"
  resolution: string; // "720p"
  negativePrompt?: string;
}

export type GrokStatus = "pending" | "processing" | "completed" | "failed";

export interface GrokVideoState {
  requestId: string;
  status: GrokStatus;
  videoUrl: string | null;
  progress: number;
  error: string | null;
}
