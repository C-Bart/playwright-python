import pytest


@pytest.mark.skip_browser("chromium")
def test_open_youtube(page):
    page.goto("https://youtube.com")


@pytest.mark.only_browser("chromium")
def test_open_only_browser(page):
    page.goto("https://youtube.com")


@pytest.mark.parametrize("email, password", [
    ("correct.email@mail.com", "1234"),
    pytest.param("wrong.email@email.com", "1234", marks=pytest.mark.xfail)
])
def test_params(page, email, password):
    page.goto("https://youtube.com")


@pytest.mark.parametrize("email",
                         ["correct.email@mail.com", pytest.param("wrong.email@email.com", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", ["1234"])
def test_params_alternative(page, email, password):
    page.goto("https://youtube.com")
