from playwright.sync_api import Page, expect
import requests
from bs4 import BeautifulSoup

class AboutPage:
    URL = "https://xkcd.com/about"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.xkcd_com_link = page.locator('center > h2 > a')
        self.back_to_main_button = page.get_by_text("Back to main")
        self.first_link = page.locator('a').nth(1)
        self.page_title = page.title()
        self.page_links_count = page.locator('a')

    def load(self) -> None:
        self.page.goto(self.URL)

    def get_page_title(self) -> None:
        return self.page_title

    def verify_all_sections_visible(self) -> None:
        about_sections = ["Who are you?", "What else do you do?", "Who else are you?", "What does XKCD stand for?"]

        for section in about_sections:
            expect(self.page.get_by_text(section)).to_be_visible()

    def get_page_links_count(self) -> int:
        print(f"{self.page_links_count.count()} link/links are found.")
        return self.page_links_count.count()

    def verify_all_links_return_200(self) -> None:
        page = requests.get(self.URL)

        # Get the response code of given URL
        response_code = str(page.status_code)

        # Display the text of the URL in str
        data = page.text

        # Use BeautifulSoup to use the built-in methods
        soup = BeautifulSoup(data, features="html.parser")

        # Iterate over all links on the given URL with the response code next to it
        assert len(soup.find_all('a')) == self.get_page_links_count()
        for link in soup.find_all('a'):
            #print(f"Url: {link.get('href')} " + f"| Status Code: {response_code}")
            assert int(response_code) == 200
        