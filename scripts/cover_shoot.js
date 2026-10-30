// AlovLab · экспорт обложек Reels (9:16) в отдельные PNG 1080x1920.
// Каждый .cover -> outdir/<data-name>.png (карточка 540x960px @2x = 1080x1920).
// Запуск: NODE_PATH=/opt/node22/lib/node_modules node scripts/cover_shoot.js <html> <outdir>
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const html = process.argv[2];
  const outdir = process.argv[3] || path.dirname(html);
  if (!html || !fs.existsSync(html)) { console.error('usage: cover_shoot.js <html> <outdir>'); process.exit(1); }
  fs.mkdirSync(outdir, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const ctx = await b.newContext({ viewport: { width: 700, height: 1100 }, deviceScaleFactor: 2 });
  const p = await ctx.newPage();
  await p.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(350);
  const covers = await p.$$('.cover');
  for (const el of covers) {
    const name = await el.getAttribute('data-name');
    await el.screenshot({ path: path.join(outdir, `${name}.png`) });
    console.log('PNG', name);
  }
  await b.close();
  console.log('done ->', outdir);
})();
