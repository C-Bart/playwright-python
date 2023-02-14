from playwright.sync_api import expect


def test_load_delay(page):
    page.goto("http://uitestingplayground.com/")
    page.locator("text=Load Delay").click()
    assert page.url == "http://uitestingplayground.com/loaddelay"
    page.locator("text=Button Appearing After Delay").click()


def test_ajax_data(page):
    page.goto("http://uitestingplayground.com/")
    page.locator("text=AJAX Data").click()
    assert page.url == "http://uitestingplayground.com/ajax"
    page.locator("text=Button Triggering AJAX Request").click()
    expect(page.locator(".bg-success")).to_have_text("Data loaded with AJAX get request.", timeout=16000)
