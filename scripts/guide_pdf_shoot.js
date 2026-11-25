const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const html = process.argv[2];
  const out = process.argv[3];
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await (await b.newContext()).newPage();
  await p.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  await p.pdf({
    path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
  });
  await b.close();
  console.log('PDF ->', out);
})();
