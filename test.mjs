import { chromium } from 'playwright';

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('PAGE LOG:', msg.type(), msg.text()));
  page.on('pageerror', error => console.log('PAGE ERROR:', error.message));
  page.on('requestfailed', request => console.log('REQUEST FAILED:', request.url(), request.failure().errorText));

  console.log('Testing flappy-bird...');
  await page.goto('http://localhost:5173/games/flappy-bird/', { waitUntil: 'networkidle' });
  
  console.log('Testing ping-pong...');
  await page.goto('http://localhost:5173/games/ping-pong/', { waitUntil: 'networkidle' });
  
  console.log('Testing 2048...');
  await page.goto('http://localhost:5173/games/2048/', { waitUntil: 'networkidle' });

  await browser.close();
})();
