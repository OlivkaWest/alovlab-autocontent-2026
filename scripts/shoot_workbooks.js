// Рендер фирменных HTML методичек → PDF (Playwright/Chromium).
// Запуск: NODE_PATH=/opt/node22/lib/node_modules node scripts/shoot_workbooks.js [22 23 ...]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = '/home/user/alovlab-autocontent-2026';
const DAYS = path.join(ROOT, 'content-30-days', 'days');

(async () => {
  const args = process.argv.slice(2).map(Number).filter(Boolean);
  const nums = args.length ? args : Array.from({ length: 30 }, (_, i) => i + 1);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  const done = [];
  for (const n of nums) {
    const nn = String(n).padStart(2, '0');
    const htmlPath = path.join(DAYS, `day-${nn}`, `alovlab-day-${nn}.html`);
    const pdfPath = path.join(DAYS, `day-${nn}`, `alovlab-day-${nn}.pdf`);
    if (!fs.existsSync(htmlPath)) { console.log('SKIP', nn, '— нет html'); continue; }
    await page.goto('file://' + htmlPath, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    await page.pdf({ path: pdfPath, format: 'A4', printBackground: true,
      margin: { top: '0', right: '0', bottom: '0', left: '0' } });
    done.push(nn);
    console.log('PDF', nn, 'ok');
  }
  await browser.close();
  console.log('Готово PDF:', done.join(','));
})();
