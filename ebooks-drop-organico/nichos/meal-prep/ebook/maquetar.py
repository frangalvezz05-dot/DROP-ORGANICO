"""Maqueta "The Sunday Sheet" (EN) a HTML con la plantilla de .claude/skills/maquetar-pdf.
Uso:  python3 maquetar.py            -> genera en en/:
        the-sunday-sheet-pantalla.html    (A5 148x210, principal)
        the-sunday-sheet-imprimible.html  (Letter, solo hojas para rellenar/pegar)
        the-mini-sunday-pantalla.html     (muestra gratis, A5)
        portadas/portada-A|B|C.html       (3 propuestas de portada)
Los PDF se sacan después con: node .claude/skills/maquetar-pdf/generar-pdf.js <html> <pdf>
Los comentarios <!-- --> del Markdown no se imprimen. Las marcas [SIN DATO ...] tampoco."""
import json, os, re, html
import markdown

AQUI = os.path.dirname(os.path.abspath(__file__))
EN = os.path.join(AQUI, 'en')
NICHO = os.path.dirname(AQUI)
MARCA = json.load(open(os.path.join(NICHO, 'marca.json'), encoding='utf-8'))
CSS = '../../../../.claude/skills/maquetar-pdf/'          # desde en/
CSS_PORTADAS = '../../../../../.claude/skills/maquetar-pdf/'  # desde en/portadas/

# Portada elegida (modo continuo): la más legible a 150 px de ancho. Ver portadas/eleccion.md
PORTADA_ELEGIDA = 'B'

TITULO = MARCA['titulo']['en']
SUB = MARCA['titulo']['subtitulo_en']
SUB_1, SUB_2 = [s.strip() for s in SUB.split(':', 1)] if ':' in SUB else (SUB, '')

def leer(p):
    return open(os.path.join(EN, p), encoding='utf-8').read()

# ----------------------------------------------------------------- iconos (sprite)
SPRITE = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
  '<symbol id="ico-ejercicio" viewBox="0 0 24 24"><path d="M4 20l1-4L16 5l3 3L8 19z"/><path d="M14 7l3 3"/></symbol>'
  '<symbol id="ico-sos" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3.8"/><path d="M5.6 5.6l3.7 3.7M14.7 14.7l3.7 3.7M18.4 5.6l-3.7 3.7M9.3 14.7l-3.7 3.7"/></symbol>'
  '<symbol id="ico-aviso" viewBox="0 0 24 24"><path d="M12 3.5l9.5 16.5h-19z"/><path d="M12 10v4.5M12 17.4v.2"/></symbol>'
  '<symbol id="ico-consejo" viewBox="0 0 24 24"><path d="M9.5 18h5M10.5 21h3"/><path d="M12 3a6 6 0 0 0-3.4 10.9c.6.5 1 1.2 1 2.1h4.8c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/></symbol>'
  '<symbol id="ico-nevera" viewBox="0 0 24 24"><rect x="6" y="2.5" width="12" height="19" rx="2"/><path d="M6 9.5h12M9 5.5v2M9 12.5v3"/></symbol>'
  '<symbol id="ico-frio" viewBox="0 0 24 24"><path d="M12 2.5v19M3.8 7.2l16.4 9.6M3.8 16.8l16.4-9.6M9.5 4l2.5 2.5L14.5 4M9.5 20l2.5-2.5 2.5 2.5"/></symbol>'
  '<symbol id="ico-reloj" viewBox="0 0 24 24"><circle cx="12" cy="13" r="8.5"/><path d="M12 8.5V13l3 2M9.5 2.5h5"/></symbol>'
  '<symbol id="ico-imprimir" viewBox="0 0 24 24"><path d="M7 9V3h10v6"/><rect x="3" y="9" width="18" height="8" rx="1.5"/><path d="M7 14h10v7H7z"/></symbol>'
  '<symbol id="ico-carro" viewBox="0 0 24 24"><path d="M2.5 3.5h3l2.4 11.2h10.6l2-7.7H6.7"/><circle cx="9.5" cy="19.5" r="1.4"/><circle cx="17" cy="19.5" r="1.4"/></symbol>'
  '</defs></svg>')

def ico(n):
    return f'<svg class="ico"><use href="#ico-{n}"/></svg>'

# ----------------------------------------------------------------- ilustración de portada (SVG propio)
COMIDA = {'arroz': '#EFE6D2', 'grano': '#D9CCAE', 'brocoli': '#4F7A43', 'brocoli2': '#6E9A58',
          'boniato': '#E2843A', 'pollo': '#C99560', 'pollo2': '#A9743F', 'pimiento': '#C9402A', 'salsa': '#D9572B'}

def tupper(x, y, w, h, tipo, tapa='#1F3A2E', fondo='#FFFFFF'):
    """Tupper rectangular visto desde arriba, con 2 compartimentos de comida."""
    s = [f'<g transform="translate({x} {y})">',
         f'<rect x="1.2" y="2" width="{w}" height="{h}" rx="4.5" fill="#000" opacity=".16"/>',
         f'<rect width="{w}" height="{h}" rx="4.5" fill="{fondo}" stroke="{tapa}" stroke-width="1.1"/>',
         f'<rect x="2.4" y="2.4" width="{w-4.8}" height="{h-4.8}" rx="3" fill="none" stroke="{tapa}" stroke-width=".35" opacity=".5"/>']
    cw = (w - 7.5) * 0.58
    # compartimento grande: base
    bx, by, bw, bh = 3.5, 3.5, cw, h - 7
    s.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="2" fill="{COMIDA["arroz"]}"/>')
    if tipo in ('a', 'c'):
        for i in range(18):
            gx = bx + 2 + (i * 5.3) % (bw - 4); gy = by + 2 + (i * 3.7) % (bh - 4)
            s.append(f'<ellipse cx="{gx:.1f}" cy="{gy:.1f}" rx="1" ry=".45" fill="{COMIDA["grano"]}" transform="rotate({(i*37)%180} {gx:.1f} {gy:.1f})"/>')
    else:
        s[-1] = f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="2" fill="#F6E3CF"/>'
        for i in range(9):
            gx = bx + 3 + (i % 3) * (bw - 6) / 2.6; gy = by + 3 + (i // 3) * (bh - 6) / 2.7
            s.append(f'<rect x="{gx:.1f}" y="{gy:.1f}" width="4.2" height="4.2" rx=".8" fill="{COMIDA["boniato"]}" transform="rotate({(i*23)%40-20} {gx+2:.1f} {gy+2:.1f})"/>')
    # proteína encima de la base (tiras de pollo)
    for i in range(3):
        px = bx + 3 + i * (bw - 8) / 3; py = by + bh * 0.28
        s.append(f'<rect x="{px:.1f}" y="{py:.1f}" width="{(bw-8)/3.4:.1f}" height="{bh*0.45:.1f}" rx="1.6" fill="{COMIDA["pollo"]}"/>')
        s.append(f'<path d="M{px+1:.1f} {py+3:.1f}h{(bw-8)/3.4-2:.1f}M{px+1:.1f} {py+6:.1f}h{(bw-8)/3.4-2:.1f}" stroke="{COMIDA["pollo2"]}" stroke-width=".5"/>')
    # compartimento pequeño: verdura + vasito de salsa
    vx = bx + bw + 1.5; vw = w - vx - 3.5
    s.append(f'<rect x="{vx}" y="{by}" width="{vw}" height="{bh}" rx="2" fill="#E8EFE0"/>')
    if tipo in ('a', 'b'):
        for i in range(5):
            cx = vx + vw * (0.3 + 0.4 * (i % 2)); cy = by + 3 + i * (bh * 0.55) / 4.5
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="2.6" fill="{COMIDA["brocoli"]}"/><circle cx="{cx-1:.1f}" cy="{cy-.8:.1f}" r="1.3" fill="{COMIDA["brocoli2"]}"/>')
    else:
        for i in range(4):
            cy = by + 3 + i * (bh * 0.55) / 4
            s.append(f'<path d="M{vx+2:.1f} {cy:.1f}q{vw/2-2:.1f} 3 {vw-4:.1f} 0" stroke="{COMIDA["pimiento"] if i%2 else "#E9B949"}" stroke-width="1.6" fill="none" stroke-linecap="round"/>')
    sy = by + bh - vw * 0.5 - 1.2
    s.append(f'<circle cx="{vx+vw/2:.1f}" cy="{sy:.1f}" r="{vw*0.36:.1f}" fill="#fff" stroke="{tapa}" stroke-width=".5"/>')
    s.append(f'<circle cx="{vx+vw/2:.1f}" cy="{sy:.1f}" r="{vw*0.27:.1f}" fill="{COMIDA["salsa"]}"/>')
    s.append('</g>')
    return ''.join(s)

def hoja_svg(x, y, w, h, rot, tinta='#1F3A2E', acento='#D9572B', papel='#FFFFFF'):
    """La hoja del domingo: cabecera, filas con minuto, casilla con check y línea de texto."""
    filas = ['0:00', '0:15', '0:35', '1:05', '1:35', '2:05']
    s = [f'<g transform="rotate({rot} {x+w/2} {y+h/2})">',
         f'<rect x="{x+1.5}" y="{y+2.5}" width="{w}" height="{h}" rx="1.5" fill="#000" opacity=".15"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="1.5" fill="{papel}"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h*0.16:.1f}" rx="1.5" fill="{tinta}"/>',
         f'<rect x="{x}" y="{y+h*0.10:.1f}" width="{w}" height="{h*0.06:.1f}" fill="{tinta}"/>',
         f'<text x="{x+4}" y="{y+h*0.105:.1f}" font-family="Inter" font-weight="800" font-size="{h*0.065:.1f}" fill="#fff" letter-spacing=".6">SUNDAY</text>',
         f'<circle cx="{x+w-6}" cy="{y+h*0.08:.1f}" r="{h*0.045:.1f}" fill="{acento}"/>']
    fh = (h * 0.80) / len(filas)
    for i, t in enumerate(filas):
        fy = y + h * 0.19 + i * fh
        cb = fh * 0.42
        s.append(f'<text x="{x+3.5}" y="{fy+fh*0.6:.1f}" font-family="Inter" font-weight="700" font-size="{fh*0.36:.1f}" fill="{acento}">{t}</text>')
        s.append(f'<rect x="{x+w*0.36:.1f}" y="{fy+fh*0.3:.1f}" width="{cb:.1f}" height="{cb:.1f}" rx=".7" fill="none" stroke="{tinta}" stroke-width=".7"/>')
        if i < 4:
            s.append(f'<path d="M{x+w*0.36+cb*0.18:.1f} {fy+fh*0.3+cb*0.55:.1f}l{cb*0.3:.1f} {cb*0.3:.1f}l{cb*0.62:.1f} {-cb*0.78:.1f}" stroke="{acento}" stroke-width="1.1" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
        lw = w * (0.48 - 0.07 * (i % 3))
        s.append(f'<rect x="{x+w*0.36+cb+2.5:.1f}" y="{fy+fh*0.43:.1f}" width="{lw:.1f}" height="{fh*0.13:.1f}" rx=".5" fill="{tinta}" opacity="{.75 if i>=4 else .3}"/>')
        s.append(f'<path d="M{x+3} {fy+fh:.1f}H{x+w-3}" stroke="{tinta}" stroke-width=".25" opacity=".3"/>')
    s.append('</g>')
    return ''.join(s)

def portada_html(var, etiqueta=None, titulo=TITULO, sub1=SUB_1, sub2=SUB_2):
    """Devuelve (css, section) de la portada A, B o C."""
    et = f'<span class="etiqueta">{etiqueta}</span>' if etiqueta else ''
    if var == 'A':  # claro ilustrado
        bg, fg = '#FAF6EF', '#1F3A2E'
        svg = ('<svg class="motivo" viewBox="0 0 148 210" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
               '<circle cx="118" cy="40" r="46" fill="#D9572B" opacity=".12"/><circle cx="22" cy="118" r="30" fill="#1F3A2E" opacity=".06"/>'
               + hoja_svg(13, 14, 52, 80, -6) + tupper(74, 12, 60, 30, 'a') + tupper(74, 47, 60, 30, 'b')
               + tupper(74, 82, 60, 30, 'c') + '</svg>')
        css = (f'.portada{{background:{bg};color:{fg}}} .portada h1{{color:{fg};font-size:40pt;letter-spacing:-.025em}}'
               f'.portada .subtitulo{{color:#2c4a3d;font-weight:600}} .portada .detalle{{color:#D9572B;opacity:1;font-weight:600}}'
               f'.portada .texto{{bottom:16mm}} .portada .marca{{color:#D9572B;opacity:1;font-weight:600}}')
        texto = f'<div class="marca">Meal prep system</div><h1>{titulo}</h1><div class="subtitulo">{sub1}</div><div class="detalle">{sub2}</div>{et}'
    elif var == 'B':  # tipográfica
        bg, fg = '#FAF6EF', '#1F3A2E'
        svg = ('<svg class="motivo" viewBox="0 0 148 210" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
               '<rect x="0" y="146" width="148" height="64" fill="#1F3A2E"/>'
               + hoja_svg(10, 128, 36, 54, -5, papel='#FFFFFF') + tupper(52, 152, 42, 29, 'a', fondo='#FAF6EF', tapa='#FAF6EF')
               + tupper(99, 152, 42, 29, 'b', fondo='#FAF6EF', tapa='#FAF6EF') + tupper(52, 185, 42, 29, 'c', fondo='#FAF6EF', tapa='#FAF6EF')
               + tupper(99, 185, 42, 29, 'a', fondo='#FAF6EF', tapa='#FAF6EF') + '</svg>')
        css = (f'.portada{{background:{bg};color:{fg}}} .portada .texto{{top:16mm;bottom:auto}}'
               f'.portada h1{{color:{fg};font-size:58pt;line-height:.92;letter-spacing:-.035em;margin-bottom:6mm}} .portada h1 span{{color:#D9572B;display:block}}'
               f'.portada .subtitulo{{color:#1F3A2E;font-weight:600;font-size:13.5pt;max-width:24em}} .portada .detalle{{color:#4a5a52;opacity:1;font-size:10.5pt;margin-top:3mm}}'
               f'.portada .marca{{color:#D9572B;opacity:1;font-weight:800}} .portada .etiqueta{{background:#D9572B;color:#fff;margin-top:5mm}}')
        t = titulo.split(' ')
        h1 = f'{t[0]}<span>{t[1]}</span>{" ".join(t[2:])}' if len(t) == 3 else titulo
        texto = f'<div class="marca">Meal prep system</div><h1>{h1}</h1><div class="subtitulo">{sub1}</div><div class="detalle">{sub2}</div>{et}'
    else:  # C: oscura premium
        bg, fg = '#1F3A2E', '#FFFFFF'
        svg = ('<svg class="motivo" viewBox="0 0 148 210" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
               '<circle cx="74" cy="66" r="62" fill="#FAF6EF" opacity=".05"/><circle cx="74" cy="66" r="44" fill="#FAF6EF" opacity=".05"/>'
               + tupper(72, 14, 64, 30, 'a', tapa='#FAF6EF', fondo='#FAF6EF') + tupper(72, 49, 64, 30, 'b', tapa='#FAF6EF', fondo='#FAF6EF')
               + tupper(72, 84, 64, 30, 'c', tapa='#FAF6EF', fondo='#FAF6EF')
               + hoja_svg(12, 16, 52, 94, -4, acento='#D9572B') + '</svg>')
        css = (f'@page :first{{background:{bg}}} .portada{{background:{bg};color:{fg}}} .portada h1{{font-size:42pt;letter-spacing:-.025em}}'
               f'.portada .marca{{color:#F08A5D;opacity:1;font-weight:600}} .portada .detalle{{color:#F3C6B1;opacity:1}} .portada .texto{{bottom:16mm}}'
               f'.portada h1 span{{color:#F08A5D}} .portada .etiqueta{{background:#D9572B;color:#fff}}')
        texto = f'<div class="marca">Meal prep system</div><h1>{titulo}</h1><div class="subtitulo">{sub1}</div><div class="detalle">{sub2}</div>{et}'
    css = f'@page :first{{background:{bg}}} ' + css
    return css, f'<section class="portada portada-{var}">{svg}<div class="texto">{texto}</div></section>'

# ----------------------------------------------------------------- CSS propio del nicho
CSS_NICHO = """
:root { --color-principal:#1F3A2E; --color-acento:#D9572B; --color-fondo-suave:#FAF6EF;
  --fuente-titulos:'Inter', sans-serif; --fuente-texto:'Source Serif 4', Georgia, serif; --suave2:#EEF2EC; }
body { background:#fff; }
a { color: var(--color-principal); }
.portada { width:148mm; height:200mm; margin:0; }
@media screen { .portada { height:210mm; } }
.portada .texto { z-index:1; }
/* tablas limpias */
table.t { width:100%; border-collapse:collapse; font-family:var(--fuente-titulos); font-size:8.6pt; line-height:1.32; margin:3mm 0 5mm; }
table.t th { background:var(--color-principal); color:#fff; font-weight:600; text-align:left; padding:1.6mm 2mm; vertical-align:bottom; }
table.t td { padding:1.5mm 2mm; border-bottom:1px solid #E4DDD0; vertical-align:top; }
table.t tbody tr:nth-child(even) td { background:var(--color-fondo-suave); }
table.t tr { break-inside:avoid; }
table.t.corta { break-inside:avoid; }
table.t.ancha { font-size:7.4pt; } table.t.ancha th, table.t.ancha td { padding:1.2mm 1.3mm; }
table.t td a { color:var(--color-acento); font-weight:600; text-decoration:none; }
table.kv td:first-child { font-weight:600; color:var(--color-principal); width:40%; }
table.kv tbody tr:nth-child(even) td { background:none; } table.kv td { border-bottom:1px solid #cfc7b8; height:7.5mm; }
table.escribir td { height:8.5mm; }
td.ck, th.ck { width:6mm; padding-right:0 !important; }
.caja-in { display:inline-block; width:3.4mm; height:3.4mm; border:1.3px solid var(--color-principal); border-radius:.8mm; vertical-align:-.5mm; background:#fff; }
td .caja-in { margin-top:.3mm; }
/* hoja del domingo */
table.hoja { font-size:7.9pt; }
table.hoja td:first-child { font-weight:800; color:var(--color-acento); white-space:nowrap; }
table.hoja td:nth-child(2) { white-space:nowrap; }
table.hoja td:nth-child(4) { color:#3d4a43; font-style:italic; }
.est { display:inline-block; font-weight:800; font-size:.86em; letter-spacing:.04em; padding:.3mm 1.4mm; border-radius:1mm; color:#fff; background:var(--color-principal); }
.est-oven { background:var(--color-acento); } .est-stove { background:#8A5A1F; } .est-cold { background:#2F6E8C; }
.est-prep { background:#5B6B62; } .est-assembly { background:var(--color-principal); }
.mientras { color:var(--color-acento); font-weight:800; }
p.antes { background:var(--suave2); border-radius:2mm; padding:3mm 4mm; font-size:.88em; line-height:1.4; }
/* rótulos (párrafo solo en negrita) */
p.rotulo { font-family:var(--fuente-titulos); font-weight:800; color:var(--color-principal); font-size:10pt; margin:5mm 0 1.5mm; break-after:avoid; text-transform:uppercase; letter-spacing:.06em; }
p.rotulo + table, p.rotulo + ul { margin-top:1mm; }
/* cita de apertura */
blockquote.destacada.cita { margin:0 0 7mm; }
blockquote.destacada .autor { font-family:var(--fuente-titulos); font-weight:400; font-size:.62em; color:#6b6b6b; margin-top:2mm; letter-spacing:.03em; }
/* fuentes al pie de capítulo */
p.fuentes { font-size:8.5pt; line-height:1.35; color:#5a5a5a; border-top:1px solid var(--linea); padding-top:3mm; margin-top:7mm; }
/* portadilla de parte */
.portadilla { break-before:page; break-after:page; height:172mm; box-sizing:border-box; background:var(--color-principal); color:#fff; border-radius:3mm;
  padding:14mm 10mm; position:relative; overflow:hidden; display:flex; flex-direction:column; justify-content:flex-end; }
.portadilla .num { font-family:var(--fuente-titulos); font-weight:800; font-size:80pt; line-height:1; color:var(--color-acento); position:absolute; top:10mm; left:10mm; }
.portadilla .etiqueta { font-family:var(--fuente-titulos); font-size:9.5pt; font-weight:600; letter-spacing:.14em; text-transform:uppercase; opacity:.8; }
.portadilla h1 { color:#fff; font-size:30pt; margin:2mm 0 5mm; }
.portadilla ul { list-style:none; margin:0; padding:0; font-family:var(--fuente-titulos); font-size:10.5pt; }
.portadilla li { border-top:1px solid rgba(255,255,255,.25); padding:2mm 0; margin:0; }
.portadilla a { color:#fff; text-decoration:none; }
.portadilla .motivo { position:absolute; right:-14mm; top:-10mm; width:80mm; height:80mm; opacity:.35; }
/* índice */
nav.indice h1 { margin-bottom:3mm; }
nav.indice > ul > li { padding:2.4mm 0; font-size:10.5pt; }
nav.indice .parte { color:var(--color-acento); text-transform:uppercase; letter-spacing:.1em; font-size:8.5pt; font-weight:800; border-bottom:none; padding-bottom:0; padding-top:4mm; }
nav.indice .ids { font-weight:400; font-size:8.3pt; line-height:1.6; color:#555; margin-top:1mm; }
nav.indice .ids a { color:var(--color-acento); margin-right:1.6mm; }
/* ficha de receta */
.receta { break-before:page; font-size:10.6pt; line-height:1.42; }
.receta-cab { display:flex; gap:3mm; align-items:flex-start; margin-bottom:2.5mm; }
.receta-id { flex:none; font-family:var(--fuente-titulos); font-weight:800; font-size:11pt; color:#fff; background:var(--color-acento); border-radius:2mm; padding:1.4mm 2.2mm; margin-top:.6mm; }
.receta h2 { margin:0; padding:0; background:none; font-size:16pt; line-height:1.15; }
.receta .bloque { font-family:var(--fuente-titulos); font-size:8pt; font-weight:600; letter-spacing:.1em; text-transform:uppercase; color:var(--color-acento); margin:0 0 1mm; }
.datos-r { display:flex; flex-wrap:wrap; gap:1.5mm; margin:0 0 3mm; font-family:var(--fuente-titulos); font-size:8pt; }
.datos-r span { background:var(--suave2); border-radius:1.2mm; padding:.8mm 2mm; color:#2a3a32; }
.datos-r b { font-weight:600; color:var(--color-principal); }
.panel { border:1.4px solid var(--color-principal); border-radius:2.5mm; overflow:hidden; margin:0 0 4mm; break-inside:avoid; font-family:var(--fuente-titulos); }
.macros { display:grid; grid-template-columns:1.15fr 1.15fr 1fr 1fr; background:var(--color-principal); color:#fff; }
.macros div { padding:2mm 2mm 1.8mm; text-align:center; border-right:1px solid rgba(255,255,255,.18); }
.macros div:last-child { border-right:0; }
.macros b { display:block; font-size:15pt; font-weight:800; line-height:1.05; }
.macros .pro b { color:#FFB08C; }
.macros small { font-size:6.8pt; letter-spacing:.08em; text-transform:uppercase; opacity:.85; }
.panel .por { background:var(--color-principal); color:#fff; font-size:6.8pt; text-align:center; padding:0 2mm 1.5mm; opacity:.95; letter-spacing:.04em; }
.hechos { display:grid; grid-template-columns:1fr 1fr; font-size:8.3pt; line-height:1.3; }
.hechos div { padding:1.8mm 2.4mm; border-top:1px solid #DDD5C6; display:flex; gap:1.6mm; align-items:flex-start; }
.hechos div:nth-child(odd) { border-right:1px solid #DDD5C6; }
.hechos .ico { width:4.2mm; height:4.2mm; color:var(--color-acento); margin-top:.1mm; }
.hechos .ancho { grid-column:1 / -1; border-right:0 !important; }
.hechos i { font-style:normal; color:#666; display:block; font-size:7pt; text-transform:uppercase; letter-spacing:.07em; }
.hechos .alerg { color:var(--color-acento); font-weight:600; }
.panel .nota-coste { font-size:6.6pt; color:#6b6b6b; padding:1.2mm 2.4mm 1.6mm; border-top:1px solid #DDD5C6; line-height:1.3; }
.va-con { font-family:var(--fuente-titulos); font-size:8.3pt; color:#3a463f; margin:0 0 4mm; }
.va-con b { color:var(--color-principal); }
.ingr { background:var(--color-fondo-suave); border-radius:2.5mm; padding:3mm 4mm 2mm; margin:0 0 4mm; font-family:var(--fuente-titulos); font-size:8.8pt; line-height:1.35; break-inside:avoid; }
.ingr h3, .pasos-r h3 { font-size:9pt; letter-spacing:.1em; text-transform:uppercase; color:var(--color-acento); margin:0 0 2mm; font-weight:800; }
.ingr ul { list-style:none; margin:0; padding:0; columns:1; }
.ingr li { margin:0 0 1.1mm; padding-left:3.5mm; position:relative; break-inside:avoid; }
.ingr li::before { content:""; position:absolute; left:0; top:.5em; width:1.5mm; height:1.5mm; border-radius:50%; background:var(--color-acento); }
.ingr p { margin:1.5mm 0 1mm; font-weight:600; }
.pasos-r ol { list-style:none; counter-reset:pr; margin:0 0 3mm; padding:0; }
.pasos-r ol > li { counter-increment:pr; position:relative; padding-left:8.5mm; margin:0 0 2.2mm; break-inside:avoid; }
.pasos-r ol > li::before { content:counter(pr); position:absolute; left:0; top:.1mm; width:5.6mm; height:5.6mm; border-radius:50%; background:var(--color-acento); color:#fff;
  font-family:var(--fuente-titulos); font-weight:800; font-size:8.5pt; line-height:5.6mm; text-align:center; }
.notas-r { display:grid; gap:2.5mm; margin-top:2mm; }
.nota-r { border-left:1.2mm solid var(--color-principal); background:var(--suave2); border-radius:0 2mm 2mm 0; padding:2.2mm 3.2mm; font-size:9.4pt; line-height:1.38; break-inside:avoid; }
.nota-r.fix { border-color:var(--color-acento); background:var(--tinte); }
.nota-r h4 { font-family:var(--fuente-titulos); font-size:7.8pt; letter-spacing:.1em; text-transform:uppercase; margin:0 0 1mm; color:var(--color-principal); }
.nota-r.fix h4 { color:var(--color-acento); }
.nota-r ul { margin:0; padding-left:3mm; } .nota-r li { margin-bottom:.8mm; } .nota-r p { margin:0; }
.macro-nota { font-size:8.3pt; color:#555; font-style:italic; margin:-2mm 0 3mm; }
/* platos firmados */
.plato { border:1px solid #DDD5C6; border-radius:2.5mm; padding:3mm 3.5mm 2mm; margin:0 0 3.5mm; break-inside:avoid; font-size:9.4pt; line-height:1.36; }
.plato-cab { display:flex; gap:2.5mm; align-items:baseline; }
.plato-cab .pid { flex:none; font-family:var(--fuente-titulos); font-weight:800; font-size:9pt; color:#fff; background:var(--color-principal); border-radius:1.4mm; padding:.5mm 1.8mm; }
.plato h3 { margin:0; font-size:11.5pt; }
.plato .partes { font-family:var(--fuente-titulos); font-size:7.8pt; color:#555; margin:1.5mm 0 2mm; line-height:1.35; }
.plato .partes a { color:#555; text-decoration:none; border-bottom:1px dotted #aaa; }
.plato .cifras { display:flex; flex-wrap:wrap; gap:1.4mm; font-family:var(--fuente-titulos); font-size:7.8pt; margin-bottom:2mm; }
.plato .cifras span { border-radius:1.2mm; padding:.6mm 1.8mm; background:var(--suave2); }
.plato .cifras .kc { background:var(--color-principal); color:#fff; font-weight:800; }
.plato .cifras .pr { background:var(--color-acento); color:#fff; font-weight:800; }
.plato ol { margin:0; padding-left:4.5mm; font-size:9pt; } .plato li { margin-bottom:.8mm; }
/* tracker vertical en pantalla */
table.tracker.t7v td { height:9mm; }
/* nota para imprimir */
.para-imprimir { display:flex; gap:2.5mm; align-items:center; font-family:var(--fuente-titulos); font-size:8.3pt; color:var(--color-principal); border:1px dashed var(--color-principal);
  border-radius:2mm; padding:2mm 3mm; margin:2mm 0 5mm; break-inside:avoid; }
.para-imprimir .ico { width:5mm; height:5mm; color:var(--color-acento); }
h2 { break-after:avoid; }
h2 + p.antes, h2 + table, p.rotulo + table { break-before:avoid; }
.caja-i.consejo ul { margin-bottom:0; }
.caja-i.ejercicio h3 { margin-top:0; }
.caja-i.ejercicio table.t { background:#fff; }
.pie-muestra { text-align:center; font-family:var(--fuente-titulos); font-weight:600; }
.link-pendiente { background:#FFE9DF; color:var(--color-acento); padding:0 1mm; border-radius:1mm; }
"""

CSS_IMPRIMIBLE = """
@page { size: Letter; margin: 15mm 15mm 17mm 15mm;
  @bottom-center { content: "The Sunday Sheet \\00B7  Printable Pack \\00B7  page " counter(page); font-family: 'Inter', sans-serif; font-size: 8pt; color: #6b6b6b; } }
.hoja h1 { font-size:19pt; margin-top:0; }
.hoja h1 .ico { width:7mm; height:7mm; }
.hoja h2 { font-size:12pt; margin:4mm 0 2mm; padding-top:3mm; }
table.t { font-size:8.6pt; }
table.hoja { font-size:7.7pt; } table.hoja td, table.hoja th { padding:1.05mm 1.6mm; }
table.hoja.vacia td { height:8.6mm; }
table.compra td { padding:1.1mm 2mm; }
table.compra { font-size:8.2pt; margin:1mm 0 2.5mm; }
.dos-col { columns:2; column-gap:7mm; } .dos-col > * { break-inside:avoid; }
.dos-col p.rotulo:first-child { margin-top:0; }
.cabecera-semana { display:flex; flex-wrap:wrap; gap:2mm 5mm; font-family:var(--fuente-titulos); font-size:8.6pt; border:1.4px solid var(--color-principal); border-radius:2mm; padding:2mm 3mm; margin:0 0 3mm; }
.cabecera-semana b { color:var(--color-principal); }
p.antes { font-size:8.4pt; padding:2mm 3mm; margin-bottom:2.5mm; }
.franja { font-family:var(--fuente-titulos); font-size:8.4pt; background:var(--color-principal); color:#fff; border-radius:2mm; padding:2mm 3mm; margin-top:2mm; }
.etiquetas { display:grid; grid-template-columns:1fr 1fr; gap:4mm; }
.etq { border:1.4px dashed #6b6b6b; border-radius:2mm; height:41mm; padding:3mm 4mm; box-sizing:border-box; font-family:var(--fuente-titulos); font-size:9.4pt; line-height:1.75; color:#1e1e1e; }
.etq b { color:var(--color-principal); font-weight:800; letter-spacing:.06em; font-size:10pt; }
.etq .l { display:inline-block; border-bottom:1px solid #777; min-width:22mm; }
.tarjeta-pag { min-height:auto; display:block; break-before:page; }
.tarjeta-pag .tarjeta { width:auto; margin:0 0 6mm; padding:6mm 7mm 4mm; }
.tarjeta .tarjeta-titulo { font-size:15pt; margin-bottom:3mm; }
.tarjeta table.t { font-size:8.6pt; background:#fff; margin:2mm 0 3mm; }
.tarjeta ul { margin:0 0 2mm 2mm; font-family:var(--fuente-titulos); font-size:9.6pt; color:#1e1e1e; }
.tarjeta ul li { list-style:disc; padding:0; margin:0 0 1.2mm; font-size:9.6pt; } .tarjeta ul li::before { content:none; }
.tarjeta p { font-family:var(--fuente-titulos); font-size:9.4pt; margin:0 0 2mm; }
.poster-regla { font-family:var(--fuente-titulos); font-weight:800; font-size:17pt; color:#fff; background:var(--color-principal); border-radius:2.5mm; padding:4mm 5mm; margin:0 0 4mm; }
.poster-regla span { color:#FFB08C; }
.cuatro { display:grid; grid-template-columns:1fr 1fr; gap:0 6mm; }
.cuatro table.t { margin:1mm 0 3mm; font-size:8.6pt; }
.cuatro table.t td:not(:first-child), .cuatro table.t th:not(:first-child) { text-align:center; width:10mm; }
.cuatro table.t td { font-weight:800; color:var(--color-acento); } .cuatro table.t td:first-child { font-weight:400; color:#1e1e1e; }
.reglas { font-size:8.6pt; columns:2; column-gap:6mm; margin:0 0 3mm; padding-left:4mm; } .reglas li { margin-bottom:1mm; break-inside:avoid; }
"""

# ----------------------------------------------------------------- utilidades Markdown -> HTML
def slug(t):
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t).lower()
    t = re.sub(r'[^a-z0-9]+', '-', t).strip('-')
    return t[:50]

def limpiar_md(t):
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
    t = re.sub(r'^>\s*\[SIN DATO[^\]]*\]\s*$', '', t, flags=re.M)
    t = re.sub(r'^\[SIN DATO[^\]]*\]\s*$', '', t, flags=re.M)
    t = re.sub(r'\[ESPACIO:\s*(\d+)[^\]]*\]', lambda m: f'\n<div class="espacio" style="--lineas:{m.group(1)}"></div>\n', t)
    t = t.replace('[TRACKER: semana · columnas Lun-Vie · fila "comido" / "tirado" · fila "motivo si se tiró"]', TRACKER_V)
    # líneas en blanco antes de tablas y listas que van pegadas a un párrafo
    out, prev = [], ''
    for ln in t.split('\n'):
        es_tabla = ln.startswith('|'); es_lista = bool(re.match(r'\s*(- |\d+\. )', ln))
        prev_tabla = prev.startswith('|'); prev_lista = bool(re.match(r'\s*(- |\d+\. )', prev))
        if prev.strip() and ((es_tabla and not prev_tabla) or (es_lista and not prev_lista and not prev.startswith('   ')) or
                             (prev_tabla and not es_tabla) or (prev_lista and not es_lista and ln.strip() and not ln.startswith('   '))):
            out.append('')
        out.append(ln); prev = ln
    return '\n'.join(out)

TRACKER_V = ('\n<table class="tracker t7v"><caption>This week: eaten or thrown out?</caption><thead><tr><th>Day</th><th>Eaten</th><th>Thrown out</th>'
             '<th>Reason, if thrown out</th></tr></thead><tbody>' + ''.join(f'<tr><td>{d}</td><td></td><td></td><td></td></tr>' for d in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']) +
             '</tbody></table>\n')

RE_REC = r'(?:P10|P[1-9]|B[1-6]|V[1-6]|S1[0-2]|S[1-9]|D[1-8]|FM10|FM[1-9]|SN[1-8])'
RE_PLA = r'(?:M1[0-2]|M[1-9]|A1[0-2]|A[1-9]|D-1[0-2]|D-[1-9]|C1[0-2]|C[1-9])'
IDS_RECETAS = set()

def enlazar_celda(m):
    inner = m.group(2).strip()
    if re.fullmatch(RE_REC, inner) and inner in IDS_RECETAS:
        return f'{m.group(1)}<a href="#receta-{inner.lower()}">{inner}</a></td>'
    if re.fullmatch(RE_PLA, inner):
        return f'{m.group(1)}<a href="#plato-{inner.lower()}">{inner}</a></td>'
    return m.group(0)

def partir_parrafos(h):
    def parte(m):
        txt = m.group(1)
        if '<br' in txt or '<table' in txt:
            return m.group(0)
        plano = re.sub(r'<[^>]+>', '', txt)
        if len(plano.split()) <= 70:
            return m.group(0)
        frases = re.split(r'(?<=[.!?])\s+(?=[A-Z"“(])', txt)
        if len(frases) < 2:
            return m.group(0)
        tot = len(plano.split()); acc = 0; corte = 1
        for i, f in enumerate(frases):
            acc += len(re.sub(r'<[^>]+>', '', f).split())
            if acc >= tot / 2:
                corte = i + 1; break
        corte = min(max(corte, 1), len(frases) - 1)
        return f'<p>{" ".join(frases[:corte])}</p>\n<p>{" ".join(frases[corte:])}</p>'
    return re.sub(r'<p>(.*?)</p>', parte, h, flags=re.S)

def tablas(h, imprimible=False):
    def una(m):
        t = m.group(0)
        cab = re.search(r'<thead>(.*?)</thead>', t, re.S)
        ths = re.findall(r'<th[^>]*>(.*?)</th>', cab.group(1), re.S) if cab else []
        cls = ['t']
        n_filas = t.count('<tr>') - (1 if cab else 0)
        if ths and all(not x.strip() for x in ths):
            t = re.sub(r'<thead>.*?</thead>', '', t, flags=re.S); cls.append('kv')
        cuerpo = re.findall(r'<td[^>]*>(.*?)</td>', t, re.S)
        if cuerpo and sum(1 for c in cuerpo if not c.strip()) > len(cuerpo) * 0.4:
            cls.append('escribir')
        txt_ths = [re.sub(r'<[^>]+>', '', x).strip() for x in ths]
        if txt_ths[:1] == ['Clock']:
            cls.append('hoja')
            t = re.sub(r'<td>(OVEN|STOVE|COLD|PREP|ASSEMBLY)( ⏱)?</td>',
                       lambda mm: f'<td><span class="est est-{mm.group(1).lower()}">{mm.group(1)}</span>{" <span class=mientras>⏱</span>" if mm.group(2) else ""}</td>', t)
        if 'Item' in txt_ths and any('×1' in x for x in txt_ths):
            cls.append('compra')
            t = re.sub(r'<tr>\s*<th', '<tr><th class="ck"></th><th', t, count=1)
            t = re.sub(r'<tr>\s*<td', '<tr><td class="ck"><span class="caja-in"></span></td><td', t)
        if len(ths) >= 7 or (len(ths) >= 6 and not imprimible and 'hoja' not in cls):
            cls.append('ancha')
        if n_filas <= 14:
            cls.append('corta')
        t = re.sub(r'(<td[^>]*>)\s*([A-Z]{1,2}-?\d{1,2})\s*</td>', enlazar_celda, t)
        return t.replace('<table>', f'<table class="{" ".join(cls)}">', 1)
    return re.sub(r'<table>.*?</table>', una, h, flags=re.S)

def checklists(h):
    def ul(m):
        c = m.group(0)
        if '<li>[ ]' not in c:
            return c
        c = re.sub(r'<li>\[ \] ?(.*?)</li>', r'<li><span class="caja"></span><span>\1</span></li>', c, flags=re.S)
        return c.replace('<ul>', '<ul class="lista-hoy">', 1)
    return re.sub(r'<ul>.*?</ul>', ul, h, flags=re.S)

def md(t, imprimible=False):
    t = limpiar_md(t)
    h = markdown.markdown(t, extensions=['tables', 'nl2br', 'sane_lists'])
    # cita de apertura
    h = re.sub(r'<blockquote>\s*<p>(.*?)<br />\s*(—[^<]*)</p>\s*</blockquote>',
               r'<blockquote class="destacada cita"><p>\1</p><p class="autor">\2</p></blockquote>', h, flags=re.S)
    h = re.sub(r'<hr />\s*<p><em>(Sources?:|The templates)(.*?)</p>', r'<p class="fuentes"><em>\1\2</p>', h, flags=re.S)
    h = h.replace('<hr />', '<hr class="sep">')
    h = re.sub(r'<p><strong>([^<]{2,60})</strong></p>', r'<p class="rotulo">\1</p>', h)
    h = re.sub(r'<p><strong>(Before 0:00[^<]*)</strong>(.*?)</p>', r'<p class="antes"><strong>\1</strong>\2</p>', h, flags=re.S)
    # "How to use this block" -> caja consejo
    h = re.sub(r'<p class="rotulo">(How to use this block)</p>\s*(<ul>.*?</ul>)',
               lambda m: f'<div class="caja-i consejo"><div class="cabecera">{ico("consejo")}{m.group(1)}</div>{m.group(2)}</div>', h, flags=re.S)
    h = checklists(h)
    h = tablas(h, imprimible)
    h = h.replace('☐', '<span class="caja-in"></span>')
    h = h.replace('[LINK_TIENDA]', '<span class="link-pendiente">[LINK_TIENDA]</span>')
    h = partir_parrafos(h)
    return h

def ids_h2(h, pref, especiales=None):
    especiales = especiales or {}
    vistos = set()
    def f(m):
        txt = m.group(1)
        plano = re.sub(r'<[^>]+>', '', txt)
        i = None
        for k, v in especiales.items():
            if re.search(k, plano):
                i = v
        if not i:
            i = f'{pref}-{slug(plano)}'
        while i in vistos:
            i += '-b'
        vistos.add(i)
        return f'<h2 id="{i}">{txt}</h2>'
    return re.sub(r'<h2>(.*?)</h2>', f, h)

def cajas_accion(h):
    """Envuelve cada sección 'Your action...' (h2 + contenido) en una caja de ejercicio."""
    partes = re.split(r'(?=<h2[ >])', h)
    out = []
    for p in partes:
        m = re.match(r'<h2([^>]*)>(Your (?:first )?action)(?::\s*)?(.*?)</h2>(.*)', p, re.S)
        if not m:
            out.append(p); continue
        resto = m.group(4)
        cola = ''
        k = resto.find('<p class="fuentes">')
        if k >= 0:
            resto, cola = resto[:k], resto[k:]
        sub = f'<h3>{m.group(3)[0].upper() + m.group(3)[1:]}</h3>' if m.group(3) else ''
        out.append(f'<div class="caja-i ejercicio largo"{m.group(1)}><div class="cabecera">{ico("ejercicio")}{m.group(2)}</div>{sub}{resto}</div>{cola}')
    return ''.join(out)

# ----------------------------------------------------------------- fichas de receta
BLOQUES = {'P': 'Protein', 'B': 'Base', 'V': 'Vegetable', 'S': 'Sauce', 'D': 'Breakfast', 'FM': 'Freezer meal', 'SN': 'Snack'}

def campos(linea):
    """'**A:** x · **B:** y' -> {'A': 'x', 'B': 'y'}"""
    d = {}
    for m in re.finditer(r'\*\*([^*:]+):\*\*\s*(.*?)(?=\s*·\s*\*\*[^*]+:\*\*|$)', linea):
        d[m.group(1).strip()] = m.group(2).strip()
    return d

def inline(t):
    h = markdown.markdown(t)
    return re.sub(r'^<p>|</p>$', '', h.strip())

def receta(texto):
    texto = re.sub(r'<!--.*?-->', '', texto, flags=re.S).strip()
    lineas = texto.split('\n')
    m = re.match(r'#{3,4}\s*([A-Z]+\d+)\s*·\s*(.*)', lineas[0])
    rid, nombre = m.group(1), m.group(2).strip()
    IDS_RECETAS.add(rid)
    meta, i = {}, 1
    nota_macro = ''
    while i < len(lineas) and not lineas[i].startswith('**Ingredients'):
        ln = lineas[i].strip()
        if ln.startswith('**Makes:**'):
            meta['makes'] = campos(ln)
        elif ln.startswith('**Per portion:**'):
            meta['per'] = ln
        elif ln.startswith('**Cost/portion:**'):
            meta['cost'] = ln.split('**Cost/portion:**', 1)[1].strip()
        elif ln.startswith('**Fridge:**'):
            meta['fridge'] = campos(ln)
        elif ln.startswith('**Goes with:**'):
            meta['goes'] = ln.split('**Goes with:**', 1)[1].strip()
        elif ln.startswith('*Macro note:*'):
            nota_macro = ln
        i += 1
    cuerpo = '\n'.join(lineas[i:])
    per = meta.get('per', '')
    num = lambda pat: (re.search(pat, per) or [None, '–'])[1]
    kcal, prot, carb, fat = num(r'(\d+)\s*kcal'), num(r'(\d+)\s*g protein'), num(r'(\d+)\s*g carbs'), num(r'(\d+)\s*g fat')
    alerg = (re.search(r'\*\*Allergens:\*\*\s*(.*)$', per) or [None, '—'])[1]
    mk = meta.get('makes', {})
    datos = ''.join(f'<span><b>{k}</b> {v}</span>' for k, v in mk.items() if v and v.lower() != 'none')
    fr = meta.get('fridge', {})
    coste = meta.get('cost', '')
    coste_v, coste_n = coste, ''
    mm = re.match(r'(about \$[\d.]+)\s*\((.*)\)\s*$', coste)
    if mm:
        coste_v, coste_n = mm.group(1), mm.group(2)
    hechos = []
    if coste:
        hechos.append(f'<div>{ico("carro")}<span><i>Cost / portion</i>{coste_v}</span></div>')
    hechos.append(f'<div>{ico("aviso")}<span><i>Allergens</i><span class="alerg">{alerg}</span></span></div>')
    hechos.append(f'<div>{ico("nevera")}<span><i>Fridge</i>{fr.get("Fridge", "—")}</span></div>')
    hechos.append(f'<div>{ico("frio")}<span><i>Freezer</i>{fr.get("Freezer", "—")}</span></div>')
    if not coste:  # rellenar la rejilla
        hechos[-1] = hechos[-1]
    hechos.append(f'<div class="ancho">{ico("reloj")}<span><i>Reheat</i>{inline(fr.get("Reheat", "—"))}</span></div>')
    if len(hechos) % 2 == 0:
        pass
    panel = (f'<div class="panel"><div class="macros"><div><b>{kcal}</b><small>kcal</small></div><div class="pro"><b>{prot} g</b><small>protein</small></div>'
             f'<div><b>{carb} g</b><small>carbs</small></div><div><b>{fat} g</b><small>fat</small></div></div>'
             f'<div class="por">PER PORTION · USDA FoodData Central</div><div class="hechos">{"".join(hechos)}</div>'
             + (f'<div class="nota-coste">Cost: {coste_n}</div>' if coste_n else '') + '</div>')
    goes = f'<p class="va-con"><b>Goes with:</b> {inline(meta["goes"])}</p>' if meta.get('goes') else ''
    # cuerpo: Ingredients / Steps / Sunday-sheet slot / Fix it / Swap
    trozos = re.split(r'^\*\*(Ingredients|Steps|Sunday-sheet slot:|Fix it:|Swap:)\*\*', cuerpo, flags=re.M)
    sec = {}
    for k in range(1, len(trozos), 2):
        sec[trozos[k].rstrip(':')] = trozos[k + 1].strip()
    ingr = sec.get('Ingredients', '')
    ingr_tit = 'Ingredients'
    mm = re.match(r'(\([^)]*\))\s*\n', ingr)
    if mm:
        ingr_tit += ' <span style="font-weight:400;text-transform:none;letter-spacing:0;color:#666">' + mm.group(1) + '</span>'
        ingr = ingr[mm.end():]
    h_ingr = markdown.markdown(limpiar_md(ingr), extensions=['sane_lists'])
    h_pasos = markdown.markdown(limpiar_md(sec.get('Steps', '')), extensions=['sane_lists'])
    notas = []
    if sec.get('Sunday-sheet slot'):
        notas.append(f'<div class="nota-r"><h4>Sunday-sheet slot</h4><p>{inline(sec["Sunday-sheet slot"])}</p></div>')
    if sec.get('Fix it'):
        notas.append(f'<div class="nota-r fix"><h4>Fix it</h4>{markdown.markdown(limpiar_md(sec["Fix it"]), extensions=["sane_lists"])}</div>')
    if sec.get('Swap'):
        notas.append(f'<div class="nota-r"><h4>Swap</h4>{markdown.markdown(sec["Swap"])}</div>')
    pref = re.match(r'[A-Z]+', rid).group(0)
    nm = f'<p class="macro-nota">{inline(nota_macro)}</p>' if nota_macro else ''
    return (f'<article class="receta" id="receta-{rid.lower()}"><p class="bloque">{BLOQUES.get(pref, "")}</p>'
            f'<div class="receta-cab"><span class="receta-id">{rid}</span><h2>{nombre}</h2></div>'
            f'<div class="datos-r">{datos}</div>{panel}{nm}{goes}'
            f'<div class="ingr"><h3>{ingr_tit}</h3>{h_ingr}</div><div class="pasos-r"><h3>Steps</h3>{h_pasos}</div>'
            f'<div class="notas-r">{"".join(notas)}</div></article>')

# ----------------------------------------------------------------- platos firmados (cap. 16)
def platos(h_md):
    """Convierte cada '### M1 · Nombre' + líneas en una tarjeta .plato (antes de pasar a HTML)."""
    def uno(m):
        pid, nombre, cuerpo = m.group(1), m.group(2).strip(), m.group(3).strip('\n')
        ls = [l for l in cuerpo.split('\n') if l.strip()]
        partes = inline(ls[0].rstrip()) if ls else ''
        partes = re.sub(r'\b(' + RE_REC + r')\b', lambda x: f'<a href="#receta-{x.group(1).lower()}">{x.group(1)}</a>', partes)
        cif = ls[1] if len(ls) > 1 else ''
        kc = (re.search(r'(\d[\d,]*) kcal', cif) or [None, ''])[1]
        pr = (re.search(r'(\d+) g protein', cif) or [None, ''])[1]
        resto = re.sub(r'^\*\*.*?\*\*\s*·\s*', '', cif)
        chips = [f'<span class="kc">{kc} kcal</span>', f'<span class="pr">{pr} g protein</span>'] + [f'<span>{inline(x.strip())}</span>' for x in resto.split(' · ') if x.strip()]
        ol = markdown.markdown('\n'.join(ls[2:]), extensions=['sane_lists'])
        return (f'\n\n<div class="plato" id="plato-{pid.lower()}"><div class="plato-cab"><span class="pid">{pid}</span><h3>{nombre}</h3></div>'
                f'<div class="partes">{partes}</div><div class="cifras">{"".join(chips)}</div>{ol}</div>\n\n')
    return re.sub(r'^### (' + RE_PLA + r') · (.*?)\n(.*?)(?=^#{2,3} |\Z)', uno, h_md, flags=re.S | re.M)

# ----------------------------------------------------------------- capítulos
MOTIVO_AP = ('<svg class="motivo" viewBox="0 0 100 100" aria-hidden="true"><g fill="none" stroke="#fff" stroke-width="1.2">'
             '<circle cx="70" cy="70" r="14"/><circle cx="70" cy="70" r="26"/><circle cx="70" cy="70" r="38"/><circle cx="70" cy="70" r="50"/></g></svg>')

def capitulo(texto, especiales=None, extra_final='', post=None):
    """'# N · Título' + resto -> section.capitulo con apertura."""
    texto = re.sub(r'<!--.*?-->', '', texto, flags=re.S).strip()
    m = re.match(r'#\s*(\d+)\s*·\s*(.*?)\n(.*)', texto, re.S)
    n, tit, resto = m.group(1), m.group(2).strip(), m.group(3)
    cid = f'cap-{n}'
    etq = 'Start here' if n == '0' else f'Chapter {n}'
    tit_h = tit.split(':', 1)[1].strip() if n == '0' and ':' in tit else tit
    if n == '0':
        tit_h = 'Start Here'
    if '16' == n:
        resto = platos(resto)
    h = md(resto)
    if post:
        h = post(h)
    h = ids_h2(h, cid, especiales)
    h = cajas_accion(h)
    sub = f'<p class="sub-ap">{tit.split(":", 1)[1].strip()}</p>' if n == '0' and ':' in tit else ''
    return cid, tit_h, (f'<section class="capitulo" id="{cid}"><div class="apertura">{MOTIVO_AP}<div class="etiqueta">{etq}</div><h1>{tit_h}</h1>{sub}</div>'
                        f'{h}{extra_final}</section>')

def portadilla(n, titulo, caps):
    lis = ''.join(f'<li><a href="#{c}">{t}</a></li>' for c, t in caps)
    mot = ('<svg class="motivo" viewBox="0 0 100 100" aria-hidden="true"><g fill="none" stroke="#FAF6EF" stroke-width="1">'
           '<circle cx="60" cy="40" r="12"/><circle cx="60" cy="40" r="24"/><circle cx="60" cy="40" r="36"/><circle cx="60" cy="40" r="48"/></g></svg>')
    return (f'<section class="portadilla" id="parte-{n}">{mot}<div class="num">{n}</div><div class="etiqueta">Part {n}</div>'
            f'<h1>{titulo}</h1><ul>{lis}</ul></section>')

def nota_imprimir(txt):
    return f'<div class="para-imprimir">{ico("imprimir")}<span>{txt}</span></div>'

def doc(titulo, fmt, cuerpo, extra_css=''):
    hojas = f'<link rel="stylesheet" href="{CSS}plantilla.css">\n<link rel="stylesheet" href="{CSS}plantilla-{fmt}.css">'
    return (f'<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><title>{titulo}</title>\n{hojas}\n'
            f'<style>{CSS_NICHO}{extra_css}</style></head><body>\n{SPRITE}\n{cuerpo}\n'
            f'<script src="{CSS}lineas.js"></script>\n</body></html>\n')

# ================================================================= EBOOK PANTALLA
def ebook_pantalla():
    # 1) fichas de receta (antes, para conocer los IDs al enlazar tablas)
    fichas = {}
    for f in sorted(os.listdir(os.path.join(EN, 'recetas'))):
        t = leer(os.path.join('recetas', f))
        fichas[f[:-3]] = receta(t)
    def orden(pref, n):
        return [f'{pref}{i}' for i in range(1, n + 1)]
    bloques_rec = {'12': orden('P', 10), '13': orden('B', 6), '14': orden('V', 6), '15': orden('S', 12),
                   '17': orden('D', 8), '18': orden('FM', 10), '19': orden('SN', 8)}
    partes_def = [(1, 'The System', ['01-why-it-gets-old.md', '02-the-2-hour-sunday.md', '03-portions.md', '04-storage.md', '05-cost.md', '06-protein.md', '07-pantry-gear.md']),
                  (2, 'The 4-Week Plan', ['08-week-1.md', '09-week-2.md', '10-week-3.md', '11-week-4.md']),
                  (3, 'Recipes', ['RECETAS']),
                  (4, 'Reference', ['20-storage-chart.md', '21-macro-allergen-index.md', '22-when-things-go-wrong.md', '23-blank-templates.md'])]
    pag_imp = {'8': 'pages 2 and 7', '9': 'pages 3 and 8', '10': 'pages 4 and 9', '11': 'pages 5 and 10'}
    def especiales_de(nombre):
        e = {r'^The Sunday Sheet · Week (\d)': None}
        mm = re.match(r'(\d+)-week-(\d)', nombre)
        if mm:
            return {rf'^The Sunday Sheet · Week {mm.group(2)}': f'hoja-semana-{mm.group(2)}', r'^Shopping list': f'compra-semana-{mm.group(2)}'}
        if nombre.startswith('20-'):
            return {r'^The chart$': 'tabla-conservacion'}
        if nombre.startswith('16-'):
            return {r'^The Mix & Match chart': 'mix-match'}
        return {}
    def post_semana(nsem):
        def p(h):
            nota = nota_imprimir(f'To print: this Sunday Sheet and the shopping list are in the printable pack ({pag_imp[nsem]}), one page each.')
            return re.sub(r'(<h2>The assembly table</h2>)', nota + r'\1', h, count=1)
        return p
    def post_cap(nombre):
        if nombre.startswith('20-'):
            return lambda h: re.sub(r'(<h2>Your action</h2>)', nota_imprimir('To print: this chart is pages 12-13 of the printable pack. Tape it inside a cupboard door.') + r'\1', h, count=1)
        if nombre.startswith('23-'):
            return lambda h: re.sub(r'(<h2>How to fill)', nota_imprimir('All these templates are in the printable pack: <em>the-sunday-sheet-printables.pdf</em> (US Letter).') + r'\1', h, count=1)
        if nombre.startswith('04-'):
            return lambda h: re.sub(r'(<h2>Your action)', nota_imprimir('To print: the fridge cards (day-5 rule, reheating by part) are pages 20-21 of the printable pack.') + r'\1', h, count=1)
        return None

    secciones, indice = [], []
    cid, t0, h0 = capitulo(leer('00-start-here.md'), post=lambda h: re.sub(r'(<h2>Before you cook)', nota_imprimir('Everything you fill in or stick on the fridge is also in the printable pack (US Letter, black-and-white friendly).') + r'\1', h, count=1))
    secciones.append(h0); indice.append(('cap', cid, 'Start Here: How This Book Works', None))
    intros = leer('12-19-recipe-intros.md')
    intros = re.sub(r'<!--.*?-->', '', intros, flags=re.S)
    trozos_intro = {mm.group(1): mm.group(0) for mm in re.finditer(r'^# (\d+) · .*?(?=^# |\Z)', intros, flags=re.S | re.M)}
    for n, titulo, archivos in partes_def:
        caps_parte, html_parte = [], []
        if archivos == ['RECETAS']:
            for nc in ['12', '13', '14', '15', '16', '17', '18', '19']:
                if nc == '16':
                    c, t, hh = capitulo(leer('16-signature-plates.md'), especiales_de('16-'))
                    caps_parte.append((c, f'{nc} · {t}', None)); html_parte.append(hh); continue
                txt = trozos_intro[nc].rstrip().rstrip('-').rstrip()
                ids = bloques_rec[nc]
                c, t, hh = capitulo(txt)
                hh = hh.replace('</section>', ''.join(fichas[i] for i in ids) + '</section>')
                caps_parte.append((c, f'{nc} · {t}', ids)); html_parte.append(hh)
        else:
            for a in archivos:
                txt = re.sub(r'^# Part \d+ · .*\n', '', leer(a))
                nsem = re.match(r'(\d+)-week', a)
                post = post_semana(str(int(nsem.group(1)))) if nsem else post_cap(a)
                c, t, hh = capitulo(txt, especiales_de(a), post=post)
                caps_parte.append((c, f'{int(a[:2])} · {t}', None)); html_parte.append(hh)
        secciones.append(portadilla(n, titulo, [(c, t) for c, t, _ in caps_parte]))
        secciones += html_parte
        indice.append(('parte', f'parte-{n}', f'Part {n} · {titulo}', None))
        indice += [('cap', c, t, ids) for c, t, ids in caps_parte]
    # índice
    lis = []
    for tipo, i, t, ids in indice:
        if tipo == 'parte':
            lis.append(f'<li class="parte"><a href="#{i}">{t}</a></li>')
        else:
            extra = ''
            if ids:
                extra = '<div class="ids">' + ''.join(f'<a href="#receta-{x.lower()}">{x}</a>' for x in ids) + '</div>'
            lis.append(f'<li><a href="#{i}">{t}</a>{extra}</li>')
    nav = f'<nav class="indice"><h1>Contents</h1><ul>{"".join(lis)}</ul></nav>'
    css_p, sec_p = portada_html(PORTADA_ELEGIDA)
    cuerpo = sec_p + nav + ''.join(secciones)
    # enlazar IDs de receta en tablas generadas antes de conocer todos los IDs
    cuerpo = re.sub(r'(<td[^>]*>)(' + RE_REC + r')</td>', lambda m: f'{m.group(1)}<a href="#receta-{m.group(2).lower()}">{m.group(2)}</a></td>', cuerpo)
    extra = css_p + '.sub-ap{position:relative;color:#fff;opacity:.85;font-family:var(--fuente-titulos);font-size:11pt;margin:2mm 0 0}'
    return doc(f'{TITULO} · {SUB_1}', 'pantalla', cuerpo, extra)

# ================================================================= IMPRIMIBLE (Letter)
def seccion_md(texto, titulo_re):
    """Devuelve el bloque Markdown de un '## titulo' hasta el siguiente '## '."""
    texto = re.sub(r'<!--.*?-->', '', texto, flags=re.S)
    m = re.search(r'^## (' + titulo_re + r').*?\n(.*?)(?=^## |\Z)', texto, flags=re.S | re.M)
    return m.group(2) if m else ''

def anadir_check(h):
    """Añade una columna ✓ vacía a la tabla de la hoja del domingo."""
    def f(m):
        t = m.group(0)
        t = re.sub(r'</th>\s*</tr>', '</th><th class="ck">✓</th></tr>', t, count=1)
        t = re.sub(r'</td>\s*</tr>', '</td><td class="ck"><span class="caja-in"></span></td></tr>', t)
        return t
    return re.sub(r'<table class="[^"]*hoja[^"]*">.*?</table>', f, h, flags=re.S)

def imprimible():
    imp = re.sub(r'<!--.*?-->', '', leer('imprimible.md'), flags=re.S)
    def sec_imp(t):
        return seccion_md(imp, re.escape(t))
    hojas = []
    def hoja(hid, titulo, icono, cont, consigna=''):
        c = f'<p class="consigna">{consigna}</p>' if consigna else ''
        hojas.append(f'<section class="hoja" id="{hid}"><h1>{ico(icono)}{titulo}</h1>{c}{cont}</section>')
    # 1. Cómo usar
    uso = sec_imp('Page 1 · How to use this pack')
    mapa = seccion_md(imp, 'Page map')
    hoja('como-usar', 'The Sunday Sheet · Printable Pack', 'imprimir', md(uso) + '<h2>What is in this pack</h2>' + md(mapa, True),
         'US Letter. Black-and-white friendly: ✓, ❄ and bold carry the meaning, not color.')
    # 2-5. Hojas del domingo rellenas
    semanas = {1: '08-week-1.md', 2: '09-week-2.md', 3: '10-week-3.md', 4: '11-week-4.md'}
    for n, a in semanas.items():
        t = leer(a)
        glance = seccion_md(t, 'The week at a glance')
        oven = (re.search(r'^\| Oven \| (.*?) \|', glance, re.M) or [None, ''])[1]
        sesion = (re.search(r'^\| Session \| (.*?) \|', glance, re.M) or [None, 'About 2 hours'])[1]
        friday = (re.search(r'^\| Freezer \| (.*?) \|', glance, re.M) or [None, ''])[1]
        sh = seccion_md(t, r'The Sunday Sheet · Week \d|Step \d · .*Sunday Sheet')
        if not sh.strip():
            sh = seccion_md(t, r'The Sunday Sheet')
        sh = re.sub(r'^\*\*Write your real time.*$', '', sh, flags=re.M)
        sh = re.sub(r'^\*Why this order:\*.*$', '', sh, flags=re.M)
        asm = seccion_md(t, 'The assembly table')
        asm_tabla = '\n'.join(l for l in asm.split('\n') if l.startswith('|'))
        cab = (f'<div class="cabecera-semana"><span><b>Week {n}</b></span><span><span class="caja-in"></span> ×1 &nbsp;<span class="caja-in"></span> ×2</span>'
               f'<span><b>Oven:</b> {inline(oven)}</span><span><b>Session:</b> {inline(sesion)}</span>'
               f'<span><b>Real time:</b> start ______ finish ______</span></div>')
        cuerpo = cab + anadir_check(md(sh, True)) + '<h2>Assembly</h2>' + md(asm_tabla, True)
        cuerpo += f'<div class="franja">❄ Friday: {inline(friday)} · Thursday morning: move Friday\'s boxes to the fridge.' + (' · Salmon: Monday and Tuesday only.' if n == 3 else '') + '</div>'
        hoja(f'hoja-semana-{n}', f'Sunday Sheet · Week {n}', 'reloj', cuerpo)
    # 6. Hoja en blanco
    blanca = sec_imp('Page 6 · Blank Sunday Sheet')
    def hoja_blanca(hid):
        h = md(blanca, True)
        h = h.replace('<table class="t escribir hoja', '<table class="t escribir hoja vacia')
        hoja(hid, 'Sunday Sheet · Blank', 'reloj', h)
    hoja_blanca('hoja-blanca')
    # 7-10. Listas de la compra
    for n, a in semanas.items():
        t = leer(a)
        sl = seccion_md(t, r'Shopping list · Week \d')
        intro, _, resto = sl.partition('\n\n**')
        resto = '**' + resto
        bloques = re.split(r'\n(?=\*\*[^*]+\*\*)', resto)
        sobra = ''
        partes = []
        for b in bloques:
            if b.startswith("**What's left over"):
                sobra = b
            else:
                partes.append(b)
        h = '<div class="dos-col">' + ''.join(f'<div>{md(b, True)}</div>' for b in partes) + '</div>'
        if sobra:
            h += '<div class="caja-i consejo">' + md(sobra, True).replace('<p class="rotulo">', '<div class="cabecera">' + ico('consejo')).replace('</p>', '</div>', 1) + '</div>'
        hoja(f'compra-semana-{n}', f'Shopping list · Week {n}', 'carro', h, inline(intro.strip()))
    # 11. Lista en blanco
    def compra_blanca(hid):
        hoja(hid, 'Shopping list · Blank', 'carro', md(sec_imp('Page 11 · Blank shopping list by aisle'), True))
    compra_blanca('compra-blanca')
    # 12-13. Tabla de conservación
    c20 = leer('20-storage-chart.md')
    reglas = seccion_md(c20, 'The rules behind the numbers')
    reglas_ol = '\n'.join(l for l in reglas.split('\n') if re.match(r'\d+\.', l))
    chart = seccion_md(c20, 'The chart')
    hoja('tabla-conservacion', 'Storage chart · All 60 recipes', 'nevera',
         '<div class="caja-i aviso"><div class="cabecera">' + ico('aviso') + 'The rules (USDA FSIS)</div>' +
         md(reglas_ol, True).replace('<ol>', '<ol class="reglas">') + '</div>' + md(chart, True))
    # 14. Mix & Match
    c16 = leer('16-signature-plates.md')
    salsas = seccion_md(c16, 'The Mix & Match chart')
    t_salsas = re.search(r'### Sauces by family\n(.*?)(?=### )', salsas, re.S).group(1)
    cuatro = ''
    for nombre in ['Proteins', 'Bases', 'Vegetables']:
        tb = re.search(r'### ' + nombre + r'\n(.*?)(?=### |\Z)', salsas, re.S).group(1)
        cuatro += f'<div><p class="rotulo">{nombre}</p>{md(tb, True)}</div>'
    hoja('mix-match', 'Mix & Match poster', 'consejo',
         '<div class="poster-regla">Pick a sauce. <span>Any ✓ in its column goes with it.</span></div>' + md(t_salsas, True) +
         f'<div class="cuatro">{cuatro}</div><p class="fuentes">1,815 combinations pass this rule. The 48 signature plates are in Chapter 16.</p>')
    # 15-16
    hoja('build-your-plate', 'Build Your Plate', 'ejercicio', md(sec_imp('Page 15 · Build Your Plate'), True))
    hoja('cost-per-box', 'Cost per box', 'carro', md(sec_imp('Page 16 · Cost per box'), True))
    # 17. Despensa
    c7 = leer('07-pantry-gear.md')
    pantry = seccion_md(c7, r'The pantry: 26 items')
    pantry = pantry.split('\n\n', 1)[1] if '\n\n' in pantry else pantry
    hoja('despensa', 'Pantry checklist · 26 items', 'carro', '<div class="dos-col">' +
         ''.join(f'<div>{md(b, True)}</div>' for b in re.split(r'\n(?=\*\*[^*]+\*\*\s*\n)', pantry.strip()) if b.strip()) + '</div>',
         'Tick what you have. Write the rest at the top of your next shopping list. From Chapter 7.')
    # 18-19. Etiquetas
    def etq(tipo):
        if tipo == 'nevera':
            return ('<div class="etq"><b>EAT BY:</b> &nbsp;MON &nbsp;TUE &nbsp;WED &nbsp;THU <small>(circle one)</small><br>'
                    'Plate: <span class="l"></span> &nbsp;Cooked: <span class="l" style="min-width:14mm"></span><br>'
                    'Sauce cup: <span class="caja-in"></span> yes &nbsp;· Reheat to 165 °F</div>')
        if tipo == 'congelador':
            return ('<div class="etq"><b>❄ FRIDAY BOX</b><br>Plate: <span class="l"></span> &nbsp;Frozen: <span class="l" style="min-width:14mm"></span><br>'
                    'Move to fridge: <b>THURSDAY MORNING</b><br>Best within: <span class="l" style="min-width:10mm"></span> months</div>')
        return ('<div class="etq"><b>❄ RESERVE</b><br>Recipe: <span class="l" style="min-width:40mm"></span><br>Frozen: <span class="l" style="min-width:14mm"></span> &nbsp;Portions: <span class="l" style="min-width:10mm"></span><br>'
                '<small>Thaw in the fridge overnight · reheat to 165 °F / 74 °C</small></div>')
    hoja('etiquetas-nevera', 'Box labels · Fridge', 'nevera', '<div class="etiquetas">' + etq('nevera') * 10 + '</div>',
         'Cut along the dashed lines, or print on a 2 × 4-inch label sheet.')
    hoja('etiquetas-congelador', 'Box labels · Freezer', 'frio', '<div class="etiquetas">' + etq('congelador') * 6 + etq('reserva') * 4 + '</div>',
         'Friday boxes and reserve portions (Week 3 meatballs, freezer meals).')
    # 20-22. Tarjetas de nevera
    fc = seccion_md(imp, re.escape('Pages 20-22 · Fridge cards'))
    cards = re.findall(r'^### Card (\d) · (.*?)\n(.*?)(?=^### |\Z)', fc, re.S | re.M)
    ids_card = {'1': 'tarjeta-nevera', '2': 'tarjeta-recalentar', '3': 'tarjeta-salsas'}
    tarjetas = []
    for num, tit, cuerpo in cards:
        h = md(cuerpo, True)
        tarjetas.append(f'<div class="tarjeta" id="{ids_card[num]}"><div class="tarjeta-top">{ico("nevera")}Fridge card {num}</div>'
                        f'<p class="tarjeta-titulo">{tit}</p>{h}<div class="tarjeta-pie">THE SUNDAY SHEET</div></div>')
    hojas.append(f'<section class="hoja tarjeta-pag">{tarjetas[0]}{tarjetas[1]}</section>')
    hojas.append(f'<section class="hoja tarjeta-pag">{tarjetas[2]}</section>')
    # 23-30 copias en blanco
    for k in range(2, 6):
        hoja_blanca(f'hoja-blanca-{k}')
    for k in range(2, 6):
        compra_blanca(f'compra-blanca-{k}')
    cuerpo = ''.join(hojas)
    fuentes = '<p class="fuentes"><em>Sources: USDA FSIS (storage, safe temperatures, thawing). USDA FoodData Central SR Legacy (nutrition). FDA, 9 major food allergens. Not medical or nutrition advice.</em></p>'
    cuerpo = cuerpo.replace('</section>', fuentes + '</section>', 1)
    d = doc(f'{TITULO} · Printable Pack', 'imprimible', cuerpo, CSS_IMPRIMIBLE)
    return d

# ================================================================= MUESTRA
def muestra():
    t = re.sub(r'<!--.*?-->', '', leer('muestra/the-mini-sunday.md'), flags=re.S)
    m = re.match(r'# (.*?)\n### (.*?)\n(.*)', t, re.S)
    titulo, sub, resto = m.group(1).strip(), m.group(2).strip(), m.group(3)
    # recetas (####)
    recs = {}
    def rec(mm):
        h = receta(mm.group(0))
        k = f'@@REC{len(recs)}@@'
        recs[k] = h
        return f'\n\n{k}\n\n'
    resto = re.sub(r'^#### [A-Z]+\d+ · .*?(?=^#### |^---|^## |\Z)', rec, resto, flags=re.S | re.M)
    intro, _, secciones = resto.partition('\n---\n')
    h_intro = md(intro)
    trozos = re.findall(r'^## (.*?)\n(.*?)(?=^## |\Z)', secciones, re.S | re.M)
    out, lis = [], []
    out.append(f'<section class="capitulo" id="cap-intro"><div class="apertura">{MOTIVO_AP}<div class="etiqueta">Free sample</div><h1>{titulo}</h1>'
               f'<p class="sub-ap">{sub}</p></div>{h_intro}</section>')
    lis.append('<li><a href="#cap-intro">Before you start</a></li>')
    for tit, cuerpo in trozos:
        cuerpo = re.sub(r'\n---\s*$', '', cuerpo.strip())
        sid = 'm-' + slug(tit)
        if tit.startswith('3 ·'):
            sid = 'hoja-mini'
        h = md(cuerpo)
        for k, v in recs.items():
            h = re.sub(r'<p>' + re.escape(k) + r'</p>', v, h)
        if tit.startswith('Your action'):
            h = cajas_accion(f'<h2 id="{sid}">{tit}</h2>' + h)
            out.append(f'<section class="capitulo" id="{sid}-s">{h}</section>')
        else:
            n = re.match(r'(\d+) · (.*)', tit)
            etq, t1 = (f'Part {n.group(1)}', n.group(2)) if n else ('', tit)
            out.append(f'<section class="capitulo" id="{sid}"><p class="etiqueta">{etq}</p><h1>{t1}</h1>{h}</section>')
        lis.append(f'<li><a href="#{sid}">{tit}</a></li>')
    nav = f'<nav class="indice"><h1>Contents</h1><ul>{"".join(lis)}</ul></nav>'
    css_p, sec_p = portada_html(PORTADA_ELEGIDA, etiqueta='Free sample', titulo=titulo,
                                sub1='One protein, one base, one vegetable, three sauces.', sub2='Three different lunches · five boxes · a free sample of The Sunday Sheet')
    if PORTADA_ELEGIDA == 'B':
        sec_p = sec_p.replace('The<span>Mini</span>Sunday', 'The<span>Mini</span>Sunday')
    cuerpo = sec_p + nav + ''.join(out)
    cuerpo = re.sub(r'(<td[^>]*>)(' + RE_REC + r')</td>', lambda m: f'{m.group(1)}<a href="#receta-{m.group(2).lower()}">{m.group(2)}</a></td>', cuerpo)
    # en la muestra, los IDs de plato no existen: quitar esos enlaces
    cuerpo = re.sub(r'<a href="#plato-[^"]+">([^<]+)</a>', r'\1', cuerpo)
    extra = css_p + '.sub-ap{position:relative;color:#fff;opacity:.88;font-family:var(--fuente-titulos);font-size:11pt;margin:2mm 0 0} .capitulo > .etiqueta{margin:0 0 1mm}'
    return doc(f'{titulo} · free sample of {TITULO}', 'pantalla', cuerpo, extra)

# ================================================================= PORTADAS
def portadas():
    os.makedirs(os.path.join(EN, 'portadas'), exist_ok=True)
    for v in 'ABC':
        css_p, sec = portada_html(v)
        hojas = f'<link rel="stylesheet" href="{CSS_PORTADAS}plantilla.css">\n<link rel="stylesheet" href="{CSS_PORTADAS}plantilla-pantalla.css">'
        h = (f'<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><title>{TITULO} · cover {v}</title>\n{hojas}\n'
             f'<style>{CSS_NICHO}{css_p} body{{margin:0}} .portada{{height:210mm}}</style></head><body>{sec}</body></html>\n')
        open(os.path.join(EN, 'portadas', f'portada-{v}.html'), 'w', encoding='utf-8').write(h)

if __name__ == '__main__':
    portadas()
    open(os.path.join(EN, 'the-sunday-sheet-pantalla.html'), 'w', encoding='utf-8').write(ebook_pantalla())
    open(os.path.join(EN, 'the-sunday-sheet-imprimible.html'), 'w', encoding='utf-8').write(imprimible())
    open(os.path.join(EN, 'the-mini-sunday-pantalla.html'), 'w', encoding='utf-8').write(muestra())
    print('OK: pantalla, imprimible, muestra y 3 portadas en', EN)
