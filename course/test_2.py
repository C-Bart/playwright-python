import pytest


@pytest.mark.skip_browser("chromium")
def test_open_youtube(page):
    page.goto("https://youtube.com")


@pytest.mark.only_browser("chromium")
def test_open_only_browser(page):
    page.goto("https://youtube.com")
