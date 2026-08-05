import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import type { GrokVideoInput, GrokVideoState } from "./types";

// Mock Grok: настоящий по структуре payload, тестовый request_id,
// путь статусов pending → processing → completed, локальный MP4. Без обращения к xAI.
const store = new Map<string, { polls: number; input: GrokVideoInput }>();
const READY_AT = 2;

export function mockCreate(input: GrokVideoInput): { requestId: string } {
  const requestId = `grok_mock_${crypto.randomBytes(6).toString("hex")}`;
  store.set(requestId, { polls: 0, input });
  return { requestId };
}

export function mockStatus(requestId: string): GrokVideoState {
  const rec = store.get(requestId);
  if (!rec) return { requestId, status: "completed", videoUrl: `mock://${requestId}.mp4`, progress: 100, error: null };
  rec.polls += 1;
  if (rec.polls >= READY_AT) {
    return { requestId, status: "completed", videoUrl: `mock://${requestId}.mp4`, progress: 100, error: null };
  }
  return { requestId, status: rec.polls === 1 ? "pending" : "processing", videoUrl: null, progress: rec.polls * 45, error: null };
}

export async function mockDownload(requestId: string, destPath: string): Promise<string> {
  fs.mkdirSync(path.dirname(destPath), { recursive: true });
  const { synthTestClip } = await import("../video/ffmpeg");
  const ok = await synthTestClip(destPath, 4).catch(() => false);
  if (!ok) fs.writeFileSync(destPath, Buffer.from(`ALOVLAB-MOCK-GROK:${requestId}`));
  return destPath;
}
