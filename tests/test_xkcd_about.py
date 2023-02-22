from playwright.sync_api import expect, Page

from pages.home import HomePage
from pages.about import AboutPage

def test_xkcd_homepage_about_button_is_present(page: Page, home_page: HomePage) -> None:
    expect(home_page.about_button_text).to_be_visible()
    expect(home_page.about_button_locator).to_have_text("About")

def test_open_about_page_from_homepage(page: Page, home_page: HomePage) -> None:
    home_page.open_about_page()
    
    expect(page).to_have_title('xkcd - A webcomic')
    expect(page).to_have_url('https://xkcd.com/about/')

def test_about_page_can_be_accessed_via_url(page: Page, about_page: AboutPage) -> None:
    expect(page).to_have_title('xkcd - A webcomic')
    expect(page).to_have_url('https://xkcd.com/about/')
    
def test_verify_about_page_sections(page: Page, about_page: AboutPage) -> None:
    about_page.verify_all_sections_visible()

def test_xkcd_com_link(page: Page, home_page: HomePage, about_page: AboutPage) -> None:
    about_page.xkcd_com_link.click()

    expect(home_page.about_button_text).to_be_visible()
    expect(page).to_have_url('https://xkcd.com/')

def test_back_to_main_button_link(page: Page, home_page: HomePage, about_page: AboutPage) -> None:
    about_page.back_to_main_button.click()

    expect(home_page.about_button_text).to_be_visible()   
    expect(page).to_have_url('https://xkcd.com/')

def test_verify_all_links(page: Page, about_page: AboutPage) -> None:
    about_page.first_link.wait_for()
    about_page.verify_all_links_return_200()
