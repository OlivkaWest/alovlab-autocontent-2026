import { describe, it, expect } from "vitest";
import { findBannedPhrases, checkHook } from "../src/content/style";

describe("style guard", () => {
  it("ловит канцелярщину", () => {
    const issues = findBannedPhrases("Важно понимать, что данный инструмент — это круто");
    expect(issues.length).toBeGreaterThanOrEqual(2);
  });
  it("чистый текст без замечаний", () => {
    expect(findBannedPhrases("Один пост из идеи — это любитель. Профи достаёт три.")).toHaveLength(0);
  });
  it("ловит запрещённое начало хука", () => {
    const issues = checkHook("Сегодня я расскажу, как делать контент");
    expect(issues.some((i) => i.kind === "banned_hook_opener")).toBe(true);
  });
  it("нормальный хук проходит", () => {
    expect(checkHook("Ты слишком быстро сжигаешь хорошие идеи.")).toHaveLength(0);
  });
});
