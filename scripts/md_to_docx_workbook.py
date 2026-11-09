#!/usr/bin/env python3
"""Конвертер methodичка.md -> .docx для 30-дневного плана AlovLab.
Разбирает по верхнеуровневым '## ' заголовкам (разделы А, Б, В...), поддерживает **bold**,
таблицы, ``` код ```, - буллеты, - [ ] чек-листы. Не универсальный MD-парсер — рассчитан
на структуру workbook.md из content/plans/*/days/day-NN/.
Использование: python3 scripts/md_to_docx_workbook.py <входной .md> <выходной .docx> "<Тема дня>"
"""
import sys
import docx
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ORANGE = RGBColor(0xDA, 0x5F, 0x1E)
INK = RGBColor(0x1b, 0x17, 0x12)
MUTED = RGBColor(0x73, 0x68, 0x58)

if len(sys.argv) < 3:
    print(__doc__)
    sys.exit(1)
SRC_PATH = sys.argv[1]
OUT_PATH = sys.argv[2]
TOPIC = sys.argv[3] if len(sys.argv) > 3 else "AlovLab"

doc = Document()
sec = doc.sections[0]
sec.page_width = Cm(21); sec.page_height = Cm(29.7)
sec.top_margin = Cm(2.2); sec.bottom_margin = Cm(2.2)
sec.left_margin = Cm(2.4); sec.right_margin = Cm(2.4)

style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)

def add_page_number(paragraph):
    run = paragraph.add_run()
    fld1 = OxmlElement('w:fldChar'); fld1.set(qn('w:fldCharType'), 'begin')
    instr = OxmlElement('w:instrText'); instr.set(qn('xml:space'), 'preserve'); instr.text = 'PAGE'
    fld2 = OxmlElement('w:fldChar'); fld2.set(qn('w:fldCharType'), 'end')
    run._r.append(fld1); run._r.append(instr); run._r.append(fld2)

footer = sec.footer.paragraphs[0]
footer.text = f"AlovLab · {TOPIC} · стр. "
footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
add_page_number(footer)

# Title page
t = doc.add_paragraph(); t.alignment = WD_ALIGN_PARAGRAPH.LEFT
r = t.add_run("AlovLab · Автоконтент 2026"); r.font.size = Pt(10); r.font.color.rgb = ORANGE; r.bold = True
h = doc.add_heading("5 настроек ChatGPT, которые меняют каждый ответ", level=0)
for run in h.runs:
    run.font.color.rgb = INK
p = doc.add_paragraph("Мини-урок дня 1 из 30-дневной системы AlovLab. Настрой личный контекст один раз — вместо того чтобы объяснять его в каждом новом чате.")
p.runs[0].font.size = Pt(13); p.runs[0].font.color.rgb = MUTED
doc.add_page_break()

def h1(text):
    hh = doc.add_heading(text, level=1)
    for run in hh.runs:
        run.font.color.rgb = INK

def h2(text):
    hh = doc.add_heading(text, level=2)
    for run in hh.runs:
        run.font.color.rgb = ORANGE

def para(text, bold=False, italic=False):
    pp = doc.add_paragraph()
    rr = pp.add_run(text)
    rr.bold = bold; rr.italic = italic
    return pp

def code_block(text):
    pp = doc.add_paragraph()
    pp.paragraph_format.left_indent = Cm(0.5)
    rr = pp.add_run(text)
    rr.font.name = 'Consolas'
    rr.font.size = Pt(10)
    return pp

def bullet(text):
    pp = doc.add_paragraph(style='List Bullet')
    segs = re.split(r'(\*\*[^*]+\*\*)', text)
    for s in segs:
        if s.startswith('**') and s.endswith('**'):
            rr = pp.add_run(s.strip('*')); rr.bold = True
        else:
            pp.add_run(s)

# Read source markdown and do a simple structured walk (manual mapping, not generic MD parser,
# since we control the exact source and want reliable Word formatting)
import re
src = open(SRC_PATH, encoding='utf-8').read()

# Split on top-level "## " headings (А, Б, В ... sections)
blocks = re.split(r'\n(?=## )', src)
for b in blocks:
    b = b.strip()
    if not b or b.startswith('# AlovLab') or b.startswith('> ⟳'):
        continue
    lines = b.split('\n')
    heading = lines[0].replace('## ', '').strip()
    h1(heading)
    body = '\n'.join(lines[1:]).strip()
    # naive block parsing: split on blank lines, handle ```code```, tables, bullets, ### subheads
    parts = re.split(r'\n\n+', body)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if part.startswith('```'):
            code = part.strip('`').strip()
            code_block(code)
        elif part.startswith('### '):
            h2(part.replace('### ', '').strip())
        elif part.startswith('| '):
            rows = [l for l in part.split('\n') if l.strip().startswith('|')]
            rows = [r for r in rows if not re.match(r'^\|[\s\-\|]+\|$', r)]
            if rows:
                cells0 = [c.strip() for c in rows[0].strip('|').split('|')]
                table = doc.add_table(rows=0, cols=len(cells0))
                table.style = 'Light Grid Accent 2'
                for r_ in rows:
                    cells = [c.strip() for c in r_.strip('|').split('|')]
                    row_cells = table.add_row().cells
                    for i, c in enumerate(cells):
                        if i < len(row_cells):
                            row_cells[i].text = c.replace('**','')
        elif part.startswith('- ['):
            for line in part.split('\n'):
                bullet(line.replace('- [ ] ', '☐ ').replace('- [x] ', '☑ '))
        elif part.startswith('- ') or part.startswith('1. '):
            for line in part.split('\n'):
                clean = re.sub(r'^(\-|\d+\.)\s+', '', line).strip()
                if clean:
                    bullet(clean)
        elif part.startswith('**'):
            pp = doc.add_paragraph()
            txt = part
            segs = re.split(r'(\*\*[^*]+\*\*)', txt)
            for s in segs:
                if s.startswith('**') and s.endswith('**'):
                    rr = pp.add_run(s.strip('*')); rr.bold = True
                else:
                    pp.add_run(s)
        else:
            pp = doc.add_paragraph()
            segs = re.split(r'(\*\*[^*]+\*\*)', part)
            for s in segs:
                if s.startswith('**') and s.endswith('**'):
                    rr = pp.add_run(s.strip('*')); rr.bold = True
                else:
                    pp.add_run(s)
    doc.add_paragraph()

doc.save(OUT_PATH)
print("saved docx:", OUT_PATH)
