// Разбор человеческих дат из команд Claude Code: «5 августа» → 2026-08-05.

const MONTHS_RU: Record<string, number> = {
  январ: 1, феврал: 2, март: 3, апрел: 4, ма: 5, июн: 6, июл: 7,
  август: 8, сентябр: 9, октябр: 10, ноябр: 11, декабр: 12,
};

function pad(n: number): string {
  return String(n).padStart(2, "0");
}

/** Текущая дата в ISO (YYYY-MM-DD). Вынесено, чтобы подменять в тестах. */
export function todayIso(now: Date = new Date()): string {
  return `${now.getUTCFullYear()}-${pad(now.getUTCMonth() + 1)}-${pad(now.getUTCDate())}`;
}

function monthFromWord(word: string): number | null {
  const w = word.toLowerCase();
  for (const [stem, m] of Object.entries(MONTHS_RU)) {
    if (w.startsWith(stem)) return m;
  }
  return null;
}

/**
 * Приводит команду к ISO-дате. Год берётся из «сегодня», если не указан.
 * Если месяц/день уже прошли в этом году — НЕ прыгаем в прошлое, оставляем текущий год
 * (производственный контент планируется на конкретный год проекта).
 * Возвращает null, если дату не удалось распознать.
 */
export function resolveDate(input: string, today: string = todayIso()): string | null {
  const text = input.trim().toLowerCase();
  const [ty] = today.split("-").map(Number);

  // Уже ISO?
  const iso = text.match(/(\d{4})-(\d{2})-(\d{2})/);
  if (iso) return `${iso[1]}-${iso[2]}-${iso[3]}`;

  // «5 августа [2026]» или «5 август»
  const ru = text.match(/(\d{1,2})\s+([а-яё]+)(?:\s+(\d{4}))?/i);
  if (ru) {
    const day = Number(ru[1]);
    const month = monthFromWord(ru[2]);
    const year = ru[3] ? Number(ru[3]) : ty;
    if (month && day >= 1 && day <= 31) return `${year}-${pad(month)}-${pad(day)}`;
  }

  // «05.08» или «05.08.2026»
  const dot = text.match(/(\d{1,2})[.\/](\d{1,2})(?:[.\/](\d{4}))?/);
  if (dot) {
    const day = Number(dot[1]);
    const month = Number(dot[2]);
    const year = dot[3] ? Number(dot[3]) : ty;
    if (month >= 1 && month <= 12 && day >= 1 && day <= 31) return `${year}-${pad(month)}-${pad(day)}`;
  }

  return null;
}

/** Папка месяца: 2026-08. */
export function monthDir(dateIso: string): string {
  return dateIso.slice(0, 7);
}
