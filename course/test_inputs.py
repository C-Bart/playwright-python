import pytest


@pytest.mark.skip(reason="not ready")
def test_facebook(page):
    page.goto("https://www.facebook.com/register")

    input_first_name = "[aria-label='First name']"
    page.locator(input_first_name).click()
    page.locator(input_first_name).fill("Jack")
    page.locator(input_first_name).press("Tab")

    input_last_name = ""
    page.locator(input_last_name).fill("Jones")
    # page.locator(input_last_name).type("Jones")

    select_dropdown = ""
    page.locator(select_dropdown).select_option("9")

    radio_buttons = ""
    page.locator(radio_buttons).nth(1).click()

    checkbox = ""
    page.locator(checkbox).click()

    sprouts = page.locator(checkbox)
    sprouts.click()

    assert sprouts.is_checked()

    upload_button = ""
    page.locator(upload_button).click()

    upload_input = ""
    page.locator(upload_input).set_input_files("test_file.txt")

    send_button = ""
    page.locator(send_button).click()

