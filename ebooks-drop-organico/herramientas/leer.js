// Lee el texto visible de una página con Chromium (Playwright). Uso: node herramientas/leer.js "<url>" [segundos_espera] [max_caracteres]
const { chromium } = require('playwright');
(async () => {
  const [url, wait = 5, max = 15000] = process.argv.slice(2);
  const b = await chromium.launch();
  const c = await b.newContext({ locale: 'en-US', userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' });
  const p = await c.newPage();
  try {
    const r = await p.goto(url, { timeout: 60000, waitUntil: 'domcontentloaded' });
    await p.waitForTimeout(+wait * 1000);
    for (let i = 0; i < 2; i++) { await p.mouse.wheel(0, 3000); await p.waitForTimeout(1200); }
    const t = (await p.innerText('body')).replace(/[ \t]+/g, ' ').replace(/\n{2,}/g, '\n');
    console.log('ESTADO ' + r.status() + ' ' + url + '\n' + t.slice(0, +max));
  } catch (e) { console.log('ERROR ' + e.message.slice(0, 200)); }
  await b.close();
})();
