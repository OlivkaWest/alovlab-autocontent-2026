import { describe, it, expect } from "vitest";
import { resolveDate, monthDir } from "../src/dates";

describe("resolveDate", () => {
  const today = "2026-08-05";
  it("разбирает «5 августа» с годом из сегодня", () => {
    expect(resolveDate("5 августа", today)).toBe("2026-08-05");
    expect(resolveDate("Сделай ролик на 12 августа", today)).toBe("2026-08-12");
  });
  it("принимает ISO как есть", () => {
    expect(resolveDate("2026-08-05", today)).toBe("2026-08-05");
  });
  it("разбирает 05.08 и 05.08.2026", () => {
    expect(resolveDate("05.08", today)).toBe("2026-08-05");
    expect(resolveDate("05.08.2027", today)).toBe("2027-08-05");
  });
  it("явный год важнее сегодняшнего", () => {
    expect(resolveDate("5 августа 2025", today)).toBe("2025-08-05");
  });
  it("возвращает null на мусоре", () => {
    expect(resolveDate("завтра как-нибудь", today)).toBeNull();
  });
  it("monthDir", () => {
    expect(monthDir("2026-08-05")).toBe("2026-08");
  });
});
