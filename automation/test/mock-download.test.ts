import { describe, it, expect, afterAll } from "vitest";
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { mockCreateVideo, mockGetStatus } from "../src/heygen/mock";
import { downloadVideo } from "../src/heygen/download-video";
import { getVideoStatus } from "../src/heygen/get-video-status";
import { grokCreateVideo, grokGetStatus } from "../src/grok/client";

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "alovlab-test-"));
afterAll(() => fs.rmSync(tmp, { recursive: true, force: true }));

describe("HeyGen mock — путь статусов", () => {
  it("pending → processing → completed", async () => {
    const { videoId } = mockCreateVideo({ script: "x", avatarId: "a", voiceId: "v", language: "ru", width: 1080, height: 1920 });
    const s1 = mockGetStatus(videoId);
    const s2 = mockGetStatus(videoId);
    expect(s1.status).toBe("pending");
    expect(s2.status).toBe("completed");
    expect(s2.videoUrl).toContain("mock://");
  });

  it("getVideoStatus проксирует mock по префиксу", async () => {
    const { videoId } = mockCreateVideo({ script: "x", avatarId: "a", voiceId: "v", language: "ru", width: 1080, height: 1920 });
    const st = await getVideoStatus(videoId);
    expect(["pending", "processing", "completed"]).toContain(st.status);
  });
});

describe("downloadVideo — mock пишет файл", () => {
  it("создаёт локальный файл из mock:// ссылки", async () => {
    const dest = path.join(tmp, "v.mp4");
    await downloadVideo("mock://abc.mp4", dest, "mock_abc");
    expect(fs.existsSync(dest)).toBe(true);
    expect(fs.statSync(dest).size).toBeGreaterThan(0);
  });
});

describe("Grok mock", () => {
  it("создаёт задачу и доходит до completed", async () => {
    const { requestId, mock } = await grokCreateVideo({ mode: "text_to_video", prompt: "p", durationSeconds: 4, aspectRatio: "9:16", resolution: "720p" });
    expect(mock).toBe(true);
    grokGetStatus(requestId); // pending
    const s = await grokGetStatus(requestId);
    expect(s.status).toBe("completed");
  });
});
