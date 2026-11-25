# -*- coding: utf-8 -*-
"""
Пакетный рендер методичек 30 дней: workbook.md → фирменный HTML AlovLab.
HTML пишется рядом с будущим PDF в content-30-days/days/day-XX/.
Затем scripts/shoot_workbooks.js рендерит HTML → PDF (Playwright/Chromium).

Запуск:
  python3 scripts/render_all_workbooks.py            # все дни, где есть workbook.md
  python3 scripts/render_all_workbooks.py 22 23 24   # только указанные дни
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import md2pdf

ROOT = pathlib.Path(__file__).resolve().parent.parent
DAYS_DIR = ROOT / "content-30-days" / "days"


def main(argv):
    if argv:
        days = [int(x) for x in argv]
    else:
        days = list(range(1, 31))
    made = []
    for n in days:
        nn = f"{n:02d}"
        wb = DAYS_DIR / f"day-{nn}" / "workbook.md"
        if not wb.exists():
            print("SKIP day", nn, "— нет workbook.md")
            continue
        pdf_out = DAYS_DIR / f"day-{nn}" / f"alovlab-day-{nn}.pdf"
        md2pdf.build(str(wb), str(pdf_out), "AlovLab")  # пишет .html рядом
        made.append(nn)
    print("HTML собран для дней:", ",".join(made) if made else "нет")


if __name__ == "__main__":
    main(sys.argv[1:])
