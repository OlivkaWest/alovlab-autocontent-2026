import { describe, it, expect, afterAll } from "vitest";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { latestVersion, nextVersionPath, writeVersioned, saveStatus, loadStatus, setStatus, dayDir, DayStatus } from "../src/project/day-store";

const scratch = fs.mkdtempSync(path.join(os.tmpdir(), "alovlab-ver-"));
const TEST_DATE = "2099-12-31"; // не пересекается с реальными днями

afterAll(() => {
  fs.rmSync(scratch, { recursive: true, force: true });
  fs.rmSync(dayDir(TEST_DATE), { recursive: true, force: true });
});

describe("версионирование", () => {
  it("latestVersion растёт, nextVersionPath даёт +1", () => {
    expect(latestVersion(scratch, "reels_script", "json")).toBe(0);
    writeVersioned(scratch, "reels_script", "json", "{}");
    expect(latestVersion(scratch, "reels_script", "json")).toBe(1);
    const next = nextVersionPath(scratch, "reels_script", "json");
    expect(next.version).toBe(2);
    expect(next.path).toContain("reels_script_v2.json");
  });
});

describe("status.json — сохранение проекта дня", () => {
  it("save → load возвращает те же данные", () => {
    saveStatus(DayStatus.parse({ date: TEST_DATE, topic: "Тест", updated_at: new Date().toISOString() }));
    const loaded = loadStatus(TEST_DATE);
    expect(loaded?.topic).toBe("Тест");
    expect(loaded?.status).toBe("planned");
  });

  it("setStatus меняет статус и пишет историю", () => {
    setStatus(TEST_DATE, "script_ready", "gen", "v1");
    const s = loadStatus(TEST_DATE);
    expect(s?.status).toBe("script_ready");
    expect(s?.history.some((h) => h.action === "gen")).toBe(true);
  });
});
