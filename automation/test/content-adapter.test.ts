import { describe, it, expect } from "vitest";
import { getContentByDate } from "../src/content/adapter";
import { cardFileName } from "../src/carousel/template";
import { Card } from "../src/store/types";

describe("content adapter — реальный день 2026-08-05", () => {
  it("находит день и читает тему + карточки", () => {
    const c = getContentByDate("2026-08-05");
    expect(c.found).toBe(true);
    expect(c.topic).toContain("Одна идея");
    expect(c.cards.length).toBe(7);
    expect(c.cards[0].role).toBe("cover");
  });

  it("несуществующий день → found=false, без выдумок", () => {
    const c = getContentByDate("1999-01-01");
    expect(c.found).toBe(false);
    expect(c.topic).toBe("");
    expect(c.missing.length).toBeGreaterThan(0);
  });
});

describe("PNG экспорт — имена файлов карточек", () => {
  it("01_cover.png, 02_problem.png …", () => {
    expect(cardFileName(Card.parse({ id: "c", index: 0, role: "cover", title: "t", body: "", accent: "" }))).toBe("01_cover.png");
    expect(cardFileName(Card.parse({ id: "c", index: 6, role: "cta", title: "t", body: "", accent: "" }))).toBe("07_cta.png");
  });
});
