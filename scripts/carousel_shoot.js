// AlovLab · экспорт слайдов карусели в отдельные PNG 1080×1350 (4:5).
// Запуск: NODE_PATH=/opt/node22/lib/node_modules node scripts/carousel_shoot.js <html> <outdir>
// Каждый .slide -> outdir/slide-0N.png (карточка 540px @2x = 1080). Футер на карусели не пишем.
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const html = process.argv[2];
  const outdir = process.argv[3] || path.dirname(html);
  if (!html || !fs.existsSync(html)) { console.error('usage: carousel_shoot.js <html> <outdir>'); process.exit(1); }
  fs.mkdirSync(outdir, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const ctx = await b.newContext({ viewport: { width: 1240, height: 900 }, deviceScaleFactor: 2 });
  const p = await ctx.newPage();
  await p.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(350);
  const slides = await p.$$('.slide');
  for (let i = 0; i < slides.length; i++) {
    const n = String(i + 1).padStart(2, '0');
    await slides[i].screenshot({ path: path.join(outdir, `slide-${n}.png`) });
    console.log('PNG slide-' + n);
  }
  await b.close();
  console.log('done ->', outdir);
})();
