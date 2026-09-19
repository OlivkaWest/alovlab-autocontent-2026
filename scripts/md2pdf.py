import base64, pathlib, re, sys, html as _html
FONTS = pathlib.Path("/home/user/alovlab-autocontent-2026/assets/fonts")
def b64(n): return base64.b64encode((FONTS/n).read_bytes()).decode()
LOGO = base64.b64encode(pathlib.Path("/home/user/alovlab-autocontent-2026/assets/img/logo-mark.png").read_bytes()).decode()
faces=""
for w in (400,500,700,800):
    for sub in ("cyrillic","latin"):
        rng=("U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116" if sub=="cyrillic"
             else "U+0000-00FF,U+2013-2014,U+2018-201E,U+2018,U+2019,U+201C,U+201D,U+00AB,U+00BB,U+2026,U+2192")
        faces+=f"@font-face{{font-family:'Manrope';font-weight:{w};font-display:block;src:url(data:font/woff2;base64,{b64(f'manrope-{sub}-{w}.woff2')}) format('woff2');unicode-range:{rng};}}\n"

def inline(t):
    t=_html.escape(t)
    t=re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t=re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', t)
    return t

def md2html(md):
    lines=md.split('\n'); out=[]; i=0
    while i < len(lines):
        ln=lines[i]
        # code fence
        if ln.strip().startswith('```'):
            buf=[]; i+=1
            while i<len(lines) and not lines[i].strip().startswith('```'):
                buf.append(_html.escape(lines[i])); i+=1
            i+=1; out.append('<pre>'+'\n'.join(buf)+'</pre>'); continue
        # hr
        if ln.strip()=='---': out.append('<hr>'); i+=1; continue
        # heading
        m=re.match(r'^(#{1,6})\s+(.*)$', ln)
        if m:
            lvl=len(m.group(1)); h='h'+str(min(lvl,4)); out.append(f'<{h}>{inline(m.group(2))}</{h}>'); i+=1; continue
        # table
        if ln.strip().startswith('|') and i+1<len(lines) and set(lines[i+1].replace('|','').strip())<=set('-: '):
            header=[c.strip() for c in ln.strip().strip('|').split('|')]
            i+=2; rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i+=1
            th=''.join(f'<th>{inline(c)}</th>' for c in header)
            trs=''.join('<tr>'+''.join(f'<td>{inline(c)}</td>' for c in r)+'</tr>' for r in rows)
            out.append(f'<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'); continue
        # blockquote
        if ln.strip().startswith('>'):
            buf=[]
            while i<len(lines) and lines[i].strip().startswith('>'):
                buf.append(inline(lines[i].strip()[1:].strip())); i+=1
            out.append('<blockquote>'+'<br>'.join(buf)+'</blockquote>'); continue
        # list
        if re.match(r'^\s*[-*]\s+', ln):
            items=[]
            while i<len(lines) and re.match(r'^\s*[-*]\s+', lines[i]):
                item=re.sub(r'^\s*[-*]\s+','',lines[i])
                cb=re.match(r'^\[([ xX])\]\s+(.*)$', item)
                if cb:
                    box='☑' if cb.group(1).lower()=='x' else '☐'
                    items.append(f'<li class="chk">{box} {inline(cb.group(2))}</li>')
                else:
                    items.append(f'<li>{inline(item)}</li>')
                i+=1
            out.append('<ul>'+''.join(items)+'</ul>'); continue
        # numbered list
        if re.match(r'^\s*\d+\.\s+', ln):
            items=[]
            while i<len(lines) and re.match(r'^\s*\d+\.\s+', lines[i]):
                items.append('<li>'+inline(re.sub(r'^\s*\d+\.\s+','',lines[i]))+'</li>'); i+=1
            out.append('<ol>'+''.join(items)+'</ol>'); continue
        # blank
        if ln.strip()=='': i+=1; continue
        # paragraph
        out.append('<p>'+inline(ln.strip())+'</p>'); i+=1
    return '\n'.join(out)

def build(md_path, pdf_out, footer):
    md=pathlib.Path(md_path).read_text(encoding='utf-8')
    body=md2html(md)
    CSS=f"""{faces}
*{{margin:0;padding:0;box-sizing:border-box}}
@page{{size:A4;margin:18mm 16mm}}
:root{{--bg:#0d0b09;--text:#f4f0e8;--text2:#c3bbad;--dim:#7a7266;--o:#e8672a;--o2:#ff8a3d;--line:rgba(244,240,232,.12);--fld:rgba(244,240,232,.28)}}
html{{background:#0d0b09}}
body{{font-family:'Manrope',sans-serif;background:#0d0b09;color:var(--text);font-size:12.2pt;line-height:1.55;
padding:0}}
.wrap{{position:relative}}
.mast{{display:flex;align-items:center;gap:9px;margin-bottom:14px;padding-bottom:12px;border-bottom:1px solid var(--line)}}
.mast img{{width:26px;height:26px}} .mast b{{font-weight:800;font-size:15pt}}
h1{{font-weight:800;font-size:24pt;letter-spacing:-.02em;line-height:1.1;margin:2pt 0 6pt;color:#fff;break-after:avoid}}
h2{{font-weight:800;font-size:15.5pt;letter-spacing:-.01em;margin:16pt 0 5pt;color:#fff;break-after:avoid;padding-top:4pt}}
h2::before{{content:"";display:block;width:34px;height:3px;background:linear-gradient(90deg,var(--o2),var(--o));border-radius:3px;margin-bottom:8pt}}
h3{{font-weight:800;font-size:12.5pt;color:var(--o2);margin:11pt 0 3pt;break-after:avoid}}
p{{margin:0 0 6pt;color:var(--text2)}}
strong{{color:#fff;font-weight:800}} em{{color:var(--text2);font-style:italic}}
code{{font-family:'Manrope';background:#181410;border:1px solid var(--line);border-radius:5px;padding:1px 6px;color:var(--o2);font-size:10.5pt}}
pre{{background:#100e0b;border:1px solid var(--line);border-left:3px solid var(--o);border-radius:8px;padding:11px 14px;
white-space:pre-wrap;font-size:10pt;line-height:1.5;color:var(--text2);margin:7pt 0;break-inside:avoid}}
blockquote{{border-left:3px solid var(--o);background:rgba(232,103,42,.07);border-radius:0 8px 8px 0;padding:9pt 14pt;margin:8pt 0;color:var(--text);break-inside:avoid}}
blockquote strong{{color:var(--o2)}}
ul,ol{{margin:4pt 0 8pt;padding-left:2pt;list-style:none}}
li{{position:relative;padding-left:18px;margin-bottom:4pt;color:var(--text2);break-inside:avoid}}
li::before{{content:"";position:absolute;left:2px;top:8px;width:6px;height:6px;border-radius:50%;background:var(--o)}}
ol{{counter-reset:n}} ol li::before{{content:counter(n);counter-increment:n;background:none;color:var(--o2);font-weight:800;font-size:10.5pt;top:0;left:0;width:auto}}
ol li{{padding-left:22px}}
li.chk{{padding-left:24px}} li.chk::before{{content:"";border:1.6px solid var(--o);border-radius:3px;background:none;width:12px;height:12px;top:4px}}
table{{width:100%;border-collapse:collapse;margin:8pt 0;font-size:10.5pt;break-inside:avoid}}
th{{text-align:left;padding:7px 9px;font-weight:800;font-size:9.5pt;text-transform:uppercase;letter-spacing:.06em;color:var(--o2);border-bottom:1.5px solid rgba(232,103,42,.4)}}
td{{padding:7px 9px;border-bottom:1px solid var(--line);color:var(--text2);vertical-align:top}}
td strong{{color:#fff}}
hr{{border:none;border-top:1px solid var(--line);margin:12pt 0}}
tr,thead{{break-inside:avoid}}
</style>"""
    doc=f"""<!doctype html><html lang='ru'><head><meta charset='utf-8'><style>{CSS}</head><body><div class='wrap'>
<div class='mast'><img src='data:image/png;base64,{LOGO}'/><b>Alov<span style='color:#ff8a3d'>Lab</span></b></div>
{body}
</div></body></html>"""
    hp=pathlib.Path(pdf_out).with_suffix('.html'); hp.write_text(doc,encoding='utf-8')
    print("html:",hp)

if __name__=="__main__":
    build(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv)>3 else "AlovLab")
