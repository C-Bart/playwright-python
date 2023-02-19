from playwright.sync_api import Page


class HomePageLocators:

    def __int__(self, page: Page):
        self.navigation_women = page.locator("#ui-id-4")
        self.navigation_women_bottoms = page.locator("#ui-id-10")
