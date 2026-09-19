const { chromium } = require('playwright');
(async () => {
  const [html, out] = [process.argv[2], process.argv[3]];
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 900, height: 900 }, deviceScaleFactor: 2 });
  await p.goto('file://' + html);
  await p.waitForTimeout(300);
  const el = await p.$('#term');
  await el.screenshot({ path: out, omitBackground: true });
  await b.close();
  console.log('shot', out);
})();
