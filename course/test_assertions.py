from playwright.sync_api import Page, expect


def test_submitted(page: Page) -> None:
    page.goto("https://www.youtube.com/")
    page.get_by_role(
        "button",
        name="Zaakceptuj wykorzystywanie plików cookie i innych danych do opisanych celów"
    ).click()
    expect(page.get_by_role("button", name="Przewodnik")).to_be_visible()
