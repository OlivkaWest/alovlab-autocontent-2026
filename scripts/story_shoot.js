// AlovLab · экспорт story-кадра 9:16 в PNG 1080×1920. Скриншотит .story @2x.
// Запуск: NODE_PATH=/opt/node22/lib/node_modules node scripts/story_shoot.js <html> <out.png>
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const html = process.argv[2];
  const out = process.argv[3] || html.replace(/\.html$/, '.png');
  if (!html || !fs.existsSync(html)) { console.error('usage: story_shoot.js <html> <out.png>'); process.exit(1); }
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const ctx = await b.newContext({ viewport: { width: 700, height: 1100 }, deviceScaleFactor: 2 });
  const p = await ctx.newPage();
  await p.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  const el = await p.$('.story');
  await el.screenshot({ path: out });
  console.log('PNG', out);
  await b.close();
})();
