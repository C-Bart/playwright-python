def test_facebook(page):
    page.goto("https://www.facebook.com/register")

    input_first_name = "[aria-label='First name']"
    page.locator(input_first_name).click()
    page.locator(input_first_name).fill("Jack")
    page.locator(input_first_name).press("Tab")

    input_last_name = ""
    page.locator(input_last_name).fill("Jones")

    select_dropdown = ""
    page.locator(select_dropdown).select_option("9")

    radio_buttons = ""
    page.locator(radio_buttons).nth(1).click()
