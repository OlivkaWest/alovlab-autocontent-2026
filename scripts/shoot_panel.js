const { chromium } = require('playwright');
(async () => {
  const [html, out, sel] = [process.argv[2], process.argv[3], process.argv[4] || '#panel'];
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1600, height: 1000 }, deviceScaleFactor: 2 });
  await p.goto('file://' + html);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(350);
  await (await p.$(sel)).screenshot({ path: out });
  await b.close(); console.log('shot', out);
})();
