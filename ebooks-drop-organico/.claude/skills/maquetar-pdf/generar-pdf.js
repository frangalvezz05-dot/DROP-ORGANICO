// HTML -> PDF (o PNG) con Chromium/Playwright. Funciona en la nube (Linux) y en Windows si Playwright está instalado.
// Uso: node generar-pdf.js <archivo.html> <salida.pdf>
//      node generar-pdf.js <archivo.html#ancla> <salida.png> [ancho] [alto] [escala]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [src, out, w = 559, h = 794, s = 1] = process.argv.slice(2);
  if (!src || !out) { console.log('Uso: node generar-pdf.js entrada.html salida.pdf|png'); process.exit(1); }
  const [file, hash] = src.split('#');
  const url = 'file://' + path.resolve(file) + (hash ? '#' + hash : '');
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: +s });
  await p.goto(url, { waitUntil: 'networkidle' });
  await p.waitForTimeout(1500);
  if (out.endsWith('.pdf')) await p.pdf({ path: out, preferCSSPageSize: true, printBackground: true });
  else await p.screenshot({ path: out });
  await b.close();
  console.log('OK ' + out);
})().catch(e => { console.log('ERROR ' + e.message); process.exit(1); });
