// Versión para la nube (Linux) de generar-imagenes.ps1, con Chromium/Playwright. Mismo resultado.
// Uso: node .claude/skills/imagenes-producto/generar-imagenes.js <nicho> <idioma>
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const [nicho, idioma] = process.argv.slice(2);
  if (!nicho || !idioma) { console.log('Uso: node generar-imagenes.js <nicho> <idioma>'); process.exit(1); }
  const skill = __dirname, raiz = path.resolve(skill, '../../..');
  const nd = path.join(raiz, 'nichos', nicho), eb = path.join(nd, 'ebook', idioma), out = path.join(nd, 'tienda', 'imagenes', idioma);
  fs.mkdirSync(out, { recursive: true });
  const uri = p => 'file://' + path.resolve(p);
  const ls = (d, re) => fs.existsSync(d) ? fs.readdirSync(d).filter(f => re.test(f)).sort().map(f => path.join(d, f)) : [];
  const marca = JSON.parse(fs.readFileSync(path.join(nd, 'marca.json'), 'utf8'));
  const cont = JSON.parse(fs.readFileSync(path.join(out, 'contenido.json'), 'utf8'));
  const b = await chromium.launch();
  const shot = async (url, w, h, png, s = 1) => { const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: s }); await p.goto(url, { waitUntil: 'networkidle' }); await p.waitForTimeout(1500); await p.screenshot({ path: png }); await p.close(); };
  const dim = async f => { const p = await b.newPage(); await p.goto(uri(f)); const d = await p.evaluate(() => ({ w: document.images[0].naturalWidth, h: document.images[0].naturalHeight })); await p.close(); return d; };
  let portada = path.join(eb, 'portadas', 'portada-producto.png');
  if (!fs.existsSync(portada)) portada = ls(eb, /pantalla-portada\.png$/)[0];
  if (!portada) throw new Error('Falta *pantalla-portada.png en ' + eb);
  let ints = ls(eb, /interior.*\.png$/).filter(f => !/tarjeta/.test(f));
  let tarj = ls(eb, /tarjeta.*\.png$/)[0];
  const html = ls(eb, /pantalla\.html$/)[0];
  for (let n = 0; ints.length < 3 && html && cont.anclas && n < cont.anclas.length; n++) {
    const f = path.join(out, `_interior-auto-${n}.png`), w = path.join(out, '_wrap.html');
    fs.writeFileSync(w, `<html><body style='margin:0;background:#fff;padding:30px 32px'><iframe src='${uri(html)}#${cont.anclas[n]}' style='border:0;width:495px;height:734px'></iframe></body></html>`);
    await shot(uri(w), 559, 794, f); fs.unlinkSync(w); ints.push(f);
  }
  if (ints.length < 3) throw new Error('Hacen falta al menos 3 páginas interiores (PNG o anclas en contenido.json)');
  if (!tarj) tarj = ints[0];
  const imp = ls(eb, /imprimible\.html$/)[0];
  let sc = 1;
  if (cont.ancla_tarjeta && imp) { tarj = path.join(out, '_tarjeta-2x.png'); await shot(uri(imp) + '#' + cont.ancla_tarjeta, 900, 1200, tarj, 2); sc = 2; }
  // recorta márgenes blancos de la tarjeta (solo el primer bloque)
  const pg = await b.newPage();
  await pg.goto(uri(tarj));
  const rect = await pg.evaluate((sc) => { const im = document.images[0], c = document.createElement('canvas'); c.width = im.naturalWidth; c.height = im.naturalHeight; const x = c.getContext('2d'); x.drawImage(im, 0, 0); const d = x.getImageData(0, 0, c.width, c.height).data;
    let x0 = c.width, y0 = c.height, x1 = 0, y1 = 0, st = false, bl = 0;
    for (let y = 0; y < c.height; y += 2) { let hit = false; for (let xx = 0; xx < c.width; xx += 2) { const i = (y * c.width + xx) * 4; if (d[i] < 245 || d[i + 1] < 245 || d[i + 2] < 245) { hit = true; if (xx < x0) x0 = xx; if (xx > x1) x1 = xx; } }
      if (hit) { if (!st) { st = true; y0 = y; } y1 = y; bl = 0; } else if (st) { bl++; if (bl > 30 * sc) break; } }
    const m = 12 * sc; x0 = Math.max(0, x0 - m); y0 = Math.max(0, y0 - m); x1 = Math.min(c.width - 1, x1 + m); y1 = Math.min(c.height - 1, y1 + m);
    return { x: x0, y: y0, width: x1 - x0 + 1, height: y1 - y0 + 1 }; }, sc);
  // viewport = tamaño real de la imagen: si es mayor, Chromium centra la imagen sobre fondo negro y el recorte sale desplazado
  const nat = await pg.evaluate(() => ({ w: document.images[0].naturalWidth, h: document.images[0].naturalHeight }));
  await pg.setViewportSize({ width: nat.w, height: nat.h });
  const tarjFile = path.join(out, '_tarjeta-recorte.png');
  await pg.screenshot({ path: tarjFile, clip: rect }); await pg.close();
  const pd = await dim(portada), td = await dim(tarjFile);
  const d = { color_principal: marca.color_principal, color_acento: marca.color_acento, color_fondo_suave: marca.color_fondo_suave, fuente_titulos: marca.fuente_titulos, fuente_texto: marca.fuente_texto,
    portada: { src: uri(portada), w: pd.w, h: pd.h }, interiores: ints.slice(0, 3).map(uri), tarjeta: { src: uri(tarjFile), w: td.w, h: td.h }, incluye: cont.incluye, extras: cont.extras, textos: cont.textos };
  const trabajo = path.join(out, '_trabajo'); fs.mkdirSync(trabajo, { recursive: true });
  fs.copyFileSync(path.join(skill, 'plantilla.html'), path.join(trabajo, 'plantilla.html'));
  fs.writeFileSync(path.join(trabajo, 'datos.js'), 'window.DATOS=' + JSON.stringify(d, null, 1) + ';');
  const nombres = { 1: 'portada', 2: 'escaparate', 3: 'incluye', 4: 'perspectivas', 5: 'extras' };
  for (let t = 1; t <= 5; t++) for (const [f, w, h, n] of [['c', 1080, 1080, 'cuadrado'], ['v', 1080, 1350, 'vertical']]) {
    const png = path.join(out, `${t}-${nombres[t]}-${n}.png`); await shot(uri(path.join(trabajo, 'plantilla.html')) + `?t=${t}&f=${f}`, w, h, png); console.log(png);
  }
  await b.close();
  fs.readdirSync(out).filter(f => f.startsWith('_') && f.endsWith('.png')).forEach(f => fs.unlinkSync(path.join(out, f)));
  fs.rmSync(trabajo, { recursive: true, force: true });
  fs.writeFileSync(path.join(out, 'info.md'), `# Imágenes de producto (${nicho}, ${idioma})\n\nGenerado: ${new Date().toISOString().slice(0, 10)}\n\n**Avatar**: ${cont.avatar}\n\n**Ángulo**: ${cont.angulo}\n\nFormatos: 1080x1080 (c) y 1080x1350 (v). Páginas reales del ebook; sin imágenes de terceros; marcos de dispositivo genéricos.\n`);
})().catch(e => { console.log('ERROR ' + e.message); process.exit(1); });
