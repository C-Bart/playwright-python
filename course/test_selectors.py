def test_selectors(context):
    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()

    page.goto("https://magento.softwaretestingboard.com/")

    # page.locator("#ui-id-4").hover()
    page.locator("text=Women").hover()
    # context.tracing.stop(path="trace.zip")
    page.locator("#ui-id-10").hover()
    page.locator("#ui-id-16").click()
    page.wait_for_load_state("domcontentloaded")


