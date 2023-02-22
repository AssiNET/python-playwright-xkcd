from playwright.sync_api import Page, expect

class HomePage:
    URL = "https://xkcd.com"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.about_button_text = page.get_by_text("About")
        self.about_button_locator = page.locator('#topLeft > ul > li').nth(2)

    def load(self) -> None:
        self.page.goto(self.URL)

    def open_about_page(self) -> None:
        self.about_button_text.click()


