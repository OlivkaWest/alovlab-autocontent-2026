import { z } from "zod";

// ─── Статусы задачи генерации (человеческие подписи в pipeline/statuses.ts) ───
export const JOB_STATUSES = [
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
  "failed",
] as const;
export const JobStatus = z.enum(JOB_STATUSES);
export type JobStatus = z.infer<typeof JobStatus>;

// ─── Цели контента ───
export const CONTENT_GOALS = [
  "reach",
  "subscribe",
  "save",
  "comment",
  "telegram",
  "course_sale",
  "studio_lead",
  "warmup",
] as const;
export const ContentGoal = z.enum(CONTENT_GOALS);
export type ContentGoal = z.infer<typeof ContentGoal>;

// ─── Бриф (шаг 1: создание темы) ───
export const Brief = z.object({
  theme: z.string().min(1),
  audience: z.string().default(""),
  goal: ContentGoal.default("reach"),
  platform: z.string().default("instagram"),
  desiredAction: z.string().default(""),
  cardCount: z.number().int().min(3).max(12).default(7),
  reelsDurationSeconds: z.number().int().min(15).max(90).default(30),
});
export type Brief = z.infer<typeof Brief>;

// ─── Карточка карусели ───
export const CARD_ROLES = [
  "cover",
  "problem",
  "insight",
  "solution",
  "example",
  "action",
  "cta",
] as const;
export const CardRole = z.enum(CARD_ROLES);
export type CardRole = z.infer<typeof CardRole>;

export const Card = z.object({
  id: z.string(),
  index: z.number().int().min(0),
  role: CardRole,
  title: z.string(),
  body: z.string().default(""),
  accent: z.string().default(""), // ключевая фраза, которую подсвечиваем оранжевым
});
export type Card = z.infer<typeof Card>;

export const Carousel = z.object({
  title: z.string(),
  cards: z.array(Card),
  caption: z.string().default(""), // описание поста
  cta: z.string().default(""),
});
export type Carousel = z.infer<typeof Carousel>;

// ─── Сцена Reels ───
export const SCENE_TYPES = ["avatar", "broll"] as const;
export const SceneType = z.enum(SCENE_TYPES);

export const Scene = z.object({
  id: z.string(),
  durationSeconds: z.number().min(1).max(20),
  type: SceneType,
  spokenText: z.string().default(""),
  onScreenText: z.string().default(""),
  visualSource: z.string().default(""), // avatar | card:<index> | broll:<id>
  cameraMotion: z.string().default(""),
  transition: z.string().default(""),
  subtitle: z.string().default(""),
  disabled: z.boolean().default(false),
});
export type Scene = z.infer<typeof Scene>;

// ─── Сценарий Reels ───
export const VIDEO_MODES = ["avatar_only", "avatar_broll"] as const;
export const VideoMode = z.enum(VIDEO_MODES);
export type VideoMode = z.infer<typeof VideoMode>;

export const ReelsScript = z.object({
  title: z.string(),
  durationSeconds: z.number().int().min(10).max(120),
  goal: z.string(),
  mode: VideoMode.default("avatar_broll"),
  hook: z.string(),
  avatarScript: z.string(),
  voiceoverScript: z.string(),
  cta: z.string(),
  scenes: z.array(Scene).min(1),
});
export type ReelsScript = z.infer<typeof ReelsScript>;

// ─── Субтитр ───
export const SubtitleCue = z.object({
  index: z.number().int(),
  startMs: z.number().int().min(0),
  endMs: z.number().int().min(0),
  text: z.string(),
});
export type SubtitleCue = z.infer<typeof SubtitleCue>;

// ─── Запись о задаче HeyGen ───
export const HeygenJob = z.object({
  videoId: z.string(),
  sceneId: z.string().nullable().default(null), // null = весь ролик; иначе — одна сцена
  status: z.string(),
  mock: z.boolean().default(false),
  videoUrl: z.string().nullable().default(null),
  localPath: z.string().nullable().default(null),
  creditsUsed: z.number().nullable().default(null),
  error: z.string().nullable().default(null),
  createdAt: z.string(),
  updatedAt: z.string(),
});
export type HeygenJob = z.infer<typeof HeygenJob>;

// ─── История перегенераций ───
export const HistoryEntry = z.object({
  at: z.string(),
  action: z.string(),
  detail: z.string().default(""),
});
export type HistoryEntry = z.infer<typeof HistoryEntry>;

// ─── Экспорт карусели ───
export const CarouselExport = z.object({
  pngFiles: z.array(z.string()).default([]),
  zipFile: z.string().nullable().default(null),
  jsonFile: z.string().nullable().default(null),
  previewFile: z.string().nullable().default(null),
});
export type CarouselExport = z.infer<typeof CarouselExport>;

// ─── Проект целиком ───
export const Project = z.object({
  id: z.string(),
  createdAt: z.string(),
  updatedAt: z.string(),
  status: JobStatus.default("draft"),
  brief: Brief,
  carousel: Carousel.nullable().default(null),
  carouselExport: CarouselExport.nullable().default(null),
  script: ReelsScript.nullable().default(null),
  subtitles: z.array(SubtitleCue).default([]),
  heygenJobs: z.array(HeygenJob).default([]),
  finalVideoPath: z.string().nullable().default(null),
  history: z.array(HistoryEntry).default([]),
});
export type Project = z.infer<typeof Project>;
