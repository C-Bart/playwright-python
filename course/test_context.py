from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    iphone_11 = p.devices["iPhone 11 Pro"]
    browser = p.webkit.launch(headless=False, slow_mo=4000)
    context = browser.new_context(
        **iphone_11,
        locale='de-DE',
        geolocation={'longitude': 12.492507, 'latitude': 41.889938},
        permissions=['geolocation']
    )
    page = context.new_page()
    page.goto("https://youtube.com/")
    # page.pause()
    page.close()
