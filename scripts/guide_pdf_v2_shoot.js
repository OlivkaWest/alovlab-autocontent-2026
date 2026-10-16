const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const html = process.argv[2];
  const pdfOut = process.argv[3];
  const pagesDir = process.argv[4];
  fs.mkdirSync(pagesDir, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const ctx = await b.newContext({ viewport: { width: 1240, height: 1754 }, deviceScaleFactor: 2 });
  const p = await ctx.newPage();
  await p.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  // PDF
  await p.pdf({ path: pdfOut, format: 'A4', printBackground: true, preferCSSPageSize: true });
  // per-page PNG
  const pages = await p.$$('.page');
  for (let i = 0; i < pages.length; i++) {
    const n = String(i + 1).padStart(2, '0');
    await pages[i].screenshot({ path: path.join(pagesDir, `page-${n}.png`) });
  }
  console.log('PDF + PNG pages:', pages.length);
  await b.close();
})();
