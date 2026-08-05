// Стиль текста AlovLab: живые короткие фразы, спокойная уверенность.
// Здесь — защита от канцелярщины и шаблонных AI-фраз.

// Запрещено в любом тексте (п.11 брифа).
export const BANNED_PHRASES = [
  "важно понимать",
  "следует отметить",
  "данный инструмент",
  "позволяет вывести на новый уровень",
  "от идеи до реализации",
  "уникальный контент",
  "в современном мире",
  "откройте новые возможности",
  "давайте погрузимся",
  "революционный подход",
  "меняет правила игры",
];

// Запрещённые начала хука (п.7 брифа).
export const BANNED_HOOK_OPENERS = [
  "сегодня я расскажу",
  "в этом видео разберём",
  "в этом видео разберем",
  "вы когда-нибудь задумывались",
  "сейчас нейросети меняют мир",
  "давайте разберёмся",
  "давайте разберемся",
  "в современном мире",
];

export interface StyleIssue {
  kind: "banned_phrase" | "banned_hook_opener";
  match: string;
  where: string;
}

function norm(s: string): string {
  return s.toLowerCase().replace(/[«»"'`]/g, "").replace(/\s+/g, " ").trim();
}

/** Проверяет произвольный текст на канцелярщину. */
export function findBannedPhrases(text: string, where = "text"): StyleIssue[] {
  const n = norm(text);
  const issues: StyleIssue[] = [];
  for (const phrase of BANNED_PHRASES) {
    if (n.includes(phrase)) issues.push({ kind: "banned_phrase", match: phrase, where });
  }
  return issues;
}

/** Проверяет, что хук не начинается с запрещённого вступления. */
export function checkHook(hook: string): StyleIssue[] {
  const n = norm(hook);
  const issues: StyleIssue[] = [];
  for (const opener of BANNED_HOOK_OPENERS) {
    if (n.startsWith(opener)) {
      issues.push({ kind: "banned_hook_opener", match: opener, where: "hook" });
    }
  }
  issues.push(...findBannedPhrases(hook, "hook"));
  return issues;
}

/** Полная проверка стиля: возвращает список проблем (пустой = чисто). */
export function auditStyle(input: {
  hook?: string;
  texts?: Array<{ text: string; where: string }>;
}): StyleIssue[] {
  const issues: StyleIssue[] = [];
  if (input.hook !== undefined) issues.push(...checkHook(input.hook));
  for (const t of input.texts || []) issues.push(...findBannedPhrases(t.text, t.where));
  return issues;
}
