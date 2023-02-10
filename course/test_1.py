import asyncio

from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("http://playwright.dev")
    print(page.title())
    page.screenshot(path="example.png")
    browser.close()


async def main():
    async with async_playwright() as pw:
        browser_async = await pw.chromium.launch(headless=False, slow_mo=2000)
        page_async = await browser_async.new_page()
        await page_async.goto("http://playwright.dev")
        print(await page_async.title())
        await browser_async.close()


asyncio.run(main())
