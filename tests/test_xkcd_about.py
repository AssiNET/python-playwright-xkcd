# Import libraries
from bs4 import BeautifulSoup
import requests
from playwright.sync_api import expect, Page

def test_xkcd_homepage_about_button_is_present(page: Page) -> None:
    page.goto('https://xkcd.com')

    expect(page.get_by_text("About")).to_be_visible()
    expect(page.locator('#topLeft > ul > li').nth(2)).to_have_text("About")

def test_open_about_page_from_homepage(page: Page) -> None:
    page.goto('https://xkcd.com')
    page.get_by_text("About").click()

    expect(page).to_have_title('xkcd - A webcomic')
    expect(page).to_have_url('https://xkcd.com/about/')

def test_about_page_can_be_accessed_via_url(page: Page) -> None:
    page.goto('https://xkcd.com/about/')

    expect(page).to_have_title('xkcd - A webcomic')
    expect(page).to_have_url('https://xkcd.com/about/')
    
def test_verify_about_page_sections(page: Page) -> None:
    page.goto('https://xkcd.com/about/')
    about_sections = ["Who are you?", "What else do you do?", "Who else are you?", "What does XKCD stand for?"]

    for section in about_sections:
        expect(page.get_by_text(section)).to_be_visible()

def test_xkcd_com_link(page: Page) -> None:
    page.goto('https://xkcd.com/about/')
    page.locator('center > h2 > a').click()

    expect(page.get_by_text("About")).to_be_visible()
    expect(page).to_have_url('https://xkcd.com/')

def test_back_to_main_button_link(page: Page) -> None:
    page.goto('https://xkcd.com/about/')
    page.get_by_text("Back to main").click()

    expect(page.get_by_text("About")).to_be_visible()
    expect(page).to_have_url('https://xkcd.com/')

def test_verify_all_links(page:Page) -> None:
    page.goto('https://xkcd.com/about/')
    #page.wait_for_timeout(500)
    page.locator('a').nth(-1).wait_for()
    links_count = page.locator('a').count()
    
    print(f"{links_count} link/links are found.")
    
    url = "https://xkcd.com/about"

    # Make a request to get the URL
    page = requests.get(url)

    # Get the response code of given URL
    response_code = str(page.status_code)

    # Display the text of the URL in str
    data = page.text

    # Use BeautifulSoup to use the built-in methods
    soup = BeautifulSoup(data, features="html.parser")

    # Iterate over all links on the given URL with the response code next to it
    assert len(soup.find_all('a')) == links_count
    for link in soup.find_all('a'):
        #print(f"Url: {link.get('href')} " + f"| Status Code: {response_code}")
        assert int(response_code) == 200