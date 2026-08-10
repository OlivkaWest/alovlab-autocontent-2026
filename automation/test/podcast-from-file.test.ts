import { describe, it, expect } from "vitest";
import { parseScriptMarkdown } from "../src/podcast/from-file";

const MD = `# Подкаст · День 7 · «Связка недели»

**Формат:** монолог, ~5–6 минут.
**Тема:** одна идея — семь ролей.

---

## Сценарий (читать как речь, паузы — по смыслу)

Первая мысль вслух.

Вторая мысль вслух.

---

## Короткое описание эпизода (для площадки)

Аннотация для карточки эпизода.
`;

describe("parseScriptMarkdown — verbatim, без утечки мета", () => {
  const p = parseScriptMarkdown(MD);

  it("берёт заголовок из первого H1", () => {
    expect(p.title).toContain("Связка недели");
  });

  it("речь — только тело сценария, дословно", () => {
    expect(p.narration).toContain("Первая мысль вслух.");
    expect(p.narration).toContain("Вторая мысль вслух.");
  });

  it("в речь не попадают мета-строки, ремарка и описание", () => {
    expect(p.narration).not.toContain("Формат:");
    expect(p.narration).not.toContain("читать как речь");
    expect(p.narration).not.toContain("Аннотация для карточки");
  });

  it("описание эпизода вытащено отдельно (для подписи)", () => {
    expect(p.description).toContain("Аннотация для карточки эпизода.");
  });

  it("без секции «Сценарий» — читает тело, срезая front-matter", () => {
    const plain = parseScriptMarkdown("# Заголовок\n\n**Тема:** x\n\nПросто речь.\n");
    expect(plain.narration).toBe("Просто речь.");
  });
});
