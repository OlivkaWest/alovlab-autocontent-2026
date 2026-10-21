# -*- coding: utf-8 -*-
"""Отрисовка кадров (кроссовок сток/commercial) для продакшн-карусели. Только <g>, без вложенных <svg>."""

# кроссовок в локальных координатах ~0..232 x 0..108 (носок справа), стоит на y~104. Низкий длинный профиль.
def sneaker(sole, mid, body, toe, collar, lace, swoosh):
    return (
      f'<path d="M10 88 C4 102 22 106 36 104 L206 92 C228 90 234 78 222 74 C214 82 150 84 40 84 C22 83 14 84 10 88 Z" fill="{sole}"/>'
      f'<path d="M40 84 C122 82 200 78 210 78 L208 84 C150 86 70 86 40 86 Z" fill="{mid}"/>'
      f'<path d="M40 84 C36 62 80 56 112 55 L152 55 C186 56 200 66 202 78 C150 80 70 82 40 84 Z" fill="{body}"/>'
      f'<path d="M202 78 C204 68 196 58 178 59 C179 70 170 76 160 78 C178 78 196 77 202 78 Z" fill="{toe}"/>'
      f'<path d="M40 84 C36 62 55 55 72 57 C60 61 53 72 57 84 Z" fill="{collar}"/>'
      f'<path d="M60 62 C72 57 86 56 98 58 L96 63 C86 62 74 63 66 68 Z" fill="{collar}" opacity="0.65"/>'
      f'<g stroke="{lace}" stroke-width="3.2" stroke-linecap="round"><path d="M86 64 l20 8"/><path d="M100 60 l20 8"/><path d="M114 57 l18 8"/></g>'
      f'<path d="M56 78 C104 69 152 71 188 76" stroke="{swoosh}" stroke-width="6" fill="none" stroke-linecap="round"/>'
    )

GREY = dict(sole="#39352f", mid="#454039", body="#565049", toe="#4c463f", collar="#403a34", lace="#2e2a25", swoosh="#33302a")
LIT  = dict(sole="#cabfb0", mid="#e9e2d8", body="#f4efe7", toe="#ffb877", collar="#d8ccbc", lace="#b0a494", swoosh="#ff8a3d")

def _sneaker_at(px, py, sc, colors):
    return f'<g transform="translate({px:.1f},{py:.1f}) scale({sc:.3f})">{sneaker(**colors)}</g>'

def frame(ox, oy, w, h, good, lbl, tags=None, callouts=None):
    sc = w / 276.0
    sw = 232 * sc
    px = ox + (w - sw) / 2
    groundY = oy + h * 0.60
    py = groundY - 104 * sc
    inner = []
    if good:
        inner.append(f'<rect x="{ox}" y="{oy}" width="{w}" height="{h}" rx="16" fill="url(#haze)" stroke="url(#ig)" stroke-width="2.5"/>')
        inner.append(f'<ellipse cx="{ox+w/2:.0f}" cy="{oy+h*0.30:.0f}" rx="{w*0.42:.0f}" ry="{h*0.24:.0f}" fill="url(#rl)"/>')
        inner.append(f'<rect x="{ox+w*0.12:.0f}" y="{groundY+4:.0f}" width="{w*0.76:.0f}" height="12" rx="3" fill="#231d16"/>')
        inner.append(f'<rect x="{ox+w*0.12:.0f}" y="{groundY+4:.0f}" width="{w*0.76:.0f}" height="3" rx="1.5" fill="#5a4630"/>')
        # отражение
        refY = groundY + 104*sc*0.5
        inner.append(f'<g transform="translate({px:.1f},{refY:.1f}) scale({sc:.3f},{-sc*0.5:.3f})" opacity="0.16">{sneaker(**LIT)}</g>')
        inner.append(_sneaker_at(px, py, sc, LIT))
        # rim light по верху
        inner.append(f'<path d="M{px+40*sc:.0f} {py+52*sc:.0f} C{px+120*sc:.0f} {py+40*sc:.0f} {px+180*sc:.0f} {py+52*sc:.0f} {px+200*sc:.0f} {py+60*sc:.0f}" stroke="url(#ig)" stroke-width="3.5" fill="none" opacity="0.9"/>')
        inner.append(f'<circle cx="{ox+w*0.2:.0f}" cy="{groundY-6:.0f}" r="2.4" fill="#ff9a4d" opacity="0.8"/>')
        lblcol = "#ff9a4d"
    else:
        inner.append(f'<rect x="{ox}" y="{oy}" width="{w}" height="{h}" rx="16" fill="#141210" stroke="#ffffff1a" stroke-width="2"/>')
        inner.append(f'<line x1="{ox+18}" y1="{groundY:.0f}" x2="{ox+w-18}" y2="{groundY:.0f}" stroke="#2c2823" stroke-width="2"/>')
        inner.append(_sneaker_at(px, py, sc, GREY))
        lblcol = "#8a8177"
    inner.append(f'<text x="{ox+w/2:.0f}" y="{oy+h-16:.0f}" fill="{lblcol}" font-size="13" font-weight="800" font-family="Manrope" text-anchor="middle" letter-spacing="1.2">{lbl}</text>')
    if tags:
        for i, t in enumerate(tags):
            inner.append(f'<text x="{ox+18}" y="{oy+h-64+i*18:.0f}" fill="#7a7167" font-size="12" font-weight="600" font-family="Manrope">— {t}</text>')
    if callouts:
        inner.append(callouts)
    return "".join(inner)

DEFS_FRAME = ('<defs>'
  '<linearGradient id="ig" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc089"/><stop offset="1" stop-color="#f0712a"/></linearGradient>'
  '<linearGradient id="haze" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2c1c0d"/><stop offset="0.55" stop-color="#150e08"/><stop offset="1" stop-color="#0a0705"/></linearGradient>'
  '<radialGradient id="rl" cx="0.5" cy="0.3" r="0.6"><stop offset="0" stop-color="#ff8a3d" stop-opacity="0.5"/><stop offset="1" stop-color="#ff8a3d" stop-opacity="0"/></radialGradient>'
  '</defs>')

def viz_svg(w, h, inner, mh=400):
    return f'<div class="viz"><svg viewBox="0 0 {w} {h}" fill="none" style="max-height:{mh}px">{DEFS_FRAME}{inner}</svg></div>'
