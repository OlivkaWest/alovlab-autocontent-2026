import { describe, it, expect, afterAll } from "vitest";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { buildCaption, auditCaption } from "../src/publishing/telegram/caption";
import { publish, livePreflight } from "../src/publishing/telegram/client";

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "alovlab-tg-"));
afterAll(() => fs.rmSync(tmp, { recursive: true, force: true }));

describe("telegram caption", () => {
  it("строит подпись с хуком и CTA, экранирует html", () => {
    const c = buildCaption({ kind: "podcast", title: "Тема", hook: "Один пост — это любитель", cta: "Сохрани", link: "https://t.me/AlovLab" });
    expect(c).toContain("<b>Один пост");
    expect(c).toContain("Сохрани");
    expect(c).toContain("t.me/AlovLab");
  });
  it("ловит канцелярщину в подписи", () => {
    expect(auditCaption("данный инструмент открывает новые возможности").length).toBeGreaterThan(0);
  });
});

describe("telegram publish — draft по умолчанию", () => {
  it("в draft НЕ отправляет, сохраняет payload", async () => {
    const r = await publish({ method: "sendAudio", caption: "тест", title: "T", performer: "Илья" }, tmp);
    expect(r.mode).toBe("draft");
    expect(r.ok).toBe(true);
    expect(fs.existsSync(r.payloadPath!)).toBe(true);
    const payload = JSON.parse(fs.readFileSync(r.payloadPath!, "utf8"));
    expect(payload.method).toBe("sendAudio");
    expect(payload.performer).toBe("Илья");
  });
  it("livePreflight сообщает про draft и отсутствие токена", () => {
    const pf = livePreflight();
    expect(pf.ok).toBe(false);
    expect(pf.issues.length).toBeGreaterThan(0);
  });
});
